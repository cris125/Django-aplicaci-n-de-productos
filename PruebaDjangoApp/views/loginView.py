from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pagina_administracion_usuario')  
        else:
            from django.template import loader
            from django.http import HttpResponse
            template = loader.get_template('login.html')
            loginn="Login"
            signupn="Sing Up"
            context = {
                'login': loginn,
                'signup':signupn,}          
            return render(request, 'login.html',context, {'error': 'Credenciales inválidas'})
    else:
        loginn="Login"
        signupn="Sing Up"
        context = {
                'login': loginn,
                'signup':signupn,}
        return render(request, 'login.html',context)
    
def logout_view(request):
    logout(request)
    # Redirige al usuario a una página de tu elección después del logout.
    return redirect('/login/')       