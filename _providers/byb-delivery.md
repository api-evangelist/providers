---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API for BYB Delivery logistics services
  name: BYB Delivery API
  slug: byb-delivery-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/byb-delivery/llms/byb-delivery-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/byb-delivery-llms.txt
- group: other
  href: https://artifacts.apis.io/byb-delivery/hosts/byb-delivery-hosts.yml
  title: ''
  type: Hosts
  url: hosts/byb-delivery-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://byb.delivery/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://byb.delivery/privacy/
- group: start
  title: ''
  type: Login
  url: https://customer.byb.delivery/login
- group: auth
  href: https://artifacts.apis.io/byb-delivery/security/byb-delivery-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/byb-delivery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://byb.delivery/
created: '2026-11-03'
description: Big Yellow Box (BYB) Delivery offers real-time tracking, secure deliveries, and customized logistics solutions across Accra, Ghana. It provides reliable courier services for businesses, featuring fast shipping, secure handling, and a user-friendly platform for managing shipments and logistics needs.
image: https://byb.delivery/images/photos/hero.jpg
layout: provider
modified: '2026-11-03'
name: Big Yellow Box Delivery
nav: Providers
network: true
overview: Big Yellow Box Delivery is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Delivery, Ghana, Couriers, and Business.
random_paper: 6
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Byb Delivery Domain Security
  slug: byb-delivery-domain-security
  summary_line: TLSv1.3 · HSTS
slug: byb-delivery
tags:
- Logistics
- Delivery
- Ghana
- Couriers
- Business
website: https://byb.delivery/
---
