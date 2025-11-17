from django import forms
from salas.models import Bloco, Sala, Turma, Curso

DIAS_CHOICES = (
    ('segunda', 'Segunda-feira'),
    ('terca', 'Terça-feira'),
    ('quarta', 'Quarta-feira'),
    ('quinta', 'Quinta-feira'),
    ('sexta', 'Sexta-feira'),
    ('sabado', 'Sábado'),
    ('domingo', 'Domingo'),
)

PERIODOS_CHOICES = (
    ('primeiro', '1º Período'),
    ('segundo', '2º Período'),
    ('terceiro', '3º Período'),
    ('quarto', '4º Período'),
    ('integral', 'Integral'),
)
class VerificacaoReserva(forms.Form):
    
    # --- Seção 1: Infos Acadêmicas ---
    id_curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=False, label='Curso')
    id_turma = forms.ModelChoiceField(queryset=Turma.objects.all(), required=True, label="Turma")
    professor = forms.CharField(max_length=255, required=True, label="Professor responsável")

    # --- Seção 2: Local e Vigência --
    id_bloco = forms.ModelChoiceField(Bloco.objects.all(), required=True)
    id_sala = forms.ModelChoiceField(Sala.objects.all(), required=True)
    data_inicial = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    data_final = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    # --- Seção 3: Horários ---
    turno = forms.ChoiceField(choices=[
    ('Matutino', 'Matutino'),
    ('Vespertino', 'Vespertino'),
    ('Noturno', 'Noturno'),
])
    dias_semana = forms.MultipleChoiceField(choices=DIAS_CHOICES, widget=forms.CheckboxSelectMultiple, required=True)
    periodos = forms.MultipleChoiceField(choices=PERIODOS_CHOICES, widget=forms.CheckboxSelectMultiple, required=True)
    descricao = forms.CharField(widget=forms.Textarea(attrs={'rows': 2}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        data_inicial = cleaned_data.get('data_inicial')
        data_final = cleaned_data.get('data_final')

        if data_inicial and data_final:
            if data_final < data_inicial:
                raise forms.ValidationError("A data final não pode ser anterior a data inicial")
            

        periodos = cleaned_data.get("periodos", [])
        if "integral" in periodos and len(periodos) > 1:
            raise forms.ValidationError("Se 'Integral' for selecionado, nenhum outro período pode ser marcado.")
        
        return cleaned_data
