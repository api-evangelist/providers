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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 53
  human_in_the_loop: 4
  name: Timescale Agentic Access
  operation_count: 83
  slug: timescale-agentic-access
  summary_line: 83 operations · 53 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: A publicly reachable, anonymous Model Context Protocol server (server name pg-aiguide) serving hybrid semantic + BM25 search over Tiger Cloud, TimescaleDB, PostgreSQL and PostGIS documentation, plus a
  name: Tiger Docs MCP Server
  slug: tiger-docs-mcp-server
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Analytics API from Timescale — 2 operation(s) for analytics.
  name: Timescale Analytics API
  slug: timescale-analytics-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Auth API from Timescale — 2 operation(s) for auth.
  name: Timescale Auth API
  slug: timescale-auth-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Feedback API from Timescale — 1 operation(s) for feedback.
  name: Timescale Feedback API
  slug: timescale-feedback-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Health API from Timescale — 1 operation(s) for health.
  name: Timescale Health API
  slug: timescale-health-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Invites API from Timescale — 3 operation(s) for invites.
  name: Timescale Invites API
  slug: timescale-invites-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Pricing API from Timescale — 1 operation(s) for pricing.
  name: Timescale Pricing API
  slug: timescale-pricing-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Projects API from Timescale — 1 operation(s) for projects.
  name: Timescale Projects API
  slug: timescale-projects-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Read Replica Sets API from Timescale — 6 operation(s) for read replica sets.
  name: Timescale Read Replica Sets API
  slug: timescale-read-replica-sets-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: Manage services, read replicas, and their associated actions.
  name: Timescale Services API
  slug: timescale-services-api
- baseURL: https://console.cloud.tigerdata.com/public/api/v1
  baseurl_source: declared
  description: The Spaces API from Timescale — 31 operation(s) for spaces.
  name: Timescale Spaces API
  slug: timescale-spaces-api
- baseURL: https://mcp.tigerdata.com/docs
  baseurl_source: declared
  description: Manage VPCs and their peering connections.
  name: Timescale VP Cs API
  slug: timescale-vpcs-api
- description: The database itself is accessed via the PostgreSQL wire protocol (port 5432), with TimescaleDB SQL functions for hypertable management, compression, continuous aggregates and hyperfunctions. Not a RES
  name: Timescale PostgreSQL Wire Interface
  slug: timescale-postgres-wire
artifact_total: 67
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Timescale Analytics API
  slug: open-timescale-analytics-api
- collection_type: open
  name: Timescale Auth API
  slug: open-timescale-auth-api
- collection_type: open
  name: Ghost Feedback API
  slug: open-timescale-feedback-api
- collection_type: open
  name: Ghost Health API
  slug: open-timescale-health-api
- collection_type: open
  name: Ghost Invites API
  slug: open-timescale-invites-api
- collection_type: open
  name: Ghost Pricing API
  slug: open-timescale-pricing-api
- collection_type: open
  name: Tiger Cloud Projects API
  slug: open-timescale-projects-api
- collection_type: open
  name: Tiger Cloud Read Replica Sets API
  slug: open-timescale-read-replica-sets-api
- collection_type: open
  name: Tiger Cloud Services API
  slug: open-timescale-services-api
- collection_type: open
  name: Ghost Spaces API
  slug: open-timescale-spaces-api
- collection_type: open
  name: Tiger Cloud VP Cs API
  slug: open-timescale-vpcs-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/rules/timescale-rules.yml
  title: ''
  type: Spectral
  url: rules/timescale-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/json-ld/timescale-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/timescale-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/vocabulary/timescale-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/timescale-vocabulary.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/lifecycle/timescale-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/timescale-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/llms/timescale-ghost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/timescale-ghost-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/integrations/timescale-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/timescale-integration-edges.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tigerdata.com/blog/rss
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/capabilities/timescale-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/timescale-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/agentic-access/timescale-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/timescale-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/security/timescale-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/timescale-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/security/timescale-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/timescale-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/security/timescale-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/timescale-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/authentication/timescale-authentication.yml
  title: ''
  type: Authentication
  url: authentication/timescale-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tigerdata.com/security/vulnerability-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://www.tigerdata.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/conformance/timescale-conformance.yml
  title: ''
  type: Conformance
  url: conformance/timescale-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/packages/timescale-packages.yml
  title: ''
  type: Packages
  url: packages/timescale-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/packages/timescale-packages.yml
  title: ''
  type: SDKs
  url: packages/timescale-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://pypi.org/project/timescale-vector/
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@timescaledb/typeorm
- group: build
  title: ''
  type: Ruby SDK
  url: https://rubygems.org/gems/timescaledb
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/cli/timescale-cli.yml
  title: ''
  type: CLI
  url: cli/timescale-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/mcp/timescale-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/timescale-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/mcp/timescale-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/timescale-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/well-known/timescale-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/timescale-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/well-known/timescale-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/timescale-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/llms/timescale-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/timescale-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/conventions/timescale-conventions.yml
  title: ''
  type: Conventions
  url: conventions/timescale-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/errors/timescale-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/timescale-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/data-model/timescale-data-model.yml
  title: ''
  type: DataModel
  url: data-model/timescale-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/lifecycle/timescale-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/timescale-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tigerdata.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/changelog/timescale-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/timescale-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.tigerdata.com/docs/get-started/news/new
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/sandbox/timescale-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/timescale-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://console.cloud.tigerdata.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/overlays/timescale-tiger-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/timescale-tiger-cloud-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.tigerdata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tigerdata.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.tigerdata.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tigerdata.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tigerdata.com/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.tigerdata.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tigerdata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/timescale
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tigerdata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.timescale.com/signup
- group: start
  title: ''
  type: Login
  url: https://console.cloud.timescale.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tigerdata.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tigerdata.com/legal/privacy
