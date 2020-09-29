from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
import csv
from django.urls import reverse
from stockmgmt_2.models import Stock_2,Category_2,StockHistory_2
from stockmgmt_2.forms import StockCreateForm_2, StockHistorySearchForm_2, StockSearchForm_2, StockUpdateForm_2, ExportForm_2, ImportForm_2, ReorderLevelForm_2, CategoryForm_2
from django.contrib import messages
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def list_product(request):
    factory_title = 'MARUYAMA OTA FACTORY'
    title = 'List of Stock Product'
    form = StockSearchForm_2(request.POST or None)
    queryset = Stock_2.objects.all()
    dict = {
        'title': title ,
        'factory_title':factory_title,
        'form':form,
        'queryset':queryset}

    if request.method == 'POST':
        category = form['category'].value()
        queryset = StockHistory_2.objects.filter(item_name__icontains=form['item_name'].value())
        if (category != ''):
            queryset = queryset.filter(category_id=category)
        dict = {
            'title': title,
            'factory_title':factory_title,
            'form':form,
            'queryset':queryset}

        if form['export_to_CSV'].value()==True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition']='attachment; filename="List of product.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY','ITEM NAME','QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response
    return render(request, 'list_product.html', context=dict)

@login_required
def list_product_history(request):
    factory_title = 'MARUYAMA OTA FACTORY'
    title = 'EXPORT / IMPORT  HISTORY'
    queryset = StockHistory_2.objects.all()
    form = StockHistorySearchForm_2(request.POST or None)
    dict = {
        'title':title,
        'queryset':queryset ,
        'form':form,
        'factory_title':factory_title}

    if request.method == 'POST':
        queryset = StockHistory_2.objects.filter(
                                	last_updated__range=[
                                							form['start_date'].value(),
                                							form['end_date'].value()
                                						]
                                	)
        if form['export_to_CSV'].value()==True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition']='attachment; filename="Export/Import_Ota_Factory.csv"'
            writer = csv.writer(response)
            writer.writerow([
                'CATEGORY',
                'ITEM NAME',
                'QUANTITY',
                'EXPORT',
                'EXPORT BY',
                'IMPORT',
                'IMPORT BY',
                'LAST UPDATED'
                ])
            instance = queryset
            for stock in instance:
                writer.writerow([
                    stock.category,
                    stock.item_name,
                    stock.quantity,
                    stock.export_quantity,
                    stock.export_by,
                    stock.import_quantity,
                    stock.import_by,
                    stock.last_updated
                    ])
            return response
    dict = {
        'title':title,
        'queryset':queryset,
        'form':form,
        'factory_title':factory_title}
    return render(request, 'list_product_history.html', context=dict)

@login_required
def add_product(request):
    factory_title = 'MARUYAMA OTA FACTORY'
    title = 'Add Product'
    form = StockCreateForm_2(request.POST or None)
    if form.is_valid():
        form.save()
    dict = {
        'title':title,
        'factory_title':factory_title,
        'form':form}
    return render(request, 'add_product.html', context=dict)

def update_product(request,pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    title = 'Update Product'
    queryset = Stock_2.objects.get(id=pk)
    form = StockUpdateForm_2(instance=queryset)
    if request.method == 'POST':
        form = StockUpdateForm_2(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Successfully')
            return HttpResponseRedirect(reverse('stockmgmt_2:list_product'))
    dict = {
        'title':title,
        'form':form,
        'queryset':queryset,
        'factory_title':factory_title}
    return render(request, 'add_items.html', context=dict)

def delete_product(request, pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    queryset = Stock_2.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, 'Delete Successfully')
        return HttpResponseRedirect(reverse('stockmgmt_2:list_product'))
    dict = {
        'factory_title':factory_title
    }
    return render (request, 'delete_items.html', context=dict)

@login_required
def export_product(request,pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    queryset = Stock_2.objects.get(id=pk)
    form = ExportForm_2(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.import_quantity = 0
        if instance.quantity - instance.export_quantity>=0:
            instance.quantity -= instance.export_quantity
            instance.export_by = str(request.user)
            messages.success(request, "Export " + str(instance.export_quantity) + " " + str(instance.item_name)+ " Successfully || " + str(instance.quantity)+" " + str(instance.item_name) + "s now left in Store")
            instance.save()
            return redirect('stockmgmt_2:stock_details_product', pk=str(instance.id))
        else:
            messages.success(request, 'Product are not enough')
    dict={
        'title':'Export ' + str(queryset.item_name),
        'queryset':queryset,
        'form':form,
        'username': 'Export By : '+str(request.user)}
    return render(request, 'add_product.html', context=dict)

@login_required
def import_product(request,pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    queryset = Stock_2.objects.get(id=pk)
    form = ImportForm_2(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.export_quantity = 0
        instance.quantity += instance.import_quantity
        instance.save()
        messages.success(request, "Import " + str(instance.import_quantity) + " " + str(instance.item_name)+ " Successfully || " + str(instance.quantity)+ " "+str(instance.item_name)+ "s now in store")
        return redirect('stockmgmt_2:stock_details_product', pk=str(instance.id))
    dict={
        'title': 'Import '+ str(queryset.item_name),
        'queryset':queryset,
        'form':form,
        'username':'Import By:' +str(request.user)}
    return render(request, 'add_product.html', context=dict )

@login_required
def stock_details_product(request, pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    queryset = Stock_2.objects.get(id=pk)
    dict = {
        'queryset':queryset,
        'factory_title':factory_title}
    return render(request, 'stock_details_product.html', context=dict)

@login_required
def reorder_product_level(request, pk):
    factory_title = 'MARUYAMA OTA FACTORY'
    queryset = Stock_2.objects.get(id=pk)
    form = ReorderLevelForm_2(request.POST or None, instance=queryset)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Reorder level for ' + str(instance.item_name) + ' is updated to '+ str(instance.reorder_level))
        return HttpResponseRedirect(reverse('stockmgmt_2:list_product'))

    dict = {
        'instance':queryset,
        'form':form,
        'factory_title':factory_title}
    return render(request, 'add_product.html', context=dict)
