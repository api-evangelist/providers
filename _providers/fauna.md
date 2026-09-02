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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Fauna Agentic Access
  operation_count: 10
  slug: fauna-agentic-access
  summary_line: 10 operations · 8 acting
api_count: 1
apis:
- description: The Fauna Event Streaming API enables real-time change data capture by maintaining an open connection to the Fauna database and pushing events to clients as they occur. Developers can subscribe to doc
  name: Fauna Event Streaming API
  slug: event-streaming-api
- description: The Fauna Event Feeds API provides a polling-based approach to change data capture, complementing the real-time Event Streaming API. Event feeds allow developers to retrieve batches of change events a
  name: Fauna Event Feeds API
  slug: event-feeds-api
- description: 'The Fauna GraphQL API allows developers to interact with their Fauna databases using standard GraphQL queries and mutations. By uploading a GraphQL schema, Fauna automatically generates the necessary '
  name: Fauna GraphQL API
  slug: graphql-api
- description: The Fauna JavaScript Driver is the official client SDK for interacting with Fauna from JavaScript and TypeScript applications. It provides template-based FQL query interpolation with type safety and a
  name: Fauna JavaScript Driver
  slug: javascript-driver
- description: The Fauna Python Driver is the official client SDK for accessing Fauna from Python applications. It provides idiomatic Python interfaces for composing and executing FQL v10 queries, managing authentic
  name: Fauna Python Driver
  slug: python-driver
- description: The Fauna .NET Driver is the official client SDK for interacting with Fauna from C# and .NET applications. It is designed for use with FQL v10 and provides strongly-typed query construction and respon
  name: Fauna .NET Driver
  slug: dotnet-driver
- description: Poll-based change data capture using event feeds. Retrieve batches of change events at your own pace for scheduled synchronization and batch processing workflows.
  name: fauna EventFeeds API
  slug: fauna-eventfeeds-api
- description: Execute Fauna Query Language (FQL) queries against a Fauna database.
  name: fauna Query API
  slug: fauna-query-api
- description: Fetch, update, validate, and manage a database's schema as FSL files. Supports staged schema changes with status checking, committing, and abandoning.
  name: fauna Schema API
  slug: fauna-schema-api
artifact_total: 48
asyncapis:
- description: The Fauna Event Streaming API enables real-time change data capture by maintaining an open connection to the Fauna database and pushing events to clients as they occur. Developers can subscribe to doc
  name: Fauna Event Streaming
  slug: fauna-event-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/fauna-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fauna-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fauna-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/faunainc
- group: design
  title: ''
  type: JSONLD
  url: json-ld/fauna-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fauna-document-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fauna-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/fauna-query-schema.json
description: Fauna is a distributed document-relational database delivered as a cloud API that combines the relational query power of SQL with the flexibility of documents and global serverless distribution.
finops:
- name: Fauna Finops
  service_category: Database / Serverless
  slug: fauna-finops
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
modified: '2026-05-19'
name: fauna
nav: Providers
network: true
overview: 'fauna publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Event Streaming API, GraphQL API, EventFeeds API, and 2 more.


  The fauna catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  fauna''s developer surface includes authentication and 7 more developer resources.'
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
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: fauna API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: fauna-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: fauna API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: fauna-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 72.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 65.2
    developer_ergonomics: 16.7
    discoverability: 44.4
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fauna/refs/heads/main/screenshots/fauna-2026-06-20T181057.png
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
---
