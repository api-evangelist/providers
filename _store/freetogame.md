---
aid: freetogame
name: FreeToGame
description: FreeToGame is a platform that offers a wide selection of free-to-play online games for gamers to enjoy.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-28'
position: Consumer
tags:
  - Games
  - Gaming
url: https://raw.githubusercontent.com/api-evangelist/freetogame/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: freetogame:freetogame
    name: FreeToGame
    tags:
      - Games
      - Gaming
    humanURL: https://www.freetogame.com/api-doc
    baseURL: https://www.freetogame.com/api
    properties:
      - url: https://www.freetogame.com/api-doc
        type: Documentation
      - url: openapi/freetogame-openapi.yml
        type: OpenAPI
    description: The FreeToGame API provides access to a comprehensive database of free-to-play games and free MMO games. The API is read-only, returns JSON, requires no authentication, and is rate limited to 10 requests per second.
common:
  - type: Website
    url: https://www.freetogame.com/
  - type: Documentation
    url: https://www.freetogame.com/api-doc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
