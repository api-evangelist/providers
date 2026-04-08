---
aid: google-translate
url: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/apis.yml
apis:
- name: Google Cloud Translation API
  description: REST API for translating text between languages, detecting source languages, and listing supported languages using Google's neural machine translation models.
  humanURL: https://cloud.google.com/translate/docs
  baseURL: https://translation.googleapis.com
  properties:
  - type: Documentation
    url: https://cloud.google.com/translate/docs/reference/rest
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/translate/docs/setup
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/json-schema/google-translate.json
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/google-translate/refs/heads/main/json-ld/google-translate.jsonld
name: Google Cloud Translation API
tags:
- Google Cloud
- Internationalization
- Language Detection
- Localization
- Machine Translation
- Natural Language Processing
- Translation
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Google Cloud Translation API provides programmatic access to Google's neural machine translation technology. It enables developers to dynamically translate text between thousands of language pairs, detect the source language of text, and retrieve lists of supported languages. The API supports both basic (v2) and advanced (v3) translation capabilities including batch translation, custom models, glossaries, and adaptive translation.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

