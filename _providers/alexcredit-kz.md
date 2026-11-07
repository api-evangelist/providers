---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AlexCredit micro‑loan marketplace (MCP JSON‑RPC)
  name: AlexCredit API
  slug: alexcredit-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/alexcredit-kz/llms/alexcredit-kz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alexcredit-kz-llms.txt
- group: agent
  href: https://artifacts.apis.io/alexcredit-kz/mcp/alexcredit-kz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alexcredit-kz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/alexcredit-kz/well-known/alexcredit-kz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alexcredit-kz-well-known.yml
- group: other
  href: https://artifacts.apis.io/alexcredit-kz/hosts/alexcredit-kz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alexcredit-kz-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alexcredit.kz/privacy
- group: auth
  href: https://artifacts.apis.io/alexcredit-kz/security/alexcredit-kz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alexcredit-kz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alexcredit.kz/
created: '2026-11-01'
description: AlexCredit is a financial marketplace in Kazakhstan offering micro‑loans ranging from 10 000 to 1 000 000 tenge from licensed micro‑finance organisations (MFO). The platform lets users compare loan offers, apply for various products such as virtual cards, 0 % interest loans, and view reviews. It provides transparent terms, interest rates, repayment schedules, and detailed information on each MFO, helping consumers make informed borrowing decisions across a wide range of financial products.
image: https://alexcredit.kz/logo-text.svg
layout: provider
mcp_servers:
- description: Remote MCP server at alexcredit.kz.
  name: AlexCredit MCP Server
  slug: alexcredit-kz-mcp-yml
modified: '2026-11-01'
name: AlexCredit
nav: Providers
network: true
overview: AlexCredit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Kazakhstan, Lending, Microfinance, and Consumer.
plans:
- name: Alexcredit Kz Plans Pricing
  plan_count: 0
  slug: alexcredit-kz-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Alexcredit Kz Rate Limits
  slug: alexcredit-kz-rate-limits
scopes:
- name: Alexcredit Kz Scopes
  scope_count: 0
  slug: alexcredit-kz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - kazakhstan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 9.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Alexcredit Kz Authentication
  slug: alexcredit-kz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Alexcredit Kz Domain Security
  slug: alexcredit-kz-domain-security
  summary_line: no transport/DNS hardening detected
slug: alexcredit-kz
tags:
- Finance
- Kazakhstan
- Lending
- Microfinance
- Consumer
website: https://alexcredit.kz/
---
