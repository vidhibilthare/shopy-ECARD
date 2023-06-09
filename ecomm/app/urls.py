from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.ProductView.as_view(), name="home"),
    path(
        "product-detail/<int:pk>",
        views.ProductDetailView.as_view(),
        name="product-detail",
    ),
    path("add-to-cart/", views.add_to_cart, name="add-to-cart"),
    path("cart/", views.show_cart, name="show_cart"),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path("buy/", views.buy_now, name="buy-now"),
    # path("profile/", views.profile, name="profile"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path("address/", views.address, name="address"),
    path("orders/", views.orders, name="orders"),
    path("changepassword/", views.change_password, name="changepassword"),
    path("mobile/", views.mobile, name="mobile"),
    path("login/", views.login, name="login"),
    # path("registration/", views.customerregistration, name="customerregistration"),
      path('registration/', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path("checkout/", views.checkout, name="checkout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
