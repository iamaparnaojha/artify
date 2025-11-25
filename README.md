# Artify

A full-stack social media web application built with **Python Django** and a **modern, responsive UI**.  
Users can create posts, follow other users, like and comment, manage their profiles, and interact in a clean, Instagram/Twitter-style interface.

---

## ✨ Features

- **Authentication & Profiles**
  - User registration, login, logout
  - Edit profile (avatar, bio, links, etc.)
  - View others’ profiles with follower/following count

- **Posts & Feed**
  - Create, edit, delete posts (text + images)
  - Global feed (all posts)
  - Personalized feed (posts from people you follow)
  - Image upload & display

- **Social Features**
  - Like / Unlike posts
  - Comment on posts
  - Follow / Unfollow users
  - Basic notifications (e.g., new followers / likes / comments) *(optional depending on your implementation)*

- **Modern UI**
  - Fully responsive layout (mobile, tablet, desktop)
  - Clean, minimal design inspired by popular social apps
  - Dark/light-friendly color palette
  - Sticky navbar, smooth hover states, and card-based layout

- **Extras (if implemented in your project)**
  - Search users / posts
  - Hashtags or tags
  - Pagination or infinite scroll
  - Edit profile cover image
  - Deactivate/delete account

---

## 🧱 Tech Stack

- **Backend:** Django
- **Frontend:** Django Templates + HTML5, CSS3, JavaScript  
  - (With modern styling using **Tailwind CSS / Bootstrap / custom CSS** – depending on your implementation)
- **Database:** SQLite (default) 

---

🚀 Getting Started (Local Setup)
1. Clone the Repository
git clone https://github.com/iamaparnaojha/artify.git
cd artify

2. Create and Activate Virtual Environment
3. Install Dependencies
pip install -r requirements.txt

🔐 Environment Variables

Create a .env file in the project root (same level as manage.py), and add:

SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost


🗄️ Database Setup & Migrations

Run migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (admin account):

python manage.py createsuperuser


Follow the prompts to set username, email, and password.

▶️ Run the Development Server
python manage.py runserver


Open your browser and visit:

http://127.0.0.1:8000/


or

http://localhost:8000/


You can access the Django admin at:

http://127.0.0.1:8000/admin/

🖼️ Static Files & Media (Images)

Make sure your settings.py includes something like:

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / "media"

