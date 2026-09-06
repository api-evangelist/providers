---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Clickhouse Agentic Access
  operation_count: 5
  slug: clickhouse-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- description: HTTP interface (default port 8123, HTTPS 8443) for executing SQL queries against ClickHouse. Supports SELECT via GET, mutations via POST, multiple output formats (JSON, CSV, XML, TabSeparated), and au
  name: ClickHouse HTTP Interface
  slug: clickhouse-http-interface
- description: Native binary TCP protocol used by ClickHouse client libraries for maximum throughput between client and server (default port 9000).
  name: ClickHouse Native TCP Interface
  slug: clickhouse-native
- description: MySQL wire protocol compatibility allowing existing MySQL clients and BI tools to query ClickHouse without driver changes.
  name: ClickHouse MySQL Interface
  slug: clickhouse-mysql
- description: PostgreSQL wire protocol compatibility for connecting psql, JDBC and other PostgreSQL clients to ClickHouse.
  name: ClickHouse PostgreSQL Interface
  slug: clickhouse-postgresql
- description: gRPC interface defined by clickhouse_grpc.proto for efficient binary communication.
  name: ClickHouse gRPC Interface
  slug: clickhouse-grpc
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The ClickHouse HTTP Interface API from ClickHouse — 1 operation(s) for clickhouse http interface.
  name: ClickHouse ClickHouse HTTP Interface API
  slug: clickhouse-clickhouse-http-interface-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Ping API from ClickHouse — 1 operation(s) for ping.
  name: ClickHouse Ping API
  slug: clickhouse-ping-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Play API from ClickHouse — 1 operation(s) for play.
  name: ClickHouse Play API
  slug: clickhouse-play-api
- baseURL: https://{clickhouse-host}:8443
  baseurl_source: declared
  description: The Replicas Status API from ClickHouse — 1 operation(s) for replicas status.
  name: ClickHouse Replicas Status API
  slug: clickhouse-replicas-status-api
- baseURL: https://api.clickhouse.cloud/v1
  baseurl_source: declared
  description: The ClickHouse Cloud control-plane REST API — 148 operations across 86 paths for organizations, services, users and roles, API keys, backups, ClickPipes, ClickStack observability, Managed Postgres, UD
  name: ClickHouse Cloud API
  slug: clickhouse-cloud-api
artifact_total: 35
asyncapis:
- description: AsyncAPI description of the documented streaming surface that ClickHouse offers through the Kafka table engine. ClickHouse itself does NOT publish a public WebSocket, Server-Sent Events, or push-style
  name: ClickHouse Kafka Table Engine (Consumer-Side Streaming)
  slug: clickhouse-kafka-engine-asyncapi
- description: ''
  name: Clickhouse Webhooks
  slug: clickhouse-webhooks
collections:
- collection_type: postman
  name: ClickHouse HTTP Interface API
  slug: postman-clickhouse-clickhouse-http-interface-api
- collection_type: postman
  name: ClickHouse HTTP Interface Ping API
  slug: postman-clickhouse-ping-api
- collection_type: postman
  name: ClickHouse HTTP Interface Play API
  slug: postman-clickhouse-play-api
- collection_type: postman
  name: ClickHouse HTTP Interface Replicas Status API
  slug: postman-clickhouse-replicas-status-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClickHouse HTTP Interface API
  slug: open-clickhouse-clickhouse-http-interface-api
- collection_type: open
  name: ClickHouse HTTP Interface Ping API
  slug: open-clickhouse-ping-api
- collection_type: open
  name: ClickHouse HTTP Interface Play API
  slug: open-clickhouse-play-api
- collection_type: open
  name: ClickHouse HTTP Interface Replicas Status API
  slug: open-clickhouse-replicas-status-api
- collection_type: open
  name: ClickHouse HTTP Interface
  slug: open-clickhouse
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clickhouse-vulnerability-disclosure.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/clickhouse/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clickhouse-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clickhouse-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clickhouse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clickhouse-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clickhouseinc
- group: company
  title: ''
  type: Website
  url: https://clickhouse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://clickhouse.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://clickhouse.com/docs/quick-start
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ClickHouse/ClickHouse
- group: company
  title: ''
  type: Blog
  url: https://clickhouse.com/blog
- group: operate
  title: ''
  type: Community
  url: https://clickhouse.com/community
