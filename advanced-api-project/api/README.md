Documentation for Filtering, Searching, and Ordering
We can filter the list of books using query parameters:
GET /api/books/?title=Dracula&author=Stoker
Available filter fields:
title
author
publication_year
SEARCH

---

Search by text across title and author fields:
GET /api/books/?search=Dracula
Searchable fields:
title
author
publication_year

----ODERING---
Sort results by any of the allowed fields:
GET /api/books/?ordering=title
GET /api/books/?ordering=-publication_year
Orderable fields:
title
publication_year
