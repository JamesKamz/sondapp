
from django import forms
from .models import Question, Choix

class QuestionForm(forms.ModelForm):
    choice1 = forms.CharField(max_length=100)
    choice2 = forms.CharField(max_length=100)
    choice3 = forms.CharField(max_length=100)
    choice4 = forms.CharField(max_length=100)

    class Meta:
        model = Question
        fields = ['question_text', 'choice1', 'choice2', 'choice3', 'choice4' ]

    choice1 = forms.CharField(max_length=100)
    choice2 = forms.CharField(max_length=100)
    choice3 = forms.CharField(max_length=100)
    choice4 = forms.CharField(max_length=100)
    
    def clean(self):
        cleaned_data = super().clean()
        choice1 = cleaned_data.get('choice1')
        choice2 = cleaned_data.get('choice2')
        choice3 = cleaned_data.get('choice3')
        choice4 = cleaned_data.get('choice4')

        if not choice1 or not choice2 or not choice3 or not choice4:
            raise forms.ValidationError("Veuillez fournir 4 choix.")

        return cleaned_data

    def save(self, commit=False):
        instance = super().save(commit=True)

        if commit:
            instance.save()

        Choix.objects.create(
            question=instance,
            choix_texte=self.cleaned_data['choice1']
        )
        Choix.objects.create(
            question=instance,
            choix_texte=self.cleaned_data['choice2']
        )
        Choix.objects.create(
            question=instance,
            choix_texte=self.cleaned_data['choice3']
        )
        Choix.objects.create(
            question=instance,
            choix_texte=self.cleaned_data['choice4']
        )

        return instance