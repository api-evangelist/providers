---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/tryhala/plans/tryhala-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tryhala-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tryhala/hosts/tryhala-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tryhala-hosts.yml
- group: other
  href: https://artifacts.apis.io/tryhala/vendors/tryhala-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tryhala-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tryhala.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://tryhala.ai/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tryhala.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://tryhala.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://tryhala.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryhala.ai/
- group: auth
  href: https://artifacts.apis.io/tryhala/security/tryhala-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tryhala-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tryhala.ai/
coverage:
  checked: '2026-10-19'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.tryhala.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Hala AI provides an AI voice assistant platform for businesses, offering automated phone calls, WhatsApp, Instagram and website chat handling in Arabic, English, and French. Built in Lebanon, it helps SMEs qualify leads, book appointments, and deliver 24/7 customer support across multiple channels.
image: https://tryhala.ai/og-image.png
layout: provider
modified: '2026-10-19'
name: Hala
nav: Providers
network: true
overview: 'Hala is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Voice Assistant, Payments, and Small Business.


  Hala''s developer surface includes support, pricing, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Tryhala Plans Pricing
  plan_count: 4
  slug: tryhala-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 19.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tryhala/tryhala-2026-11-03T145137.png
security:
- kind: domain-security
  name: Tryhala Domain Security
  slug: tryhala-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tryhala
tags:
- Company
- Artificial Intelligence
- Voice Assistant
- Payments
- Small Business
website: https://tryhala.ai/
---
