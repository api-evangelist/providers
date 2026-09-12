---
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: 'Agent-native interfaces for TrickyBird: a structured llms.txt and a documented WebMCP in-page tool surface. No REST/OpenAPI/GraphQL/Postman contract and no remote MCP server.'
  name: TrickyBird Agent Surface
  slug: trickybird-agent-surface
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://trickybird.com
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/trickybird-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/trickybird-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trickybird-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trickybird-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/trickybird-security.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/trickybird-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trickybird-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://trickybird.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trickybird.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trickybird.com/privacy
created: '2026-09-09'
description: 'Free web proxy to open blocked sites in a normal browser tab with no account and no install. Exposes agent-native surfaces only: an llms.txt and an in-page WebMCP tool surface (13 named tools across specific pages).'
image: https://trickybird.com/opengraph-image?v=cp-v0.6.3
layout: provider
modified: '2026-09-10'
name: TrickyBird
nav: Providers
network: true
overview: 'TrickyBird publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include web proxy, unblock, no account, no install, and browser.


  TrickyBird''s developer surface includes support and 10 more developer resources.'
plans:
- name: Trickybird Plans Pricing
  plan_count: 1
  slug: trickybird-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Trickybird Rate Limits
  slug: trickybird-rate-limits
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 24.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trickybird Domain Security
  slug: trickybird-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Trickybird Vulnerability Disclosure
  slug: trickybird-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: trickybird
tags:
- web proxy
- unblock
- no account
- no install
- browser
- agent-native
- WebMCP
- llms.txt
- privacy
- anonymity
- network filtering circumvention
- consumer utility
website: https://trickybird.com
---
