from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('matricula', 'nome', 'email_institucional', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('matricula', 'nome', 'email_institucional')
    ordering = ('matricula',)

    fieldsets = (
        (None, {'fields': ('matricula', 'senha')}),
        ('Informações pessoais', {'fields': ('nome', 'email_institucional')}),
        ('Permissões', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('matricula', 'nome', 'email_institucional', 'senha1', 'senha2', 'is_staff', 'is_active')}
        ),
    )

    # Mapeia senha para AbstractBaseUser corretamente
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

admin.site.register(Usuario, UsuarioAdmin)
