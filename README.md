# Personal Portfolio Website

A professional, responsive portfolio website built with **Django** (backend) and **React** (frontend) with **Tailwind CSS** for styling.

## 🌟 Features

- ✨ **Modern Design**: Clean, professional UI with smooth animations
- 🌓 **Dark/Light Mode**: Toggle between themes with preference saved locally
- 📱 **Fully Responsive**: Works seamlessly on desktop, tablet, and mobile
- 🚀 **Dynamic Portfolio**: Projects fetched from Django REST API
- 🎨 **Tailwind CSS**: Modern utility-first CSS framework
- 📝 **Resume Section**: Showcase education, experience, skills, and certifications
- 📧 **Contact Form**: Easy way for visitors to get in touch
- 🔧 **Easy Management**: Add/edit projects via Django Admin panel

## 🏗️ Project Structure

```
personal-website/
├── backend/                 # Django Backend
│   ├── portfolio/          # Main Django project
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── projects/           # Projects app
│   │   ├── models.py       # Project model
│   │   ├── serializers.py  # DRF serializers
│   │   ├── views.py        # API views
│   │   ├── urls.py         # API routes
│   │   └── admin.py        # Admin configuration
│   ├── manage.py
│   └── requirements.txt
│
└── frontend/               # React Frontend
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── components/     # React components
    │   │   ├── Navbar.js
    │   │   ├── HeroSection.js
    │   │   ├── About.js
    │   │   ├── Resume.js
    │   │   ├── Portfolio.js
    │   │   ├── ContactForm.js
    │   │   └── Footer.js
    │   ├── context/        # React context
    │   │   └── ThemeContext.js
    │   ├── utils/          # Utility functions
    │   │   └── api.js      # API calls
    │   ├── App.js
    │   ├── index.js
    │   └── index.css
    ├── package.json
    └── tailwind.config.js
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+ and npm
- Git

### Backend Setup (Django)

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment**:
   ```bash
   # On Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and update configuration as needed.

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```
   Follow prompts to create admin account.

7. **Create media directory**:
   ```bash
   mkdir media
   ```

8. **Run development server**:
   ```bash
   python manage.py runserver
   ```

   Backend will be available at: `http://localhost:8000`
   Admin panel at: `http://localhost:8000/admin`

### Frontend Setup (React)

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create environment file**:
   ```bash
   cp .env.example .env
   ```
   The default API URL is already set to `http://localhost:8000/api`

4. **Run development server**:
   ```bash
   npm start
   ```

   Frontend will be available at: `http://localhost:3000`

## 📝 Usage

### Adding Projects

1. Navigate to Django admin panel: `http://localhost:8000/admin`
2. Login with superuser credentials
3. Click on "Projects" → "Add Project"
4. Fill in project details:
   - Title
   - Description
   - Image (optional)
   - GitHub Link (optional)
   - Live Link (optional)
   - Technologies (comma-separated)
   - Project Type
5. Save the project

The project will automatically appear on the frontend portfolio section!

### Customizing Content

#### Update Personal Information

Edit the following files to customize your content:

- **HeroSection**: `frontend/src/components/HeroSection.js`
  - Update name, title, tagline
  - Update social media links
  - Update profile image/initials

- **About**: `frontend/src/components/About.js`
  - Update bio text
  - Update fun facts

- **Resume**: `frontend/src/components/Resume.js`
  - Update education, experience, skills, certifications

- **Footer**: `frontend/src/components/Footer.js`
  - Update contact information

#### Update Colors/Theme

Edit `frontend/tailwind.config.js` to customize colors and theme.

## 🔌 API Endpoints

### Projects

- `GET /api/projects/` - List all projects
- `POST /api/projects/` - Create new project
- `GET /api/projects/{id}/` - Retrieve specific project
- `PUT /api/projects/{id}/` - Update project
- `PATCH /api/projects/{id}/` - Partial update project
- `DELETE /api/projects/{id}/` - Delete project

## 🛠️ Technologies Used

### Backend
- Django 5.0
- Django REST Framework
- Django CORS Headers
- Pillow (image handling)
- SQLite (default, can use PostgreSQL in production)

### Frontend
- React 18
- Tailwind CSS 3
- Axios
- React Icons
- Context API (state management)

## 📦 Building for Production

### Backend

1. Update `settings.py`:
   - Set `DEBUG = False`
   - Update `ALLOWED_HOSTS`
   - Use environment variables for sensitive data
   - Configure production database (PostgreSQL recommended)

2. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

3. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn portfolio.wsgi:application
   ```

### Frontend

1. Build the production bundle:
   ```bash
   npm run build
   ```

2. Serve the `build` folder using a web server (Nginx, Apache, etc.)

## 🌐 Deployment

### Recommended Platforms

- **Backend**:
  - Heroku
  - DigitalOcean
  - AWS EC2
  - Railway
  - PythonAnywhere

- **Frontend**:
  - Vercel
  - Netlify
  - GitHub Pages
  - AWS S3 + CloudFront

- **Full Stack**:
  - DigitalOcean App Platform
  - Heroku
  - AWS Elastic Beanstalk

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Contact

Your Name - [your.email@example.com](mailto:your.email@example.com)

Project Link: [https://github.com/yourusername/personal-website](https://github.com/yourusername/personal-website)

## 🙏 Acknowledgments

- Icons by [React Icons](https://react-icons.github.io/react-icons/)
- UI inspiration from various portfolio designs
- Built with ❤️ using React and Django

---

Made with ❤️ by [Your Name](https://github.com/yourusername)
