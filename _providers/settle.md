---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.settle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.settle.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.settle.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.settle.co/sign-up/payers/product
- group: operate
  title: ''
  type: Support
  url: https://help.settle.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.settle.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.settle.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.settle.com/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/settle-domain-security.yml
created: '2026-07-17'
description: Settle is a financial operations platform built for consumer packaged goods (CPG) brands and ecommerce companies, unifying procurement, accounts payable automation, and working capital financing in one back office. Teams create and manage purchase orders, track goods received and true landed costs, collect and approve bills, pay vendors with real-time visibility, and access flexible inventory and growth financing ($20K-$15M) underwritten from payables and purchasing data. Founded in 2019 and backed by Ribbit Capital, Kleiner Perkins, and Founders Fund, Settle has funded more than $3 billion to brands. A developer API covering bill pay, payments, and landed-cost data is in early access via a public waitlist.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/settle.png
layout: provider
modified: '2026-07-21'
name: Settle
nav: Providers
network: true
overview: 'Settle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Accounts Payable, and Procurement.


  Settle''s developer surface includes pricing, signup flow, support, engineering blog, and 5 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/settle/refs/heads/main/screenshots/settle-2026-09-02T155029.png
security:
- kind: domain-security
  name: Settle Domain Security
  slug: settle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: settle
tags:
- Company
- Fintech
- Payments
- Accounts Payable
- Procurement
- Working Capital
- Bill Pay
- CPG
- E-Commerce
- Financing
website: https://www.settle.com
---
