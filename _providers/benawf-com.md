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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for BenAwf platform (access gated behind sign‑in).
  name: BenAwf API
  slug: benawf-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/benawf-com/llms/benawf-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/benawf-com-llms.txt
- group: other
  href: https://artifacts.apis.io/benawf-com/hosts/benawf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/benawf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/benawf-com/vendors/benawf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/benawf-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://benawf.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://benawf.com/privacy
- group: auth
  href: https://artifacts.apis.io/benawf-com/security/benawf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/benawf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://benawf.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://benawf.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://benawf.com/faq
coverage:
  checked: '2026-11-02'
  detail: API documentation requires sign‑in, no public contract found.
  evidence:
  - status: 200
    url: https://benawf.com/integrations
  reason: auth-required
  state: gated
created: '2026-11-02'
description: The workbench for AI-assisted trading. Write strategies in plain language, backtest them against real market history, version every experiment, and deploy to paper-first sessions when the evidence holds up. Live venue trading is beta.
image: https://benawf.com/og-image.png
layout: provider
modified: '2026-11-02'
name: BenAwf
nav: Providers
network: true
overview: 'BenAwf is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Trading, Finance, Platform, and Strategy.


  BenAwf''s developer surface includes getting-started guide, support, and 7 more developer resources.'
plans:
- name: Benawf Com Plans Pricing
  plan_count: 0
  slug: benawf-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Benawf Com Rate Limits
  slug: benawf-com-rate-limits
scopes:
- name: Benawf Com Scopes
  scope_count: 0
  slug: benawf-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 22.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Benawf Com Authentication
  slug: benawf-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Benawf Com Domain Security
  slug: benawf-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: benawf-com
tags:
- Artificial Intelligence
- Trading
- Finance
- Platform
- Strategy
- Backtesting
website: https://benawf.com/
---
