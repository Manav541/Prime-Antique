from django import forms
from prime_antique.models import user, category, product, cart, order, payment, feedback, product_details, order_item


class userForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ["name", "address", "contact", "email", "password", "dob", "role_id"]


class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ["category_name","subcategory_id"]


class productForm(forms.ModelForm):
    class Meta:
        model = product
        fields = ["category_id", "user_id", "product_name", "product_image",
                  "product_desc"]


class productDetailForm(forms.ModelForm):
    class Meta:
        model = product_details
        fields = ["product_id", "product_details_price", "product_details_qty"]

class cartForm(forms.ModelForm):
    class Meta:
        model = cart
        fields = ["product_id", "user_id", "cart_date", "cart_qty", "total_amt"]


class orderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ["user_id", "contact", "address", "order_date", "order_status", "total_amount", "payment_status", "order_certificate"]


class orderItemForm(forms.ModelForm):
    class Meta:
        model = order_item
        fields = ["order_id", "order_item_date", "order_item_address", "order_item_qty"]


class paymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = ["order_id", "payment_amount", "payment_status", "payment_date"]


class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ["user_id", "product_id", "feedback_date", "feedback_desc"]