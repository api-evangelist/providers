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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Billforward subscription management and billing API
  name: Billforward API
  slug: billforward-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/billforward/plans/billforward-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/billforward-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/billforward/hosts/billforward-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billforward-hosts.yml
- group: other
  href: https://artifacts.apis.io/billforward/vendors/billforward-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billforward-vendors.yml
- group: build
  href: https://artifacts.apis.io/billforward/packages/billforward-packages.yml
  title: ''
  type: SDKs
  url: packages/billforward-packages.yml
- group: build
  href: https://artifacts.apis.io/billforward/packages/billforward-packages.yml
  title: ''
  type: Packages
  url: packages/billforward-packages.yml
- group: auth
  href: https://artifacts.apis.io/billforward/security/billforward-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billforward-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billforward.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billforward.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.billforward.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.billforward.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.billforward.io/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.billforward.io/contact-us
coverage:
  checked: '2026-10-29'
  detail: Documentation site docs.billforward.net returns HTTP 503 and appears to be a JS‑rendered portal, preventing machine‑readable contract discovery.
  evidence:
  - status: 503
    url: https://docs.billforward.net/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Billforward provides a comprehensive subscription management and recurring billing platform, offering features such as subscription lifecycle management, usage‑based billing, invoicing, dunning, and integrations with major payment gateways and ERP systems. It targets SaaS, IoT, and digital services companies seeking to automate revenue operations, with a developer‑first API that supports headless commerce and extensive analytics.
layout: provider
modified: '2026-10-29'
name: Billforward
nav: Providers
network: true
overview: 'Billforward is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Subscription, Billing, Software-as-a-Service, Payments, and Company.


  Billforward''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Billforward Plans Pricing
  plan_count: 12
  slug: billforward-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 15.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 19.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 7.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/billforward/billforward-2026-11-03T121727.png
security:
- kind: domain-security
  name: Billforward Domain Security
  slug: billforward-domain-security
  summary_line: TLSv1.3 · HSTS
slug: billforward
tags:
- Subscription
- Billing
- Software-as-a-Service
- Payments
- Company
website: https://www.billforward.io
---
