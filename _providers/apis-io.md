---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Apis Io Agentic Access
  operation_count: 64
  slug: apis-io-agentic-access
  summary_line: 64 operations · 1 acting
api_count: 11
apis:
- description: Index of HTTP application programming interfaces.
  name: APIs.io APIs API
  slug: apis-io-apis-api
- description: The API Evangelist areas taxonomy — curated topic collections (authentication, webhooks, payments, …), each a scored provider index with its own site. Pro.
  name: APIs.io Areas API
  slug: apis-io-areas-api
- description: First-class, per-type artifact collections (OpenAPI, AsyncAPI, Arazzo, Postman, JSON Schema, and more). Each path filters and normalizes one artifact type across all providers.
  name: APIs.io Artifact Types API
  slug: apis-io-artifact-types-api
- description: Industry verticals grouping providers across the catalog.
  name: APIs.io Industries API
  slug: apis-io-industries-api
- description: Demand-side intelligence — what ~5,800 companies (Fortune 1000 + API providers) build, buy, and hire for around APIs, data, and AI, derived from job postings, press, and engineering blogs. Discovery i
  name: APIs.io Insights API
  slug: apis-io-insights-api
- description: Organizations publishing APIs on the network.
  name: APIs.io Providers API
  slug: apis-io-providers-api
- description: 'The APIs.io API rating system — a 0–100 composite score, five bands, a trend marker, and six weighted facets measuring how complete, governed, and integration-ready each provider''s public API surface '
  name: APIs.io Ratings API
  slug: apis-io-ratings-api
- description: Geographic regions grouping providers across the catalog.
  name: APIs.io Regions API
  slug: apis-io-regions-api
- description: Search using a cloud search engine.
  name: APIs.io Search API
  slug: apis-io-search-api
- description: Decision-grade composites over the catalog — provider comparison, gap analysis, catalog change feed, and recommended-stack design. Pro.
  name: APIs.io Synthesis API
  slug: apis-io-synthesis-api
- description: The tag taxonomy, with network-wide ranking metadata.
  name: APIs.io Tags API
  slug: apis-io-tags-api
arazzos:
- description: Run two keyword searches against APIs.io and compare how many APIs the index holds for each term.
  name: APIs.io Compare Keyword Coverage
  slug: apis-io-compare-keyword-coverage-workflow
- description: Read the first page of a keyword search, learn the total page count, then fetch a following page of results.
  name: APIs.io Paginate Search Results
  slug: apis-io-paginate-search-results-workflow
- description: Search the APIs.io registry for APIs matching a keyword and branch on whether any results were returned.
  name: APIs.io Search APIs by Keyword
  slug: apis-io-search-apis-workflow
- description: Submit a valid APIs.json to the APIs.io index, then search the registry to confirm the submitted API appears.
  name: APIs.io Submit and Verify API
  slug: apis-io-submit-and-verify-api-workflow
artifact_total: 92
collections:
- collection_type: postman
  name: .io Search APIs API
  slug: postman-apis-io-apis-api
- collection_type: postman
  name: .io Search APIs Areas API
  slug: postman-apis-io-areas-api
- collection_type: postman
  name: .io Search APIs Artifact Types API
  slug: postman-apis-io-artifact-types-api
- collection_type: postman
  name: .io Search APIs Industries API
  slug: postman-apis-io-industries-api
- collection_type: postman
  name: .io Search APIs Insights API
  slug: postman-apis-io-insights-api
- collection_type: postman
  name: .io Search APIs Providers API
  slug: postman-apis-io-providers-api
- collection_type: postman
  name: .io Search APIs Ratings API
  slug: postman-apis-io-ratings-api
- collection_type: postman
  name: .io Search APIs Regions API
  slug: postman-apis-io-regions-api
- collection_type: postman
  name: .io APIs Search API
  slug: postman-apis-io-search-api
- collection_type: postman
  name: .io Search APIs Synthesis API
  slug: postman-apis-io-synthesis-api
- collection_type: postman
  name: .io Search APIs Tags API
  slug: postman-apis-io-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apisio/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apis-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apis-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apis-io-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apis-io-compare-keyword-coverage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apis-io-paginate-search-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apis-io-search-apis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/apis-io-submit-and-verify-api-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://apis.io
- group: company
  title: ''
  type: About
  url: https://apis.io/about/
- group: company
  title: ''
  type: Blog
  url: https://apis.io/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apis.io/developer/
- group: company
  title: Developer Blog
  type: Blog
  url: https://apis.io/developer/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.io/developer/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://apis.io/developer/authentication/
- group: commercial
  title: ''
  type: Plans
  url: https://apis.io/developer/plans/
- group: operate
  title: ''
  type: ChangeLog
  url: https://apis.io/developer/change-log/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://apis.io/developer/change-log/
