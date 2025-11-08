from django.contrib import admin
from .models import Reserva, ReservaSala, DiaSemana, Periodo

# Inlines permitem editar modelos relacionados na mesma página
class PeriodoInline(admin.TabularInline):
    model = Periodo
    extra = 0  # Não mostra linhas vazias extras
    can_delete = True
    readonly_fields = ('created_at', 'deleted_at')
    classes = ('collapse',) # Opcional: inicia recolhido para economizar espaço

class DiaSemanaInline(admin.TabularInline):
    model = DiaSemana
    extra = 0
    can_delete = True
    readonly_fields = ('created_at', 'deleted_at')
    classes = ('collapse',)

class ReservaSalaInline(admin.StackedInline): # StackedInline é melhor quando há muitos campos
    model = ReservaSala
    extra = 0
    can_delete = True
    readonly_fields = ('created_at', 'deleted_at')
    fieldsets = (
        (None, {
            'fields': (('id_sala', 'turno'), 'responsavel', 'status_reserva')
        }),
        ('Detalhes', {
            'fields': ('descricao_reserva',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = (
        'codigo_turma',
        'get_curso_nome',
        'data_inicial',
        'data_final',
        'criador_por',
        'is_deleted'
    )
    list_filter = ('data_inicial', 'data_final', 'is_deleted', 'id_curso')
    search_fields = ('codigo_turma', 'id_curso__nome_curso', 'criador_por__nome') # Assumindo que Usuario tem 'nome'
    readonly_fields = ('created_at', 'deleted_at')
    list_select_related = ('id_curso', 'id_turma', 'criador_por')
    inlines = [ReservaSalaInline] # Permite editar ReservaSala dentro da tela de Reserva

    fieldsets = (
        ('Informações da Turma', {
            'fields': ('id_curso', 'id_turma', 'codigo_turma')
        }),
        ('Vigência', {
            'fields': (('data_inicial', 'data_final'),)
        }),
        ('Auditoria', {
            'fields': ('criador_por', 'created_at', 'deleted_at', 'is_deleted'),
            'classes': ('collapse',)
        }),
    )

    @admin.display(description='Curso', ordering='id_curso__nome_curso')
    def get_curso_nome(self, obj):
        return obj.id_curso.nome_curso if obj.id_curso else '-'

@admin.register(ReservaSala)
class ReservaSalaAdmin(admin.ModelAdmin):
    list_display = (
        'get_reserva_info',
        'id_sala',
        'turno',
        'responsavel',
        'status_reserva',
        'is_deleted'
    )
    list_filter = ('status_reserva', 'turno', 'is_deleted', 'id_sala__id_bloco')
    search_fields = ('responsavel', 'id_reserva__codigo_turma', 'id_sala__numero_sala')
    list_select_related = ('id_reserva', 'id_sala')
    readonly_fields = ('created_at', 'deleted_at')
    # Inlines para editar Dias e Períodos diretamente na tela da ReservaSala
    inlines = [DiaSemanaInline, PeriodoInline] 

    @admin.display(description='Reserva Original')
    def get_reserva_info(self, obj):
        if obj.id_reserva:
             return f"{obj.id_reserva.codigo_turma} ({obj.id_reserva.id_curso})"
        return "-"

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = (
        'get_reservasala_info', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado'
    )
    list_filter = ('segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo')
    list_select_related = ('id_reservasala__id_sala', 'id_reservasala__id_reserva')

    @admin.display(description='Sala Reservada')
    def get_reservasala_info(self, obj):
        return str(obj.id_reservasala)

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = (
        'get_reservasala_info', 'primeiro', 'segundo', 'terceiro', 'quarto', 'integral'
    )
    list_filter = ('primeiro', 'segundo', 'terceiro', 'quarto', 'integral')
    list_select_related = ('id_reservasala__id_sala',)

    @admin.display(description='Sala Reservada')
    def get_reservasala_info(self, obj):
         return str(obj.id_reservasala)