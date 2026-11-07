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
- description: Public API reference for BuyNearby platform
  name: BuyNearby API
  slug: buynearby-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/buynearby-store/llms/buynearby-store-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buynearby-store-llms.txt
- group: agent
  href: https://artifacts.apis.io/buynearby-store/well-known/buynearby-store-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buynearby-store-well-known.yml
- group: other
  href: https://artifacts.apis.io/buynearby-store/hosts/buynearby-store-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buynearby-store-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buynearby.store/terms-of-service.php
- group: start
  title: ''
  type: SignUp
  url: https://buynearby.store/auth/register.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buynearby.store/privacy-policy.php
- group: company
  title: ''
  type: Blog
  url: https://buynearby.store/blog
- group: auth
  href: https://artifacts.apis.io/buynearby-store/security/buynearby-store-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buynearby-store-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buynearby.store/
coverage:
  detail: No OpenAPI, AsyncAPI, GraphQL, or gRPC spec discovered despite public API reference page.
  evidence:
  - status: 404
    url: https://api.buynearby.store/openapi.json
  - status: 404
    url: https://api.buynearby.store/openapi.yaml
  - status: 404
    url: https://api.buynearby.store/swagger.json
  - status: 404
    url: https://api.buynearby.store/v1/openapi.json
  - status: 404
    url: https://api.buynearby.store/api-docs
  - status: 404
    url: https://api.buynearby.store/docs
  - status: 404
    url: https://api.buynearby.store/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: BuyNearby is a same‑day local delivery service based in Calgary, connecting customers with neighbourhood grocery and essential stores. It enables shoppers to order groceries, household items and more online, supporting local businesses while providing fast, convenient delivery. The platform offers a marketplace for local retailers and a seamless ordering experience for consumers, emphasizing community support and rapid fulfillment.
image: https://buynearby.store/logo_192.png
layout: provider
modified: '2026-11-03'
name: BuyNearby
nav: Providers
network: true
overview: 'BuyNearby is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Delivery, Grocery, Calgary, and Marketplace.


  BuyNearby''s developer surface includes signup flow, engineering blog, and 7 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.5
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
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buynearby Store Domain Security
  slug: buynearby-store-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buynearby-store
tags:
- Company
- Delivery
- Grocery
- Calgary
- Marketplace
- Local Business
website: https://buynearby.store/
---
