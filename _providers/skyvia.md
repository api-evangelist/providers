---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: REST management API for the Skyvia platform. Programmatically read and control account users and invitations, workspaces and workspace membership, on-premise agents, data-source connections, data inte
  name: Skyvia Public API
  slug: skyvia-public-api
- description: Hosted Model Context Protocol server that publishes any Skyvia connection — 200+ cloud apps and databases — as a set of MCP tools an AI assistant can call. Each customer endpoint is served from mcp.sk
  name: Skyvia Connect MCP Endpoint
  slug: skyvia-connect-mcp-endpoint
- description: Connectivity-as-a-service layer that exposes a Skyvia connection as a secured web API without writing code. An endpoint can be published as an OData v4 service (consumable from Power BI, Excel, Tablea
  name: Skyvia Connect OData & SQL Endpoints
  slug: skyvia-connect-odata-sql-endpoints
- description: Inbound webhook surface for Skyvia Automation. Each automation with a Webhook trigger is assigned a Skyvia-issued base URL plus a user-defined event name; an external application POSTs its event paylo
  name: Skyvia Automation Webhook Triggers
  slug: skyvia-automation-webhook-triggers
artifact_total: 27
asyncapis:
- description: ''
  name: Skyvia Automation Webhooks
  slug: skyvia-automation-webhooks
collections:
- collection_type: open
  name: Skyvia Public API — Account
  slug: open-skyvia-account-api
- collection_type: open
  name: Skyvia Public API — Agents
  slug: open-skyvia-agents-api
- collection_type: open
  name: Skyvia Public API — Automations
  slug: open-skyvia-automations-api
- collection_type: open
  name: Skyvia Public API — Backups
  slug: open-skyvia-backups-api
- collection_type: open
  name: Skyvia Public API — Connections
  slug: open-skyvia-connections-api
- collection_type: open
  name: Skyvia Public API — Endpoints
  slug: open-skyvia-endpoints-api
- collection_type: open
  name: Skyvia Public API — Integrations
  slug: open-skyvia-integrations-api
- collection_type: open
  name: Skyvia Public API — Workspaces
  slug: open-skyvia-workspaces-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://skyvia.com/blog/feed/
- group: company
  title: ''
  type: Website
  url: https://skyvia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.skyvia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skyvia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skyvia.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skyvia.com/concepts.html
- group: operate
  title: ''
  type: Support
  url: https://skyvia.com/support
- group: company
  title: ''
  type: Blog
  url: https://skyvia.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://skyvia.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.skyvia.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://app.skyvia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skyvia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyvia.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.skyvia.com/recent-releases/
- group: operate
  href: https://artifacts.apis.io/skyvia/changelog/skyvia-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/skyvia-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://skyvia.com/security
- group: auth
  href: https://artifacts.apis.io/skyvia/security/skyvia-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/skyvia-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/skyvia/llms/skyvia-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/skyvia-llms.txt
- group: agent
  href: https://artifacts.apis.io/skyvia/mcp/skyvia-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/skyvia-mcp.yml
- group: auth
  href: https://artifacts.apis.io/skyvia/authentication/skyvia-authentication.yml
  title: ''
  type: Authentication
  url: authentication/skyvia-authentication.yml
- group: auth
  href: https://artifacts.apis.io/skyvia/scopes/skyvia-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/skyvia-scopes.yml
- group: design
  href: https://artifacts.apis.io/skyvia/conventions/skyvia-conventions.yml
  title: ''
  type: Conventions
  url: conventions/skyvia-conventions.yml
- group: design
  href: https://artifacts.apis.io/skyvia/lifecycle/skyvia-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/skyvia-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/skyvia/conformance/skyvia-conformance.yml
  title: ''
  type: Conformance
  url: conformance/skyvia-conformance.yml
- group: design
  href: https://artifacts.apis.io/skyvia/errors/skyvia-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/skyvia-problem-types.yml
- group: design
  href: https://artifacts.apis.io/skyvia/data-model/skyvia-data-model.yml
  title: ''
  type: DataModel
  url: data-model/skyvia-data-model.yml
- group: auth
  href: https://artifacts.apis.io/skyvia/security/skyvia-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skyvia-domain-security.yml
- group: start
  href: https://artifacts.apis.io/skyvia/sandbox/skyvia-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/skyvia-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/skyvia/plans/skyvia-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skyvia-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/skyvia/rate-limits/skyvia-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/skyvia-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/skyvia/asyncapi/skyvia-automation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/skyvia-automation-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/skyvia/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/skyvia/packages/skyvia-packages.yml
  title: ''
  type: Packages
  url: packages/skyvia-packages.yml
- group: build
  href: https://artifacts.apis.io/skyvia/packages/skyvia-packages.yml
  title: ''
  type: SDKs
  url: packages/skyvia-packages.yml
created: '2026-08-12'
description: 'Skyvia is a no-code cloud data platform from Devart covering five products on one account: Data Integration (import, export, replication, synchronization, data flow and control flow across 200+ cloud apps and databases), Automation (trigger-driven business process automation with schedule, polling-connection and HMAC-verified webhook triggers), Backup (cloud-to-cloud snapshot backup and restore), Query (an online SQL client and visual query builder), and Connect (a connectivity-as-a-service layer that publishes any connected data source as an OData endpoint, a SQL endpoint, or an MCP endpoint for AI agents). Skyvia also ships a public REST management API at api.skyvia.com that lets you drive accounts, workspaces, agents, connections, integrations, automations, backups and Connect endpoints programmatically with a scoped, expiring API token.'
finops:
- has_sources: true
  method: derived
  name: Skyvia Finops
  primary_unit: subscription
  service_category: ''
  slug: skyvia-finops
  template: false
image: https://skyvia.com/assets/img/meta-img/meta-image.png
layout: provider
mcp_servers:
- description: 'Skyvia Connect MCP endpoints are a product feature, not a single fixed server: a customer publishes any one of their Skyvia connections (200+ cloud apps and databases) as an MCP endpoint, and Skyvia s'
  name: Devart.Skyvia.Connect.Mcp
  slug: devart-skyvia-connect-mcp
modified: '2026-10-06'
name: Skyvia
nav: Providers
network: true
overview: 'Skyvia publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public API, and 3 more. Tagged areas include Data Integration, iPaaS, ETL, ELT, and Data Replication.


  The Skyvia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skyvia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Skyvia Plans Pricing
  plan_count: 18
  slug: skyvia-plans-pricing
- name: Skyvia Price Estimates
  plan_count: 0
  slug: skyvia-price-estimates
random_paper: 15
rate_limits:
- limit_count: 0
  name: Skyvia Rate Limits
  slug: skyvia-rate-limits
scopes:
- name: Skyvia Scopes
  scope_count: 0
  slug: skyvia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 51.9
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/skyvia/skyvia-2026-08-17T081918.png
security:
- kind: authentication
  name: Skyvia Authentication
  slug: skyvia-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Skyvia Domain Security
  slug: skyvia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Skyvia Trust Center
  slug: skyvia-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 5
skills:
- name: Audit and control Skyvia Connect endpoints
  slug: skyvia-audit-connect-endpoints
- name: Trigger a Skyvia backup snapshot and verify it completed
  slug: skyvia-backup-and-verify
- name: Manage Skyvia account and workspace access
  slug: skyvia-manage-workspace-access
- name: Query business data through a Skyvia Connect MCP endpoint
  slug: skyvia-query-data-via-mcp-endpoint
- name: Run a Skyvia integration and monitor it to completion
  slug: skyvia-run-and-monitor-integration
slug: skyvia
tags:
- Data Integration
- iPaaS
- ETL
- ELT
- Data Replication
- Cloud Backup
- OData
- SQL
- Workflow Automation
- No-Code
- Connectors
- Data Management
- MCP
- Agent-Native
- Data Access
website: https://skyvia.com/
---
