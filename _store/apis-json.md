---
aid: apis-json
name: APIs.json
description: APIs.json is an open, machine-readable specification that API providers can use to describe their API operations, similar to how websites use sitemap.xml. The format provides a lightweight means for individuals and organizations to document the location of their APIs, associated descriptions, human and machine-readable specifications, and ancillary information such as licensing, maintainers, and terms of service. It was created by Kin Lane and Steven Willmott in May 2014 and is maintained as an open IETF-style draft. The current stable version is 0.19, published in November 2024. APIs.json files can be placed at the root of any domain as /apis.json or /apis.yml for automated discovery. The specification defines root-level fields (name, description, url, apis, common), API-level fields (aid, humanURL, baseURL, tags, properties), and a comprehensive list of property types covering documentation, authentication, licensing, support, and governance. It is the foundation for the APIs.io search engine and API Commons initiative.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Aggregation
  - API Cataloging
  - API Commons
  - API Discovery
  - API Governance
  - API Operations
  - Machine Readable
  - Specification
  - Standard
url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apis-json:apis-json-specification
    name: APIs.json Specification
    description: The APIs.json specification defines a machine-readable JSON or YAML format for describing API operations. Unlike OpenAPI which describes the technical interface of a single API, APIs.json describes the surrounding operations of one or more APIs — documentation, authentication, pricing, terms of service, support, and other properties. Created by Kin Lane and Steven Willmott in May 2014, the specification is maintained as an informal IETF draft at apisjson.org. The current stable version is 0.19, published November 6, 2024. APIs.json files are placed at the domain root as /apis.json or /apis.yml for automated discovery by robots and search engines.
    humanURL: https://apisjson.org
    tags:
      - API Description
      - API Discovery
      - API Operations
      - Machine Readable
      - Specification
      - Standard
    properties:
      - type: Documentation
        url: https://apisjson.org/schema/
      - type: Specification
        url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/spec/apisjson_0.19.txt
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-schema/apis-json-schema-0.19.yaml
        title: Schema v0.19
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-schema/apis-json-schema-0.18.yaml
        title: Schema v0.18
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-schema/apis-json-schema-0.17.yaml
        title: Schema v0.17
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/json-schema/apis-json-schema-0.20.yaml
        title: Schema v0.20 (Draft)
common:
  - type: Website
    url: https://apisjson.org
  - type: Properties
    url: https://apisjson.org/properties/
  - type: Blog
    url: https://apisjson.org/blog/
  - type: GitHubOrganization
    url: https://github.com/apis-json
  - type: GitHubRepository
    url: https://github.com/apis-json/api-json
    title: Specification Repository
  - type: GitHubRepository
    url: https://github.com/apis-json/apis-json-website
    title: Website
  - type: GitHubRepository
    url: https://github.com/apis-json/artisanal
    title: Artisanal APIs.json Examples
  - type: GitHubRepository
    url: https://github.com/apis-json/backstage
    title: Backstage Integration
  - type: Support
    url: https://github.com/apis-json/api-json/issues
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/rules/apis-json-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apis-json/refs/heads/main/vocabulary/apis-json-vocabulary.yaml
  - type: Features
    data:
      - name: Machine-Readable API Operations
        description: Provides a machine-readable format for documenting API operations beyond just the technical interface, covering documentation, pricing, authentication, terms of service, support, and governance.
      - name: Domain Root Discovery
        description: APIs.json files can be placed at /apis.json or /apis.yml at the root of any domain, enabling automated discovery by search engines and robots without prior knowledge of the API provider.
      - name: Property Type System
        description: Defines a comprehensive enumerated set of property types (OpenAPI, Documentation, Authentication, Pricing, Support, etc.) enabling consistent machine-readable indexing of API operations.
      - name: Federation via Include
        description: Supports federated API directories through include references, allowing a root APIs.json to reference other APIs.json files on different servers or domains.
      - name: Multiple API Collections
        description: A single APIs.json file can document multiple APIs in the apis array, with shared properties in the common section, enabling organization-wide API catalogs.
      - name: Authority and Non-Authority
        description: Defines authoritative (same DNS domain) and non-authoritative entries, with conflict resolution rules giving priority to the most specific authoritative entry.
      - name: Overlay Support
        description: Supports overlay specifications that can modify or extend existing APIs.json entries, enabling provider-agnostic enrichment of API metadata.
      - name: Version History
        description: Maintained as a versioned specification from 0.11 through current 0.19, with full version history and diff comparisons available on GitHub and apisjson.org.
  - type: UseCases
    data:
      - name: API Discovery
        description: API providers publish APIs.json files at their domain root so that search engines like APIs.io can automatically discover and index all their APIs without manual submission.
      - name: API Governance
        description: Platform teams use APIs.json as a canonical machine-readable index of their API portfolio, enabling automated compliance checking of required operational properties like terms of service and authentication.
      - name: API Portal Generation
        description: Developer portals can be automatically generated from APIs.json files by reading the properties array and presenting documentation, OpenAPI specs, getting started guides, and other resources.
      - name: API Commons Participation
        description: Organizations publish APIs.json files to participate in the API Commons initiative, making their APIs discoverable and accessible to a wider developer community.
      - name: Internal API Catalog
        description: Enterprises use APIs.json as the foundation for internal API catalogs, enabling discoverability of internal, partner, and public APIs using a consistent machine-readable format.
      - name: Backstage Integration
        description: Teams use the APIs.json Backstage integration to import API metadata from APIs.json files into Spotify Backstage for internal developer portal use.
  - type: Integrations
    data:
      - name: APIs.io
        description: The APIs.io search engine is built entirely on the APIs.json specification, indexing submitted APIs.json files to power its API discovery and search capabilities.
      - name: API Commons
        description: API Commons uses APIs.json as its core metadata format for documenting API operations across the open API ecosystem.
      - name: OpenAPI
        description: APIs.json references OpenAPI specifications as a core property type, linking machine-readable API interface descriptions to their operations metadata.
      - name: Backstage
        description: APIs.json files can be imported into Spotify Backstage using the apis-json/backstage integration tool for enterprise developer portal use.
      - name: Spectral
        description: Spectral rulesets can validate APIs.json files against the specification schema and enforce organizational governance rules for API operations.
      - name: AsyncAPI
        description: APIs.json supports AsyncAPI as a property type, allowing event-driven and message-based APIs to be documented alongside REST APIs in a single APIs.json file.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
