---
access_model:
  confidence: high
  label: Demo/sales required
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - https://funnel.io/pricing
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.7
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: 'The Funnel Control Plane API provides configuration-management operations for a Funnel subscription — workspaces, data sources, custom dimensions and metrics, and data exports to BigQuery, Snowflake, '
  name: Funnel Control Plane API
  slug: funnel-control-plane-api
- description: Funnel MCP is Funnel's first-party hosted, remote Model Context Protocol server. It exposes a Funnel workspace's harmonized cross-channel marketing data, semantic field definitions and workspace conte
  name: Funnel MCP
  slug: funnel-mcp
- description: The Funnel File Import Webhook API is a documented inbound HTTP endpoint that lets a customer hand Funnel links to data files for ingestion into a File Import data source. A per-source webhook URL and
  name: Funnel File Import Webhook API
  slug: funnel-file-import-webhook-api
artifact_total: 11
asyncapis:
- description: ''
  name: Funnel Webhooks
  slug: funnel-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://funnel.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.funnel.io/en/
- group: docs
  title: ''
  type: APIReference
  url: https://registry.terraform.io/providers/funnel-io/funnel/latest/docs
- group: company
  title: ''
  type: Blog
  url: https://funnel.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.funnel.io/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://funnel.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.funnel.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://funnel.io/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://funnel.io/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/funnel-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.funnel.io
- group: build
  title: ''
  type: Packages
  url: packages/funnel-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/funnel-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/funnel-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/funnel-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/funnel-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/funnel-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/funnel-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/funnel-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://funnel.io/funnel-information-security-overview
- group: auth
  title: ''
  type: TrustCenter
  url: security/funnel-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/funnel-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/funnel-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/funnel-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/funnel-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/funnel-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/funnel-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/funnel-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/funnel-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/funnel-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Quickstart
  url: https://help.funnel.io/en/articles/15014203-quick-start-guide-using-funnel-mcp
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.funnel.io/en/
- group: start
  title: ''
  type: Login
  url: https://app.funnel.io/
created: '2026-07-17'
description: Funnel (funnel.io) is a marketing intelligence and marketing data hub that helps agencies and brands become more data-driven. It connects to hundreds of advertising, analytics, CRM, and social data platforms, then automatically collects, normalizes, and transforms that marketing data into a single, business-ready model. Funnel exports the harmonized data to cloud data warehouses (BigQuery, Snowflake), Google Cloud Storage, BI and visualization tools, and back to ad platforms, and layers on advanced marketing measurement (Marketing Mix Modeling and Multi-Touch Attribution) plus dashboards and reporting. Programmatic configuration is exposed through the Funnel Control Plane API, consumed via an official Terraform provider and an OAuth 2.0 client-credentials (Auth0) system-user flow, with regional US and EU data residency. Funnel also ships a first-party hosted MCP server (Funnel MCP) that exposes six read-only tools over OAuth to Claude, ChatGPT, Cursor and other MCP clients,
  plus a documented inbound file-import webhook API. Funnel publishes no OpenAPI or AsyncAPI for any of the three surfaces.
image: https://funnel.io/hubfs/Blog%20images.006.jpeg
layout: provider
mcp_servers:
- description: Funnel's first-party hosted, remote MCP server. It exposes a Funnel workspace's harmonized cross-channel marketing data, field/semantic definitions and workspace context to any MCP-compatible client (
  name: Funnel MCP
  slug: funnel-mcp
modified: '2026-08-12'
name: Funnel
nav: Providers
network: true
overview: 'Funnel publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Marketing Intelligence, Marketing Data, and Analytics.


  The Funnel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Funnel''s developer surface includes documentation, API reference, engineering blog, support, pricing, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Funnel Plans Pricing
  plan_count: 3
  slug: funnel-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Funnel Rate Limits
  slug: funnel-rate-limits
scopes:
- name: Funnel Scopes
  scope_count: 0
  slug: funnel-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 49.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 55.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/funnel/refs/heads/main/screenshots/funnel-2026-07-25T215322.png
security:
- kind: authentication
  name: Funnel Authentication
  slug: funnel-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Funnel Domain Security
  slug: funnel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Funnel Trust Center
  slug: funnel-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II, CSA STAR Level 1
slug: funnel
tags:
- Company
- Marketing
- Marketing Intelligence
- Marketing Data
- Analytics
- Advertising
- Data Integration
- ETL
- Data Warehouse
- Attribution
- Reporting
- Business Intelligence
- MCP
- AI Agents
- Marketing Mix Modeling
website: https://funnel.io/
---
