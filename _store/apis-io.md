---
aid: apis-io
name: APIs.io
description: APIs.io is an open source API search engine and directory that uses APIs.json files to discover, index, and catalog APIs across the web. Built on the APIs.json specification, it provides a searchable entry point for developers to find public APIs by keyword, resource, action, persona, domain, and schema. The platform indexes 779 providers, 3,188 APIs, 587 capabilities, 36,602 schemas, 49 event specs, 2,078 vocabularies, and 450 rulesets. It is maintained by Kin Lane, Nicolas Grenier, and Steven Willmott and supports both API producers (submitting APIs) and API consumers (discovering APIs). APIs.io uses a Spectral-powered rating system to evaluate API documentation quality.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Aggregation
  - API Directory
  - API Discovery
  - API Indexing
  - API Rating
  - API Search
  - APIs.json
  - Search Engine
url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: apis-io:search-api
    name: APIs.io Search API
    description: The APIs.io Search API allows developers to search for APIs across all indexed APIs.json files using keywords or phrases, and to submit new APIs to the index by providing a valid APIs.json document. The API supports pagination, filtering, and returns results with name, description, tags, score, and URLs. Authentication is handled via the separate Authentication API which converts GitHub Personal Access Tokens into API keys.
    humanURL: https://developer.apis.io/documentation/
    baseURL: https://search-api.apis.io
    tags:
      - API Discovery
      - API Indexing
      - API Search
      - APIs.json
    properties:
      - type: Documentation
        url: https://developer.apis.io/documentation/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/openapi/apis-io-search-openapi.yaml
      - type: Postman Collection
        url: https://www.postman.com/api-evangelist/apis-io-api-evangelist-engine/collection/hn8xpmd/apis-io-search-api
      - type: Authentication
        url: https://developer.apis.io/authentication/
      - type: RateLimits
        url: https://developer.apis.io/plans/
      - type: ChangeLog
        url: https://developer.apis.io/change-log/
      - type: StatusPage
        url: https://www.postman.com/api-evangelist/apis-io/monitor/APIs-io-Search---Status~1ef6bc29-9da9-4040-b98b-cef03be1155e
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/json-schema/apis-io-search-search-schema.json
        title: Search Response Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/json-schema/apis-io-search-ap-is-json-schema.json
        title: APIs.json Schema
common:
  - type: Website
    url: https://apis.io
  - type: About
    url: https://apis.io/about/
  - type: Blog
    url: https://apis.io/blog/
  - type: DeveloperPortal
    url: https://developer.apis.io/
  - type: Blog
    url: https://developer.apis.io/blog/
    title: Developer Blog
  - type: GettingStarted
    url: https://developer.apis.io/getting-started/
  - type: Authentication
    url: https://developer.apis.io/authentication/
  - type: Plans
    url: https://developer.apis.io/plans/
  - type: ChangeLog
    url: https://developer.apis.io/change-log/
  - type: ReleaseNotes
    url: https://developer.apis.io/change-log/
  - type: Versioning
    url: https://developer.apis.io/versioning/
  - type: Support
    url: https://developer.apis.io/support/
  - type: TermsOfService
    url: https://developer.apis.io/terms-of-service/
  - type: PrivacyPolicy
    url: https://developer.apis.io/privacy-policy/
  - type: GitHubOrganization
    url: https://github.com/api-search
  - type: GitHubRepository
    url: https://github.com/apisio/apis.io
  - type: GitHubRepository
    url: https://github.com/api-search/apis-io-search
    title: Search API
  - type: GitHubRepository
    url: https://github.com/api-search/apis-io-engine
    title: Search Engine
  - type: GitHubRepository
    url: https://github.com/api-search/apis-io-authentication
    title: Authentication API
  - type: GitHubRepository
    url: https://github.com/api-search/apis-io-ratings
    title: Ratings API
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/rules/apis-io-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/vocabulary/apis-io-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/capabilities/api-discovery-search.yaml
    title: API Discovery and Search Capability
  - type: Features
    data:
      - name: API Search
        description: Full-text search across 3,000+ indexed APIs by keyword, resource, action, persona, domain, and schema using a cloud search engine.
      - name: APIs.json Indexing
        description: Automatically indexes APIs.json files submitted by API producers to build a comprehensive, machine-readable catalog of API operations.
      - name: API Submission
        description: API producers can submit their APIs to the index by providing a valid APIs.json document via the Search API POST endpoint or GitHub issues.
      - name: Spectral API Ratings
        description: Spectral-powered quality rating system that evaluates API documentation completeness and scores APIs to help consumers identify high-quality APIs.
      - name: Microservice Architecture
        description: Built as a set of microservices including Search, Engine, Authentication, Publishing, Tags, Rules, Properties, Maintainers, and Ratings APIs.
      - name: Topic Search Nodes
        description: Specialized search nodes for domain-specific API discovery including AI, Healthcare, Banking, Payments, Weather, CRM, Cloud, and many more topic areas.
      - name: Open Source
        description: The platform is open source, licensed under Apache-2.0, with all microservice APIs available on GitHub under the api-search organization.
  - type: UseCases
    data:
      - name: API Discovery
        description: Developers can search for APIs relevant to their project by keyword, discovering APIs across thousands of providers without knowing where to look.
      - name: API Submission
        description: API producers can submit their APIs.json files to ensure their APIs are discoverable in the index and properly cataloged with metadata.
      - name: Quality Assessment
        description: Development teams use the Spectral ratings system to identify high-quality APIs and avoid poorly documented or unmaintained options.
      - name: Catalog Building
        description: Platform teams use APIs.io as a reference implementation for building their own internal API catalogs using the APIs.json format.
      - name: Domain-Specific Search
        description: Developers searching for APIs in specific domains (healthcare, finance, AI) can use topic-specific search nodes for more targeted discovery.
  - type: Integrations
    data:
      - name: APIs.json
        description: Core integration with the APIs.json specification for machine-readable API description and discovery across the web.
      - name: OpenAPI
        description: APIs indexed in APIs.io reference OpenAPI specifications as a key property, linking consumers to technical API contracts.
      - name: Spectral
        description: Spectral ruleset integration powers the APIs.io rating system, evaluating API documentation quality against standardized rules.
      - name: GitHub
        description: GitHub integration for API submission via issues, source of truth for indexed APIs.json files, and authentication via Personal Access Tokens.
      - name: Postman
        description: Postman public workspace integration for running and testing the APIs.io Search API via pre-built collections.
      - name: AWS API Gateway
        description: The APIs.io Search API is deployed and managed through AWS API Gateway for scalable, managed API access.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
