---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Fauna Agentic Access
  operation_count: 10
  slug: fauna-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 1
apis:
- baseURL: https://db.fauna.com
  baseurl_source: declared
  description: The Fauna Event Streaming API enables real-time change data capture by maintaining an open connection to the Fauna database and pushing events to clients as they occur. Developers can subscribe to doc
  name: Fauna Event Streaming API
  slug: event-streaming-api
- description: The Fauna Event Feeds API provides a polling-based approach to change data capture, complementing the real-time Event Streaming API. Event feeds allow developers to retrieve batches of change events a
  name: Fauna Event Feeds API
  slug: event-feeds-api
- description: The Fauna JavaScript Driver is the official client SDK for interacting with Fauna from JavaScript and TypeScript applications. It provides template-based FQL query interpolation with type safety and a
  name: Fauna JavaScript Driver
  slug: javascript-driver
- description: The Fauna Python Driver is the official client SDK for accessing Fauna from Python applications. It provides idiomatic Python interfaces for composing and executing FQL v10 queries, managing authentic
  name: Fauna Python Driver
  slug: python-driver
- description: The Fauna .NET Driver is the official client SDK for interacting with Fauna from C# and .NET applications. It is designed for use with FQL v10 and provides strongly-typed query construction and respon
  name: Fauna .NET Driver
  slug: dotnet-driver
- baseURL: https://db.fauna.com
  baseurl_source: declared
  description: Poll-based change data capture using event feeds. Retrieve batches of change events at your own pace for scheduled synchronization and batch processing workflows.
  name: fauna EventFeeds API
  slug: fauna-eventfeeds-api
- baseURL: https://db.fauna.com
  baseurl_source: declared
  description: Execute Fauna Query Language (FQL) queries against a Fauna database.
  name: fauna Query API
  slug: fauna-query-api
- baseURL: https://db.fauna.com
  baseurl_source: declared
  description: Fetch, update, validate, and manage a database's schema as FSL files. Supports staged schema changes with status checking, committing, and abandoning.
  name: fauna Schema API
  slug: fauna-schema-api
- baseURL: https://db.fauna.com
  baseurl_source: declared
  description: Execute GraphQL queries and mutations against a Fauna database.
  name: Fauna Graph QL API
  slug: fauna-graph-ql-api
artifact_total: 47
asyncapis:
- description: The Fauna Event Streaming API enables real-time change data capture by maintaining an open connection to the Fauna database and pushing events to clients as they occur. Developers can subscribe to doc
  name: Fauna Event Streaming
  slug: fauna-event-streaming-asyncapi
collections:
- collection_type: open
  name: Fauna Core HTTP API
  slug: open-fauna-core-http-api
- collection_type: open
  name: Fauna Core HTTP EventFeeds API
  slug: open-fauna-eventfeeds-api
- collection_type: open
  name: Fauna Core HTTP EventFeeds GraphQL API
  slug: open-fauna-graphql-api
- collection_type: open
  name: Fauna Core HTTP EventFeeds Query API
  slug: open-fauna-query-api
- collection_type: open
  name: Fauna Core HTTP EventFeeds Schema API
  slug: open-fauna-schema-api
common:
- group: agent
  href: https://artifacts.apis.io/fauna/agentic-access/fauna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fauna-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/fauna/security/fauna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fauna-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fauna/authentication/fauna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fauna-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/faunainc
- group: design
  href: https://artifacts.apis.io/fauna/json-ld/fauna-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fauna-context.jsonld
- group: docs
  href: https://artifacts.apis.io/fauna/json-schema/fauna-document-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fauna-document-schema.json
- group: docs
  href: https://artifacts.apis.io/fauna/json-schema/fauna-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fauna-event-schema.json
- group: docs
  href: https://artifacts.apis.io/fauna/json-schema/fauna-query-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/fauna-query-schema.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fauna
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/fauna/faunadb
- group: build
  href: https://artifacts.apis.io/fauna/packages/fauna-packages.yml
  title: ''
  type: Packages
  url: packages/fauna-packages.yml
- group: build
  href: https://artifacts.apis.io/fauna/packages/fauna-packages.yml
  title: ''
  type: SDKs
  url: packages/fauna-packages.yml
- group: build
  href: https://artifacts.apis.io/fauna/cli/fauna-cli.yml
  title: ''
  type: CLI
  url: cli/fauna-cli.yml
- group: design
  href: https://artifacts.apis.io/fauna/lifecycle/fauna-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fauna-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fauna/conventions/fauna-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fauna-conventions.yml
- group: design
  href: https://artifacts.apis.io/fauna/errors/fauna-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fauna-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fauna/data-model/fauna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fauna-data-model.yml