- group: design
  title: ''
  type: Versioning
  url: https://apis.io/developer/versioning/
- group: operate
  title: ''
  type: Support
  url: https://apis.io/developer/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apis.io/developer/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apis.io/developer/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-search
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apisio/apis.io
- group: build
  title: Search API
  type: GitHubRepository
  url: https://github.com/api-search/apis-io-search
- group: build
  title: Search Engine
  type: GitHubRepository
  url: https://github.com/api-search/apis-io-engine
- group: build
  title: Authentication API
  type: GitHubRepository
  url: https://github.com/api-search/apis-io-authentication
- group: build
  title: Ratings API
  type: GitHubRepository
  url: https://github.com/api-search/apis-io-ratings
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/rules/apis-io-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/vocabulary/apis-io-vocabulary.yaml
created: '2026-03-26'
description: APIs.io is an open source API search engine and directory that uses APIs.json files to discover, index, and catalog APIs across the web. Built on the APIs.json specification, it provides a searchable entry point for developers to find public APIs by keyword, resource, action, persona, domain, and schema. The platform indexes 779 providers, 3,188 APIs, 587 capabilities, 36,602 schemas, 49 event specs, 2,078 vocabularies, and 450 rulesets. It is maintained by Kin Lane, Nicolas Grenier, and Steven Willmott and supports both API producers (submitting APIs) and API consumers (discovering APIs). APIs.io uses a Spectral-powered rating system to evaluate API documentation quality.
examples:
- key_count: 1
  name: Apis Io Search Add Ap Is Json Example
  slug: apis-io-search-add-ap-is-json-example
- key_count: 0
  name: Apis Io Search Ap Is Example
  slug: apis-io-search-ap-is-example
- key_count: 11
  name: Apis Io Search Ap Is Json Example
  slug: apis-io-search-ap-is-json-example
- key_count: 9
  name: Apis Io Search Api Example
  slug: apis-io-search-api-example
- key_count: 9
  name: Apis Io Search Contact Example
  slug: apis-io-search-contact-example
- key_count: 2
  name: Apis Io Search Include Example
  slug: apis-io-search-include-example
- key_count: 5
  name: Apis Io Search Link Example
  slug: apis-io-search-link-example
- key_count: 1
  name: Apis Io Search Maintainer Example
  slug: apis-io-search-maintainer-example
- key_count: 5
  name: Apis Io Search Meta Example
  slug: apis-io-search-meta-example
- key_count: 2
  name: Apis Io Search Meta Information Example
  slug: apis-io-search-meta-information-example
- key_count: 2
  name: Apis Io Search Property Example
  slug: apis-io-search-property-example
- key_count: 3
  name: Apis Io Search Search Example
  slug: apis-io-search-search-example
- key_count: 0
  name: Apis Io Search Tag Example
  slug: apis-io-search-tag-example
features:
- description: Full-text search across 3,000+ indexed APIs by keyword, resource, action, persona, domain, and schema using a cloud search engine.
  name: API Search
- description: Automatically indexes APIs.json files submitted by API producers to build a comprehensive, machine-readable catalog of API operations.
  name: APIs.json Indexing
- description: API producers can submit their APIs to the index by providing a valid APIs.json document via the Search API POST endpoint or GitHub issues.
  name: API Submission
- description: Spectral-powered quality rating system that evaluates API documentation completeness and scores APIs to help consumers identify high-quality APIs.
  name: Spectral API Ratings
- description: Built as a set of microservices including Search, Engine, Authentication, Publishing, Tags, Rules, Properties, Maintainers, and Ratings APIs.
  name: Microservice Architecture
- description: Specialized search nodes for domain-specific API discovery including AI, Healthcare, Banking, Payments, Weather, CRM, Cloud, and many more topic areas.
  name: Topic Search Nodes
- description: The platform is open source, licensed under Apache-2.0, with all microservice APIs available on GitHub under the api-search organization.
  name: Open Source
finops:
- name: Apis Io Finops
  service_category: API
  slug: apis-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apis-io.png
integrations:
- description: Core integration with the APIs.json specification for machine-readable API description and discovery across the web.
  name: APIs.json
- description: APIs indexed in APIs.io reference OpenAPI specifications as a key property, linking consumers to technical API contracts.
  name: OpenAPI
- description: Spectral ruleset integration powers the APIs.io rating system, evaluating API documentation quality against standardized rules.
  name: Spectral
- description: GitHub integration for API submission via issues, source of truth for indexed APIs.json files, and authentication via Personal Access Tokens.
  name: GitHub
- description: Postman public workspace integration for running and testing the APIs.io Search API via pre-built collections.
  name: Postman
- description: The APIs.io Search API is deployed and managed through AWS API Gateway for scalable, managed API access.
  name: AWS API Gateway
