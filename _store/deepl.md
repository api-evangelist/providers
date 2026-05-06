---
aid: deepl
name: DeepL
url: https://raw.githubusercontent.com/api-evangelist/deepl/refs/heads/main/apis.yml
type: Contract
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Deep Learning
  - Glossaries
  - Localization
  - Machine Learning
  - Machine Translation
  - Translation
created: '2024-11-07'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: DeepL is an AI-powered translation service that delivers high-quality machine translation between dozens of languages, with support for context-aware translation, document translation, glossaries, and rephrasing/improvement via DeepL Write. The DeepL API is offered in Pro and Free tiers and exposes endpoints for text translation, document translation, glossaries, language metadata, usage, and write/rephrase.
apis:
  - aid: deepl:deepl-translation-api
    name: DeepL Translation API
    description: The DeepL Translation API provides programmatic access to DeepL's machine translation technology including text translate, document translate, glossaries, language metadata, usage, and DeepL Write rephrasing.
    humanURL: https://developers.deepl.com/
    baseURL: https://api.deepl.com/v2
    tags:
      - Documents
      - Glossaries
      - Languages
      - Translate
      - Usage
      - Write
    properties:
      - type: Documentation
        url: https://developers.deepl.com/docs
      - type: Reference
        url: https://developers.deepl.com/docs/api-reference
      - type: OpenAPI
        url: openapi/deepl-translation-api-openapi.yml
      - type: JSONSchema
        url: json-schema/deepl-translation.json
      - type: JSONSchema
        url: json-schema/deepl-glossary.json
      - type: Rules
        url: rules/deepl-translation-api-rules.yml
      - type: Capabilities
        url: capabilities/deepl-translation-api-capabilities.yml
common:
  - type: Website
    url: https://www.deepl.com/
  - type: Portal
    url: https://developers.deepl.com/
  - type: Documentation
    url: https://developers.deepl.com/docs
  - type: Authentication
    url: https://developers.deepl.com/docs/getting-started/auth
  - type: Pricing
    url: https://www.deepl.com/pro
  - type: SDK
    url: https://github.com/DeepLcom/deepl-python
  - type: SDK
    url: https://github.com/DeepLcom/deepl-node
  - type: Terms of Service
    url: https://www.deepl.com/pro-license
  - type: Privacy Policy
    url: https://www.deepl.com/privacy
  - type: JSON-LD
    url: json-ld/deepl-context.jsonld
  - type: Vocabulary
    url: vocabulary/deepl-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
