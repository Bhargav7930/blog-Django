from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from rest_framework.response import Response

class RegisterView(APIView):
    def post(self, request):
        response ={}
        response["status"]= 500
        response["message"]="went wrong message"
        try:
            data = request.data

            if data.get('username') is None:
                response['message']="key username not found"
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message']="key password not found"
                raise Exception('key password not found')
            check_user = User.objects.filter(username =data.get('username')).first()

            if check_user:
                response['message']="username already taken"
                raise Exception('username already taken')

            user_obj=User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['message']="user created successfully"
            response['status']= 200

        except Exception as e:
            print(e)
        return Response(response)

RegisterView=RegisterView.as_view()


class LoginView(APIView):

    def post(self, request):
        response ={}
        response['status']= 500
        response['message']="something went wrong"
        try:
            data = request.data

            if data.get('username') is None:
                response['message']="key username not found"
                raise Exception('key username not found')
            if data.get('password') is None:
                response['message']="key password not found"
                raise Exception('key password not found')
            check_user = User.objects.filter(username =data.get('username')).first()
            if check_user is None:
                response['message']="invalid user not found"
                raise Exception('invalid user not found')
            user_obj = authenticate(username=data.get('username'),password=data.get('password'))
            if user_obj:
                login(request,user_obj)
                response['status']= 200
                response['message']="welcome"
            else:
                response['message']="invalid password"
                raise Exception('invalid password or username')

        except Exception as e:
            print(e)
        return Response(response)

LoginView=LoginView.as_view()