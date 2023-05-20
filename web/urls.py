from . import views
from django.urls import path

app_name='web'

urlpatterns=[
    path("",views.index,name="index"),
    path("about/",views.about,name="about"),
    path("shop/",views.shop,name="shop"),
    path('book-detail/<int:id>/',views.book_detail,name="book-detail"),
    path("contact/",views.contact,name="contact"),
    path("login/",views.login_1,name="login"),
    path('logout/',views.logout,name='logout'),
    path("signup/",views.register_1,name="signup"),
    # path('comments/submit/', views.comment_submit, name='comment_submit'),

]