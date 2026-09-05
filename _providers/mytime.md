---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mytime-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mytime-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mytime.com/
- group: company
  title: ''
  type: Website
  url: https://get.mytime.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://get.mytime.com/pricing/pricing-packages/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://get.mytime.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://get.mytime.com/terms/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://get.mytime.com/resource-center/blog/
- group: operate
  title: ''
  type: Support
  url: https://mytime.freshdesk.com/support/home
- group: start
  title: ''
  type: Login
  url: https://www.mytime.com/users/sign_in
created: '2026-07-17'
description: MyTime is an all-in-one business management platform for retail service chains and franchises, combining point-of-sale (POS), online appointment scheduling, integrated payments, customer management, inventory, staff and payroll tools, loyalty, reputation management, and marketing automation across single- and multi-location operations. It serves beauty salons, barbershops, pet grooming, wellness spas, and learning services, offering omnichannel booking (web, Google Reserve, Instagram/Facebook, ClassPass) and analytics. MyTime runs a first-party API host (api.mytime.com) that backs its web and native iPhone/Android apps, and offers partner integrations (Stripe, QuickBooks, Shopify, ADP, Zapier), but does not publish a public developer API portal or OpenAPI definition. Backed by 500 Global.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mytime.png
layout: provider
modified: '2026-07-20'
name: MyTime
nav: Providers
network: true
overview: 'MyTime is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scheduling, Appointments, Booking, and Point-of-Sale.


  MyTime''s developer surface includes pricing, engineering blog, support, and 7 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 14.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mytime/refs/heads/main/screenshots/mytime-2026-08-07T184548.png
security:
- kind: domain-security
  name: Mytime Domain Security
  slug: mytime-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mytime
tags:
- Company
- Scheduling
- Appointments
- Booking
- Point-of-Sale
- Payments
- Retail
- Franchise
- Business Management
- Salon Software
website: https://get.mytime.com/
---
