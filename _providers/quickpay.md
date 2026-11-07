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
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/quickpay/plans/quickpay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quickpay-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/quickpay/security/quickpay-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/quickpay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/quickpay/well-known/quickpay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/quickpay-security.txt
- group: agent
  href: https://artifacts.apis.io/quickpay/well-known/quickpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quickpay-well-known.yml
- group: other
  href: https://artifacts.apis.io/quickpay/hosts/quickpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quickpay-hosts.yml
- group: other
  href: https://artifacts.apis.io/quickpay/vendors/quickpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quickpay-vendors.yml
- group: auth
  href: https://artifacts.apis.io/quickpay/security/quickpay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/quickpay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/quickpay/security/quickpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quickpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quickpay.net/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.quickpay.net/tech-talk/api/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.quickpay.net/tech-talk/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://quickpay.net/
- group: operate
  title: ''
  type: Support
  url: https://quickpay.net/helpdesk
- group: company
  title: ''
  type: Blog
  url: https://quickpay.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://quickpay.net/prices-eu
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quickpay.net/terms-of-service
created: '2026-10-27'
description: Quickpay is a European payment service provider offering a RESTful API for online merchants to accept a wide range of payment methods, including cards, mobile wallets, and local schemes. It supports multi‑currency processing, recurring payments, and detailed reporting, serving thousands of merchants across the EU. The platform emphasizes security, compliance with PSD2, and easy integration via SDKs and documentation.
layout: provider
modified: '2026-10-27'
name: Quickpay
nav: Providers
network: true
overview: 'Quickpay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Fintech, European, and E-Commerce.


  Quickpay''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Quickpay Plans Pricing
  plan_count: 3
  slug: quickpay-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 35.7
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/quickpay/quickpay-2026-11-03T141834.png
security:
- kind: domain-security
  name: Quickpay Domain Security
  slug: quickpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Quickpay Vulnerability Disclosure
  slug: quickpay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: quickpay
tags:
- Payments
- Fintech
- European
- E-Commerce
website: https://quickpay.net/
---
