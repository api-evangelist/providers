---
aid: google-cloud-translation
name: Google Cloud Translation
description: Google Cloud Translation API enables dynamic translation of text between thousands of language pairs. It supports both basic translation using pre-trained Neural Machine Translation models and advanced translation with custom models and glossaries for domain-specific terminology.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-translation/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Google Cloud
  - Language
  - Localization
  - Machine Learning
  - Translation
apis:
  - name: Google Cloud Translation API
    description: Dynamically translates text between thousands of language pairs using Google's Neural Machine Translation models with support for custom glossaries and batch translation.
    humanURL: https://cloud.google.com/translate
    baseURL: https://translation.googleapis.com
    tags:
      - Language
      - Localization
      - Translation
    properties:
      - type: Documentation
        url: https://cloud.google.com/translate/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/translate/docs/setup
      - type: JSONSchema
        url: json-schema/translation.json
      - type: JSONLD
        url: json-ld/context.jsonld
common:
  - type: Portal
    url: https://cloud.google.com/translate
  - type: Getting Started
    url: https://cloud.google.com/translate/docs/setup
  - type: Documentation
    url: https://cloud.google.com/translate/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/translate/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/translate/docs/support
  - type: JSONLD
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
