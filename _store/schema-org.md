---
name: Schema.org
description: Schema.org is a collaborative, community-driven project that creates and maintains a shared vocabulary for structured data on the web. Founded by Google, Microsoft, Yahoo, and Yandex in 2011, it provides types and properties that developers and webmasters use to annotate content in formats like JSON-LD, RDFa, and Microdata, enabling search engines and applications to better understand web content. The vocabulary currently consists of 800+ Types, 1500+ Properties, and covers domains including commerce, healthcare, organizations, events, creative works, and more. The Schema.org WebAPI type provides a standardized vocabulary for describing APIs in structured data.
url: https://github.com/api-evangelist/schema-org
x-type: standard
tags:
  - Schema.org
  - Structured Data
  - Linked Data
  - JSON-LD
  - Vocabulary
  - SEO
  - Web Standards
  - RDF
  - Ontology
created: '2026-05-02'
modified: '2026-05-02'
apis:
  - name: Schema.org Vocabulary
    description: Schema.org is a collaborative, community-driven vocabulary for structured data on the internet. It provides a collection of shared vocabularies that webmasters and developers can use to mark up pages in ways recognized by major search engines. The vocabulary covers entities, relationships between entities, and actions. Machine-readable definitions are available in RDF/Turtle, JSON-LD, CSV, and other formats.
    humanURL: https://schema.org/docs/developers.html
    baseURL: https://schema.org
    tags:
      - Schema.org
      - Vocabulary
      - Structured Data
      - Linked Data
      - JSON-LD
      - RDF
      - Microdata
      - RDFa
      - SEO
      - Web Standards
    properties:
      - type: Documentation
        url: https://schema.org/docs/developers.html
      - type: Reference
        url: https://schema.org/docs/schemas.html
      - type: DataModel
        url: https://schema.org/docs/datamodel.html
      - type: ChangeLog
        url: https://schema.org/docs/releases.html
      - type: GitHubRepository
        url: https://github.com/schemaorg/schemaorg
      - type: JSONSchema
        url: json-schema/schema-org-thing-schema.json
  - name: Schema.org JSON-LD Context
    description: The Schema.org JSON-LD Context provides the canonical JSON-LD context file for the Schema.org vocabulary. This context file maps Schema.org terms to their full IRIs, enabling JSON-LD processors to correctly interpret structured data markup. Google recommends JSON-LD as the preferred format for Schema.org structured data on websites.
    humanURL: https://schema.org/docs/developers.html
    baseURL: https://schema.org
    tags:
      - JSON-LD
      - Linked Data
      - Context
      - Vocabulary
      - Structured Data
    properties:
      - type: Documentation
        url: https://schema.org/docs/developers.html
      - type: JSON-LD Context
        url: https://schema.org/docs/jsonldcontext.json
  - name: Schema.org Markup Validator
    description: The Schema.org Markup Validator tests and validates structured data markup against the Schema.org vocabulary. It supports JSON-LD, Microdata, and RDFa formats and helps ensure structured data will be correctly interpreted by search engines.
    humanURL: https://validator.schema.org/
    baseURL: https://validator.schema.org
    tags:
      - Validation
      - Structured Data
      - Testing
      - Schema
      - Markup
    properties:
      - type: Documentation
        url: https://validator.schema.org/
  - name: Schema.org WebAPI Type
    description: The Schema.org WebAPI type defines a Web API accessible over Web and Internet technologies. It provides standardized properties for describing APIs including documentation URL, terms of service, provider, and API entry point. The WebAPI type enables search engines and automated tools to discover and understand published APIs.
    humanURL: https://schema.org/WebAPI
    baseURL: https://schema.org
    tags:
      - WebAPI
      - API Description
      - Structured Data
      - Linked Data
      - Schema
    properties:
      - type: Documentation
        url: https://schema.org/WebAPI
      - type: JSONSchema
        url: json-schema/schema-org-web-api-schema.json
common:
  - type: Website
    url: https://schema.org/
  - type: Documentation
    url: https://schema.org/docs/documents.html
  - type: Blog
    url: https://blog.schema.org/
  - type: Support
    url: https://github.com/schemaorg/schemaorg/issues
  - type: SpectralRules
    url: rules/schema-org-rules.yml
  - type: JSONLDContext
    url: json-ld/schema-org-context.jsonld
  - type: Vocabulary
    url: vocabulary/schema-org-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
