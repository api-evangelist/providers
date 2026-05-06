---
aid: corporate-bullshit-generator-api
name: Corporate Bullshit Generator API
x-type: company
description: The Corporate Bullshit Generator API is a free public REST API that returns randomly-generated corporate jargon phrases as JSON. Each request returns a single buzzword-laden phrase suitable for placeholder text, parody content, test fixtures, or comic relief in mock dashboards. The API is unauthenticated and returns a single phrase property in the JSON response body.
url: https://raw.githubusercontent.com/api-evangelist/corporate-bullshit-generator-api/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
type: Index
access: 3rd-Party
position: Consuming
tags:
  - Buzzwords
  - Comedy
  - Corporate Jargon
  - Fake Data
  - Free
  - Generator
  - JSON
  - Mock Data
  - Phrases
  - Public API
  - REST
  - Test Data
  - Unauthenticated
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: corporate-bullshit-generator-api:cbsg-api
    name: Corporate Bullshit Generator API
    description: 'A single-endpoint public REST API that returns a randomly-generated corporate jargon phrase as JSON. Each call to the root path returns a new phrase in the form {"phrase": "..."}. No authentication, no rate limit headers, and no parameters are required.'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
    humanURL: https://corporatebs-generator.sameerkumar.website/
    baseURL: https://corporatebs-generator.sameerkumar.website
    tags:
      - Free
      - JSON
      - Public API
      - REST
      - Unauthenticated
    properties:
      - type: HumanURL
        url: https://corporatebs-generator.sameerkumar.website/
      - type: GitHub
        url: https://github.com/sameerkumar18/corporate-bs-generator
      - type: OpenAPI
        url: openapi/corporate-bullshit-generator-api-openapi.yml
      - type: Rules
        url: rules/corporate-bullshit-generator-api-rules.yml
      - type: Capabilities
        url: capabilities/corporate-bullshit-generator-api-capabilities.yml
      - type: JSONLD
        url: json-ld/corporate-bullshit-generator-context.jsonld
      - type: Vocabulary
        url: vocabulary/corporate-bullshit-generator-vocabulary.yml
common:
  - type: Website
    url: https://corporatebs-generator.sameerkumar.website/
  - type: GitHub
    url: https://github.com/sameerkumar18/corporate-bs-generator
  - type: Author
    url: https://sameerkumar.website/
  - type: PublicAPIsListing
    url: https://github.com/public-apis/public-apis
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
