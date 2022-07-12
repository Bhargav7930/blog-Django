from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('',views.home,name='index' ),
    path('login/',views.login_page,name='login' ),
    path('logout/',views.logoutpage,name='logout' ),
    path('register/',views.register_page,name='register' ),
    path('add-blog/',views.add_blog,name='add_blog' ),
    path('blog-detail/<slug>/',views.blog_detail,name='blog_detail' ),
    path('see-blog/',views.see_blog,name='see_blog' ),
    path('blog-delete/<int:id>/',views.blog_delete,name='blog_delete' ),
    path('blog-update/<slug>/',views.blog_update,name='blog_update' ),
    path('user-profile/<int:id>/',views.user_profile,name='user_profile' ),
]