- group: operate
  title: ''
  type: SLA
  url: https://www.tigerdata.com/legal/service-level-agreement
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/timescale_stock/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/plans/timescale-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/timescale-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/rate-limits/timescale-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/timescale-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/finops/timescale-finops.yml
  title: ''
  type: FinOps
  url: finops/timescale-finops.yml
created: '2026-08-05'
description: Timescale — rebranded as Tiger Data in 2025 — is the PostgreSQL data platform company behind TimescaleDB, the open-source PostgreSQL extension for time-series and real-time analytics, and Tiger Cloud, a fully managed PostgreSQL cloud service on AWS and Azure. The platform adds hypertables (automatic time-based partitioning), Hypercore hybrid row-columnar storage, native columnar compression, continuous aggregates, tiered storage to S3, database forks, read replica sets and connection pooling on top of standard PostgreSQL. The company also ships pg_textsearch (BM25 full-text search in Postgres), pgvectorscale and pgai for vector and AI workloads, the Tiger Cloud REST API for programmatic service management, the Tiger CLI with a built-in MCP server, and Ghost, an agent-oriented Postgres provisioning service at ghost.build.
finops:
- has_sources: true
  method: generated
  name: Timescale Finops
  primary_unit: ''
  service_category: Database (Time-Series)
  slug: timescale-finops
  template: false
image: https://www.tigerdata.com/favicon.ico
json_schemas:
- name: AuthInfo
  property_count: 3
  slug: timescale-auth-info
- name: Database
  property_count: 9
  slug: timescale-database
- name: DatabaseShare
  property_count: 6
  slug: timescale-database-share
- name: FeedbackRequest
  property_count: 4
  slug: timescale-feedback-request
- name: ForkServiceCreate
  property_count: 6
  slug: timescale-fork-service-create
- name: IdentifyRequest
  property_count: 1
  slug: timescale-identify-request
- name: InviteActionResult
  property_count: 2
  slug: timescale-invite-action-result
- name: LogoutRequest
  property_count: 1
  slug: timescale-logout-request
- name: MetricSeries
  property_count: 2
  slug: timescale-metric-series
- name: MetricsSeriesRequest
  property_count: 6
  slug: timescale-metrics-series-request
- name: PaymentMethod
  property_count: 7
  slug: timescale-payment-method
- name: PeeringCreate
  property_count: 3
  slug: timescale-peering-create
- name: Peering
  property_count: 7
  slug: timescale-peering
- name: Pricing
  property_count: 2
  slug: timescale-pricing
- name: Project
  property_count: 2
  slug: timescale-project
- name: ReadReplicaSetCreate
  property_count: 4
  slug: timescale-read-replica-set-create
- name: ReadReplicaSet
  property_count: 9
  slug: timescale-read-replica-set
- name: ReceivedInvite
  property_count: 6
  slug: timescale-received-invite
- name: ResizeInput
  property_count: 2
  slug: timescale-resize-input
- name: ServiceCreate
  property_count: 7
  slug: timescale-service-create
- name: ServiceLogs
  property_count: 3
  slug: timescale-service-logs
- name: Service
  property_count: 16
  slug: timescale-service
- name: SetEnvironmentInput
  property_count: 1
  slug: timescale-set-environment-input
- name: SpaceDetail
  property_count: 4
  slug: timescale-space-detail
- name: SpaceUsage
  property_count: 10
  slug: timescale-space-usage
- name: StatusResponse
  property_count: 1
  slug: timescale-status-response
- name: TrackRequest
  property_count: 2
  slug: timescale-track-request
- name: UpdateOverageSettingsRequest
  property_count: 2
  slug: timescale-update-overage-settings-request
- name: VPC
  property_count: 4
  slug: timescale-vpc
- name: VPCCreate
  property_count: 3
  slug: timescale-vpccreate
- name: VPCRename
  property_count: 1
  slug: timescale-vpcrename
jsonld:
- class_count: 87
  name: Timescale Context
  property_count: 132
  slug: timescale-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tigerdata.com.
  name: Timescale MCP Server
  slug: timescale-mcp-yml
modified: '2026-10-06'
name: Timescale
nav: Providers
network: true
overview: 'Timescale publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Auth API, Feedback API, and 10 more. Tagged areas include Company, Database, PostgreSQL, Time Series, and Analytics.


  The Timescale catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Timescale''s developer surface includes authentication, CLI, changelog, release notes, sandbox, developer console, documentation, and 49 more developer resources.'
plans:
- name: Timescale Plans Pricing
  plan_count: 6
  slug: timescale-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Timescale Rate Limits
  slug: timescale-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Timescale API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: timescale-rules
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.0
    catalog_earned_first_party: 0.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 9.0
  facets:
    access_clarity: 61.8
    contract_governance: 19.7
    contract_quality: 59.6
    developer_ergonomics: 82.7
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/timescale/refs/heads/main/screenshots/timescale-2026-08-17T082356.png
security:
- kind: authentication
  name: Timescale Authentication
  slug: timescale-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Timescale Domain Security
  slug: timescale-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Timescale Vulnerability Disclosure
  slug: timescale-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Timescale Trust Center
  slug: timescale-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: timescale
tags:
- Company
- Database
- PostgreSQL
- Time Series
- Analytics
- Cloud Infrastructure
- Data Platform
- Vector Search
- Developer Tools
- Open Source
website: https://www.tigerdata.com/
---
