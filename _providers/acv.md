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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.acvauctions.com/
- group: company
  title: ''
  type: About
  url: https://www.acvauctions.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.acvauctions.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/acv-auctions
- group: commercial
  title: ''
  type: Pricing
  url: https://www.acvauctions.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.acvauctions.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.acvauctions.com/support
- group: company
  title: ''
  type: Careers
  url: https://www.acvauctions.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.acvauctions.com/contact-us
- group: start
  title: ''
  type: Login
  url: https://app.acvauctions.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.acvauctions.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.acvauctions.com/legal/privacy-policy
created: '2026-07-17'
description: 'ACV Auctions (NASDAQ: ACVA) operates the nation''s largest online wholesale marketplace and daily auto auction platform, connecting franchise and independent dealers to buy and sell used vehicles. Founded in 2014 and headquartered in Buffalo, New York, ACV pairs a mobile-first bidding app with third-party vehicle inspections and condition reports, real-time market data (ACV MAX and market insights), transportation logistics, and dealer floor-plan financing through ACV Capital. This is a company profile in the API Evangelist network; ACV does not publish a public developer API surface.'
image: https://cdn.prod.website-files.com/61df0075e6ac6a4373114030/6214df2c7223d937aad401a3_Open%20Graph%20Image.jpg
layout: provider
modified: '2026-07-18'
name: ACV
nav: Providers
network: true
overview: 'ACV is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Automotive, Marketplace, and Auctions.


  ACV''s developer surface includes engineering blog, pricing, support, and 10 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 3
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 14.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acv/refs/heads/main/screenshots/acv-2026-07-25T181540.png
security:
- kind: domain-security
  name: Acv Domain Security
  slug: acv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acv
tags:
- Company
- Commerce
- Automotive
- Marketplace
- Auctions
- Wholesale
- Used Vehicles
website: https://www.acvauctions.com/
---
