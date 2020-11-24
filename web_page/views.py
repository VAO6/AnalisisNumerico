from django.shortcuts import render
from web_page.models import Project
from .forms import InputForm, InputForm2, InputForm3, InputForm4, InputForm5, InputForm6
from .src.methods.busquedas import Busquedas
from .src.methods.biseccion import Biseccion
from .src.methods.newton import Newton
from .src.methods.regla_falsa import ReglaFalsa
from .src.methods.gauss import Gauss
from .src.methods.piv_par import Piv_par
from .src.methods.piv_tot import Piv_tot
from .src.methods.diferenciasDivididas import diferenciasDivididas
from .src.methods.gseidel import Gausseidel
from .src.methods.jacobi import Jacobi


def web_page_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'web_page_index.html', context)

def web_page_detail(request, pk):
    if pk==2:
        return web_page_detail2(request, pk)
    if pk==3:
        return web_page_detail3(request, pk)
    if pk==4:
        return web_page_detail4(request, pk)
    if pk==8:
        return web_page_detail5(request, pk)
    if pk==9:
        return web_page_detail6(request, pk)
    if pk==10:
        return web_page_detail7(request, pk)
    if pk==11:
        return web_page_detail8(request, pk)
    if pk==13:
        return web_page_detail9(request, pk)
    if pk==14:
        return web_page_detail10(request, pk)
        
    project = Project.objects.get(pk=pk)
    form = InputForm()
    a = None
    b = None
    function = None
    iterations = None
    error = None
    method = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            function = form.cleaned_data['function']
            iterations = form.cleaned_data['iterations']
            error = form.cleaned_data['error']
        method = Biseccion(function, a, b, iterations, error)
    try:
        result = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
    
    context = {
        'project': project,
        'a': a,
        'b': b,
        'form': form,
        'iterations': iterations,
        'function': function,
        'error': error,
        'result': result
    }
    
    return render(request, 'web_page_detail.html', context)
    
def web_page_detail2(request, pk):
    project = Project.objects.get(pk=pk)
    form = InputForm2()
    x = None
    function = None
    iterations = None
    delta = None
    method = None
    result = ''

    if request.method == 'POST':
        form = InputForm2(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            function = form.cleaned_data['function']
            iterations = form.cleaned_data['iterations']
            delta = form.cleaned_data['delta']
        method = Busquedas(function, x, delta, iterations)
    try:
        result = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
    
    context = {
        'project': project,
        'x': x,
        'form': form,
        'iterations': iterations,
        'function': function,
        'delta': delta,
        'result': result
    }
    
    return render(request, 'web_page_detail2.html', context)
    
def web_page_detail3(request, pk):
    project = Project.objects.get(pk=pk)
    form = InputForm3()
    x = None
    function = None
    iterations = None
    tol = None
    method = None
    result = []

    if request.method == 'POST':
        form = InputForm3(request.POST)
        if form.is_valid():
            x = form.cleaned_data['x']
            function = form.cleaned_data['function']
            iterations = form.cleaned_data['iterations']
            tol = form.cleaned_data['tol']
        method = Newton(function, x, tol, iterations)
    try:
        result = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'x': x,
        'form': form,
        'iterations': iterations,
        'function': function,
        'tol': tol,
        'result': result
    }
    
    return render(request, 'web_page_detail3.html', context)

def web_page_detail4(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm()
    a = None
    b = None
    function = None
    iterations = None
    error = None
    method = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            function = form.cleaned_data['function']
            iterations = form.cleaned_data['iterations']
            error = form.cleaned_data['error']
        method = ReglaFalsa(function, a, b, iterations, error)
    try:
        result = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'a': a,
        'b': b,
        'form': form,
        'iterations': iterations,
        'function': function,
        'error': error,
        'result': result
    }
    
    return render(request, 'web_page_detail.html', context)

