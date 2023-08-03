import random
import sys
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from prime_antique.models import user,category,product,payment,order,feedback,cart,product_details, order_item
from prime_antique.forms import categoryForm,productForm,orderForm,cartForm,userForm,productDetailForm,orderItemForm,feedbackForm,paymentForm
from prime_antique.functions import handle_uploaded_file, handle_uploaded_file_certy


#------------------------Show Data---------------------------------------

def user_table(request):
    usr = user.objects.all()
    return render(request,'user.html', {'user': usr})

def category_table(request):
    cat = category.objects.all()
    return render(request,'category.html',{'category':cat})

def product_table(request):
    prd = product.objects.all()
    return render(request,'product.html',{'product':prd})

def productDetails_table(request):
    prddtl = product_details.objects.all()
    return render(request,"productdetails.html",{'prddetails':prddtl})

def cart_table(request):
    crt = cart.objects.all()
    return render(request, "cart.html", {'cart': crt})

def order_table(request):
    ordr = order.objects.all()
    return render(request, "order.html", {'order': ordr})

def order_item_table(request):
    orditm = order_item.objects.all()
    return render(request,'order_item.html',{'orderitem':orditm})

def payment_table(request):
    pymt = payment.objects.all()
    return render(request, "payment.html", {'payment': pymt})

def feedback_table(request):
    fdbk = feedback.objects.all()
    return render(request, "feedback.html", {'feedback': fdbk})


#------------------------Delete Data-------------------------------------

def delete_category(request, id):
    cat = category.objects.get(category_id=id)
    cat.delete()
    return redirect("/category_table")

def delete_product(reqeust, id):
    prdt = product.objects.get(product_id=id)
    prdt.delete()
    return redirect("/product_table")

def delete_productDetails(reqeust, id):
    prdtdtl = product_details.objects.get(product_details_id=id)
    prdtdtl.delete()
    return redirect("/productDetails_table")

def delete_cart(reqeust, id):
    crt = cart.objects.get(cart_id=id)
    crt.delete()
    return redirect("/cart_table")


def delete_order(reqeust, id):
    ordr = order.objects.get(order_id=id)
    ordr.delete()
    return redirect("/order_table")

def delete_order_item(reqeust, id):
    ordr = order_item.objects.get(order_item_id=id)
    ordr.delete()
    return redirect("/orderItem_table")

def delete_payment(reqeust, id):
    pymt = payment.objects.get(payment_id=id)
    pymt.delete()
    return redirect("/payment_table")


def delete_feedback(reqeust, id):
    fdbk = feedback.objects.get(feedback_id=id)
    fdbk.delete()
    return redirect("/feedback_table")


#------------------------Insert Data-------------------------------------

def insert_Category(request):
    category_records = category.objects.all()
    if request.method == "POST":
        form = categoryForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/category_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = categoryForm()

    return render(request, 'insert_category.html', {'form': form, 'category': category_records})

def insert_Product(request):
    category_records = category.objects.all()
    user_records = user.objects.all()
    if request.method == "POST":
        form = productForm(request.POST, request.FILES)
        print("=====", request.POST.get('product_image'))
        print("-------------", form.errors)
        if form.is_valid():
            try:
                handle_uploaded_file(request.FILES['product_image']),
                form.save()
                return redirect('/product_table')

            except:
                print("---------------", sys.exc_info())
    else:
        form = productForm()

    return render(request, 'insert_product.html', {'form': form, 'category': category_records, 'user':user_records})

