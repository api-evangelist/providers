---
aid: languagetool
name: LanguageTool
description: LanguageTool is an open-source proofreading and grammar checking tool that supports more than 25 languages. The HTTP API enables developers to programmatically check texts for grammar and style issues, list supported languages, and manage personal dictionaries.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Grammar
  - Language
  - Proofreading
  - Spell Check
  - Style Check
  - Text Analysis
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/languagetool/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: languagetool:languagetool
    name: LanguageTool HTTP API
    description: The LanguageTool HTTP API provides programmatic access to grammar and style checking. The /check endpoint analyzes a text in a given language and returns matches with messages, replacements, and rule context. The /languages endpoint lists all supported languages, and the /words endpoints manage entries in a user's personal dictionaries.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://languagetool.org/http-api/
    baseURL: https://api.languagetool.org/v2
    tags:
      - Grammar
      - Proofreading
      - Spell Check
      - Style Check
    properties:
      - type: Documentation
        url: https://languagetool.org/http-api/
      - type: SwaggerUI
        url: https://languagetool.org/http-api/swagger-ui/
      - type: OpenAPI
        url: openapi/languagetool-openapi.yml
      - type: JSONSchema
        url: json-schema/languagetool-match-schema.json
common:
  - type: Website
    url: https://languagetool.org
  - type: Documentation
    url: https://languagetool.org/http-api/
  - type: Developer
    url: https://dev.languagetool.org/
  - type: GitHub
    url: https://github.com/languagetool-org/languagetool
  - type: PrivacyPolicy
    url: https://languagetool.org/legal/privacy
  - type: TermsOfService
    url: https://languagetool.org/legal/terms
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
