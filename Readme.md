# perusable

Ref:

- https://testdriven.io/courses/django-full-text-search
- https://github.com/ParentJA/django-postgres-elasticsearch

⚠️ server/catalog/fixtures/wines.json is large; added to the codebase for convenience

Points where this repo differs from the course:

- added pgAdmin (useful to make sure the extensions are installed, and to double check indexes)
- Part 1, Chapter 8: next steps with image `ImageField(..., upload_to=...)` and with a couple migrations
- Part 2, Chapter 13: use `SearchHeadline` instead of custom function for highlighting
- Part 2, Chapter 14: use `GinIndex` to create index, and add a reverse to `RunPython` to allow for back and forth when making index mistakes :)
- Part 4, Chapter 31: fix `test_suggests_words_for_spelling_mistakes` test to account for test fixtures

Questions:

- Part 2, Chapter 14: `TrigramSimilarity` annotation doesn't use the index, so /api/v1/wine-search-words/ is too slow (~100 ms)
- Part 3, Chapter 21: `AsyncTypeahead` breaks my React app
- Part 3, Chapter 22: OK, but how do I dockerise for production use case (`yarn build` + serve static files with React ?)
