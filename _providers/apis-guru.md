---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apis Guru Agentic Access
  operation_count: 7
  slug: apis-guru-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: Actions relating to APIs in the collection
  name: APIs.guru APIs API
  slug: apis-guru-apis-api
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: .guru APIs API
  slug: open-apis-guru-apis-api
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/APIs-guru/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/APIs-guru/openapi-directory/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/APIs-guru/openapi-directory/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apis-guru-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apis-guru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apis.guru
- group: company
  title: ''
  type: About
  url: https://apis.guru/about
- group: docs
  title: ''
  type: Documentation
  url: https://apis.guru/api-doc
- group: company
  title: ''
  type: Blog
  url: https://apis.guru/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APIs-guru
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/APIs-guru/openapi-directory
- group: build
  title: AsyncAPI Directory
  type: GitHubRepository
  url: https://github.com/APIs-guru/asyncapi-directory
- group: build
  title: GraphQL Voyager
  type: GitHubRepository
  url: https://github.com/APIs-guru/graphql-voyager
- group: build
  title: Awesome OpenAPI 3
  type: GitHubRepository
  url: https://github.com/APIs-guru/awesome-openapi3
- group: build
  title: AWS to OpenAPI Converter
  type: GitHubRepository
  url: https://github.com/APIs-guru/aws2openapi
- group: build
  title: Google Discovery to OpenAPI Converter
  type: GitHubRepository
  url: https://github.com/APIs-guru/google-discovery-to-swagger
- group: build
  title: GraphQL Faker
  type: GitHubRepository
  url: https://github.com/APIs-guru/graphql-faker
- group: build
  title: Public GraphQL APIs Directory
  type: GitHubRepository
  url: https://github.com/APIs-guru/graphql-apis
- group: other
  title: ''
  type: X
  url: https://x.com/APIs_guru
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/rules/apis-guru-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/vocabulary/apis-guru-vocabulary.yaml
- group: operate
  title: ''
  type: Support
  url: https://github.com/APIs-guru/openapi-directory/issues
created: '2026-03-25'
description: APIs.guru is an open source, community-driven directory of public REST API definitions in OpenAPI 2.0/3.x format, described as the Wikipedia for Web APIs. The project searches for public API definitions, converts various formats to OpenAPI 3.0, corrects errors in approximately 80% of definitions, and enriches entries with logos, categories, and metadata. It catalogs over 2,500 API descriptions with 100,000+ endpoints, updating definitions weekly from original sources. The platform is licensed under CC0-1.0 for contributed definitions and welcomes community contributions through GitHub.
examples:
- key_count: 0
  name: Apis Guru Ap Is Example
  slug: apis-guru-ap-is-example
- key_count: 3
  name: Apis Guru Api Example
  slug: apis-guru-api-example
- key_count: 8
  name: Apis Guru Api Version Example
  slug: apis-guru-api-version-example
- key_count: 14
  name: Apis Guru Metrics Example
  slug: apis-guru-metrics-example
features:
- description: Comprehensive directory of over 2,500 public API definitions in OpenAPI 2.0 and 3.x format, updated weekly from original sources.
  name: OpenAPI Directory
- description: Converts various API description formats (RAML, Google Discovery, AWS, etc.) to OpenAPI 3.0 standard for consistency and compatibility.
  name: Format Conversion
- description: Corrects errors in approximately 80% of API definitions and validates all specifications before inclusion in the directory.
  name: Quality Control
- description: Companion directory of asynchronous API specifications in AsyncAPI format for event-driven and message-based APIs.
  name: AsyncAPI Directory
- description: Visual tool that represents any GraphQL API as an interactive graph, making schema exploration intuitive and visual.
  name: GraphQL Voyager
- description: Public REST API at api.apis.guru/v2 for programmatic access to the directory, metrics, provider lists, and individual API specs.
  name: REST API Access
- description: RSS feeds for both newly added and recently updated API definitions, allowing developers to stay current with directory changes.
  name: RSS Feeds
