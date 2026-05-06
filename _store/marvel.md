---
aid: marvel
name: Marvel
description: The Marvel Comics API is a tool for developers to access data from over 70 years of Marvel comics, including characters, series, events, creators, and stories. The API requires authentication via an API key and is available through the Marvel Developer Portal.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Characters
  - Comics
  - Creators
  - Entertainment
  - Events
  - Media
  - Series
  - Stories
url: https://raw.githubusercontent.com/api-evangelist/marvel/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: marvel:marvel-comics-api
    name: Marvel Comics API
    description: The Marvel Comics API allows developers to access data from Marvel's vast library of comics, characters, creators, events, and series spanning over 70 years of Marvel history. All requests require API key authentication via a public key, timestamp, and MD5 hash.
    humanURL: https://developer.marvel.com/
    baseURL: https://gateway.marvel.com/v1/public
    tags:
      - Characters
      - Comics
      - Creators
      - Entertainment
      - Events
      - Series
      - Stories
    properties:
      - type: Documentation
        url: https://developer.marvel.com/docs
      - type: Getting Started
        url: https://developer.marvel.com/documentation/getting_started
      - type: Reference
        url: https://developer.marvel.com/documentation/apiresults
      - type: Authentication
        url: https://developer.marvel.com/documentation/authorization
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/marvel/refs/heads/main/openapi/marvel-openapi.yml
common:
  - type: Portal
    url: https://developer.marvel.com/
  - type: Sign Up
    url: https://developer.marvel.com/account
  - type: Terms of Service
    url: https://developer.marvel.com/terms
  - type: Documentation
    url: https://developer.marvel.com/docs
  - type: Website
    url: https://www.marvel.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
