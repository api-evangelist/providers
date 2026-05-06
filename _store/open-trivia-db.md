---
aid: open-trivia-db
name: Open Trivia DB
description: The Open Trivia Database provides a completely free JSON API for use in programming projects. Use of this API does not require an API key, just generate the URL and use it in your own application to retrieve trivia questions across multiple categories, difficulties, and types.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Free
  - Games
  - Questions
  - Trivia
created: '2025-02-12'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/open-trivia-db/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: open-trivia-db:open-trivia-db
    name: Open Trivia DB
    description: Free JSON trivia question API supporting categories, difficulties, question types, encodings, and optional session tokens to avoid duplicate questions across requests.
    humanURL: https://opentdb.com/api_config.php
    baseURL: https://opentdb.com
    tags:
      - Trivia
      - Questions
    properties:
      - type: Documentation
        url: https://opentdb.com/api_config.php
      - type: OpenAPI
        url: openapi/open-trivia-db-openapi.yml
common:
  - type: Website
    url: https://opentdb.com
  - type: Documentation
    url: https://opentdb.com/api_config.php
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
