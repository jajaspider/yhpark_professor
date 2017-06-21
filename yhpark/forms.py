from django import forms
from .models import Notice

class Notice_Write(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ('title','contents','notice_url')

    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.fields['file'].required = False
