from django.contrib import admin
from django.contrib.postgres.search import SearchVectorField
from django.forms import Textarea

from .models import Wine, WineSearchWord


@admin.register(Wine)
class WineAdmin(admin.ModelAdmin):
    fields = (
        "id",
        "country",
        "description",
        "points",
        "price",
        "variety",
        "winery",
        "thumbnail",
        "search_vector",
    )
    list_display = (
        "id",
        "country",
        "points",
        "price",
        "variety",
        "winery",
    )
    list_filter = (
        "country",
        "variety",
        "winery",
    )
    ordering = ("variety",)
    readonly_fields = ("id",)

    formfield_overrides = {
        SearchVectorField: {"widget": Textarea(attrs={"rows": 4, "cols": 100})},
    }


@admin.register(WineSearchWord)
class WineSearchWordAdmin(admin.ModelAdmin):
    fields = ("word",)
    list_display = ("word",)
    ordering = ("word",)
