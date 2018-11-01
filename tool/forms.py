from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "输入关键字/作者/年份"}))

    def clean(self):
        text = self.cleaned_data['text']
        return self.cleaned_data

class Click(forms.Form):
    yesorno = forms.CharField()
    def clean(self):
        yesorno = self.cleaned_data['yesorno']
        return self.cleaned_data