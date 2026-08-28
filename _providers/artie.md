---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Artie Agentic Access
  operation_count: 60
  slug: artie-agentic-access
  summary_line: 60 operations · 48 acting
api_count: 9
apis:
- description: The Column Hashing Salts API from Artie — 3 operation(s) for column hashing salts.
  name: Artie Column Hashing Salts API
  slug: artie-column-hashing-salts-api
- description: The Connectors API from Artie — 14 operation(s) for connectors.
  name: Artie Connectors API
  slug: artie-connectors-api
- description: The Data Catalog API from Artie — 1 operation(s) for data catalog.
  name: Artie Data Catalog API
  slug: artie-data-catalog-api
- description: The Encryption Keys API from Artie — 2 operation(s) for encryption keys.
  name: Artie Encryption Keys API
  slug: artie-encryption-keys-api
- description: The Ingestion API Keys API from Artie — 2 operation(s) for ingestion api keys.
  name: Artie Ingestion API Keys API
  slug: artie-ingestion-api-keys-api
- description: The Pipelines API from Artie — 10 operation(s) for pipelines.
  name: Artie Pipelines API
  slug: artie-pipelines-api
- description: The PrivateLink Connections API from Artie — 2 operation(s) for privatelink connections.
  name: Artie PrivateLink Connections API
  slug: artie-privatelink-connections-api
- description: The Source Readers API from Artie — 5 operation(s) for source readers.
  name: Artie Source Readers API
  slug: artie-source-readers-api
- description: The SSH Tunnels API from Artie — 2 operation(s) for ssh tunnels.
  name: Artie SSH Tunnels API
  slug: artie-ssh-tunnels-api
artifact_total: 24
asyncapis:
- description: Webhook event surface for Artie, derived from the webhook payload schemas published in the Artie OpenAPI. Artie POSTs an Event Payload (PayloadsWebhookEnvelope / discriminated by the `event` field) to
  name: Artie Webhooks
  slug: artie-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: Overlay
  url: overlays/artie-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artie-domain-security.yml
- group: auth
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
  title: ''
  type: LLMsTxt
  url: llms/artie-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/artie-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/artie-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/artie-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artie-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/artie-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artie-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/artie-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/artie-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/artie-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artie-agentic-access.yml
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/artie-ai-catalog.yml
created: '2026-07-17'
description: Artie is a real-time data replication platform that streams database changes to cloud data warehouses and lakehouses with sub-minute latency and exactly-once delivery. It captures change data (CDC) from sources such as PostgreSQL, MySQL, MongoDB, Oracle, and DynamoDB and continuously merges them into destinations including Snowflake, BigQuery, Databricks, Redshift, and Apache Iceberg, eliminating the need to build and operate Kafka or Debezium infrastructure. Artie handles advanced backfills, schema evolution, column-level encryption and hashing, data catalog search, PrivateLink/SSH connectivity, and observability, and exposes a REST API plus a webhook event stream so teams can programmatically manage pipelines, connectors, and source readers. Artie is venture-backed by Canaan Partners and General Catalyst.
image: https://avatars.githubusercontent.com/artie-labs
layout: provider
mcp_servers:
- description: ''
  name: Artie MCP Server
  slug: artie-mcp-server
modified: '2026-07-18'
name: Artie
nav: Providers
network: true
overview: 'Artie publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Column Hashing Salts API, Connectors API, Data Catalog API, and 6 more. Tagged areas include Company, Data Replication, Change Data Capture, Data Integration, and ETL.


  The Artie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Artie''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 50.2
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 16.7
    contract_quality: 64.3
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 26.3
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artie/refs/heads/main/screenshots/artie-2026-07-25T201330.png
security:
- kind: authentication
  name: Artie Authentication
  slug: artie-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Artie Domain Security
  slug: artie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artie
tags:
- Company
- Data Replication
- Change Data Capture
- Data Integration
- ETL
- Streaming
- Databases
- Data Warehouse
- CDC
- Data Engineering
website: https://www.artie.com
---
