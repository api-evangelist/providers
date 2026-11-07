---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Drillr Agentic Access
  operation_count: 0
  slug: drillr-agentic-access
  summary_line: 0 operations
api_count: 1
apis:
- description: Hosted Streamable HTTP MCP server (drillr-data) exposing the same financial data as ~10 agent-callable tools covering discovery, filings, signals and arbitrary SQL. Browser OAuth auth, no API key need
  name: drillr Data MCP Server
  slug: drillr-data-mcp-server
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Analyst consensus and individual rating events (US only)
  name: drillr Public Data API Analyst API
  slug: drillr-analyst-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Ticker resolution, natural-language company discovery and company profiles
  name: drillr Public Data API Company API
  slug: drillr-company-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: The machine-readable API contract itself
  name: drillr Public Data API Contract API
  slug: drillr-contract-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Earnings calendar and structured earnings-call summaries
  name: drillr Public Data API Earnings API
  slug: drillr-earnings-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: 'Corporate events: financings, deals, executive changes, corporate actions, ownership (US only)'
  name: drillr Public Data API Events API
  slug: drillr-events-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Executive roster and annual compensation (US only)
  name: drillr Public Data API Executives API
  slug: drillr-executives-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Regulatory filing lists and full-text filing search (US, Japan, China)
  name: drillr Public Data API Filings API
  slug: drillr-filings-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: The three financial statements and precomputed financial metrics
  name: drillr Public Data API Financials API
  slug: drillr-financials-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Insider holdings and transactions, institutional holdings (US only)
  name: drillr Public Data API Ownership API
  slug: drillr-ownership-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Historical bars and latest closing-price snapshots (US)
  name: drillr Public Data API Prices API
  slug: drillr-prices-api
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: Industry inflections, enterprise AI adoption and cross-source news search
  name: drillr Public Data API Signal API
  slug: drillr-signal-api
artifact_total: 23
common:
- group: other
  href: https://artifacts.apis.io/drillr/capabilities/drillr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/drillr-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://drillr.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://drillr.ai/developer
- group: docs
  title: ''
  type: Documentation
  url: https://drillr.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://drillr.ai/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://drillr.ai/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://drillr.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://drillr.ai/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drillr.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drillr.ai/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://drillr.ai/changelog
- group: agent
  href: https://artifacts.apis.io/drillr/llms/drillr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drillr-llms.txt
- group: auth
  href: https://artifacts.apis.io/drillr/authentication/drillr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drillr-authentication.yml
- group: agent
  href: https://artifacts.apis.io/drillr/well-known/drillr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drillr-well-known.yml
- group: design
  href: https://artifacts.apis.io/drillr/conformance/drillr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drillr-conformance.yml
- group: design
  href: https://artifacts.apis.io/drillr/errors/drillr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drillr-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/drillr/rate-limits/drillr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drillr-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/drillr/plans/drillr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drillr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/drillr/conventions/drillr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drillr-conventions.yml
- group: design
  href: https://artifacts.apis.io/drillr/lifecycle/drillr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drillr-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/drillr/changelog/drillr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/drillr-changelog.yml
- group: design
  href: https://artifacts.apis.io/drillr/data-model/drillr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drillr-data-model.yml
- group: build
  href: https://artifacts.apis.io/drillr/packages/drillr-packages.yml
  title: ''
  type: Packages
  url: packages/drillr-packages.yml
- group: build
  href: https://artifacts.apis.io/drillr/cli/drillr-cli.yml
  title: ''
  type: CLI
  url: cli/drillr-cli.yml
- group: other
  href: https://artifacts.apis.io/drillr/overlays/drillr-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/drillr-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/drillr/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/drillr/agentic-access/drillr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drillr-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/drillr/security/drillr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drillr-domain-security.yml
created: '2026-09-13'
description: 'drillr is a financial data and research API for the US, China and Japan. It provides financial statements, full-text filing search, natural-language company discovery, and research signals extracted from filings, news and earnings calls. The same data is served two ways: a REST API for scripts and pipelines, and a hosted MCP server for AI agents, with every reported figure linking back to its source document.'
finops:
- has_sources: true
  method: derived
  name: Drillr Finops
  primary_unit: 100 credits
  service_category: ''
  slug: drillr-finops
  template: false
layout: provider
mcp_servers:
- description: ''
  name: drillr MCP Server
  slug: data
modified: '2026-09-14'
name: drillr
nav: Providers
network: true
overview: 'drillr publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Public Data API Analyst API, Public Data API Company API, Public Data API Contract API, and 9 more. Tagged areas include Financial Data, Stocks, SEC Filings, Fundamentals, and Earnings.


  The drillr catalog on APIs.io includes 1 Spectral governance ruleset.


  drillr''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, changelog, authentication, and 21 more developer resources.'
plans:
- name: Drillr Plans Pricing
  plan_count: 7
  slug: drillr-plans-pricing
- name: Drillr Price Estimates
  plan_count: 0
  slug: drillr-price-estimates
random_paper: 1
rate_limits:
- limit_count: 1
  name: Drillr Rate Limits
  slug: drillr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 116
  extends:
  - spectral:oas
  name: drillr API Rules
  rule_count: 75
  severity_counts:
    error: 64
    hint: 0
    info: 1
    warn: 10
  slug: drillr-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.5
    catalog_earned_first_party: 20.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 71.1
    contract_governance: 31.8
    contract_quality: 59.7
    developer_ergonomics: 58.9
    discoverability: 71.7
    operational_transparency: 36.8
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/drillr/drillr-2026-10-11T103916.png
security:
- kind: authentication
  name: Drillr Authentication
  slug: drillr-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Drillr Domain Security
  slug: drillr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: drillr-company-financials-lookup
  slug: drillr-company-financials-lookup
- name: drillr-filing-research
  slug: drillr-filing-research
slug: drillr
tags:
- Financial Data
- Stocks
- SEC Filings
- Fundamentals
- Earnings
- Ownership
- Corporate Events
- Analyst Ratings
- news-signals
- MCP
- Agent-Native
website: https://drillr.ai
---
