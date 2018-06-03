from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django import forms
from .models import Blogs,UserProfile
#from .models import Name
from django.forms import ModelForm


class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    class Meta:
        model=User
        fields=(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            #'phoneNo',
            #'image'
        )
    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name=self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user
class EditProfileForm(UserChangeForm):
     class Meta:
         model=User
         fields=(
             'email',
             'first_name',
             'last_name',
             'password'
             #'__all__'
         )

class DateInput(forms.DateInput):
    input_type = 'date'

class Userprofileform(forms.ModelForm):
    class Meta():
        model= UserProfile
        fields=('__all__')

class BlogForm(forms.ModelForm):
    class Meta():
        model= Blogs
        fields=('__all__')

        def save(request):
            user = request.user()
        #exclude=('history')
        """fields = (
            'user',
            'title',
            'task_id',
            'priority',
            'status',
            'resource_name',
            'effort_estimated',
            'actual_start_date',
            'deadline',
            'actual_effort',
            'actual_date_completion',
            'resource_score',
            'reason'
        )"""

  #  class Meta:
   #     model=Name
    #    fields='__all__'



#        widgets = {
 #           'actual_start_date': DateInput(),
  #          'deadline': DateInput(),
   #         'actual_date_completion': DateInput(),
    #    }