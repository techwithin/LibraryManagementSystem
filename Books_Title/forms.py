from django import forms

class SearchField(forms.Form):
    searchinput = forms.CharField(max_length = 100, label = "Search Book")

    class Meta:
        fields = ["searchinput",]