---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-09-15'
api_count: 2
apis:
- baseURL: https://premium.aiera.com/api
  baseurl_source: declared
  description: Entitlement-aware REST API over Aiera's financial research corpus — corporate events and transcripts, calendars and estimated events, equities and sectors, companies and people, SEC filings, company-p
  name: Aiera REST API
  slug: aiera-rest-api
- description: Aiera's hosted remote Model Context Protocol server, exposing the financial research corpus to LLMs and agentic workflows as roughly three dozen specialized tools across equities and financials, index
  name: Aiera MCP Server
  slug: aiera-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://aiera.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rest.aiera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rest.aiera.com/
- group: docs
  title: ''
  type: APIReference
  url: https://rest.aiera.com/docs/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://rest.aiera.com/#quick-start
- group: operate
  title: ''
  type: Support
  url: https://support.aiera.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://aiera.com/newsroom/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aiera-inc
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.aiera.com/auth
- group: start
  title: ''
  type: Login
  url: https://dashboard.aiera.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiera.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiera.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aiera.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/mcp/aiera-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiera-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/llms/aiera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aiera-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/well-known/aiera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiera-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/authentication/aiera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiera-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/scopes/aiera-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/aiera-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/conventions/aiera-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aiera-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/lifecycle/aiera-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aiera-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/conformance/aiera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiera-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/security/aiera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiera-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/packages/aiera-packages.yml
  title: ''
  type: Packages
  url: packages/aiera-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/packages/aiera-packages.yml
  title: ''
  type: SDKs
  url: packages/aiera-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/components/aiera-components.yml
  title: ''
  type: Components
  url: components/aiera-components.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/rate-limits/aiera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiera-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/plans/aiera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiera-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/errors/aiera-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiera-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aiera/refs/heads/main/data-model/aiera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiera-data-model.yml
created: '2026-09-14'
description: Aiera is a New York-based financial research technology company that provides real-time and historical intelligence on public-company events. Its platform covers earnings calls, investor days, conferences and shareholder meetings with live AI transcription plus human-edited transcripts, and layers on AI-generated summaries, topic and tonal-sentiment analysis, SEC filings, company-published documents, broker research, expert-insight content (including Third Bridge) and financial news. Aiera exposes that corpus to buy-side and sell-side institutions through an entitlement-aware REST API, a hosted remote MCP server for LLM and agentic workflows, embeddable web components (AieraChat, Aieracast, EventList), and an open-source Python MCP package.
image: https://aiera.com/wp-content/uploads/2025/09/aiera-default-feature.jpg
layout: provider
mcp_servers:
- description: Aiera ships a hosted remote MCP server exposing its financial research corpus — earnings calls and transcripts, calendars, equities and financials, SEC filings, company-published documents, Third Brid
  name: Aiera MCP Server
  slug: aiera-mcp-server
- description: ''
  name: Aiera MCP Server
  slug: aiera-mcp-server-2
modified: '2026-09-14'
name: Aiera
nav: Providers
network: true
overview: 'Aiera publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Financial Research, Earnings Calls, Transcripts, SEC Filings, and Market Data.


  Aiera''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Aiera Plans Pricing
  plan_count: 0
  slug: aiera-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Aiera Rate Limits
  slug: aiera-rate-limits
scopes:
- name: Aiera Scopes
  scope_count: 0
  slug: aiera-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 66.1
    discoverability: 75.9
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 49.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aiera Authentication
  slug: aiera-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Aiera Domain Security
  slug: aiera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aiera
tags:
- Financial Research
- Earnings Calls
- Transcripts
- SEC Filings
- Market Data
- Financial Data
- Broker Research
- Expert Networks
- Speech-to-Text
- Financial-Services
- MCP
- agent-native
website: https://aiera.com/
---
