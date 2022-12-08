from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            elif request.user.groups.exists():
                group = request.user.groups.all()[0].name
            else:
                print('You are not allowed to view this page')
                return redirect('/')
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                print('You are not allowed to view this page')
                return redirect('/')
        return wrapper_func
    return decorator

def home_page_filter():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if request.user.is_superuser:
                print('Is super user')
                return view_func(request, *args, **kwargs)

            if group == 'moderator':
                return view_func(request, *args, **kwargs)
            elif group == 'customer':
                print('You are not allowed to view this page')
                pk = request.user.customer.id
                return redirect(f'/users/{pk}')
            elif group == 'duty clerk':
                print('You are not allowed to view this page')
                return redirect('/approved')
        return wrapper_func
    return decorator