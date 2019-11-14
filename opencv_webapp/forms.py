from django import forms
from .models import ImageUploadModel

class ImageUploadForm(forms.ModelForm):
    # 이 Form을 만들기 위해 ImageUploadModel을 쓰라고 알려주기 위한 내부 구현
    class Meta:
        model = ImageUploadModel
        # Form을 통해 받고자 하는 Model Class의 field 리스트
        fields = ('description', 'document', )
