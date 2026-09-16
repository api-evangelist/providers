---
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
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.1
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Drillr Agentic Access
  operation_count: 0
  slug: drillr-agentic-access
  summary_line: 0 operations
api_count: 2
apis:
- baseURL: https://gateway.drillr.ai/api/v2
  baseurl_source: declared
  description: REST API exposing ~29 endpoints across company discovery, filings, signals, events, ownership, executives, financials, earnings, prices and analyst data for US, China and Japan. API-key header auth (X
  name: drillr REST API
  slug: drillr-rest-api
- description: Hosted Streamable HTTP MCP server (drillr-data) exposing the same financial data as ~10 agent-callable tools covering discovery, filings, signals and arbitrary SQL. Browser OAuth auth, no API key need
  name: drillr Data MCP Server
  slug: drillr-data-mcp-server
artifact_total: 9
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/llms/drillr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drillr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/authentication/drillr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drillr-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/well-known/drillr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drillr-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/conformance/drillr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drillr-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/errors/drillr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drillr-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/rate-limits/drillr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drillr-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/plans/drillr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drillr-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/conventions/drillr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drillr-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/lifecycle/drillr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drillr-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/changelog/drillr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/drillr-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/data-model/drillr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drillr-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/packages/drillr-packages.yml
  title: ''
  type: Packages
  url: packages/drillr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/cli/drillr-cli.yml
  title: ''
  type: CLI
  url: cli/drillr-cli.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/overlays/drillr-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/drillr-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/agentic-access/drillr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drillr-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/drillr/refs/heads/main/security/drillr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drillr-domain-security.yml
created: '2026-09-13'
description: 'drillr is a financial data and research API for the US, China and Japan. It provides financial statements, full-text filing search, natural-language company discovery, and research signals extracted from filings, news and earnings calls. The same data is served two ways: a REST API for scripts and pipelines, and a hosted MCP server for AI agents, with every reported figure linking back to its source document.'
layout: provider
mcp_servers:
- description: ''
  name: drillr Public Data API MCP Server
  slug: drillr-public-data-api-mcp-server
- description: 'Hosted Streamable HTTP MCP server exposing drillr''s financial-research data as agent-callable tools: ticker resolution, qualitative company search, SEC filing discovery and full-text filing search, cr'
  name: drillr Public Data API MCP Server
  slug: drillr-public-data-api-mcp-server-2
modified: '2026-09-14'
name: drillr Public Data API
nav: Providers
network: true
overview: 'drillr Public Data API publishes 1 API on the [APIs.io](https://apis.io/) network: drillr REST API. Tagged areas include Financial Data, Equities, SEC Filings, Fundamentals, and Earnings.


  drillr Public Data API''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, changelog, authentication, and 20 more developer resources.'
plans:
- name: Drillr Plans Pricing
  plan_count: 4
  slug: drillr-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Drillr Rate Limits
  slug: drillr-rate-limits
score:
  band: strong
  composite: 57.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 58.9
    discoverability: 72.2
    operational_transparency: 36.8
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Drillr Authentication
  slug: drillr-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Drillr Domain Security
  slug: drillr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drillr
tags:
- Financial Data
- Equities
- SEC Filings
- Fundamentals
- Earnings
- Ownership
- Corporate Events
- Analyst Ratings
- news-signals
- MCP
- agent-native
website: https://drillr.ai
---
