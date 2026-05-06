---
aid: musixmatch
name: Musixmatch
description: Musixmatch is an Italian music data company and platform for users to search and share song lyrics with translations. Musixmatch has 80 million users, 8 million songs with their respective lyrics, and 115+ employees.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://developer.musixmatch.com/
created: '2024-06-07'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Lyrics
  - Music
  - Translations
apis:
  - aid: musixmatch:musixmatch-api
    name: Musixmatch API
    tags:
      - Album
      - Artist
      - Lyrics
      - Snippets
      - Subtitle
      - Track
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.musixmatch.com/ws/1.1/
    humanURL: https://developer.musixmatch.com/documentation
    properties:
      - url: https://developer.musixmatch.com/documentation
        type: Documentation
      - url: openapi/musixmatch-openapi-original.yml
        type: OpenAPI
    description: The most powerful and legal way to display lyrics on your website or in your application. Musixmatch lyrics API is a robust service that permits you to search and retrieve lyrics in the simplest possible way.
common:
  - url: https://developer.musixmatch.com/
    type: Portal
  - url: https://developer.musixmatch.com/login
    type: Login
  - url: https://blog.musixmatch.com/
    type: Blog
  - url: https://about.musixmatch.com/privacy-policy
    type: Privacy Policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
