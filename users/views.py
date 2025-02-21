from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from users.serializers import RegisterSerializer, AuthSerializer, ConfirmUserSerializer
from users.models import ConfirmationCode
import random


@api_view(['POST'])
def authorization_api_view(request):
    serializer = AuthSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'key': token.key})

    return Response(status=status.HTTP_401_UNAUTHORIZED,
                    data={'error': 'User credentials are wrong or user is not active!'})


@api_view(['POST'])
def registration_api_view(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    password = serializer.validated_data['password']
    email = serializer.validated_data.get('email')

    user = User.objects.create_user(username=username, password=password, email=email, is_active=False)
    confirmation_code = random.randint(100000, 999999)
    ConfirmationCode.objects.create(user=user, code=confirmation_code)

    return Response(data={'message': 'Пользователь зарегистрирован. Код подтверждения отправлен.'},
                    status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = ConfirmUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data['username']
    code = serializer.validated_data['code']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден!'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        confirmation_code = ConfirmationCode.objects.get(user=user, code=code)
    except ConfirmationCode.DoesNotExist:
        return Response({'error': 'Неправильный код подтверждения!'}, status=status.HTTP_400_BAD_REQUEST)


    user.is_active = True
    user.save()
    confirmation_code.delete()
    token, _ = Token.objects.get_or_create(user=user)

    return Response({
        'message': 'Пользователь успешно подтвержден.','token': token.key}, status=status.HTTP_200_OK)