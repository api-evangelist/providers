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
  url: security/perfectstay-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/perfectstay-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.perfectstay.com/
- group: operate
  title: ''
  type: Support
  url: https://www.perfectstay.com/fr-FR/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://res.cloudinary.com/perfectstay/image/upload/v1751049126/cms/files/ox7azn9e/live/370239c6321b04f7fd3bd3e8cebc107ff94e98b3.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://res.cloudinary.com/perfectstay/image/upload/v1699350940/cms/files/ox7azn9e/live/8eca4661317c12e2b0a94d7751625142dc6494e0.pdf
created: '2026-07-17'
description: PerfectStay is a French online travel company that sells curated flight-plus-hotel packages, all-inclusive stays, guided tours, city breaks and standalone flights, hotels, activities and transfers, marketed around a best-price guarantee (refunding twice any price difference), trip protection and 24/7 customer support, with installment payment options (2x/4x). Founded in Paris and backed by Partech, it also powers private, brand-operated travel-club sale sites. The company exposes no public developer platform, API, SDK or documentation surface; this profile captures its public web and security posture within the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perfectstay.png
layout: provider
modified: '2026-07-20'
name: PerfectStay
nav: Providers
network: true
overview: 'PerfectStay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Applicative Saas, Travel, Tourism, and E-Commerce.


  PerfectStay''s developer surface includes support and 5 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perfectstay/refs/heads/main/screenshots/perfectstay-2026-09-02T151051.png
security:
- kind: domain-security
  name: Perfectstay Domain Security
  slug: perfectstay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: perfectstay
tags:
- Company
- Applicative Saas
- Travel
- Tourism
- E-Commerce
- Booking
- Hospitality
- Flights
website: https://www.perfectstay.com/
---
