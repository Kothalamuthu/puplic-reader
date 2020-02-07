from django.shortcuts import render
from .forms import UserForm,UserInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from json import loads
from .serializers import UserregisterSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import User
from .models import *
# Create your views here.

@csrf_exempt
def register(request):
    registered = False
    if request.method == 'POST':
        # print(request.POST,request.body)
        data = loads(request.body)
        user_form = UserForm(data=data)
        profile_form = UserInfoForm(data=data)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            print(user)
            profile = profile_form.save(commit=False)
            profile.reader = user
            # print(user)
            profile.save()
            # registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserInfoForm()
    return HttpResponse("doing good")

# @csrf_exempt
class registerSerializers(GenericAPIView):

    def post(self,request):
        registered = False
        serializer_class = UserregisterSerializer

        if request.method == 'POST':
            data = loads(request.body)
            serializer = UserregisterSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            instance = serializer.save()
            data = {}
            data = serializer.data
            data['id'] = instance.id
            print(data)
            return JsonResponse(data)


@csrf_exempt
def loginForm(request):
    if request.method == 'POST':
        data = loads(request.body)
        username = data['username']
        password = data['password']
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     print("user",user)
        #     return HttpResponse("user Login")

        # else:
        j = User.objects.filter(password=password,username=username)
        print(j)
        return HttpResponse("Please Give proper details")


class loginSerializers(GenericAPIView):

    def post(self,request):
        registered = False
        serializer_class = UserregisterSerializer

        if request.method == 'POST':
            data = loads(request.body)
            serializer = UserregisterSerializer(data=data)
            serializer.is_valid(raise_exception=True)

            serializer.save()

            
            return HttpResponse("doing good")