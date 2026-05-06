---
aid: the-open-movie-database
name: The Open Movie Database
description: The OMDb API is a RESTful web service to obtain movie, series, and episode information. All content and images on the site are contributed and maintained by users. Access movie and TV metadata including title, year, genre, director, cast, plot, ratings, and IMDb data. Search by title or look up by IMDb ID. Requires a free API key obtained at omdbapi.com/apikey.aspx.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Movies
  - Television
  - IMDb
  - Metadata
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/the-open-movie-database/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: the-open-movie-database:the-open-movie-database
    name: The Open Movie Database API
    description: The OMDb API is a RESTful web service to obtain movie, series, and episode information. Search by title or look up by IMDb ID. Returns detailed metadata including ratings from IMDb, Rotten Tomatoes, and Metacritic.
    humanURL: https://www.omdbapi.com/
    baseURL: https://www.omdbapi.com
    tags:
      - Entertainment
      - Movies
      - Television
      - IMDb
      - Metadata
    properties:
      - type: Documentation
        url: https://www.omdbapi.com/
      - type: OpenAPI
        url: openapi/the-open-movie-database-openapi.yml
      - type: Sign Up
        url: https://www.omdbapi.com/apikey.aspx
      - type: Spectral Rules
        url: rules/the-open-movie-database-rules.yml
      - type: Naftiko Capability
        url: capabilities/movie-lookup.yaml
      - type: Naftiko Shared
        url: capabilities/shared/the-open-movie-database.yaml
      - type: JSON Schema
        url: json-schema/the-open-movie-database-movie-schema.json
      - type: JSON Structure
        url: json-structure/the-open-movie-database-movie-structure.json
      - type: JSON-LD
        url: json-ld/the-open-movie-database-context.jsonld
      - type: Example
        url: examples/the-open-movie-database-get-movie-example.json
      - type: Vocabulary
        url: vocabulary/the-open-movie-database-vocabulary.yml
common:
  - type: Website
    url: https://www.omdbapi.com/
  - type: Documentation
    url: https://www.omdbapi.com/
  - type: Sign Up
    url: https://www.omdbapi.com/apikey.aspx
  - type: Terms of Service
    url: https://www.omdbapi.com/legal.htm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
