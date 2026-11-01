---
access_model:
  confidence: high
  label: Freemium, self-service
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://alphai.io/pricing
  - https://alphai.io/account/api-keys
  - https://alphai.io/developers
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Alphaai Agentic Access
  operation_count: 15
  slug: alphaai-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: Hosted MCP server over Streamable HTTP exposing fifteen tools for news search, ticker news, trending, actionable-now, macro, economic calendar, insider news, pair analysis, article retrieval, ticker d
  name: AlphaAI MCP Server
  slug: alphaai-mcp-server
- description: 'Provider-published open-source pack of five Claude Code agent skills wrapping the MCP tools into ready-made workflows: one-ticker brief, market pulse, insider-activity scan, two-ticker read-across, an'
  name: AlphaAI Claude Code Skills
  slug: alphaai-claude-code-skills
- baseURL: https://api.alphai.io
  baseurl_source: declared
  description: Scheduled US macro releases (FOMC, CPI, jobs, GDP, PCE…).
  name: AlphaAI Calendar API
  slug: alphaai-calendar-api
- baseURL: https://api.alphai.io
  baseurl_source: declared
  description: Relevance-scored, ticker-linked news.
  name: AlphaAI News API
  slug: alphaai-news-api
- baseURL: https://api.alphai.io
  baseurl_source: declared
  description: Active equity, crypto, and foreign symbols (tickers).
  name: AlphaAI Symbols API
  slug: alphaai-symbols-api
- baseURL: https://mcp.alphai.io/mcp
  baseurl_source: declared
  description: What each data source holds — from when, how dense, with which caveats.
  name: AlphaAI Coverage API
  slug: alphaai-coverage-api
- baseURL: https://mcp.alphai.io/mcp
  baseurl_source: declared
  description: Descriptive news activity and supporting headlines.
  name: AlphaAI Radar API
  slug: alphaai-radar-api
- baseURL: https://mcp.alphai.io/mcp
  baseurl_source: declared
  description: Market events covered by two or more publishers, summarised from their sources.
  name: AlphaAI Stories API
  slug: alphaai-stories-api
artifact_total: 25
asyncapis:
- description: ''
  name: Alphaai Webhooks
  slug: alphaai-webhooks
collections:
- collection_type: open
  name: alphai REST API
  slug: open-alphaai-rest-api
common:
- group: other
  href: https://artifacts.apis.io/alphaai/capabilities/alphaai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alphaai-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/makeev/alphai-claude-skills/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/alphaai/overlays/alphaai-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alphaai-rest-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://alphai.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://alphai.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://api.alphai.io/api/schema/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://alphai.io/developers
- group: build
  title: ''
  type: Examples
  url: https://alphai.io/examples
- group: operate
  title: ''
  type: Support
  url: https://alphai.io/contact
- group: company
  title: ''
  type: Blog
  url: https://alphai.io/research
- group: company
  title: ''
  type: BlogRSS
  url: https://alphai.io/research/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makeev
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/mmakeevs-team/alphaai-financial-news-api
- group: commercial
  title: ''
  type: Pricing
  url: https://alphai.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://alphai.io/account/api-keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphai.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alphai.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alphai.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://alphai.io/changelog
- group: operate
  href: https://artifacts.apis.io/alphaai/changelog/alphaai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alphaai-changelog.yml
- group: design
  href: https://artifacts.apis.io/alphaai/lifecycle/alphaai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alphaai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/alphaai/authentication/alphaai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alphaai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/alphaai/scopes/alphaai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/alphaai-scopes.yml
- group: auth
  title: ''
  type: Security
  url: https://api.alphai.io/.well-known/security.txt
- group: auth
  href: https://artifacts.apis.io/alphaai/well-known/alphaai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/alphaai-security.txt
- group: auth
  href: https://artifacts.apis.io/alphaai/security/alphaai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alphaai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/alphaai/security/alphaai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphaai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/alphaai/well-known/alphaai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphaai-well-known.yml
- group: design
  href: https://artifacts.apis.io/alphaai/conformance/alphaai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alphaai-conformance.yml
