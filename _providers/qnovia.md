---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://qnovia.com/
- group: company
  title: ''
  type: About
  url: https://qnovia.com/about/story
- group: other
  title: ''
  type: Product
  url: https://qnovia.com/product
- group: other
  title: ''
  type: Technology
  url: https://qnovia.com/technology
- group: other
  title: ''
  type: Pipeline
  url: https://qnovia.com/pipeline
- group: other
  title: ''
  type: Team
  url: https://qnovia.com/team
- group: company
  title: ''
  type: News
  url: https://qnovia.com/news
- group: company
  title: ''
  type: Careers
  url: https://qnovia.com/careers
- group: operate
  title: ''
  type: Support
  url: https://qnovia.com/contact
- group: company
  title: ''
  type: Investors
  url: https://qnovia.com/investors
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qnovia.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qnovia.com/privacy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/qnovia_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qnovia-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qnovia-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/qnovia-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qnovia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qnovia-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: 'Qnovia is a clinical-stage drug-device company that does write software — BLE device firmware and the cloud-connected Neblit AI companion app — but ships none of it to third parties: the qnovia.com route table extracted from its own JavaScript bundle has no developer, API or docs route, and the only HTTP API on the host is the private /api/ backend behind its contact and investor-portal forms, which answered 401 "Not authenticated".'
  evidence:
  - status: 401
    url: https://qnovia.com/api/investors/me
  - status: 200
    url: https://qnovia.com/openapi.json
  - status: 200
    url: https://qnovia.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/qnovia
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Qnovia, Inc. is a clinical-stage pharmaceutical and drug-device company developing inhaled therapeutics built on its proprietary RespiRx aseptically pre-filled, portable vibrating-mesh nebulizer platform. Its lead asset, the RespiRx Nicotine Inhaler (QN-01), is a prescription smoking-cessation therapy that cleared FDA IND review and has dosed patients in a U.S. Phase 1 study; a cognitive behavioral therapy (CBT) program is advancing toward a second IND. The device is Bluetooth Low Energy connected and pairs with Neblit AI, a cloud-connected companion app and machine-learning platform that tracks dose events and delivers behavioral interventions, which the company positions as a digital therapeutic layer over the pharmacotherapy. Founded in 2018 as Respira Technologies and rebranded to Qnovia in 2022, the company is led by founder and CEO Mario Danek, operates R&D and manufacturing in Newport Beach/Irvine, California and an R&D facility in Richmond, Virginia, and has raised roughly
  $50 million to date. Qnovia publishes no public API, developer portal, SDK, or machine-readable contract; its corporate site is a client-rendered single-page application whose only HTTP API is a private backend serving its own contact, careers and investor-portal forms.
image: https://qnovia.com/favicon.png
layout: provider
modified: '2026-08-26'
name: Qnovia
nav: Providers
network: true
overview: 'Qnovia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Medical Devices, Drug Delivery, and Digital Health.


  Qnovia''s developer surface includes product news, support, and 16 more developer resources.'
plans:
- name: Qnovia Plans Pricing
  plan_count: 0
  slug: qnovia-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Qnovia Rate Limits
  slug: qnovia-rate-limits
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qnovia/refs/heads/main/screenshots/qnovia-2026-09-02T152531.png
security:
- kind: domain-security
  name: Qnovia Domain Security
  slug: qnovia-domain-security
  summary_line: TLSv1.3 · HSTS
slug: qnovia
tags:
- Company
- Pharmaceuticals
- Medical Devices
- Drug Delivery
- Digital Health
- Digital Therapeutics
- Respiratory
- Smoking Cessation
- Connected Devices
- Clinical Trials
- Artificial Intelligence
- Health
website: https://qnovia.com/
---
