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
- description: Unified WhatsApp API providing REST endpoints for messaging, chats, groups, and channels.
  name: WaAPI
  slug: waapi
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/waapi-app/plans/waapi-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/waapi-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/waapi-app/well-known/waapi-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/waapi-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/waapi-app/hosts/waapi-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/waapi-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/waapi-app/vendors/waapi-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/waapi-app-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://waapi.app/status
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@waapiapp/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://waapi.app/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://waapi.app/login
- group: company
  title: ''
  type: Blog
  url: https://waapi.app/blog
- group: docs
  title: ''
  type: APIReference
  url: https://waapi.readme.io/reference/waapi-api-documentation
- group: auth
  href: https://artifacts.apis.io/waapi-app/security/waapi-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/waapi-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://waapi.app/
created: '2026-10-31'
description: WaAPI provides a unified WhatsApp API for developers, enabling sending and receiving messages, managing chats, groups, and channels through a single REST interface. It offers a flat-rate pricing model per connected account with unlimited messages and requires no prior approval, simplifying integration for businesses and developers alike.
image: https://waapi.app/og-image.png
layout: provider
modified: '2026-10-31'
name: waapi-app
nav: Providers
network: true
overview: 'waapi-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, WhatsApp, and Communications.


  waapi-app''s developer surface includes engineering blog, API reference, and 10 more developer resources.'
plans:
- name: Waapi App Plans Pricing
  plan_count: 1
  slug: waapi-app-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 20.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Waapi App Domain Security
  slug: waapi-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: waapi-app
tags:
- Company
- Messaging
- WhatsApp
- Communications
website: https://waapi.app/
---
