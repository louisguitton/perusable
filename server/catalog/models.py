import uuid

from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import (
    SearchQuery,
    SearchRank,
    SearchHeadline,
    SearchVectorField,
    TrigramSimilarity
)

from django.db import models
from django.db.models import F, Q


class WineQuerySet(models.query.QuerySet):
    def search(self, value: str):
        query = SearchQuery(value)
        search_query = Q(Q(search_vector=query))
        return (
            self.annotate(
                variety_headline=SearchHeadline(
                    "variety",
                    query,
                    start_sel="<mark>",
                    stop_sel="</mark>",
                ),
                winery_headline=SearchHeadline(
                    "winery",
                    query,
                    start_sel="<mark>",
                    stop_sel="</mark>",
                ),
                description_headline=SearchHeadline(
                    "description",
                    query,
                    start_sel="<mark>",
                    stop_sel="</mark>",
                ),
                search_rank=SearchRank(F("search_vector"), query),
            )
            .filter(search_query)
            .order_by("-search_rank", "id")
        )


class Wine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    country = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    variety = models.CharField(max_length=255)
    winery = models.CharField(max_length=255)
    thumbnail = models.ImageField(null=True, upload_to="wines")
    search_vector = SearchVectorField(null=True, blank=True)

    objects = WineQuerySet.as_manager()

    class Meta:
        indexes = [GinIndex(fields=["search_vector"], name="search_vector_index")]

    def __str__(self):
        return f"{self.id}"


class WineSearchWordQuerySet(models.query.QuerySet):
    def search(self, query):
        return self.annotate(
            similarity=TrigramSimilarity('word', query)
        ).filter(similarity__gte=0.3).order_by('-similarity')


class WineSearchWord(models.Model):
    word = models.CharField(max_length=255, unique=True)

    objects = WineSearchWordQuerySet().as_manager()

    class Meta:
        indexes = [
            GinIndex(
                fields=["word"],
                name="wine_search_word_trigram_index",
                opclasses=["gin_trgm_ops"],
            )
        ]

    def __str__(self):
        return self.word
