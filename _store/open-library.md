---
aid: open-library
name: Open Library
description: Open Library offers a suite of APIs to help developers get up and running with its data. This includes RESTful APIs that make Open Library data available in JSON, YAML, and RDF/XML formats, plus a Search Inside full-text search service, cover image endpoints, and read-protocol library lookup APIs. Most resources also expose machine-readable representations by appending .json, .yml, or .rdf to any Open Library URL.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Authors
  - Books
  - Catalog
  - Covers
  - Libraries
  - Open Data
  - Reading Lists
  - Search
  - Subjects
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/open-library/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: open-library:open-library-search-api
    name: Open Library Search API
    description: Search Open Library's catalog of books, authors, lists, and subjects. Returns JSON results for full-text and faceted queries, with options for pagination, field selection, and language filtering.
    humanURL: https://openlibrary.org/dev/docs/api/search
    tags:
      - Books
      - Catalog
      - Search
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/search
  - aid: open-library:open-library-search-inside-api
    name: Open Library Search Inside API
    description: Full-text search across the millions of digitized books in the Internet Archive's collection, returning matching passages and book identifiers.
    humanURL: https://openlibrary.org/dev/docs/api/search_inside
    tags:
      - Books
      - Full Text
      - Search
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/search_inside
  - aid: open-library:open-library-works-api
    name: Open Library Works API
    description: Retrieve work-level records (the abstract concept of a book independent of edition) by Open Library Work ID. Returns JSON, YAML, or RDF/XML.
    humanURL: https://openlibrary.org/dev/docs/api/books
    tags:
      - Books
      - Catalog
      - Works
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/books
  - aid: open-library:open-library-editions-api
    name: Open Library Editions API
    description: Retrieve edition-level records (specific printings, ISBNs, formats) by Open Library Edition ID, ISBN-10, ISBN-13, OCLC, or LCCN.
    humanURL: https://openlibrary.org/dev/docs/api/books
    tags:
      - Books
      - Catalog
      - Editions
      - ISBN
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/books
  - aid: open-library:open-library-authors-api
    name: Open Library Authors API
    description: Fetch author records and their works by Open Library Author ID. Supports JSON, YAML, and RDF/XML representations.
    humanURL: https://openlibrary.org/dev/docs/api/authors
    tags:
      - Authors
      - Catalog
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/authors
  - aid: open-library:open-library-subjects-api
    name: Open Library Subjects API
    description: Retrieve books, works, and metadata grouped by subject (genre, topic, place, time, person) with paging and faceting.
    humanURL: https://openlibrary.org/dev/docs/api/subjects
    tags:
      - Catalog
      - Subjects
      - Taxonomy
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/subjects
  - aid: open-library:open-library-covers-api
    name: Open Library Covers API
    description: Retrieve book and author cover images by Open Library ID, ISBN, OCLC, LCCN, or Goodreads ID, in small, medium, and large sizes.
    humanURL: https://openlibrary.org/dev/docs/api/covers
    tags:
      - Covers
      - Images
      - Media
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/covers
  - aid: open-library:open-library-lists-api
    name: Open Library Lists API
    description: Read and manage user-curated reading lists. Authenticated patrons can create lists and add or remove works, editions, and subjects.
    humanURL: https://openlibrary.org/dev/docs/api/lists
    tags:
      - Lists
      - Reading Lists
      - User Data
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/lists
  - aid: open-library:open-library-mybooks-api
    name: Open Library My Books API
    description: 'Access a patron''s public reading log: Want to Read, Currently Reading, and Already Read shelves for a given Open Library account.'
    humanURL: https://openlibrary.org/dev/docs/api/mybooks
    tags:
      - Reading Log
      - User Data
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/mybooks
  - aid: open-library:open-library-recent-changes-api
    name: Open Library Recent Changes API
    description: Stream recent edits across the Open Library catalog including works, editions, authors, lists, and subjects, with filtering by kind and time range.
    humanURL: https://openlibrary.org/dev/docs/api/recentchanges
    tags:
      - Activity
      - Changes
      - Feed
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/recentchanges
  - aid: open-library:open-library-read-api
    name: Open Library Read API
    description: Legacy partner API that returns availability and read URLs for books matched by ISBN, OCLC, LCCN, or OLID identifiers across libraries and the Internet Archive.
    humanURL: https://openlibrary.org/dev/docs/api/read
    tags:
      - Availability
      - Libraries
      - Lookup
    properties:
      - type: Documentation
        url: https://openlibrary.org/dev/docs/api/read
common:
  - type: Website
    url: https://openlibrary.org/
  - type: Developer Documentation
    url: https://openlibrary.org/developers/api
  - type: Bulk Data Dumps
    url: https://openlibrary.org/developers/dumps
  - type: GitHub Organization
    url: https://github.com/internetarchive/openlibrary
  - type: Issues
    url: https://github.com/internetarchive/openlibrary/issues
  - type: Blog
    url: https://blog.openlibrary.org/
  - type: Terms of Service
    url: https://archive.org/about/terms.php
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
