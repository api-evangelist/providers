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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Shared memory map API for people and AI
  name: Cairn Memory API
  slug: cairn-memory-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/cairn-ink/plans/cairn-ink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cairn-ink-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cairn-ink/well-known/cairn-ink-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cairn-ink-well-known.yml
- group: other
  href: https://artifacts.apis.io/cairn-ink/hosts/cairn-ink-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cairn-ink-hosts.yml
- group: other
  href: https://artifacts.apis.io/cairn-ink/vendors/cairn-ink-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cairn-ink-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cairn.ink/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cairn.ink/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cairn.ink/pricing
- group: start
  title: ''
  type: Login
  url: https://cairn.ink/sign-in
- group: auth
  href: https://artifacts.apis.io/cairn-ink/security/cairn-ink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cairn-ink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cairn.ink/
coverage:
  checked: '2026-11-03'
  detail: OpenAPI spec not found at https://api.cairn.ink/openapi.json (404)
  evidence:
  - status: 404
    url: https://api.cairn.ink/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: Cairn provides a shared memory map for people and AI, enabling every AI you use to stay up to speed. It keeps memories with receipts so agents can find decision origins and continue from there. The platform offers free and pro plans, with features like private collections, AI allowances, and Moss Care passes.
image: https://cairn.ink/og/cairn-share.png
layout: provider
modified: '2026-11-03'
name: Cairn
nav: Providers
network: true
overview: 'Cairn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Memory, Platform, and Collaboration.


  Cairn''s developer surface includes pricing and 9 more developer resources.'
plans:
- name: Cairn Ink Plans Pricing
  plan_count: 3
  slug: cairn-ink-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cairn Ink Domain Security
  slug: cairn-ink-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cairn-ink
tags:
- Company
- Artificial Intelligence
- Memory
- Platform
- Collaboration
website: https://cairn.ink/
---
