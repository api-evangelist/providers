---
aid: demo-openapi
name: Manage OpenAPI via GitHub Demo
url: https://raw.githubusercontent.com/api-evangelist/demo-openapi/refs/heads/main/apis.yml
type: Contract
position: Producer
access: 1st-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - APIs.json
  - Demo
  - GitHub
  - OpenAPI
  - Reference
  - Search
created: '2024-10-31'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
description: This is a demo repository showing how GitHub can be used to manage an API contract using an APIs.json index plus an OpenAPI definition and supporting artifacts. The API used in the demo is the APIs.io Search API, which exposes search and submission endpoints over the APIs.io index. The repository is referenced by an API Evangelist blog post on managing OpenAPI in GitHub.
apis:
  - aid: demo-openapi:apis-io-search-api
    name: APIs.io Search API
    description: Demo OpenAPI for the APIs.io Search API, exposing keyword search of APIs in the APIs.io index plus a submit endpoint that accepts a valid APIs.json document for inclusion. Used here purely as a demonstration subject for the GitHub-based API management workflow.
    humanURL: https://developer.apis.io/documentation/
    baseURL: https://search-api.apis.io/
    tags:
      - APIs.io
      - Demo
      - Search
      - Submit
    properties:
      - type: Documentation
        url: https://developer.apis.io/documentation/
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: OpenAPIReview
        url: openapi/openapi-review.yml
      - type: Rules
        url: rules/apis-io-search-api-rules.yml
      - type: Capabilities
        url: capabilities/apis-io-search-api-capabilities.yml
      - type: Teams
        url: common/team.yml
      - type: UseCases
        url: common/use-cases.yml
common:
  - type: BlogPost
    url: https://github.com/api-evangelist/demo-openapi
  - type: CanonicalRepo
    url: https://github.com/api-evangelist/search-api
  - type: APIsIo
    url: https://apis.io
  - type: Developer
    url: https://developer.apis.io
  - type: SupportEmail
    url: mailto:kin@apievangelist.com
  - type: Vocabulary
    url: vocabulary/demo-openapi-vocabulary.yml
  - type: JSON-LD
    url: json-ld/demo-openapi-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
