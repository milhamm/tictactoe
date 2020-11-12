from django.shortcuts import render

# Create your views here.

def index(req):
    nama = "Aang"
    num_of_rows = 3
    context = {'nama':nama, 'range':range(num_of_rows ** 2), 'num_of_rows': num_of_rows}
    return render(req, 'tictactoe_app/index.html', context)