def web_page_detail5(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm4()
    matrix = None
    b = None

    if request.method == 'POST':
        form = InputForm4(request.POST)
        if form.is_valid():
            matrix = form.cleaned_data['matrix']
            b = form.cleaned_data['b']
        method = Gauss(matrix, b)
    try:
        result, x = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'matrix': matrix,
        'b': b,
        'form': form,
        'result': result,
        'x': x
    }
    
    return render(request, 'web_page_detail4.html', context)

def web_page_detail6(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm4()
    matrix = None
    b = None

    if request.method == 'POST':
        form = InputForm4(request.POST)
        if form.is_valid():
            matrix = form.cleaned_data['matrix']
            b = form.cleaned_data['b']
        method = Piv_par(matrix, b)
    try:
        result, x = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'matrix': matrix,
        'b': b,
        'form': form,
        'result': result,
        'x': x
    }
    
    return render(request, 'web_page_detail4.html', context)

def web_page_detail7(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm4()
    matrix = None
    b = None

    if request.method == 'POST':
        form = InputForm4(request.POST)
        if form.is_valid():
            matrix = form.cleaned_data['matrix']
            b = form.cleaned_data['b']
        method = Piv_tot(matrix, b)
    try:
        result, x = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'matrix': matrix,
        'b': b,
        'form': form,
        'result': result,
        'x': x
    }
    
    return render(request, 'web_page_detail4.html', context)

def web_page_detail8(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm5()
    X = None
    Y = None

    if request.method == 'POST':
        form = InputForm5(request.POST)
        if form.is_valid():
            X = form.cleaned_data['X']
            Y = form.cleaned_data['Y']
        method = diferenciasDivididas(X, Y)
    try:
        result, x, pol = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
        pol = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'X': X,
        'Y': Y,
        'form': form,
        'result': result,
        'x': x,
        'pol': pol
    }
    
    return render(request, 'web_page_detail5.html', context)

def web_page_detail9(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm6()
    matrix = None
    b = None
    tol = None
    x0 = None
    iteration = None

    if request.method == 'POST':
        form = InputForm6(request.POST)
        if form.is_valid():
            matrix = form.cleaned_data['matrix']
            b = form.cleaned_data['b']
            tol = form.cleaned_data['tol']
            x0 = form.cleaned_data['x0']
            iteration = form.cleaned_data['iteration']
        method = Gausseidel(matrix, b, x0, tol, iteration)
    try:
        T, C, result, x, iterations, error = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
        T = ['An error ocurred, try again with valid parameters']
        C = ['An error ocurred, try again with valid parameters']
        iterations = ['An error ocurred, try again with valid parameters']
        error = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'T': T,
        'C': C,
        'form': form,
        'result': result,
        'x': x,
        'iteration': iterations,
        'error': error
    }
    
    return render(request, 'web_page_detail6.html', context)

def web_page_detail10(request, pk):        
    project = Project.objects.get(pk=pk)
    form = InputForm6()
    matrix = None
    b = None
    tol = None
    x0 = None
    iteration = None

    if request.method == 'POST':
        form = InputForm6(request.POST)
        if form.is_valid():
            matrix = form.cleaned_data['matrix']
            b = form.cleaned_data['b']
            tol = form.cleaned_data['tol']
            x0 = form.cleaned_data['x0']
            iteration = form.cleaned_data['iteration']
        method = Jacobi(matrix, b, x0, tol, iteration)
    try:
        T, C, result, x, iterations, error = method.run()
    except:
        result = ['An error ocurred, try again with valid parameters']
        x = ['An error ocurred, try again with valid parameters']
        T = ['An error ocurred, try again with valid parameters']
        C = ['An error ocurred, try again with valid parameters']
        iterations = ['An error ocurred, try again with valid parameters']
        error = ['An error ocurred, try again with valid parameters']
    context = {
        'project': project,
        'T': T,
        'C': C,
        'form': form,
        'result': result,
        'x': x,
        'iteration': iterations,
        'error': error
    }
    
    return render(request, 'web_page_detail6.html', context)