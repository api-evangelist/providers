---
access_model:
  confidence: medium
  label: Paid, sales-onboarded
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://reevo.ai/pricing
  - https://help.reevo.ai/Data-management-and-migration/Integrations-With-Other-Tools
  - https://help.reevo.ai/AI-and-productivity/Reevo-MCP
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    well_known_catalog: true
  schema_version: 0.2
  score: 51.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Reevo's permission-scoped public REST API. Endpoints cover account and contact upsert, accounts (create/update/get/search-by-domain), contacts (get/search), opportunities (create/update/get/search/shi
  name: Reevo Public REST API
  slug: reevo-public-rest-api
- description: 'Reevo''s remote Model Context Protocol server. An MCP client POSTs to https://mcp.reevo.ai/mcp over MCP streamable-HTTP transport with OAuth 2.0 authorization (dynamic client registration, PKCE S256). '
  name: Reevo MCP Server
  slug: reevo-mcp-server
artifact_total: 9
asyncapis:
- description: ''
  name: Reevo Webhooks
  slug: reevo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.reevo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://help.reevo.ai
- group: docs
  title: ''
  type: APIReference
  url: https://help.reevo.ai/Data-management-and-migration/Integrations-With-Other-Tools
- group: start
  title: ''
  type: GettingStarted
  url: https://help.reevo.ai/Getting-started/Onboarding
- group: operate
  title: ''
  type: Support
  url: https://help.reevo.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reevo.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.reevo.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.reevo.ai/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/reevo-changelog.yml
- group: start
  title: ''
  type: Login
  url: https://app.reevo.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.reevo.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.reevo.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReevoAI
- group: auth
  title: ''
  type: Compliance
  url: https://www.reevo.ai/pricing
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reevo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/reevo-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/reevo-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reevo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reevo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reevo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/reevo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/reevo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reevo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reevo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reevo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reevo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/reevo-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/reevo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reevo-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reevo-domain-security.yml
created: '2026-07-17'
description: 'Reevo is an AI-native revenue platform ("revenue operating system") that consolidates the sales workflow into one system across four products: Find (lead sourcing, enrichment, routing and scoring), Engage (email sequences, dialing, inbox and meeting prep), Win (deal monitoring, smart task logging and coaching) and Foundation (a native CRM with an AI copilot, reporting, workflows and integrations). It helps GTM teams eliminate tool sprawl and automate repetitive sales work. Backed by Kleiner Perkins and Khosla Ventures. Reevo ships two callable surfaces: a permission-scoped public REST API at https://api.reevo.ai/api/v1/public authenticated with an x-api-key header (accounts, contacts, opportunities, tasks, manual activities, users, mailboxes and sequence enrollments), and a remote Model Context Protocol server at https://mcp.reevo.ai/mcp that exposes roughly 30 CRM tools over streamable-HTTP with OAuth 2.0 and granular read/create/update scopes. Neither surface publishes an
  OpenAPI or AsyncAPI definition — the contract is documented in prose in the Reevo Knowledge Base.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reevo.png
layout: provider
mcp_servers:
- description: ''
  name: Reevo MCP
  slug: reevo-mcp
modified: '2026-08-13'
name: Reevo
nav: Providers
network: true
overview: 'Reevo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Sales, CRM, and Revenue Operations.


  The Reevo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reevo''s developer surface includes documentation, API reference, getting-started guide, support, pricing, engineering blog, changelog, and 24 more developer resources.'
plans:
- name: Reevo Plans Pricing
  plan_count: 3
  slug: reevo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Reevo Rate Limits
  slug: reevo-rate-limits
scopes:
- name: Reevo Scopes
  scope_count: 22
  slug: reevo-scopes
  summary_line: 22 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 50.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reevo/refs/heads/main/screenshots/reevo-2026-08-17T081502.png
security:
- kind: authentication
  name: Reevo Authentication
  slug: reevo-authentication
  summary_line: apiKey/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Reevo Domain Security
  slug: reevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reevo
tags:
- Company
- Artificial Intelligence
- Sales
- CRM
- Revenue Operations
- Sales Automation
- Lead Generation
- Agents
- MCP
- Sales Engagement
website: https://www.reevo.ai
---
