from rest_framework import serializers

from .models import Wine, WineSearchWord


class WineSerializer(serializers.ModelSerializer):
    variety = serializers.SerializerMethodField()
    winery = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    @staticmethod
    def get_highlighted_field(field: str, obj: object):
        if hasattr(obj, f"{field}_headline"):
            return getattr(obj, f"{field}_headline")
        return getattr(obj, f"{field}")

    def get_variety(self, obj):
        return WineSerializer.get_highlighted_field("variety", obj)

    def get_winery(self, obj):
        return WineSerializer.get_highlighted_field("winery", obj)

    def get_description(self, obj):
        return WineSerializer.get_highlighted_field("description", obj)

    class Meta:
        model = Wine
        fields = (
            "id",
            "country",
            "description",
            "points",
            "price",
            "variety",
            "winery",
        )


class WineSearchWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WineSearchWord
        fields = ("word",)
