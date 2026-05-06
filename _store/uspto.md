---
aid: uspto
name: USPTO
description: The United States Patent and Trademark Office (USPTO) is the federal agency responsible for granting U.S. patents and registering trademarks. USPTO provides a suite of developer APIs through the Open Data Portal (developer.uspto.gov) and data.uspto.gov for programmatic access to patent applications, granted patents, PTAB trial proceedings, trademark status, patent assignments, office actions, and citation data. All USPTO APIs are open government data and return JSON and XML responses. An ODP API key is required for most endpoints.
type: Index
image: https://www.uspto.gov/sites/default/files/USPTO_Logo.png
tags:
  - Government
  - Intellectual Property
  - Open Data
  - Patents
  - Regulatory
  - Trademarks
  - USPTO
url: https://raw.githubusercontent.com/api-evangelist/uspto/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: uspto:patent-api
    name: USPTO Patent & Trademark API
    description: The United States Patent and Trademark Office (USPTO) provides REST APIs for patent search, PTAB trial proceedings, trademark status lookup, and patent citation data. APIs are hosted at developer.uspto.gov and data.uspto.gov. An ODP API key is required for most endpoints.
    tags:
      - Assignments
      - Government
      - Patents
      - PTAB
      - Regulatory
      - Trademarks
    humanURL: https://developer.uspto.gov/
    baseURL: https://data.uspto.gov/api/v1
    properties:
      - type: Documentation
        url: https://developer.uspto.gov/
      - type: Reference
        url: https://developer.uspto.gov/api-catalog
      - type: OpenAPI
        url: openapi/uspto-patent-api-openapi.yml
      - type: JSONSchema
        url: json-schema/uspto-patent-schema.json
  - aid: uspto:ptab-api
    name: USPTO Patent Trial and Appeal Board (PTAB) API
    description: The USPTO PTAB API provides access to Patent Trial and Appeal Board proceedings data including inter partes reviews (IPR), post-grant reviews (PGR), and covered business method (CBM) reviews. Returns trial status, petitions, decisions, and related documents.
    tags:
      - Government
      - PTAB
      - Patents
      - Regulatory
    humanURL: https://data.uspto.gov/ptab
    properties:
      - type: Documentation
        url: https://data.uspto.gov/ptab
      - type: OpenAPI
        url: https://data.uspto.gov/swagger/index.html
  - aid: uspto:tsdr-api
    name: USPTO Trademark Status and Document Retrieval (TSDR) API
    description: The USPTO Trademark Status and Document Retrieval (TSDR) API enables programmatic access to trademark case status, filing history, and associated documents. Returns status information for trademark applications and registrations.
    tags:
      - Government
      - Regulatory
      - Trademarks
    humanURL: https://developer.uspto.gov/swagger/tsdr-api-v1
    properties:
      - type: Documentation
        url: https://developer.uspto.gov/swagger/tsdr-api-v1
      - type: OpenAPI
        url: https://developer.uspto.gov/swagger/tsdr-api-v1
  - aid: uspto:assignment-search-api
    name: USPTO Patent Assignment Search API
    description: The USPTO Patent Assignment Search API retrieves patent assignment information including ownership transfers, recorded assignments, and assignment history for individual patents and patent portfolios.
    tags:
      - Assignments
      - Government
      - Patents
      - Regulatory
    humanURL: https://developer.uspto.gov/api-catalog
    properties:
      - type: Documentation
        url: https://developer.uspto.gov/api-catalog
  - aid: uspto:office-actions-api
    name: USPTO Office Action Text Retrieval API
    description: The USPTO Office Action Text Retrieval API provides access to the full text of USPTO patent examiner office actions. Returns rejection text, claims analysis, and prior art citations for patent applications under examination.
    tags:
      - Government
      - Office Actions
      - Patents
      - Regulatory
    humanURL: https://developer.uspto.gov/ds-api-docs/index.html?url=https%3A//developer.uspto.gov/ds-api/swagger/docs/oa_actions.json
    properties:
      - type: Documentation
        url: https://developer.uspto.gov/ds-api-docs/index.html?url=https%3A//developer.uspto.gov/ds-api/swagger/docs/oa_actions.json
      - type: OpenAPI
        url: https://developer.uspto.gov/ds-api/swagger/docs/oa_actions.json
  - aid: uspto:enriched-citation-api
    name: USPTO Enriched Citation API
    description: The USPTO Enriched Citation API provides enriched citation reference metadata for patent documents including non-patent literature and patent citations. Returns structured citation data for patent analysis, competitive intelligence, and IP research.
    tags:
      - Citations
      - Government
      - Patents
      - Regulatory
    humanURL: https://developer.uspto.gov/ds-api-docs/index.html?url=https%3A//developer.uspto.gov/ds-api/swagger/docs/enriched_cited_reference_metadata.json/V3
    properties:
      - type: Documentation
        url: https://developer.uspto.gov/ds-api-docs/index.html?url=https%3A//developer.uspto.gov/ds-api/swagger/docs/enriched_cited_reference_metadata.json/V3
      - type: OpenAPI
        url: https://developer.uspto.gov/ds-api/swagger/docs/enriched_cited_reference_metadata.json
common:
  - type: Portal
    url: https://developer.uspto.gov/
  - type: Documentation
    url: https://developer.uspto.gov/
  - type: GettingStarted
    url: https://developer.uspto.gov/api-catalog
  - type: DeveloperTools
    url: https://data.uspto.gov/
  - type: PrivacyPolicy
    url: https://www.uspto.gov/privacy-policy
  - type: Website
    url: https://www.uspto.gov/
  - type: JSONSchema
    url: json-schema/uspto-patent-schema.json
  - type: JSONLDContext
    url: json-ld/uspto-context.jsonld
  - type: JSONStructure
    url: json-structure/uspto-patent-structure.json
  - type: SpectralRules
    url: rules/uspto-rules.yml
  - type: Vocabulary
    url: vocabulary/uspto-vocabulary.yml
  - type: NaftikoCapability
    url: capabilities/patent-research.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
