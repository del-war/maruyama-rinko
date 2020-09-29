from django import forms
from stockmgmt_2.models import Stock_2, Category_2, StockHistory_2

class StockCreateForm_2(forms.ModelForm):
    class Meta:
        model = Stock_2
        fields = ['category', 'item_name']

class StockSearchForm_2(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    class Meta:
        model = Stock_2
        fields = ['category', 'item_name']


class StockHistorySearchForm_2(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    class Meta:
        model = StockHistory_2
        fields = ['start_date', 'end_date']

class StockUpdateForm_2(forms.ModelForm):
    class Meta:
        model = Stock_2
        fields = ['category', 'item_name','quantity']

class ExportForm_2(forms.ModelForm):
    class Meta:
        model = Stock_2
        fields = ['export_quantity', 'export_to']

class ImportForm_2(forms.ModelForm):
    class Meta:
        model = Stock_2
        fields = ['import_quantity', 'import_by']

class ReorderLevelForm_2(forms.ModelForm):
    class Meta:
        model = Stock_2
        fields = ['reorder_level']

class CategoryForm_2(forms.ModelForm):
    class Meta:
        model = Category_2
        fields = ['name']
