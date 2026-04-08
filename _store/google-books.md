---
aid: google-books
url: https://raw.githubusercontent.com/api-evangelist/google-books/refs/heads/main/apis.yml
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
name: Google Books
tags:
- Books
- eBooks
- Google
- Library
- Publishing
- Reading
- Search
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Books API allows you to perform full-text searches and retrieve book information, viewability, and eBook availability. You can search for volumes, access detailed metadata including authors, publishers, and ISBNs, manage personal bookshelves, and determine content accessibility.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

