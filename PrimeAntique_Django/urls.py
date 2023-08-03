from django.contrib import admin
from django.urls import path
from prime_antique import views

urlpatterns = [

    # ----------------------------Show Data-------------------------------------

    path('admin/', admin.site.urls),
    path('user_table/', views.user_table),
    path('category_table/', views.category_table),
    path('product_table/', views.product_table),
    path('productDetails_table/', views.productDetails_table),
    path('cart_table/', views.cart_table),
    path('order_table/', views.order_table),
    path('orderItem_table/', views.order_item_table),
    path('payment_table/', views.payment_table),
    path('feedback_table/', views.feedback_table),

    # ---------------------------Delete Data-----------------------------------

    path('delete_category/<int:id>', views.delete_category),
    path('delete_product/<int:id>', views.delete_product),
    path('delete_productdetails/<int:id>', views.delete_productDetails),
    path('delete_cart/<int:id>', views.delete_cart),
    path('delete_order/<int:id>', views.delete_order),
    path('delete_order_item/<int:id>', views.delete_order_item),
    path('delete_payment/<int:id>', views.delete_payment),
    path('delete_feedback/<int:id>', views.delete_feedback),

    # -----------------------------Insert Data-------------------------------

    path('insert_category/', views.insert_Category),
    path('insert_product/', views.insert_Product),
    path('insert_productdetails/', views.insert_ProductDetails),
    path('insert_cart/', views.insert_Cart),
    path('insert_order/', views.insert_Order),
    path('insert_order_item/', views.insert_OrderItem),
    path('insert_payment/', views.insert_Payment),
    path('insert_feedback/', views.insert_Feedback),

    # -----------------------------Update Data-------------------------------

    path('select_category/<int:id>', views.select_category),
    path('update_category/<int:id>', views.update_Category),
    path('select_product/<int:id>', views.select_product),
    path('update_product/<int:id>', views.update_Product),
    path('select_productdetails/<int:id>', views.select_productdetails),
    path('update_productdetails/<int:id>', views.update_ProductDetails),
    path('select_order/<int:id>', views.select_order),
    path('update_order/<int:id>', views.update_Order),
    path('select_cart/<int:id>', views.select_cart),
    path('update_cart/<int:id>', views.update_Cart),

    # -----------------------Login-Logout, Forget-Reset------------------------

    path('login/', views.login),
    path('logout/', views.logout),
    path('forget_password/', views.forget_password),
    path('send_otp/', views.sendotp),
    path('reset/', views.set_password),

    # -------------------------Dashboard, Profile----------------------------

    path('dashboard/', views.dashboard),
    path('profile/', views.profile),
    path('update_profile/', views.update_profile),

    path("api_show/",views.api_show),

]
