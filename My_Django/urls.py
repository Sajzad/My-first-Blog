from django.contrib import admin
from django.urls import path, include
from .import views


urlpatterns = [
	path('registration/', views.user_registration, name='signup'),
    path('admin/', admin.site.urls),
	path('login/', views.user_login, name="login"),
	path('logout/', views.user_logout, name="logout"),
	path('home/', views.home, name="home"),
	path('blog/', include('blog_post.urls'), name='blog'),
	path('expense/', include('cost.urls'), name='expense'),
	path('user/',include('user_info.urls'), name='user'),
	path('user-form/', include('form.urls'), name= 'form'),
	path('D-info/', include('information.urls'), name= 'D-info'),
	
]
