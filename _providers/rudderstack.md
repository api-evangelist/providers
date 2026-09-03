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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Rudderstack Agentic Access
  operation_count: 12
  slug: rudderstack-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 1
apis:
- description: The RudderStack Config Backend API manages workspace configuration objects — sources, destinations, connections, and workspace settings — supporting full programmatic provisioning of pipelines outside
  name: RudderStack Config Backend API
  slug: rudderstack-config-backend-api
- description: The RudderStack Transformations API manages user-defined transformation functions (JavaScript, with Python on Enterprise) attached to a destination connection to filter, mask, enrich, or reshape event
  name: RudderStack Transformations API
  slug: rudderstack-transformations-api
- description: The RudderStack Tracking Plan API defines and enforces the canonical event schema (events, properties, traits, types, required fields) used to validate ingested events and surface violations.
  name: RudderStack Tracking Plan API
  slug: rudderstack-tracking-plan-api
- description: The RudderStack Data Catalog API exposes the inventory of events and properties seen across all sources, supporting schema discovery, lineage, and governance reporting.
  name: RudderStack Data Catalog API
  slug: rudderstack-data-catalog-api
- description: The RudderStack Profiles API powers warehouse-native identity resolution, customer feature engineering, and unified Customer 360 model definitions executed inside the customer's data warehouse.
  name: RudderStack Profiles API
  slug: rudderstack-profiles-api
- description: The RudderStack Audiences API builds and manages audience definitions in the warehouse and activates them across destinations via Reverse ETL.
  name: RudderStack Audiences API
  slug: rudderstack-audiences-api
- description: The RudderStack Reverse ETL API manages warehouse-source-to-SaaS-destination syncs, including model definitions, sync schedules, run history, and incremental cursor management.
  name: RudderStack Reverse ETL API
  slug: rudderstack-reverse-etl-api
- description: The RudderStack Event Stream API manages real-time event-stream pipelines — sources, destinations, connections, event filters, and feature toggles — that route events from collection to downstream too
  name: RudderStack Event Stream API
  slug: rudderstack-event-stream-api
- baseURL: https://{dataPlaneUrl}
  baseurl_source: declared
  description: The RudderStack Webhook Source API receives inbound webhooks from third-party SaaS tools and normalizes them into RudderStack events for downstream routing.
  name: RudderStack Webhook Source API
  slug: rudderstack-webhook-source-api
- description: The RudderStack Warehouse Destination API configures and operates loads into supported warehouses (Snowflake, BigQuery, Redshift, Postgres, Databricks, Trino, S3 Data Lake) with configurable sync inte
  name: RudderStack Warehouse Destination API
  slug: rudderstack-warehouse-destination-api
- description: The RudderStack Orchestration API integrates with Airflow and Dagster to coordinate Reverse ETL syncs, Profiles model runs, and other RudderStack jobs from external orchestration systems.
  name: RudderStack Orchestration API
  slug: rudderstack-orchestration-api
- baseURL: https://{dataPlaneUrl}
  baseurl_source: declared
  description: The HTTP API API from RudderStack — 7 operation(s) for http api.
  name: RudderStack HTTP API API
  slug: rudderstack-http-api-api
- baseURL: https://{dataPlaneUrl}
  baseurl_source: declared
  description: The Internal API API from RudderStack — 5 operation(s) for internal api.
  name: RudderStack Internal API API
  slug: rudderstack-internal-api-api
artifact_total: 32
asyncapis:
- description: AsyncAPI 2.6 specification describing RudderStack's event-streaming surfaces over HTTP. RudderStack ingests customer events server-side via the HTTP Tracking API (identify, track, page, screen, group,
  name: RudderStack Event Streaming API
  slug: rudderstack-event-streaming-asyncapi
collections:
- collection_type: postman
  name: RudderStack HTTP HTTP API API
  slug: postman-rudderstack-http-api-api
- collection_type: postman
  name: RudderStack HTTP HTTP API Internal API API
  slug: postman-rudderstack-internal-api-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RudderStack HTTP API
  slug: open-rudderstack-gateway
- collection_type: open
  name: RudderStack HTTP HTTP API API
  slug: open-rudderstack-http-api-api
- collection_type: open
  name: RudderStack HTTP HTTP API Internal API API
  slug: open-rudderstack-internal-api-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/rudderstack/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rudderstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rudderstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rudderstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rudderstack
- group: company
  title: ''
  type: Website
  url: https://www.rudderstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rudderstack.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.rudderstack.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.rudderstack.com/docs/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rudderstack.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.rudderstack.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.rudderstack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rudderlabs
- group: other
  title: ''
  type: Open Source Server
  url: https://github.com/rudderlabs/rudder-server
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/rudderlabs/rudder-sdk-js
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/rudderlabs/rudder-sdk-node
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/rudderlabs/rudder-sdk-python
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/rudderlabs/rudder-sdk-java
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/rudderlabs/analytics-go
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/rudderlabs/rudder-sdk-ruby
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/rudderlabs/rudder-sdk-php
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/rudderlabs/rudder-analytics-dotnet
- group: build
  title: ''
  type: iOS SDK
  url: https://github.com/rudderlabs/rudder-sdk-ios
