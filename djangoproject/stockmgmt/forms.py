from django import forms
from stockmgmt.models import Stock,StockHistory,Category

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name']

class StockSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category', 'item_name']


class StockHistorySearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = StockHistory
        fields = ['start_date', 'end_date']

class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category', 'item_name','quantity']

class ExportForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['export_quantity', 'export_to']

class ImportForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['import_quantity', 'import_by']

class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
