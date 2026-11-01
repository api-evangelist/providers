---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 43
  human_in_the_loop: 0
  name: Artie Agentic Access
  operation_count: 60
  slug: artie-agentic-access
  summary_line: 60 operations · 43 acting
api_count: 1
apis:
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Column Hashing Salts API from Artie — 3 operation(s) for column hashing salts.
  name: Artie Column Hashing Salts API
  slug: artie-column-hashing-salts-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Connectors API from Artie — 14 operation(s) for connectors.
  name: Artie Connectors API
  slug: artie-connectors-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Data Catalog API from Artie — 1 operation(s) for data catalog.
  name: Artie Data Catalog API
  slug: artie-data-catalog-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Encryption Keys API from Artie — 2 operation(s) for encryption keys.
  name: Artie Encryption Keys API
  slug: artie-encryption-keys-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Ingestion API Keys API from Artie — 2 operation(s) for ingestion api keys.
  name: Artie Ingestion API Keys API
  slug: artie-ingestion-api-keys-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Pipelines API from Artie — 10 operation(s) for pipelines.
  name: Artie Pipelines API
  slug: artie-pipelines-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The PrivateLink Connections API from Artie — 2 operation(s) for privatelink connections.
  name: Artie PrivateLink Connections API
  slug: artie-privatelink-connections-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Source Readers API from Artie — 5 operation(s) for source readers.
  name: Artie Source Readers API
  slug: artie-source-readers-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The SSH Tunnels API from Artie — 2 operation(s) for ssh tunnels.
  name: Artie SSH Tunnels API
  slug: artie-ssh-tunnels-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Artie API API from Artie — 0 operation(s) for artie api.
  name: Artie API
  slug: artie-artie-api-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Company API from Artie — 1 operation(s) for company.
  name: Artie Company API
  slug: artie-company-api
- baseURL: https://api.artie.com
  baseurl_source: declared
  description: The Kafka Clusters API from Artie — 19 operation(s) for kafka clusters.
  name: Artie Kafka Clusters API
  slug: artie-kafka-clusters-api
artifact_total: 31
asyncapis:
- description: Webhook event surface for Artie, derived from the webhook payload schemas published in the Artie OpenAPI. Artie POSTs an Event Payload (PayloadsWebhookEnvelope / discriminated by the `event` field) to
  name: Artie Webhooks
  slug: artie-webhooks-asyncapi
collections:
- collection_type: open
  name: Artie Column Hashing Salts API
  slug: open-artie-column-hashing-salts-api
- collection_type: open
  name: Artie Column Hashing Salts Connectors API
  slug: open-artie-connectors-api
- collection_type: open
  name: Artie Column Hashing Salts Data Catalog API
  slug: open-artie-data-catalog-api
- collection_type: open
  name: Artie Column Hashing Salts Encryption Keys API
  slug: open-artie-encryption-keys-api
- collection_type: open
  name: Artie Column Hashing Salts Ingestion API Keys API
  slug: open-artie-ingestion-api-keys-api
- collection_type: open
  name: Artie Column Hashing Salts Pipelines API
  slug: open-artie-pipelines-api
- collection_type: open
  name: Artie Column Hashing Salts PrivateLink Connections API
  slug: open-artie-privatelink-connections-api
- collection_type: open
  name: Artie Column Hashing Salts Source Readers API
  slug: open-artie-source-readers-api
- collection_type: open
  name: Artie Column Hashing Salts SSH Tunnels API
  slug: open-artie-ssh-tunnels-api
common:
- group: commercial
  href: https://artifacts.apis.io/artie/plans/artie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/artie-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/artie/capabilities/artie-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/artie-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/artie/overlays/artie-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/artie-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/artie/security/artie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artie-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/artie/authentication/artie-authentication.yml
  title: ''
  type: Authentication
  url: authentication/artie-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.artie.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.artie.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.artie.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.artie.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.artie.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.artie.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.artie.com/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/artie-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.artie.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.artie.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.artie.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.artie.com/docs/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.artie.com/docs/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.artie.com/
