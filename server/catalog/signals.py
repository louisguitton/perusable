"""Database Signals.

Handle update of the search vector field upon creation or update of a record.
"""

from django.contrib.postgres.search import SearchVector
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Wine


@receiver(post_save, sender=Wine, dispatch_uid="on_wine_save")
def on_wine_save(sender, instance, *args, **kwargs):
    sender.objects.filter(pk=instance.id).update(
        search_vector=(
            SearchVector("variety", weight="A")
            + SearchVector("winery", weight="A")
            + SearchVector("description", weight="B")
        )
    )

    with connection.cursor() as cursor:
        # we don't use the search_vector column because we want non stemmed words
        # so, we rebuild the search_vector with the 'simple' configuration
        cursor.execute(
            """
            insert into catalog_winesearchword (word)
            select word from ts_stat('
                select
                    to_tsvector(''simple'', variety) ||
                    to_tsvector(''simple'', winery) ||
                    to_tsvector(''simple'', coalesce(description, ''''))
                from catalog_wine
                where id = '%s'
            ')
            on conflict (word) do nothing;
        """,
            [
                str(instance.id),
            ],
        )
