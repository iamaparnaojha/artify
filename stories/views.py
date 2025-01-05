from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Story
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.exceptions import PermissionDenied

# Create your views here.

@login_required
def create_story(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        caption = request.POST.get('caption', '')
        
        if image:
            story = Story.objects.create(
                user=request.user,
                image=image,
                caption=caption
            )
            return JsonResponse({'status': 'success', 'story_id': story.id})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def view_stories(request):
    # Get all active stories from users that the current user follows
    following = request.user.profile.following.all()
    current_time = timezone.now()
    active_stories = Story.objects.filter(
        user__in=following,
        created_at__gte=current_time - timezone.timedelta(hours=24)
    ).select_related('user').order_by('user', '-created_at')

    # Group stories by user
    stories_by_user = {}
    for story in active_stories:
        if not story.user in stories_by_user:
            stories_by_user[story.user] = []
        stories_by_user[story.user].append(story)

    return render(request, 'stories/view_stories.html', {
        'stories_by_user': stories_by_user
    })

@login_required
@require_POST
def delete_story(request, story_id):
    try:
        story = Story.objects.get(id=story_id)
        if story.user != request.user:
            raise PermissionDenied
        story.delete()
        return JsonResponse({'status': 'success'})
    except Story.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

@login_required
def my_stories(request):
    current_time = timezone.now()
    stories = Story.objects.filter(
        user=request.user,
        created_at__gte=current_time - timezone.timedelta(hours=24)
    ).order_by('-created_at')
    
    return render(request, 'stories/my_stories.html', {
        'stories': stories
    })
