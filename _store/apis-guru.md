---
aid: apis-guru
name: APIs.guru
description: APIs.guru is an open source, community-driven directory of public REST API definitions in OpenAPI 2.0/3.x format, described as the Wikipedia for Web APIs. The project searches for public API definitions, converts various formats to OpenAPI 3.0, corrects errors in approximately 80% of definitions, and enriches entries with logos, categories, and metadata. It catalogs over 2,500 API descriptions with 100,000+ endpoints, updating definitions weekly from original sources. The platform is licensed under CC0-1.0 for contributed definitions and welcomes community contributions through GitHub.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Catalog
  - API Directory
  - API Discovery
  - Community
  - GraphQL
  - Open Source
  - OpenAPI
url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apis-guru:apis-guru-api
    name: APIs.guru REST API
    description: The APIs.guru REST API provides programmatic access to the directory of public API definitions, allowing developers to search, browse, and retrieve OpenAPI specifications from the catalog. The API is public and requires no authentication. It provides endpoints to list all APIs, fetch metrics, retrieve provider lists, and access specific API version details including direct links to OpenAPI specs in JSON and YAML formats.
    humanURL: https://apis.guru/api-doc
    baseURL: https://api.apis.guru/v2
    tags:
      - API Catalog
      - API Directory
      - API Discovery
      - OpenAPI
    properties:
      - type: Documentation
        url: https://apis.guru/api-doc
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/openapi/apis-guru-openapi.yaml
      - type: Postman Collection
        url: https://www.postman.com/api-evangelist/apis-guru/documentation/wtbfnfn/apis-guru
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/json-schema/apis-guru-api-schema.json
        title: API Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/json-schema/apis-guru-api-version-schema.json
        title: API Version Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/json-schema/apis-guru-metrics-schema.json
        title: Metrics Schema
common:
  - type: Website
    url: https://apis.guru
  - type: About
    url: https://apis.guru/about
  - type: Documentation
    url: https://apis.guru/api-doc
  - type: Blog
    url: https://apis.guru/blog
  - type: GitHubOrganization
    url: https://github.com/APIs-guru
  - type: GitHubRepository
    url: https://github.com/APIs-guru/openapi-directory
  - type: GitHubRepository
    url: https://github.com/APIs-guru/asyncapi-directory
    title: AsyncAPI Directory
  - type: GitHubRepository
    url: https://github.com/APIs-guru/graphql-voyager
    title: GraphQL Voyager
  - type: GitHubRepository
    url: https://github.com/APIs-guru/awesome-openapi3
    title: Awesome OpenAPI 3
  - type: GitHubRepository
    url: https://github.com/APIs-guru/aws2openapi
    title: AWS to OpenAPI Converter
  - type: GitHubRepository
    url: https://github.com/APIs-guru/google-discovery-to-swagger
    title: Google Discovery to OpenAPI Converter
  - type: GitHubRepository
    url: https://github.com/APIs-guru/graphql-faker
    title: GraphQL Faker
  - type: GitHubRepository
    url: https://github.com/APIs-guru/graphql-apis
    title: Public GraphQL APIs Directory
  - type: X
    url: https://x.com/APIs_guru
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/rules/apis-guru-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/vocabulary/apis-guru-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/capabilities/api-discovery.yaml
    title: API Discovery Capability
  - type: Support
    url: https://github.com/APIs-guru/openapi-directory/issues
  - type: Features
    data:
      - name: OpenAPI Directory
        description: Comprehensive directory of over 2,500 public API definitions in OpenAPI 2.0 and 3.x format, updated weekly from original sources.
      - name: Format Conversion
        description: Converts various API description formats (RAML, Google Discovery, AWS, etc.) to OpenAPI 3.0 standard for consistency and compatibility.
      - name: Quality Control
        description: Corrects errors in approximately 80% of API definitions and validates all specifications before inclusion in the directory.
      - name: AsyncAPI Directory
        description: Companion directory of asynchronous API specifications in AsyncAPI format for event-driven and message-based APIs.
      - name: GraphQL Voyager
        description: Visual tool that represents any GraphQL API as an interactive graph, making schema exploration intuitive and visual.
      - name: REST API Access
        description: Public REST API at api.apis.guru/v2 for programmatic access to the directory, metrics, provider lists, and individual API specs.
      - name: RSS Feeds
        description: RSS feeds for both newly added and recently updated API definitions, allowing developers to stay current with directory changes.
      - name: Metadata Enrichment
        description: Enriches API definitions with logos, categories, provider names, and other metadata to improve discoverability and browsability.
  - type: UseCases
    data:
      - name: API Discovery
        description: Developers can search and browse the directory to discover public APIs across thousands of providers by category, provider, or keyword.
      - name: SDK Generation
        description: OpenAPI specs from the directory can be used with tools like Microsoft Kiota and Speakeasy to generate API client SDKs.
      - name: API Documentation
        description: ReDoc and other documentation tools use the directory specs to generate beautiful, interactive API documentation automatically.
      - name: API Testing
        description: HTTP Toolkit and other testing tools leverage the directory for debugging and mocking API requests against standardized specs.
      - name: Schema Exploration
        description: GraphQL Voyager allows teams to visually explore GraphQL schema relationships to understand API structure quickly.
      - name: API Catalog Building
        description: Organizations can use the directory as a foundation for building their own internal API catalogs and governance programs.
  - type: Integrations
    data:
      - name: HTTP Toolkit
        description: HTTP debugging and testing platform that integrates with API definitions from the APIs.guru directory for request interception.
      - name: Microsoft Kiota
        description: Microsoft's API client generator that uses OpenAPI specs from APIs.guru to generate typed API clients in multiple languages.
      - name: Speakeasy
        description: SDK generation platform that pulls OpenAPI definitions from the directory to generate production-ready SDKs for API providers.
      - name: ReDoc
        description: API documentation generation tool that uses OpenAPI specs from APIs.guru to create beautiful, customizable documentation sites.
      - name: Open Collective
        description: Community funding platform where APIs.guru receives financial support from sponsors who benefit from the open directory.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