- group: agent
  href: https://artifacts.apis.io/artie/llms/artie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/artie-llms.txt
- group: build
  href: https://artifacts.apis.io/artie/packages/artie-packages.yml
  title: ''
  type: Packages
  url: packages/artie-packages.yml
- group: build
  href: https://artifacts.apis.io/artie/cli/artie-cli.yml
  title: ''
  type: CLI
  url: cli/artie-cli.yml
- group: agent
  href: https://artifacts.apis.io/artie/mcp/artie-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/artie-mcp.yml
- group: design
  href: https://artifacts.apis.io/artie/conventions/artie-conventions.yml
  title: ''
  type: Conventions
  url: conventions/artie-conventions.yml
- group: design
  href: https://artifacts.apis.io/artie/errors/artie-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/artie-problem-types.yml
- group: design
  href: https://artifacts.apis.io/artie/lifecycle/artie-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/artie-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/artie/changelog/artie-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/artie-changelog.yml
- group: design
  href: https://artifacts.apis.io/artie/conformance/artie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/artie-conformance.yml
- group: design
  href: https://artifacts.apis.io/artie/data-model/artie-data-model.yml
  title: ''
  type: DataModel
  url: data-model/artie-data-model.yml
- group: docs
  href: https://artifacts.apis.io/artie/asyncapi/artie-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/artie-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/artie/asyncapi/artie-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/artie-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/artie/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/artie/agentic-access/artie-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/artie-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/artie/ai-catalog/artie-ai-catalog.yml
  title: ''
  type: AICatalog
  url: ai-catalog/artie-ai-catalog.yml
created: '2026-07-17'
description: Artie is a real-time data replication platform that streams database changes to cloud data warehouses and lakehouses with sub-minute latency and exactly-once delivery. It captures change data (CDC) from sources such as PostgreSQL, MySQL, MongoDB, Oracle, and DynamoDB and continuously merges them into destinations including Snowflake, BigQuery, Databricks, Redshift, and Apache Iceberg, eliminating the need to build and operate Kafka or Debezium infrastructure. Artie handles advanced backfills, schema evolution, column-level encryption and hashing, data catalog search, PrivateLink/SSH connectivity, and observability, and exposes a REST API plus a webhook event stream so teams can programmatically manage pipelines, connectors, and source readers. Artie is venture-backed by Canaan Partners and General Catalyst.
finops:
- has_sources: true
  method: derived
  name: Artie Finops
  primary_unit: billable rows
  service_category: ''
  slug: artie-finops
  template: false
image: https://avatars.githubusercontent.com/artie-labs
layout: provider
modified: '2026-09-16'
name: Artie
nav: Providers
network: true
overview: 'Artie publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Column Hashing Salts API, Connectors API, Data Catalog API, and 9 more. Tagged areas include Company, Data Replication, Change Data Capture, Data Integration, and ETL.


  The Artie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Artie''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Artie Plans Pricing
  plan_count: 3
  slug: artie-plans-pricing
- name: Artie Price Estimates
  plan_count: 0
  slug: artie-price-estimates
random_paper: 5
score:
  band: strong
  composite: 59.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.0
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 57.5
    developer_ergonomics: 66.1
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/artie/artie-2026-07-25T201330.png
security:
- kind: authentication
  name: Artie Authentication
  slug: artie-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Artie Domain Security
  slug: artie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Create and start a replication pipeline
  slug: artie-create-and-start-pipeline
- name: Search the data catalog
  slug: artie-search-data-catalog
- name: Configure column encryption and hashing
  slug: artie-secure-columns
slug: artie
tags:
- Company
- Data Replication
- Change Data Capture
- Data Integration
- ETL
- Streaming
- Database
- Data Warehouse
- Data Engineering
website: https://www.artie.com
---
