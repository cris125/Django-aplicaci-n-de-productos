from PruebaDjangoApp.models.user import User
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from PruebaDjangoApp.serializers.userSerializer import UserSerializer
from django.shortcuts import redirect

class UserCreateView(views.APIView):

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Check if the user already exists
        username = request.data.get("username")
        if User.objects.filter(username=username).exists():
            return Response({"message": "El usuario ya existe."}, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            user = serializer.save()

            # Generate the JWT token for the user
            refresh = RefreshToken.for_user(user)
            token_data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            # Add the token data to the response for automatic authentication
            response_data = {
                'message': 'Usuario creado exitosamente.',
                'token': token_data,
            }

            # Redirect to the user administration page
            return redirect('pagina_administracion_usuario')
