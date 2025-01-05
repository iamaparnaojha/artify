from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Conversation, Message
from django.utils import timezone

# Create your views here.

@login_required
def inbox(request):
    conversations = request.user.conversations.all()
    return render(request, 'messages/inbox.html', {
        'conversations': conversations
    })

@login_required
def conversation(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    
    # Get or create conversation
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if content or image:
            message = Message.objects.create(
                conversation=conversation,
                sender=request.user,
                content=content,
                image=image
            )
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'message': {
                        'content': message.content,
                        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M'),
                        'sender_name': message.sender.username,
                        'image_url': message.image.url if message.image else None
                    }
                })
            return redirect('messages:conversation', user_id=user_id)
    
    # Mark messages as read
    Message.objects.filter(conversation=conversation).exclude(sender=request.user).update(is_read=True)
    
    return render(request, 'messages/conversation.html', {
        'conversation': conversation,
        'other_user': other_user
    })

@login_required
def get_messages(request, conversation_id):
    conversation = get_object_or_404(Conversation, id=conversation_id, participants=request.user)
    messages = conversation.messages.all()
    
    messages_data = [{
        'id': message.id,
        'content': message.content,
        'sender_name': message.sender.username,
        'created_at': message.created_at.strftime('%Y-%m-%d %H:%M'),
        'is_read': message.is_read,
        'image_url': message.image.url if message.image else None
    } for message in messages]
    
    return JsonResponse({'messages': messages_data})

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    if query:
        users = User.objects.filter(
            Q(username__icontains=query) | 
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query)
        ).exclude(id=request.user.id)[:10]
        
        users_data = [{
            'id': user.id,
            'username': user.username,
            'name': f"{user.first_name} {user.last_name}".strip()
        } for user in users]
        
        return JsonResponse({'users': users_data})
    return JsonResponse({'users': []})
