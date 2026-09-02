---
access_model:
  confidence: medium
  label: Customer-gated
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.meetleo.com/pricing
  - https://www.meetleo.com/mcp
  - openapi/leo-account-api-openapi.yml
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for account entitlements, credit balance, commercial-insurance prospect search across 134 filter properties, single-prospect retrieval, and asynchronous decision-maker contact enrichment with
  name: LeO Public API
  slug: leo-public-api
- description: First-party, hosted, remote MCP server exposing LeO's insurance intelligence -- 25M+ US businesses across 200+ filters, x-dates, Form 5500 financials, benefits red flags, DOT Intelligence, Trucking Tr
  name: LeO MCP Connector
  slug: leo-mcp-connector
- description: Platform-provided Wix Site MCP server fronting LeO's marketing site, advertised in LeO's llms.txt. Nine tools covering business details, site search and generic Wix site tooling. Unauthenticated, publ
  name: LeO Site MCP (Wix-provided)
  slug: leo-site-mcp-wix-provided
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/leo-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.meetleo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meetleo.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/leo-plans-pricing.yml
- group: start
  title: ''
  type: SignUp
  url: https://insights-app.meetleo.com/signup/register
- group: start
  title: ''
  type: Login
  url: https://insights-app.meetleo.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.meetleo.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.meetleo.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.meetleo.com/blog
- group: other
  title: ''
  type: Resources
  url: https://www.meetleo.com/resources
- group: company
  title: ''
  type: Press
  url: https://www.meetleo.com/media
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meetleo.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meetleo.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.meetleo.com/ai-transparency
- group: design
  title: ''
  type: Conformance
  url: conformance/leo-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.meetleo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.meetleo.com/docs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/leo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/leo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leo-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leo-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leo-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/leo-servers-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/leo-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/leo-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leo-domain-security.yml
created: '2026-07-17'
description: 'LeO is an AI-powered sales and prospecting platform for commercial insurance professionals, serving property & casualty (P&C) brokers, employee benefits advisors, and nonprofit insurance specialists. The platform pairs a commercial-lines prospect database of 25M+ US businesses and 200+ filters -- NAICS codes, revenue thresholds, workers'' compensation, DOT/FMCSA records, OSHA compliance history, Form 5500 benefits and pension filings, and IRS 990 nonprofit data -- with a renewal-date (X-date) database carrying key contacts and AI-predicted renewal months. LeO generates AI-personalized email outreach, produces pre-meeting intelligence on incumbent carriers, brokers, coverage and risk gaps, and pushes qualified prospects to CRM or CSV export. Founded by CEO Liri Halperin Segal, LeO is a Techstars portfolio company and has been certified HIPAA compliant by an external auditing firm. Alongside the subscription web application it ships two programmatic surfaces: a REST "Leo Public
  API" at api.meetleo.com with a published OpenAPI 3.0.0 definition covering account, credits, prospect search and asynchronous contact enrichment, and a first-party, OAuth-protected MCP Connector at mcp.meetleo.com marketed for Claude, ChatGPT, Gemini and Copilot. Both are entitlement-gated to existing customers and metered in credits.'
image: https://static.wixstatic.com/media/38dea4_5b1d1b85783146d8b6cf1c6f354c9be8%7Emv2.jpg/v1/fit/w_2500,h_1330,al_c/38dea4_5b1d1b85783146d8b6cf1c6f354c9be8%7Emv2.jpg
layout: provider
mcp_servers:
- description: ''
  name: LeO MCP Connector
  slug: leo-mcp-connector
- description: ''
  name: LeO MCP Server
  slug: leo-mcp-server
- description: ''
  name: LeO 3.0 Site Visitor Assistant
  slug: leo-30-site-visitor-assistant
modified: '2026-08-14'
name: LeO
nav: Providers
network: true
overview: 'LeO publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Insurance, Commercial Insurance, Property and Casualty, and Employee Benefits.


  LeO''s developer surface includes pricing, signup flow, support, FAQ, engineering blog, documentation, API reference, and 23 more developer resources.'
plans:
- name: Leo Plans Pricing
  plan_count: 4
  slug: leo-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Leo Rate Limits
  slug: leo-rate-limits
scopes:
- name: Leo Scopes
  scope_count: 0
  slug: leo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.3
  coverage:
    artifact_dirs: 20
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 55.1
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 54.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 78.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/screenshots/leo-2026-07-25T224918.png
security:
- kind: authentication
  name: Leo Authentication
  slug: leo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Leo Domain Security
  slug: leo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leo
tags:
- Company
- Insurance
- Commercial Insurance
- Property and Casualty
- Employee Benefits
- Insurtech
- Artificial Intelligence
- Sales
- Lead Generation
- Prospecting
- Data Enrichment
- Sales Intelligence
- Non-Profit
- Trucking
- MCP
- agent-native
website: https://www.meetleo.com/
---
