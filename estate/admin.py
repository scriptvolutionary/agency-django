
from django.contrib import admin

from estate.models import Contract, Holder, Immovable, Realtor

admin.site.site_header = 'Агентство недвижимости'
admin.site.page_title = 'Админ панель'
admin.site.site_branding = 'Админ панель'


@admin.register(Holder)
class HolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'tel', 'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    search_fields = ('name', 'mail')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('identity', 'holderName', 'realtorName',
                    'status', 'summ', 'executionAt', 'createdAt', 'updatedAt')
    list_filter = ('status', 'executionAt', 'createdAt', 'updatedAt')
    search_fields = ('holderName', 'realtorName')


@admin.register(Immovable)
class ImmovableAdmin(admin.ModelAdmin):
    list_display = ('label', 'address', 'type', 'status',
                    'holder', 'contract', 'contractIdentity', 'publishAt', 'updatedAt', 'updatedAt')
    list_filter = ('status', 'publishAt', 'createdAt', 'updatedAt')
    search_fields = ('label', 'address', 'holder')


@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'tel', 'createdAt', 'updatedAt')
    list_filter = ('createdAt', 'updatedAt')
    search_fields = ('name', 'mail')