- group: operate
  title: ''
  type: Slack
  url: https://clickhouse.com/slack
- group: commercial
  title: ''
  type: Pricing
  url: https://clickhouse.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://clickhouse.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clickhouse.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clickhouse.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clickhouse.com/legal/clickhouse-general-terms-and-conditions
- group: design
  title: ''
  type: JSONLD
  url: json-ld/clickhouse-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/clickhouse-rules.yml
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/clickhouse-ai-catalog.yml
- group: build
  title: ''
  type: Packages
  url: packages/clickhouse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clickhouse-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clickhouse-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clickhouse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/clickhouse-security.txt
- group: other
  title: ''
  type: APICatalog
  url: well-known/clickhouse-api-catalog.json
- group: auth
  title: ''
  type: Security
  url: security/clickhouse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: security/clickhouse-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clickhouse-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clickhouse-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clickhouse-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/clickhouse-grpc.proto
- group: design
  title: ''
  type: Conformance
  url: conformance/clickhouse-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clickhouse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clickhouse-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clickhouse-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clickhouse-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clickhouse-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clickhouse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clickhouse-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clickhouse-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/clickhouse-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clickhouse-rate-limits.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clickhouse-cloud-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clickhouse.com/docs/cloud/manage/api/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://clickhouse.com/docs/products/cloud/api-reference/organization/get-list-of-available-organizations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClickHouse
- group: start
  title: ''
  type: SignUp
  url: https://console.clickhouse.cloud/signUp
- group: start
  title: ''
  type: Quickstart
  url: https://clickhouse.com/docs/quick-start
- group: other
  title: ''
  type: Playground
  url: https://sql.clickhouse.com
created: '2024-01-01'
description: ClickHouse is a fast open-source column-oriented database management system that enables real-time analytical reporting using SQL. ClickHouse exposes multiple interfaces - an HTTP interface for SQL queries, native TCP, MySQL and PostgreSQL wire-compatible interfaces, and a gRPC interface - and the ClickHouse Cloud management plane offers a public OpenAPI-described REST API for provisioning and managing services, organizations, members, API keys, backups, and private endpoints.
finops:
- name: Clickhouse Finops
  service_category: API
  slug: clickhouse-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clickhouse.png
jsonld:
- class_count: 0
  name: Clickhouse Context
  property_count: 5
  slug: clickhouse-context
layout: provider
mcp_servers:
- description: ''
  name: ClickHouse MCP Server
  slug: clickhouse-mcp-server
modified: '2026-09-05'
name: ClickHouse
nav: Providers
network: true
overview: 'ClickHouse publishes 5 APIs on the [APIs.io](https://apis.io/) network, including ClickHouse HTTP Interface API, Ping API, Play API, and 2 more. Tagged areas include Analytics, Cloud Database, Column-Oriented, Database, and OLAP.


  The ClickHouse catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  ClickHouse''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, engineering blog, pricing, support, and 46 more developer resources.'
plans:
- name: Clickhouse Plans Pricing
  plan_count: 4
  slug: clickhouse-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Clickhouse Rate Limits
  slug: clickhouse-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: ClickHouse API Rules
  rule_count: 3
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 3
  slug: clickhouse-asyncapi-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: ClickHouse API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 5
  slug: clickhouse-rules
scopes:
- name: Clickhouse Scopes
  scope_count: 0
  slug: clickhouse-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 63.8
    catalog_earned_first_party: 20.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 27.6
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 15.9
    contract_quality: 60.1
    developer_ergonomics: 83.3
    discoverability: 66.7
    governance: 15.9
    operational_transparency: 73.7
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/clickhouse/refs/heads/main/screenshots/clickhouse-2026-06-20T174515.png
security:
- kind: authentication
  name: Clickhouse Authentication
  slug: clickhouse-authentication
  summary_line: http/apiKey/oauth2 · 0 schemes
- kind: domain-security
  name: Clickhouse Domain Security
  slug: clickhouse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clickhouse Vulnerability Disclosure
  slug: clickhouse-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Clickhouse Trust Center
  slug: clickhouse-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: clickhouse
tags:
- Analytics
- Cloud Database
- Column-Oriented
- Database
- OLAP
- Open-Source
- Real-Time
- SQL
website: https://clickhouse.com/
---
