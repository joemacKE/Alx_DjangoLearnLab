import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

@pytest.fixture
def user(db):
    return User.objects.create_user(username='john', password='pass12345')

@pytest.fixture
def other_user(db):
    return User.objects.create_user(username='jane', password='pass12345')

@pytest.fixture
def post(user):
    return Post.objects.create(title="Test Post", content="Content here", author=user)

# ----------------
# List View Tests
# ----------------
@pytest.mark.django_db
def test_post_list_view(client, post):
    url = reverse('post-list')
    response = client.get(url)
    assert response.status_code == 200
    assert "Test Post" in response.content.decode()

# ----------------
# Detail View Tests
# ----------------
@pytest.mark.django_db
def test_post_detail_view(client, post):
    url = reverse('post-detail', args=[post.id])
    response = client.get(url)
    assert response.status_code == 200
    assert post.title in response.content.decode()

# ----------------
# Create View Tests
# ----------------
@pytest.mark.django_db
def test_create_post_authenticated(client, user):
    client.login(username='john', password='pass12345')
    url = reverse('post-create')
    data = {"title": "New Post", "content": "New content"}
    response = client.post(url, data)
    assert response.status_code == 302  # Redirect after success
    assert Post.objects.filter(title="New Post").exists()

@pytest.mark.django_db
def test_create_post_unauthenticated(client):
    url = reverse('post-create')
    response = client.get(url)
    assert response.status_code == 302  # Redirect to login

# ----------------
# Update View Tests
# ----------------
@pytest.mark.django_db
def test_update_post_authorized(client, user, post):
    client.login(username='john', password='pass12345')
    url = reverse('post-update', args=[post.id])
    data = {"title": "Updated", "content": "Updated content"}
    response = client.post(url, data)
    post.refresh_from_db()
    assert post.title == "Updated"
    assert response.status_code == 302

@pytest.mark.django_db
def test_update_post_unauthorized(client, other_user, post):
    client.login(username='jane', password='pass12345')
    url = reverse('post-update', args=[post.id])
    response = client.get(url)
    assert response.status_code == 403  # Forbidden

# ----------------
# Delete View Tests
# ----------------
@pytest.mark.django_db
def test_delete_post_authorized(client, user, post):
    client.login(username='john', password='pass12345')
    url = reverse('post-delete', args=[post.id])
    response = client.post(url)
    assert not Post.objects.filter(id=post.id).exists()

@pytest.mark.django_db
def test_delete_post_unauthorized(client, other_user, post):
    client.login(username='jane', password='pass12345')
    url = reverse('post-delete', args=[post.id])
    response = client.post(url)
    assert response.status_code == 403
    assert Post.objects.filter(id=post.id).exists()
