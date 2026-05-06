---
aid: google-books
name: Google Books
description: The Google Books API allows you to perform full-text searches and retrieve book information, viewability, and eBook availability. You can search for volumes, access detailed metadata including authors, publishers, and ISBNs, manage personal bookshelves, and determine content accessibility.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-books/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Books
  - eBooks
  - Google
  - Library
  - Publishing
  - Reading
  - Search
apis:
  - aid: google-books:google-books
    name: Google Books API V1
    description: The Google Books API provides programmatic access to Google Books data. Search for volumes, retrieve book metadata, manage bookshelves, and access eBook availability information.
    humanURL: https://developers.google.com/books
    baseURL: https://www.googleapis.com/books/v1
    properties:
      - type: OpenAPI
        url: openapi/books.yml
      - type: JSONSchema
        url: json-schema/books.json
common:
  - type: Getting Started
    url: https://developers.google.com/books/docs/v1/getting_started
  - type: Pricing
    url: https://developers.google.com/books/docs/v1/using
  - type: JSON-LD
    url: json-ld/books.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
