---
access_model:
  confidence: low
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/aoapps-io/llms/aoapps-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aoapps-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/aoapps-io/well-known/aoapps-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aoapps-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aoapps-io/hosts/aoapps-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aoapps-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aoapps-io/vendors/aoapps-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aoapps-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://account.aoapps.io/signin
- group: auth
  href: https://artifacts.apis.io/aoapps-io/security/aoapps-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aoapps-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aoapps.io/
- group: docs
  title: ''
  type: Documentation
  url: https://aoapps.io/guides
- group: operate
  title: ''
  type: Support
  url: https://aoapps.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aoapps.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aoapps.io/privacy
coverage:
  checked: '2026-11-01'
  detail: AO offers a suite of small apps for tradespeople but does not publish a public API.
  evidence:
  - status: 404
    url: https://api.aoapps.io/openapi.json
  reason: tenant-only
  state: none
created: '2026-11-01'
description: AO provides a suite of small, single-purpose apps that help tradespeople and local businesses answer every customer call, generate same-day estimates, collect reviews, and receive AI-driven recommendations. The platform lets users manage multiple apps under one account and billing, offering tools for job pricing, money-back guarantees, and AI visibility checks. AO aims to streamline workflows for trades, households, and service providers, delivering faster quotes, more reviews, and increased revenue.
image: https://aoapps.io/brand/ao-hero.jpg
layout: provider
modified: '2026-11-01'
name: AO
nav: Providers
network: true
overview: 'AO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Automation, Estimates, Reviews, and Trade.


  AO''s developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Aoapps Io Plans Pricing
  plan_count: 0
  slug: aoapps-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aoapps Io Rate Limits
  slug: aoapps-io-rate-limits
scopes:
- name: Aoapps Io Scopes
  scope_count: 0
  slug: aoapps-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 16.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aoapps Io Authentication
  slug: aoapps-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aoapps Io Domain Security
  slug: aoapps-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aoapps-io
tags:
- Artificial Intelligence
- Automation
- Estimates
- Reviews
- Trade
- SmallApps
website: https://aoapps.io/
---
