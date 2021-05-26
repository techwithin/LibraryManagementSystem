from django import forms

class SearchField(forms.Form):
    searchinput = forms.CharField(max_length = 100, label = "Search Book", widget=forms.TextInput(attrs={'placeholder': 'Search here'}))

    class Meta:
        fields = ["searchinput",]