def insert_ProductDetails(request):
    product_records = product.objects.all()
    if request.method == "POST":
        form = productDetailForm(request.POST)
        print("-------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/productDetails_table')

            except:
                print("---------------", sys.exc_info())
    else:
        form = productDetailForm()

    return render(request, 'insert_productdetails.html', {'form': form, 'product':product_records})

def insert_Cart(request):
    user_records = user.objects.all()
    product_record = product.objects.all()
    if request.method == "POST":
        form = cartForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/cart_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = cartForm()

    return render(request, 'insert_cart.html', {'form': form, 'user': user_records, 'product': product_record})

def insert_Order(request):
    user_records = user.objects.all()
    if request.method == "POST":
        form = orderForm(request.POST, request.FILES)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                handle_uploaded_file_certy(request.FILES['order_certificate']),
                form.save()
                return redirect('/order_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = orderForm()

    return render(request, 'insert_order.html', {'form': form, 'user': user_records})

def insert_OrderItem(request):
    ordritm_records = order_item.objects.all()
    ordr_records = order.objects.all()
    if request.method == "POST":
        form = orderItemForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/orderItem_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = orderItemForm()

    return render(request, 'insert_order_item.html', {'form': form, 'orderitem': ordritm_records, 'order': ordr_records})

def insert_Payment(request):
    order_records = order.objects.all()
    if request.method == "POST":
        form = paymentForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/payment_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = paymentForm()

    return render(request, 'insert_payment.html', {'form': form, 'order': order_records})

def insert_Feedback(request):
    user_records = user.objects.all()
    product_record = product.objects.all()
    if request.method == "POST":
        form = feedbackForm(request.POST)
        print("-------------", form.errors)

        if form.is_valid():
            try:
                form.save()
                return redirect('/feedback_table')
            except:
                print("---------------", sys.exc_info())
    else:
        form = feedbackForm()

    return render(request, 'insert_feedback.html', {'form': form, 'user': user_records, 'product': product_record})

#-----------------------------Update Data------------------------------------

def select_category(request, id):
    cat = category.objects.get(category_id=id)
    return render(request, 'update_category.html', {'category': cat})

def update_Category(request, id):
    cat = category.objects.get(category_id=id)
    form = categoryForm(request.POST, instance=cat)
    if form.is_valid():
        form.save()
        return redirect("/category_table")
    return render(request, 'update_category.html', {'category': cat})


def select_product(request, id):
    prd = product.objects.get(product_id=id)
    cat = category.objects.all()
    usr = user.objects.all()
    return render(request, 'update_product.html', {'category': cat, 'product':prd, 'user':usr})

def update_Product(request, id):
    prd = product.objects.get(product_id=id)
    cat = category.objects.all()
    usr = user.objects.all()
    form = productForm(request.POST, request.FILES, instance=prd)
    print("-------------", form.errors)
    if form.is_valid():
        handle_uploaded_file(request.FILES['product_image']),
        form.save()

        return redirect("/product_table")
    return render(request, 'update_product.html', {'category': cat, 'product':prd, 'user':usr})


def select_productdetails(request, id):
    prddtl = product_details.objects.get(product_details_id=id)
    prd = product.objects.all()
    return render(request, 'update_productdetails.html', {'productdetails':prddtl, 'product':prd})

def update_ProductDetails(request, id):
    prddtl = product_details.objects.get(product_details_id=id)
    prd = product.objects.all()
    form = productDetailForm(request.POST, instance=prddtl)
    print("-------------", form.errors)
    if form.is_valid():
        form.save()
        return redirect("/productDetails_table")
    return render(request, 'update_product.html', {'productdetails':prddtl, 'product':prd})

def select_order(request, id):
    ord = order.objects.get(order_id=id)
    usr_records = user.objects.all()
    return render(request, 'update_order.html', {'order': ord, 'user': usr_records})

def update_Order(request, id):
    ord = order.objects.get(order_id=id)
    usr_records = user.objects.all()
    form = orderForm(request.POST, request.FILES, instance=ord)
    if form.is_valid():
        handle_uploaded_file_certy(request.FILES['order_certificate']),
        form.save()
        return redirect("/order_table")
    return render(request, 'update_order.html', {'order': ord, 'user': usr_records })


def select_cart(request, id):
    crt = cart.objects.get(cart_id=id)
    usr_records = user.objects.all()
    prod_records = product.objects.all()
    return render(request, 'update_cart.html', {'cart': crt, 'user': usr_records, 'product': prod_records})

def update_Cart(request, id):
    crt = cart.objects.get(cart_id=id)
    usr_records = user.objects.all()
    prod_records = product.objects.all()
    form = cartForm(request.POST, instance=crt)
    if form.is_valid():
        form.save()
        return redirect("/cart_table")
    return render(request, 'update_cart.html', {'cart': crt, 'user': usr_records, 'product': prod_records})

#----------------------------------------------------------------------------------------
# Dashboard
def dashboard(request):
    u = user.objects.all().count()
    ordr = order.objects.all()
    o = order.objects.all().count()
    p = product.objects.all().count()
    f = feedback.objects.all().count()
    return render(request, "dashboard.html", {'order': ordr, 'user': u, 'ordr': o, 'product': p, 'feedback':f})

# ---------------------------------Login,Logout Forget & Reset Password---------------------------------------
def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = user.objects.filter(email=email, password=password, role_id=1).count()
        print("--------------", email, "---------", password)
        if val == 1:
            data = user.objects.filter(email=email, password=password, role_id=1)
            for item in data:
                request.session['admin_email'] = item.email
                request.session['admin_password'] = item.password
                request.session['admin_user_id'] = item.user_id
            if request.POST.get("remember"):  # remember :it's a checkbox name.(in html page)
                response = redirect("/dashboard/")
                response.set_cookie('cookie_admin_email', request.POST[
                    "email"])  # cemail is a key     #email : it's a textbox name (in html page)
                response.set_cookie('cookie_admin_password', request.POST[
                    "password"])  # cpass is a key       #password: it's a textbox name(in html page)
                return response
            return redirect('/dashboard/')
        else:
            messages.error(request, "Invalid user name and password")
            return redirect('/login/')
    else:
        if request.COOKIES.get("cookie_admin_email"):
            return render(request, "login.html",
                          {'c_admin_email': request.COOKIES['cookie_admin_email'],
                           'c_admin_password': request.COOKIES[
                               'cookie_admin_password']})  # cookie1 and cookie2 are keys
        else:
            return render(request, "login.html")
        return render(request, "login.html")

def logout(request):
    # session for logout
    try:
        del request.session['admin_email']
        del request.session['admin_password']
        del request.session['admin_user_id']
        return redirect("/login/")
    except:
        pass
        return redirect("/login/")

# Forget
def forget_password(request):
    return render(request, 'forget_password.html')

# Sending OTP
def sendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e
    print("-------------", e)

    obj = user.objects.filter(email=e).count()

    if obj == 1:
        val = user.objects.filter(email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)
        return render(request, 'set_password.html')

# Reseting a password
def set_password(request):
    if request.method == "POST":

        T_otp = request.POST['OTP']
        T_pass = request.POST['pass']
        T_cpass = request.POST['rpass']

        if T_pass == T_cpass:
            e = request.session['temail']

            val = user.objects.filter(email=e, otp=T_otp, otp_used=0).count()

            if val == 1:
                user.objects.filter(email=e).update(otp_used=1, password=T_pass)
                return redirect("/login/")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "set_password.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "set_password.html")

    else:
        return redirect("/forget_password")

def profile(request):
    a_id = request.session['admin_user_id']
    u = user.objects.get(user_id=a_id)
    dob = u.dob
    date = dob.strftime("%Y-%m-%d")
    print("====", dob)
    return render(request, "profile.html", {'ca': u, 'date': date})

def update_profile(request):
    a_id = request.session['admin_user_id']
    u = user.objects.get(user_id=a_id)
    form = userForm(request.POST, instance=u)
    print("-------------", form.errors)
    if form.is_valid():
        try:
            form.save()
            return redirect("/dashboard/")
        except:
            print("---------------", sys.exc_info())
    else:
        pass
    return render(request, "profile.html", {'ca': u})

def api_show(request):
    usrdtl = user.objects.all()
    usrjson=[]
    for data in usrdtl:
        dtls={"name":data.name,"email":data.email,"password":data.password}
        usrjson.append(dtls)
    return JsonResponse(usrjson,safe=False)