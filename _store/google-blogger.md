---
aid: google-blogger
name: Google Blogger
description: The Google Blogger API v3 allows you to integrate Blogger content with your application. You can create, read, update, and delete blogs, posts, pages, comments, and user information using RESTful operations with OAuth 2.0 authentication.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-blogger/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Blogging
  - CMS
  - Comments
  - Google
  - Pages
  - Posts
  - Publishing
apis:
  - aid: google-blogger:google-blogger
    name: Google Blogger API V3
    description: The Blogger API v3 provides programmatic access to Blogger data. Manage blogs, posts, pages, comments, and users through RESTful endpoints.
    humanURL: https://developers.google.com/blogger
    baseURL: https://www.googleapis.com/blogger/v3
    properties:
      - type: OpenAPI
        url: openapi/blogger.yml
      - type: JSONSchema
        url: json-schema/blogger.json
common:
  - type: Getting Started
    url: https://developers.google.com/blogger/docs/3.0/getting_started
  - type: Pricing
    url: https://developers.google.com/blogger/docs/3.0/using
  - type: JSON-LD
    url: json-ld/blogger.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
