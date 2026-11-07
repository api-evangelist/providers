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
  href: https://artifacts.apis.io/microacquire-com/plans/microacquire-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microacquire-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/microacquire-com/hosts/microacquire-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microacquire-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/microacquire-com/vendors/microacquire-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microacquire-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicroAcquire
- group: auth
  href: https://artifacts.apis.io/microacquire-com/security/microacquire-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microacquire-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://microacquire.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.acquire.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.acquire.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://acquire.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://acquire.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://acquire.com/privacy/
- group: start
  title: ''
  type: SignUp
  url: https://app.acquire.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.acquire.com/
coverage:
  checked: '2026-10-25'
  detail: Acquire.com provides a JavaScript‑rendered help site with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://acquire.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Acquire.com, formerly MicroAcquire, operates the world’s largest marketplace for buying and selling profitable online businesses. Founded to simplify micro‑acquisitions, it has expanded to serve SaaS, e‑commerce, and other digital assets, facilitating over $2 billion in deal volume and supporting a community of 500k+ entrepreneurs and buyers.
layout: provider
modified: '2026-10-25'
name: Acquire.com (fka MicroAcquire)
nav: Providers
network: true
overview: 'Acquire.com (fka MicroAcquire) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Software-as-a-Service, E-Commerce, and Entrepreneurship.


  Acquire.com (fka MicroAcquire)''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: Microacquire Com Plans Pricing
  plan_count: 2
  slug: microacquire-com-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 2.6
  previous_composite: 21.4
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/microacquire-com/microacquire-com-2026-11-03T135549.png
security:
- kind: domain-security
  name: Microacquire Com Domain Security
  slug: microacquire-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microacquire-com
tags:
- Company
- Marketplace
- Software-as-a-Service
- E-Commerce
- Entrepreneurship
website: https://microacquire.com
---
