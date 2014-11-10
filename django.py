from django import forms
from models import tabla


persona = forms.ModelMultipleChoiceField(required=True,queryset=tabla.objects.all(),
            widget=forms.CheckboxSelectMultiple())



# esta es la clase

class Recommend(models.Model):
  user=models.ForeignKey(User)
  book=models.ForeignKey(BookModel)
  friends=models.ManyToManyField(User, related_name="recommended")

# este es la plantilla
{% for friend in friends %}

<input type="checkbox" name="recommendations" id="option{{friend.id}}" value={{friend.username}} />
<label for="option{{friend.id}}"><b>{{friend.username}}</b></label><br />

{% endfor %}

# esta es la vista
if request.method == 'POST': 
  recommendations=request.POST.getlist('recommendations')

