---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AlphaCreek MCP provides SEC filing retrieval via a REST API.
  name: AlphaCreek MCP
  slug: alphacreek-mcp
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/alphacreek-ai/plans/alphacreek-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alphacreek-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/alphacreek-ai/well-known/alphacreek-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alphacreek-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/alphacreek-ai/hosts/alphacreek-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alphacreek-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/alphacreek-ai/vendors/alphacreek-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alphacreek-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alphacreek.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphacreek.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alphacreek.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.alphacreek.ai/auth/jwt/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.alphacreek.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.alphacreek.ai/blog
- group: auth
  href: https://artifacts.apis.io/alphacreek-ai/security/alphacreek-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alphacreek-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alphacreek.ai/
created: '2026-11-01'
description: AlphaCreek provides a hosted MCP that gives financial AI agents structured, citation‑ready SEC filing data. Covering over 6,000 US tickers, it offers fast retrieval, citation URLs, and seamless integration for Claude, Perplexity, ChatGPT and other models, enabling compliance‑aware AI products without building their own filing pipelines.
image: https://www.alphacreek.ai/assets/images/logo/logo400x400.png
layout: provider
modified: '2026-11-01'
name: AlphaCreek
nav: Providers
network: true
overview: 'AlphaCreek is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Artificial Intelligence, SEC, Data, and MCP.


  AlphaCreek''s developer surface includes pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Alphacreek Ai Plans Pricing
  plan_count: 5
  slug: alphacreek-ai-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 24.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 19.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alphacreek Ai Domain Security
  slug: alphacreek-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alphacreek-ai
tags:
- Finance
- Artificial Intelligence
- SEC
- Data
- MCP
website: https://www.alphacreek.ai/
---
