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
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://api.meetleo.com
  baseurl_source: declared
  description: REST API for account entitlements, credit balance, commercial-insurance prospect search across 134 filter properties, single-prospect retrieval, and asynchronous decision-maker contact enrichment with
  name: LeO Public API
  slug: leo-public-api
- description: First-party, hosted, remote MCP server exposing LeO's insurance intelligence -- 25M+ US businesses across 200+ filters, x-dates, Form 5500 financials, benefits red flags, DOT Intelligence, Trucking Tr
  name: LeO MCP Connector
  slug: leo-mcp-connector
- description: Platform-provided Wix Site MCP server fronting LeO's marketing site, advertised in LeO's llms.txt. Nine tools covering business details, site search and generic Wix site tooling. Unauthenticated, publ
  name: LeO Site MCP (Wix-provided)
  slug: leo-site-mcp-wix-provided
- baseURL: https://api.meetleo.com
  baseurl_source: declared
  description: The Health API from LeO — 1 operation(s) for health.
  name: LeO Health API
  slug: leo-health-api
artifact_total: 12
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/capabilities/leo-capability-edges.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/plans/leo-plans-pricing.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/conformance/leo-conformance.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/llms/leo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/authentication/leo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/leo-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/scopes/leo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/leo-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/conventions/leo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/errors/leo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/data-model/leo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leo-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/rate-limits/leo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leo-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/lifecycle/leo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leo-lifecycle.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/overlays/leo-servers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leo-servers-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/mcp/leo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leo-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/well-known/leo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leo-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/leo/refs/heads/main/security/leo-domain-security.yml
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
overview: 'LeO publishes 2 APIs on the [APIs.io](https://apis.io/) network: Public API and Health API. Tagged areas include Company, Insurance, Commercial Insurance, Property and Casualty, and Employee Benefits.


  LeO''s developer surface includes pricing, signup flow, support, FAQ, engineering blog, documentation, API reference, and 23 more developer resources.'
plans:
- name: Leo Plans Pricing
  plan_count: 4
  slug: leo-plans-pricing
random_paper: 12
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
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 37.5
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
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
    score: 71.2
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Agent-Native
website: https://www.meetleo.com/
---
