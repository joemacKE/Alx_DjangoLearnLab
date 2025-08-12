# Django Authentication System Documentation

## verview

This authentication system provides the following features:

- User registration with email
- Secure login and logout using Django’s built-in views
- Profile management for authenticated users
- Passwords stored securely using Django’s password hashing
- Access control using login restrictions
- CSRF protection for all forms

## System Components

### 1. Registration

- **File:** `views.py`
- **Form Used:** `UserRegisterForm` (extends `UserCreationForm`)
- **Template:** `templates/users/register.html`
- **URL:** `/register/`

Allows users to create an account

- Fields: `username`, `email`, `password1`, `password2`
- On success: Redirects to login page and shows a success message

### 2. Login

- **View Used:** `LoginView` from `django.contrib.auth.views`
- **Template:** `templates/registration/login.html`
- **URL:** `/login/`

Authenticates users via username and password

- Uses Django’s session framework to maintain login state

### 3. Logout

- **View Used:** `LogoutView` from `django.contrib.auth.views`
- **Template:** `templates/registration/logged_out.html` (optional)
- **URL:** `/logout/`

Logs out the user and clears the session

- Optionally redirects to login or home page

### 4. Profile View & Update

- **View:** `profile()` (custom view with `@login_required`)
- **Forms Used:**
  - `UserUpdateForm` — updates username and email
  - `ProfileUpdateForm` — updates bio and profile picture
- **Template:** `templates/users/profile.html`
- **URL:** `/profile/`

Only accessible when logged in

- Uses two forms to update both User and Profile models
- Includes file upload (profile picture)

### 5. Models and Forms

#### 👤 Profile Model:

- Extends the built-in User model via `OneToOneField`
- Fields: `bio`, `image`
- Auto-created using signals (`post_save`)

#### Forms:

- `UserRegisterForm` – used for registration
- `UserUpdateForm` – used to edit User fields
- `ProfileUpdateForm` – used to edit extended Profile fields

## Security Features

- **CSRF Protection:** All forms use `{% csrf_token %}` and are protected by Django’s `CsrfViewMiddleware`.
- **Password Hashing:** Django uses PBKDF2 by default — secure and salted.
- **Access Control:** Profile view is protected with `@login_required`
- **Form Validation:** Custom forms extend Django’s form classes for built-in validation

## How to Test Each Feature

Run the dev server:

```bash
python manage.py runserver
```