json_schemas:
- name: AddAPIsJSON
  property_count: 1
  slug: apis-io-search-add-ap-is-json
- name: APIsJSON
  property_count: 11
  slug: apis-io-search-ap-is-json
- name: APIs
  property_count: 0
  slug: apis-io-search-ap-is
- name: API
  property_count: 9
  slug: apis-io-search-api
- name: Contact
  property_count: 9
  slug: apis-io-search-contact
- name: Include
  property_count: 2
  slug: apis-io-search-include
- name: Link
  property_count: 5
  slug: apis-io-search-link
- name: Maintainer
  property_count: 1
  slug: apis-io-search-maintainer
- name: metaInformation
  property_count: 2
  slug: apis-io-search-meta-information
- name: Meta
  property_count: 5
  slug: apis-io-search-meta
- name: Property
  property_count: 2
  slug: apis-io-search-property
- name: Search
  property_count: 3
  slug: apis-io-search-search
- name: Tag
  property_count: 0
  slug: apis-io-search-tag
json_structures:
- name: Apis Io Search Add Ap Is Json Structure
  property_count: 1
  slug: apis-io-search-add-ap-is-json-structure
- name: Apis Io Search Ap Is Json Structure
  property_count: 11
  slug: apis-io-search-ap-is-json-structure
- name: Apis Io Search Ap Is Structure
  property_count: 0
  slug: apis-io-search-ap-is-structure
- name: Apis Io Search Api Structure
  property_count: 9
  slug: apis-io-search-api-structure
- name: Apis Io Search Contact Structure
  property_count: 9
  slug: apis-io-search-contact-structure
- name: Apis Io Search Include Structure
  property_count: 2
  slug: apis-io-search-include-structure
- name: Apis Io Search Link Structure
  property_count: 5
  slug: apis-io-search-link-structure
- name: Apis Io Search Maintainer Structure
  property_count: 1
  slug: apis-io-search-maintainer-structure
- name: Apis Io Search Meta Information Structure
  property_count: 2
  slug: apis-io-search-meta-information-structure
- name: Apis Io Search Meta Structure
  property_count: 5
  slug: apis-io-search-meta-structure
- name: Apis Io Search Property Structure
  property_count: 2
  slug: apis-io-search-property-structure
- name: Apis Io Search Search Structure
  property_count: 3
  slug: apis-io-search-search-structure
- name: Apis Io Search Tag Structure
  property_count: 0
  slug: apis-io-search-tag-structure
jsonld:
- class_count: 15
  name: Apis Io Context
  property_count: 34
  slug: apis-io-context
layout: provider
modified: '2026-05-19'
name: APIs.io
nav: Providers
network: true
overview: 'APIs.io publishes 11 APIs on the [APIs.io](https://apis.io/) network, including APIs API, Areas API, Artifact Types API, and 8 more. Tagged areas include API Aggregation, API Directory, API Discovery, API Indexing, and API Rating.


  The APIs.io catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  APIs.io''s developer surface includes authentication, engineering blog, getting-started guide, changelog, release notes, support, and 24 more developer resources.'
plans:
- name: Apis Io Plans Pricing
  plan_count: 3
  slug: apis-io-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Apis Io Rate Limits
  slug: apis-io-rate-limits
rules:
- name: APIs.io API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apis-io-jsonschema-spectral-rules
- name: APIs.io API Rules
  rule_count: 42
  severity_counts:
    error: 13
    hint: 0
    info: 6
    warn: 23
  slug: apis-io-spectral-rules
score:
  band: strong
  composite: 62.0
  delta: -4.4
  facets:
    commercial_clarity: 60.5
    contract_quality: 76.5
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apis-io/refs/heads/main/screenshots/apis-io-2026-06-20T172253.png
security:
- kind: authentication
  name: Apis Io Authentication
  slug: apis-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Apis Io Domain Security
  slug: apis-io-domain-security
  summary_line: TLSv1.3
slug: apis-io
tags:
- API Aggregation
- API Directory
- API Discovery
- API Indexing
- API Rating
- API Search
- APIs.json
- Search Engine
use_cases:
- description: Developers can search for APIs relevant to their project by keyword, discovering APIs across thousands of providers without knowing where to look.
  name: API Discovery
- description: API producers can submit their APIs.json files to ensure their APIs are discoverable in the index and properly cataloged with metadata.
  name: API Submission
- description: Development teams use the Spectral ratings system to identify high-quality APIs and avoid poorly documented or unmaintained options.
  name: Quality Assessment
- description: Platform teams use APIs.io as a reference implementation for building their own internal API catalogs using the APIs.json format.
  name: Catalog Building
- description: Developers searching for APIs in specific domains (healthcare, finance, AI) can use topic-specific search nodes for more targeted discovery.
  name: Domain-Specific Search
website: https://apis.io
---
