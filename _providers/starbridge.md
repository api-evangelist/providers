---
access_model:
  confidence: high
  label: Book a demo / contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans/starbridge-plans-pricing.yml
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://dashboard.starbridge.ai
  baseurl_source: declared
  description: The Bridges API from Starbridge — 4 operation(s) for bridges.
  name: Starbridge Bridges API
  slug: starbridge-bridges-api
- baseURL: https://dashboard.starbridge.ai
  baseurl_source: declared
  description: The Buyer API from Starbridge — 4 operation(s) for buyer.
  name: Starbridge Buyer API
  slug: starbridge-buyer-api
- baseURL: https://dashboard.starbridge.ai
  baseurl_source: declared
  description: The Columns API from Starbridge — 1 operation(s) for columns.
  name: Starbridge Columns API
  slug: starbridge-columns-api
- baseURL: https://dashboard.starbridge.ai
  baseurl_source: declared
  description: The External MCP API from Starbridge — 11 operation(s) for external mcp.
  name: Starbridge External MCP API
  slug: starbridge-external-mcp-api
- baseURL: https://dashboard.starbridge.ai
  baseurl_source: declared
  description: The Signal API from Starbridge — 2 operation(s) for signal.
  name: Starbridge Signal API
  slug: starbridge-signal-api
artifact_total: 20
asyncapis:
- description: ''
  name: Starbridge Webhooks
  slug: starbridge-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Starbridge External Public Bridges API
  slug: open-starbridge-bridges-api
- collection_type: open
  name: Starbridge External Public Bridges Buyer API
  slug: open-starbridge-buyer-api
- collection_type: open
  name: Starbridge External Public Bridges Columns API
  slug: open-starbridge-columns-api
- collection_type: open
  name: Starbridge External Public Bridges External API API
  slug: open-starbridge-external-api-api
- collection_type: open
  name: Starbridge External Public Bridges External MCP API
  slug: open-starbridge-external-mcp-api
- collection_type: open
  name: Starbridge External Public Bridges Signal API
  slug: open-starbridge-signal-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/starbridge-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/starbridge-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/starbridge-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/starbridge-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/starbridge-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/starbridge-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/starbridge-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/starbridge-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/starbridge-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/starbridge-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/starbridge-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/starbridge-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/starbridge-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/starbridge-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/starbridge-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/starbridge-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://hc.starbridge.ai/release-notes
- group: operate
  title: ''
  type: StatusPage
  url: https://starbridge.statuspage.io
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/starbridge-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/starbridge-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/starbridge-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/starbridge-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/starbridge-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/starbridge-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/starbridge-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/starbridge-openapi-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://hc.starbridge.ai
- group: docs
  title: ''
  type: APIReference
  url: https://hc.starbridge.ai/api-reference/rest/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://hc.starbridge.ai/api-reference/rest/generating-an-api-key
- group: operate
  title: ''
  type: HelpCenter
  url: https://hc.starbridge.ai
- group: company
  title: ''
  type: Blog
  url: https://starbridge.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/starbridge-ai
- group: start
  title: ''
  type: SignUp
  url: https://auth.starbridge.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://starbridge.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://starbridge.ai/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://starbridge.ai
created: '2026-07-17'
description: Starbridge is an AI-powered go-to-market and sales-intelligence platform for vendors selling to the public sector and education — government agencies, K-12 school districts, and higher-education institutions. It surfaces early buying signals (RFPs, board meetings, purchases, conferences, contact and job changes), scores and enriches target accounts, and drafts personalized outbound and RFP responses. Starbridge exposes an external REST API (Bearer API keys), Ed25519-signed webhooks, and a hosted OAuth MCP server, plus published Agent Skills, so buyer intelligence can be pulled into CRMs (Salesforce, HubSpot), Slack, Zapier, and AI agents. Backed by Craft Ventures.
image: https://cdn.prod.website-files.com/68a834f29776727eae1bc0f6/694fa319b9cd6a197c7be433_1_Starbridge%20Homepage%20OpenGraph.webp
layout: provider
mcp_servers:
- description: Official hosted, remote Model Context Protocol server that brings a Starbridge organization's bridges, feed, signals, and buyer research into any MCP client. Installs as a Claude plugin or as a custom
  name: Starbridge MCP
  slug: starbridge-mcp
modified: '2026-08-14'
name: Starbridge
nav: Providers
network: true
overview: 'Starbridge publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bridges API, Buyer API, Columns API, and 2 more. Tagged areas include Company, Artificial Intelligence, Sales Intelligence, Go-To-Market, and Public Sector.


  The Starbridge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Starbridge''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, signup flow, and 30 more developer resources.'
plans:
- name: Starbridge Plans Pricing
  plan_count: 0
  slug: starbridge-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Starbridge Rate Limits
  slug: starbridge-rate-limits
scopes:
- name: Starbridge Scopes
  scope_count: 0
  slug: starbridge-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 63.5
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 59.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 74.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/starbridge/refs/heads/main/screenshots/starbridge-2026-08-17T082105.png
security:
- kind: authentication
  name: Starbridge Authentication
  slug: starbridge-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Starbridge Domain Security
  slug: starbridge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Starbridge Trust Center
  slug: starbridge-trust-center
  summary_line: SOC 2 Type II
slug: starbridge
tags:
- Company
- Artificial Intelligence
- Sales Intelligence
- Go-To-Market
- Public Sector
- Education
- Government
- Procurement
- Buyer Intelligence
- MCP
website: https://starbridge.ai
---
