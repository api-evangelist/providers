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
- description: AI sprite and animation generation API (requires sign‑in).
  name: God Mode AI API
  slug: god-mode-ai-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/godmodeai-co/plans/godmodeai-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/godmodeai-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/godmodeai-co/llms/godmodeai-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/godmodeai-co-llms.txt
- group: agent
  href: https://artifacts.apis.io/godmodeai-co/well-known/godmodeai-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/godmodeai-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/godmodeai-co/hosts/godmodeai-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/godmodeai-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/godmodeai-co/vendors/godmodeai-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/godmodeai-co-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.godmodeai.co/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.godmodeai.co/plans
- group: auth
  href: https://artifacts.apis.io/godmodeai-co/security/godmodeai-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/godmodeai-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://godmodeai.co/
coverage:
  checked: '2026-10-31'
  detail: API reference at /api redirects to a sign‑in page, requiring authentication to access any contract.
  evidence:
  - status: 307
    url: https://www.godmodeai.co/api
  reason: auth-required
  state: gated
created: '2026-10-30'
description: God Mode AI provides cutting‑edge AI‑powered tools that generate high‑quality game sprites and animations. Their platform creates artifact‑free looping animations, supports multiple camera views, rich action types, and advanced visual effects. It offers commercial licensing and aims to accelerate game development by automating asset creation with deep learning models.
image: https://www.godmodeai.co/godmodeai-hero-anim.webp
layout: provider
modified: '2026-10-30'
name: godmodeai-co
nav: Providers
network: true
overview: 'godmodeai-co is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Game Development, Animation, Asset Generation, and Sprite Tools.


  godmodeai-co''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Godmodeai Co Plans Pricing
  plan_count: 4
  slug: godmodeai-co-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.3
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 16.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/godmodeai-co/godmodeai-co-2026-11-03T132911.png
security:
- kind: domain-security
  name: Godmodeai Co Domain Security
  slug: godmodeai-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: godmodeai-co
tags:
- Artificial Intelligence
- Game Development
- Animation
- Asset Generation
- Sprite Tools
website: https://godmodeai.co/
---