- group: design
  href: https://artifacts.apis.io/fauna/conformance/fauna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fauna-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fauna/llms/fauna-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fauna-llms.txt
- group: design
  href: https://artifacts.apis.io/fauna/vocabulary/fauna-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fauna-vocabulary.yml
- group: commercial
  href: https://artifacts.apis.io/fauna/plans/fauna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fauna-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fauna/rate-limits/fauna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fauna-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fauna/finops/fauna-finops.yml
  title: ''
  type: FinOps
  url: finops/fauna-finops.yml
- group: design
  href: https://artifacts.apis.io/fauna/rules/fauna-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/fauna-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/fauna/json-structure/fauna-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/fauna-structure.json
created: '2026-05-04'
description: Fauna, Inc. built a distributed document-relational database delivered as a cloud API, combining the relational query power of SQL with the flexibility of documents, global serverless distribution and strictly serializable ACID transactions over plain HTTPS. Fauna announced End-of-Service in March 2025 and shut the hosted service down on 2025-05-30; as of 2026-09-17 every Fauna service host returns NXDOMAIN and the apex domain forwards to an unrelated company. This profile is maintained as an archival record of the API surface as it stood at shutdown.
finops:
- has_sources: true
  method: generated
  name: Fauna Finops
  primary_unit: operation | GB
  service_category: Database / Serverless
  slug: fauna-finops
  template: false
graphqls:
- description: 'The Fauna GraphQL API allows developers to interact with their Fauna databases using standard GraphQL queries and mutations. By uploading a GraphQL schema, Fauna automatically generates the necessary '
  name: fauna GraphQL API
  slug: fauna-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fauna.png
json_schemas:
- name: Fauna Document
  property_count: 4
  slug: fauna-document
- name: ErrorResponse
  property_count: 5
  slug: fauna-errorresponse
- name: Fauna Event
  property_count: 5
  slug: fauna-event
- name: EventFeedRequest
  property_count: 4
  slug: fauna-eventfeedrequest
- name: EventFeedResponse
  property_count: 4
  slug: fauna-eventfeedresponse
- name: EventStats
  property_count: 5
  slug: fauna-eventstats
- name: GraphQLError
  property_count: 4
  slug: fauna-graphqlerror
- name: GraphQLErrorResponse
  property_count: 1
  slug: fauna-graphqlerrorresponse
- name: GraphQLRequest
  property_count: 3
  slug: fauna-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: fauna-graphqlresponse
- name: Fauna Query
  property_count: 0
  slug: fauna-query
- name: QueryRequest
  property_count: 2
  slug: fauna-queryrequest
- name: QueryResponse
  property_count: 7
  slug: fauna-queryresponse
- name: QueryStats
  property_count: 8
  slug: fauna-querystats
- name: SchemaAbandonResponse
  property_count: 1
  slug: fauna-schemaabandonresponse
- name: SchemaCommitResponse
  property_count: 1
  slug: fauna-schemacommitresponse
- name: SchemaFile
  property_count: 2
  slug: fauna-schemafile
- name: SchemaFilesResponse
  property_count: 2
  slug: fauna-schemafilesresponse
- name: SchemaStatusResponse
  property_count: 3
  slug: fauna-schemastatusresponse
- name: SchemaUpdateResponse
  property_count: 2
  slug: fauna-schemaupdateresponse
- name: SchemaValidationResponse
  property_count: 3
  slug: fauna-schemavalidationresponse
json_structures:
- name: Fauna Structure
  property_count: 0
  slug: fauna-structure
jsonld:
- class_count: 0
  name: Fauna Context
  property_count: 9
  slug: fauna-context
layout: provider
modified: '2026-09-17'
name: Fauna
nav: Providers
network: true
overview: 'Fauna publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Event Streaming API, EventFeeds API, Query API, and 6 more. Tagged areas include Database, Document Database, Serverless, Distributed Systems, and Change Data Capture.


  The Fauna catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Fauna''s developer surface includes authentication, CLI, and 23 more developer resources.'
plans:
- name: Fauna Plans Pricing
  plan_count: 4
  slug: fauna-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Fauna Rate Limits
  slug: fauna-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Fauna — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: fauna-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Fauna — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: fauna-jsonschema-spectral-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fauna/fauna-2026-06-20T181057.png
security:
- kind: authentication
  name: Fauna Authentication
  slug: fauna-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fauna Domain Security
  slug: fauna-domain-security
  summary_line: DMARC
slug: fauna
tags:
- Database
- Document Database
- Serverless
- Distributed Systems
- Change Data Capture
- GraphQL
- Cloud
- Developer Tools
- Defunct
---
