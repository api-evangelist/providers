---
aid: raml
name: RAML
description: RAML (RESTful API Modeling Language) is a YAML-based specification language for describing RESTful APIs with first-class support for reusable patterns, traits, resource types, data type annotations, libraries, overlays, and extensions. Developed by MuleSoft and Salesforce, RAML 1.0 is the current stable version. The raml-org GitHub organization maintains the canonical specification and related tooling, all of which are archived and read-only as of February 2024.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Design
  - Specification Language
  - Standards
  - YAML
  - REST
  - API Modeling
created: '2026-03-25'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/raml/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: raml:raml-spec
    name: RAML Specification
    description: The RAML (RESTful API Modeling Language) specification defines a YAML 1.2-based language for describing HTTP-based APIs. RAML 1.0 introduces a unified type system, annotations, libraries, overlays, extensions, and improved OAuth support over RAML 0.8.
    humanURL: https://raml.org
    tags:
      - API Design
      - Specification Language
      - Standards
      - YAML
    properties:
      - type: Documentation
        url: https://raml.org/developers/raml-100-tutorial
      - type: Specification
        url: https://github.com/raml-org/raml-spec
      - type: GitHub Repository
        url: https://github.com/raml-org/raml-spec
      - type: JSONSchema
        url: json-schema/raml-document-schema.json
      - type: JSONStructure
        url: json-structure/raml-document-structure.json
common:
  - type: Website
    url: https://raml.org
  - type: Documentation
    url: https://raml.org/developers/raml-100-tutorial
  - type: Specification
    url: https://github.com/raml-org/raml-spec
  - type: GitHub Organization
    url: https://github.com/raml-org
  - type: Forum
    url: https://forum.raml.org
  - type: Parser JavaScript
    url: https://github.com/raml-org/raml-js-parser-2
  - type: Parser PHP
    url: https://github.com/raml-org/raml-php-parser
  - type: TCK
    url: https://github.com/raml-org/raml-tck
  - type: JSONSchemaConverter
    url: https://github.com/raml-org/ramldt2jsonschema
  - type: WebapiParser
    url: https://github.com/raml-org/webapi-parser
  - type: JSONLD
    url: json-ld/raml-context.jsonld
  - type: Vocabulary
    url: vocabulary/raml-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
