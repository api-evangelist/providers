---
aid: linguatools
name: Linguatools
description: Linguatools provides language APIs including a collocations dictionary with more than 2 million English collocations, a sentence generator, and a multilingual disambiguator. The collocations API returns syntactically related word pairs along with significance scores and example sentences.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Collocations
  - Dictionary
  - English
  - Language
  - Linguistics
  - NLP
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/linguatools/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: linguatools:collocations
    name: Linguatools Collocations API
    description: The Linguatools Collocations API returns collocations for an English query word, filtered by syntactic relation, minimum significance, and part of speech. Each result includes the collocate, relation type, significance score, and up to three example sentences. Distributed via RapidAPI.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://linguatools.org/language-apis/linguatools-collocation-api/
    baseURL: https://linguatools-collocations.p.rapidapi.com
    tags:
      - Collocations
      - Dictionary
      - Language
      - NLP
    properties:
      - type: Documentation
        url: https://linguatools.org/language-apis/linguatools-collocation-api/
      - type: SignUp
        url: https://rapidapi.com/linguatools/api/linguatools-collocations
      - type: OpenAPI
        url: openapi/linguatools-collocations-openapi.yml
      - type: JSONSchema
        url: json-schema/linguatools-collocation-schema.json
      - type: JSONLD
        url: json-ld/linguatools-context.jsonld
common:
  - type: Website
    url: https://linguatools.org
  - type: Documentation
    url: https://linguatools.org/language-apis/
  - type: SignUp
    url: https://rapidapi.com/linguatools
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
