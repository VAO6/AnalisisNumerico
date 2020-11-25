from django import forms


class InputForm(forms.Form):
    function = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the function f(x) ="
        })
    )
    a = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter A"
        })
    )
    b = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter B"
        })
    )
    iterations = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )
    error = forms.IntegerField(
        # max_length=2,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the error, 10^:"
        })
    )

class InputForm2(forms.Form):
    function = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a function (natural logarithm: log(), euler: exp()):"
        })
    )
    x = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a value that will be the starting point X0:"
        })
    )
    delta = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter delta"
        })
    )
    iterations = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )

class InputForm3(forms.Form):
    function = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a function (natural logarithm: log(), euler: exp()):"
        })
    )
    x = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a value that will be the starting point X0:"
        })
    )
    tol = forms.IntegerField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "How many tolerance do you want: 10^:"
        })
    )
    iterations = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )

class InputForm4(forms.Form):
    matrix = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3):"
        })
    )
    b = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the vector B separated by spaces. Example: (1 1 1):"
        })
    )

class InputForm5(forms.Form):
    X = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter X with each element separated by spaces. Example: (1 1 1):"
        })
    )
    Y = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter Y with each element separated by spaces. Example: (1 1 1):"
        })
    )

class InputForm6(forms.Form):
    matrix = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3):"
        })
    )
    b = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the vector B separated by spaces. Example: (1 1 1):"
        })
    )
    x0 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a value that will be the starting point X0:"
        })
    )
    tol = forms.IntegerField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "How many tolerance do you want: 10^:"
        })
    )
    iteration = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )

class InputForm7(forms.Form):
    function_f = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the function f(x) ="
        })
    )
    function_g = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the function g(x) ="
        })
    )
    a = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter A"
        })
    )
    b = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter B"
        })
    )
    iterations = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )
    error = forms.IntegerField(
        # max_length=2,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the error, 10^:"
        })
    )

class InputForm8(forms.Form):
    function = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the function f(x) ="
        })
    )
    a = forms.FloatField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter A"
        })
    )
    iterations = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )
    error = forms.IntegerField(
        # max_length=2,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the error, 10^:"
        })
    )


class InputForm10(forms.Form):
    matrix = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the matrix, each line separated by a coma (,) and each element of the line separated by space. Example: (1 1 1,2 2 2,3 3 3):"
        })
    )
    b = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the vector B separated by spaces. Example: (1 1 1):"
        })
    )
    xinicial = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter a value that will be the starting point X0:"
        })
    )
    tol = forms.IntegerField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "How many tolerance do you want: 10^:"
        })
    )
    iteration = forms.IntegerField(
        # max_length=4,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the number of maximum iterations"
        })
    )
    w = forms.IntegerField(
        # max_length=5,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter the value of W:"
        })
    )