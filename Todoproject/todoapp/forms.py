from django import forms
from .models import Task 

class TaskForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Add task here...'})
    )
    
    class Meta:
        model = Task
        fields = ['content']
      
class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields = '__all__'       
        
      