- group: build
  title: ''
  type: Android SDK
  url: https://github.com/rudderlabs/rudder-sdk-android
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rudderstack.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rudderstack.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.rudderstack.com/docs/releases/
- group: commercial
  title: ''
  type: License
  url: https://github.com/rudderlabs/rudder-server/blob/master/LICENSE.md
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/RudderStack
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/RudderStack
- group: operate
  title: ''
  type: Slack Community
  url: https://www.rudderstack.com/join-rudderstack-slack-community/
- group: commercial
  title: ''
  type: Plans
  url: plans/rudderstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rudderstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rudderstack-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/rudderstack-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/rudderstack-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rudderstack-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rudderstack-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rudderstack-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rudderstack-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rudderstack-well-known.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/rudderstack-grpc.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rudderstack-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/rudderstack-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rudderstack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rudderstack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/rudderstack-vulnerability-disclosure.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rudderstack-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rudderstack-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rudderstack-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rudderstack-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rudderstack-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/rudderstack-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/rudderstack-event-streaming-asyncapi.yml
- group: build
  title: ''
  type: Postman
  url: https://www.getpostman.com/collections/480307c55ad2b9dd4e27
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.rudderstack.com/docs/dev-tools/
- group: operate
  title: ''
  type: Support
  url: https://www.rudderstack.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rudderstack.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rudderstack.com/privacy-policy/
- group: commercial
  title: ''
  type: MasterServiceAgreement
  url: https://www.rudderstack.com/master-service-agreement/
- group: auth
  title: ''
  type: SecurityOverview
  url: https://www.rudderstack.com/security/
- group: docs
  title: ''
  type: AgentSkillsDocs
  url: https://www.rudderstack.com/docs/ai-features/agent-skills/
- group: docs
  title: ''
  type: MCPDocs
  url: https://www.rudderstack.com/docs/ai-features/rudderstack-mcp/
created: '2026-05-08'
description: RudderStack is a warehouse-native customer data platform (CDP) for developers, with open-source data plane SDKs (rudder-server) and a managed control plane. The platform exposes an HTTP Tracking (Event Stream) API for ingest, a Config Backend API for managing sources/destinations/connections, a Transformations API for in-flight event transforms, a Tracking Plan API for schema governance, a Profiles API for identity resolution and audiences, and a Reverse ETL API for warehouse-to-SaaS sync.
finops:
- name: Rudderstack Finops
  service_category: Customer Data Platform
  slug: rudderstack-finops
graphqls:
- description: This conceptual GraphQL schema models the RudderStack customer data platform (CDP) API surface. RudderStack is a warehouse-native CDP for developers that provides an open-source data plane and a manag
  name: RudderStack GraphQL Schema
  slug: rudderstack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rudderstack.png
layout: provider
mcp_servers:
- description: 'RudderStack operates an official, centrally hosted remote MCP server at https://mcp.rudderstack.com/mcp. It is an OAuth 2.0 protected resource: an anonymous POST of tools/list returns HTTP 401 invalid'
  name: RudderStack MCP Server
  slug: rudderstack-mcp-server
modified: '2026-08-13'
name: RudderStack
nav: Providers
network: true
overview: 'RudderStack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Webhook Source API, HTTP API API, and Internal API API. Tagged areas include Customer Data Platform, CDP, Data Pipeline, Open-Source, and Event Streaming.


  The RudderStack catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  RudderStack''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 57 more developer resources.'
plans:
- name: Rudderstack Plans Pricing
  plan_count: 3
  slug: rudderstack-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Rudderstack Rate Limits
  slug: rudderstack-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: RudderStack API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: rudderstack-asyncapi-spectral-rules
scopes:
- name: Rudderstack Scopes
  scope_count: 0
  slug: rudderstack-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 76.9
  coverage:
    artifact_dirs: 30
    catalog_gap: 51.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 67.1
    developer_ergonomics: 100.0
    discoverability: 66.7
    governance: 31.8
    operational_transparency: 84.2
  previous_composite: 76.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rudderstack/refs/heads/main/screenshots/rudderstack-2026-06-20T193249.png
security:
- kind: authentication
  name: Rudderstack Authentication
  slug: rudderstack-authentication
  summary_line: http/oauth2 · 5 schemes
- kind: domain-security
  name: Rudderstack Domain Security
  slug: rudderstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rudderstack Vulnerability Disclosure
  slug: rudderstack-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Rudderstack Trust Center
  slug: rudderstack-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: rudderstack
tags:
- Customer Data Platform
- CDP
- Data Pipeline
- Open-Source
- Event Streaming
- Reverse ETL
- Analytics
- Identity Resolution
website: https://www.rudderstack.com/
---
