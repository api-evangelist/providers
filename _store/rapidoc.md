---
aid: rapidoc
name: RapiDoc
description: RapiDoc is a web component that allows developers to easily integrate interactive documentation for their APIs. It provides a user-friendly interface for exploring and testing API endpoints, displaying detailed information about request and response parameters, and offering code examples in multiple programming languages. RapiDoc also supports authentication methods, response validation, and custom theming options to tailor the documentation to a specific brand or project.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Documentation
  - Platform
  - Web Components
  - OpenAPI
access: 3rd-Party
position: Consumer
created: '2025-01-08'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rapidoc/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: rapidoc:rapidoc
    name: RapiDoc
    description: RapiDoc is a fast, embeddable web component that renders OpenAPI (Swagger) 2.0/3.x specifications as interactive API documentation. Drop the element into any web page to get a searchable, navigable UI with endpoint details, request/response schemas, examples, and code snippets. It includes a built-in "Try It" console with auth support (API key, Bearer, Basic, OAuth), server selection, and environment variables, so developers can test calls directly from the docs.
    humanURL: https://rapidocweb.com/
    tags:
      - Documentation
      - Platform
      - Web Components
      - OpenAPI
    properties:
      - type: Documentation
        url: https://rapidocweb.com/
      - type: OpenAPI
        url: openapi/rapidoc-rapidoc-openapi.yml
      - type: JSONSchema
        url: json-schema/rapidoc-configuration.json
      - type: JSONSchema
        url: json-schema/rapidoc-slots.json
      - type: JSONSchema
        url: json-schema/rapidoc-events.json
      - type: JSONLD
        url: json-ld/rapidoc-context.jsonld
      - type: JSONStructure
        url: json-structure/rapidoc-configuration-structure.json
      - type: JSONStructure
        url: json-structure/rapidoc-events-structure.json
      - type: JSONStructure
        url: json-structure/rapidoc-slots-structure.json
      - type: Example
        url: examples/rapidoc-basic-embed-example.json
      - type: Example
        url: examples/rapidoc-branded-embed-example.json
      - type: Example
        url: examples/rapidoc-javascript-api-example.json
      - type: SpectralRules
        url: rules/rapidoc-rules.yml
common:
  - type: Documentation
    url: https://rapidocweb.com/api.html
    name: RapiDoc API Reference
  - type: Examples
    url: https://rapidocweb.com/examples.html
    name: RapiDoc Examples and Demos
  - type: GettingStarted
    url: https://rapidocweb.com/quickstart.html
    name: RapiDoc Quick Start
  - type: GitHubRepository
    url: https://github.com/rapi-doc/RapiDoc
  - type: NPM
    url: https://www.npmjs.com/package/rapidoc
  - type: Vocabulary
    url: vocabulary/rapidoc-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