- group: design
  href: https://artifacts.apis.io/alphaai/conventions/alphaai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alphaai-conventions.yml
- group: design
  href: https://artifacts.apis.io/alphaai/errors/alphaai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alphaai-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/alphaai/rate-limits/alphaai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alphaai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/alphaai/plans/alphaai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphaai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/alphaai/data-model/alphaai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alphaai-data-model.yml
- group: design
  href: https://artifacts.apis.io/alphaai/asyncapi/alphaai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/alphaai-webhooks.yml
- group: build
  href: https://artifacts.apis.io/alphaai/packages/alphaai-packages.yml
  title: ''
  type: Packages
  url: packages/alphaai-packages.yml
- group: build
  href: https://artifacts.apis.io/alphaai/packages/alphaai-packages.yml
  title: ''
  type: SDKs
  url: packages/alphaai-packages.yml
- group: build
  href: https://artifacts.apis.io/alphaai/cli/alphaai-cli.yml
  title: ''
  type: CLI
  url: cli/alphaai-cli.yml
- group: start
  href: https://artifacts.apis.io/alphaai/sandbox/alphaai-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/alphaai-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/alphaai/llms/alphaai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alphaai-llms.txt
- group: agent
  href: https://artifacts.apis.io/alphaai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/alphaai/agentic-access/alphaai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alphaai-agentic-access.yml
created: '2026-07-05'
description: A REST API and agent-native platform for relevance-scored, ticker-linked financial news, built for trading bots, agent backends, and dashboards. Every article is enriched at ingest with a 1-10 relevance score, one of fourteen categories, validated ticker links, and per-ticker sentiment with an impact analysis and confidence rating, plus structured SEC Form 4 insider data sourced from EDGAR. The same data core is served three ways — an OpenAPI 3.1 REST API at api.alphai.io, a hosted MCP server with OAuth 2.1 and dynamic client registration at mcp.alphai.io, and HMAC-signed webhooks on the Pro tier — alongside first-party Python, TypeScript and Rust clients and a provider-published pack of Claude Code agent skills.
finops:
- has_sources: true
  method: derived
  name: Alphaai Finops
  primary_unit: subscription
  service_category: ''
  slug: alphaai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alphaai.png
layout: provider
mcp_servers:
- description: ''
  name: AlphaAI MCP Server
  slug: mcp
modified: '2026-08-11'
name: AlphaAI
nav: Providers
network: true
overview: 'AlphaAI publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calendar API, News API, Symbols API, and 5 more. Tagged areas include Financial News, Stock Market, SEC Filings, Insider Trading, and Fintech.


  The AlphaAI catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AlphaAI''s developer surface includes documentation, API reference, getting-started guide, code examples, support, engineering blog, pricing, and 35 more developer resources.'
plans:
- name: Alphaai Plans Pricing
  plan_count: 4
  slug: alphaai-plans-pricing
- name: Alphaai Price Estimates
  plan_count: 0
  slug: alphaai-price-estimates
random_paper: 0
rate_limits:
- limit_count: 6
  name: Alphaai Rate Limits
  slug: alphaai-rate-limits
scopes:
- name: Alphaai Scopes
  scope_count: 2
  slug: alphaai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 63.6
    developer_ergonomics: 90.5
    discoverability: 65.0
    operational_transparency: 86.8
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 40.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/alphaai/alphaai-2026-08-17T080047.png
security:
- kind: authentication
  name: Alphaai Authentication
  slug: alphaai-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Alphaai Domain Security
  slug: alphaai-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Alphaai Vulnerability Disclosure
  slug: alphaai-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 5
skills:
- name: insider-radar
  slug: alphaai-insider-radar
- name: manage-alerts
  slug: alphaai-manage-alerts
- name: market-pulse
  slug: alphaai-market-pulse
- name: peer-readacross
  slug: alphaai-peer-readacross
- name: stock-brief
  slug: alphaai-stock-brief
slug: alphaai
tags:
- Financial News
- Stock Market
- SEC Filings
- Insider Trading
- Fintech
- Market Data
- Sentiment
- AI Agents
- MCP
- LLM
- Trading
website: https://alphai.io/developers
---