- description: Enriches API definitions with logos, categories, provider names, and other metadata to improve discoverability and browsability.
  name: Metadata Enrichment
finops:
- name: Apis Guru Finops
  service_category: API
  slug: apis-guru-finops
graphqls:
- description: ''
  name: APIs.guru GraphQL API
  slug: apis-guru-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apis-guru.png
integrations:
- description: HTTP debugging and testing platform that integrates with API definitions from the APIs.guru directory for request interception.
  name: HTTP Toolkit
- description: Microsoft's API client generator that uses OpenAPI specs from APIs.guru to generate typed API clients in multiple languages.
  name: Microsoft Kiota
- description: SDK generation platform that pulls OpenAPI definitions from the directory to generate production-ready SDKs for API providers.
  name: Speakeasy
- description: API documentation generation tool that uses OpenAPI specs from APIs.guru to create beautiful, customizable documentation sites.
  name: ReDoc
- description: Community funding platform where APIs.guru receives financial support from sponsors who benefit from the open directory.
  name: Open Collective
json_schemas:
- name: APIs
  property_count: 0
  slug: apis-guru-ap-is
- name: API
  property_count: 3
  slug: apis-guru-api
- name: ApiVersion
  property_count: 8
  slug: apis-guru-api-version
- name: Metrics
  property_count: 14
  slug: apis-guru-metrics
json_structures:
- name: Apis Guru Ap Is Structure
  property_count: 0
  slug: apis-guru-ap-is-structure
- name: Apis Guru Api Structure
  property_count: 3
  slug: apis-guru-api-structure
- name: Apis Guru Api Version Structure
  property_count: 8
  slug: apis-guru-api-version-structure
- name: Apis Guru Metrics Structure
  property_count: 14
  slug: apis-guru-metrics-structure
jsonld:
- class_count: 5
  name: Apis Guru Context
  property_count: 23
  slug: apis-guru-context
layout: provider
modified: '2026-05-19'
name: APIs.guru
nav: Providers
network: true
overview: 'APIs.guru publishes 1 API on the [APIs.io](https://apis.io/) network: APIs API. Tagged areas include API Catalog, API Directory, API Discovery, Community, and GraphQL.


  The APIs.guru catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  APIs.guru''s developer surface includes documentation, engineering blog, support, and 19 more developer resources.'
plans:
- name: Apis Guru Plans Pricing
  plan_count: 3
  slug: apis-guru-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Apis Guru Rate Limits
  slug: apis-guru-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: APIs.guru API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apis-guru-jsonschema-spectral-rules
- effective_rule_count: 75
  extends:
  - spectral:oas
  name: APIs.guru API Rules
  rule_count: 34
  severity_counts:
    error: 13
    hint: 0
    info: 5
    warn: 16
  slug: apis-guru-spectral-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 29.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 65.3
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apis-guru/refs/heads/main/screenshots/apis-guru-2026-06-20T172300.png
security:
- kind: domain-security
  name: Apis Guru Domain Security
  slug: apis-guru-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apis-guru
tags:
- API Catalog
- API Directory
- API Discovery
- Community
- GraphQL
- Open-Source
- OpenAPI
use_cases:
- description: Developers can search and browse the directory to discover public APIs across thousands of providers by category, provider, or keyword.
  name: API Discovery
- description: OpenAPI specs from the directory can be used with tools like Microsoft Kiota and Speakeasy to generate API client SDKs.
  name: SDK Generation
- description: ReDoc and other documentation tools use the directory specs to generate beautiful, interactive API documentation automatically.
  name: API Documentation
- description: HTTP Toolkit and other testing tools leverage the directory for debugging and mocking API requests against standardized specs.
  name: API Testing
- description: GraphQL Voyager allows teams to visually explore GraphQL schema relationships to understand API structure quickly.
  name: Schema Exploration
- description: Organizations can use the directory as a foundation for building their own internal API catalogs and governance programs.
  name: API Catalog Building
website: https://apis.guru
---
