from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from PruebaDjangoApp.models.user import User
from PruebaDjangoApp.serializers.userSerializer import UserSerializer
from django.http import JsonResponse

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail': 'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        # Enviar una respuesta JSON con la URL de redirección
        redirect_url = '/user/home/'  # Ruta de la página de administración del usuario
        return JsonResponse({'redirect': redirect_url})
