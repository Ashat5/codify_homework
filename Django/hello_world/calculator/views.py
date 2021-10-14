from django.shortcuts import render
from calculator.forms import MyForm
# Create your views here.


def get_result(request):
    result = None
    if request.method == "POST":
        data = request.POST
        my_form = MyForm(data = data)
        if my_form.is_valid():
            first_number = my_form.cleaned_data['first_number']
            second_number = my_form.cleaned_data['second_number']
            operation = my_form.cleaned_data['operation']
            print(first_number, second_number, operation)
            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '/':
                if second_number != 0:
                    result = first_number / second_number
                    print(result)
                else:
                    result = "You can't divide by zero"
            return render(request, 'calculator.html', {'form': my_form, 'result' : result})
    form = MyForm()        
    return render(request, 'calculator.html', {'form': form})