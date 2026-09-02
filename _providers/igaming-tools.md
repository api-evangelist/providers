---
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
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'Token-authenticated REST API providing structured iGaming data: slot providers, slots, news articles, jobs, and regulatory entities. OpenAPI 3.0.3, cursor-paginated, ETag-friendly, with incremental sy'
  name: iGamingScraper REST API
  slug: igamingscraper-rest-api
- description: 'Free public hosted MCP server (Streamable HTTP, no API key, read-only, not metered) exposing the same iGaming dataset as 17 tools: provider search and profiles, slot search and full spec sheets, serie'
  name: iGaming Tools MCP Server
  slug: igaming-tools-mcp-server
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://i-gaming.tools/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://i-gaming.tools/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://i-gaming.tools/api/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://i-gaming.tools/docs/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://i-gaming.tools/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://i-gaming.tools/register/
- group: start
  title: ''
  type: Login
  url: https://i-gaming.tools/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://i-gaming.tools/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://i-gaming.tools/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/igaming-tools-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/igaming-tools-docs-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/igaming-tools-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/igaming-tools-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/igaming-tools-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/igaming-tools-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/igaming-tools-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/igaming-tools-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/igaming-tools-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-30'
description: iGaming Tools (i-gaming.tools) is an independent data provider that documents online casino slot games and the industry around them. Its own automated pipeline drives headless browsers against live provider demos to extract 45+ structured fields per slot — RTP and up to 30 variants, volatility, max win, reels, bet mechanic, full paytables with per-symbol payouts and hex colours, bonus rounds, and ~21 screenshots with WebP derivatives — alongside slot providers, game series, themes, features, licensing regulators, ingested industry news, iGaming job vacancies and a computed search-demand layer. Access is a token-authenticated, read-only REST API (OpenAPI 3.0.3, 29 GET operations, cursor pagination, ETag/304, ?updated_since incremental sync with tombstone reconcile) plus a free unauthenticated hosted MCP server exposing 17 read-only tools, and two llms.txt files. It is not a casino, operator or betting service.
image: https://i-gaming.tools/media/site_assets/apple_touch_icon/2026/06/5-9b0bb4a0cfe6f9a7.png
layout: provider
mcp_servers:
- description: Probed manifest with deployment block (mode remote, endpoint https://mcp.i-gaming.tools/mcp, auth none, verified probed) and all 17 tools.
  name: iGaming Tools MCP Server
  slug: igaming-tools-mcp-server
- description: LIVE remote MCP endpoint, 17 read-only tools, no credential. Requires the MCP initialize handshake for a session id — a bare tools/list returns 400, which reads as broken but is correct protocol. Veri
  name: iGaming Tools MCP Server
  slug: igaming-tools-mcp-server-2
modified: '2026-08-30'
name: iGaming Tools
nav: Providers
network: true
overview: 'iGaming Tools publishes 1 API on the [APIs.io](https://apis.io/) network: iGamingScraper REST API. Tagged areas include iGaming, Online Casino, Gambling, slot games, and slot metadata.


  iGaming Tools'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Igaming Tools Plans Pricing
  plan_count: 3
  slug: igaming-tools-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Igaming Tools Rate Limits
  slug: igaming-tools-rate-limits
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -2.7
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 55.6
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 54.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Igaming Tools Authentication
  slug: igaming-tools-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Igaming Tools Domain Security
  slug: igaming-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: igaming-tools
tags:
- iGaming
- Online Casino
- Gambling
- slot games
- slot metadata
- gambling regulation
- Industry News
- Job
- market demand
- Analytics
- REST API
- OpenAPI
- MCP Server
- llms-txt
- LLM Tooling
- slot RTP
- paytable data
- search demand
- iGaming jobs
- agent-ready API
- read-only API
website: https://i-gaming.tools/docs/
---
