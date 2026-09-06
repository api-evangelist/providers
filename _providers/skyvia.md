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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-05'
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
artifact_total: 21
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
  title: ''
  type: ChangeLog
  url: changelog/skyvia-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://skyvia.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/skyvia-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skyvia-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skyvia-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyvia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skyvia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyvia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skyvia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skyvia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skyvia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skyvia-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyvia-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/skyvia-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skyvia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skyvia-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/skyvia-automation-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/skyvia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skyvia-packages.yml
created: '2026-08-12'
description: 'Skyvia is a no-code cloud data platform from Devart covering five products on one account: Data Integration (import, export, replication, synchronization, data flow and control flow across 200+ cloud apps and databases), Automation (trigger-driven business process automation with schedule, polling-connection and HMAC-verified webhook triggers), Backup (cloud-to-cloud snapshot backup and restore), Query (an online SQL client and visual query builder), and Connect (a connectivity-as-a-service layer that publishes any connected data source as an OData endpoint, a SQL endpoint, or an MCP endpoint for AI agents). Skyvia also ships a public REST management API at api.skyvia.com that lets you drive accounts, workspaces, agents, connections, integrations, automations, backups and Connect endpoints programmatically with a scoped, expiring API token.'
image: https://skyvia.com/assets/img/meta-img/meta-image.png
layout: provider
mcp_servers:
- description: ''
  name: Devart.Skyvia.Connect.Mcp
  slug: devartskyviaconnectmcp
- description: ''
  name: Skyvia MCP Server
  slug: skyvia-mcp-server
modified: '2026-08-12'
name: Skyvia
nav: Providers
network: true
overview: 'Skyvia publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Data Integration, iPaaS, ETL, ELT, and Data Replication.


  The Skyvia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skyvia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Skyvia Plans Pricing
  plan_count: 0
  slug: skyvia-plans-pricing
random_paper: 12
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
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 23.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 41.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyvia/refs/heads/main/screenshots/skyvia-2026-08-17T081918.png
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
- Workflow-Automation
- No-Code
- Connectors
- Data Management
- MCP
- agent-native
- Data Access
website: https://skyvia.com/
---
