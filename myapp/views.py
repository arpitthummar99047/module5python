
from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.models import *
# Create your views here.


def home(request):
    context = {}
    if request.method == "POST":
        Product.objects.create(
            Product_id=request.POST["id"],
            product_name=request.POST["pname"]
        )
        context["msg"] = "value updated successfully"
    return render(request, "home.html", context)


def records(request):
    context = {}
    all_records = Product.objects.all()
    # print(dict(all_records))
    context["all_records"] = all_records
    return render(request, "records.html", context)


def delete_record(request, pk):
    delete_data = Product.objects.get(id=pk)
    delete_data.delete()
    return redirect('records')


def update_record(request, pk):
    context = {}
    update_data = Product.objects.get(id=pk)
    context["update_data"] = update_data
    if request.method == "POST":
        update_data.Product_id = request.POST["id"]
        update_data.product_name = request.POST["pname"]
        update_data.save()
        return redirect('records')
    return render(request, "updates.html", context)