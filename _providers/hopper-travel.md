---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 7
apis:
- description: Consumer mobile and web app for booking flights, hotels, homes, and cars. Pioneered price prediction, Price Freeze, and flexible cancellation for end travelers. No public API.
  name: Hopper Consumer App
  slug: consumer-app
- description: Hopper Technology Solutions lodging e-commerce platform that gives partners access to global hotel inventory with conversion-optimized UX and merchandising. Partner-gated; integration via HTS sales.
  name: HTS Stays
  slug: hts-stays
- description: Car rental e-commerce platform from HTS that partners embed for global car rental inventory and booking. Partner-gated.
  name: HTS Cars
  slug: hts-cars
- description: Bundled flight + hotel package product from HTS. Partner-gated.
  name: HTS Packages
  slug: hts-packages
- description: 'Proprietary fintech ancillaries that partners attach to their bookings — Cancel for Any Reason (airlines and hotels), Disruption Assistance for Any Reason, and HTS Seat Upgrades. Marketed as Hopper''s '
  name: HTS Fintech Ancillaries (Cancel for Any Reason, Disruption Assistance, Seat Upgrades)
  slug: hts-fintech-ancillaries
- description: Travel loyalty portals powering bank travel programs, used by partners such as Capital One Travel and RBC. Partner-gated.
  name: HTS Travel Loyalty Portals (Banks)
  slug: hts-loyalty-portals
- description: Agentic AI built specifically for airline and travel customer service, delivering end-to-end autonomous resolutions via voice and chat. Sold to airlines and travel partners; integration is sales-led.
  name: HTS Assist (Agentic AI Customer Service)
  slug: hts-assist
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hopper-travel-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hopper
- group: company
  title: ''
  type: LinkedInHTS
  url: https://www.linkedin.com/company/hts-hopper-technology-solutions
- group: company
  title: ''
  type: Website
  url: https://hopper.com/
- group: company
  title: ''
  type: HTSWebsite
  url: https://hts.hopper.com/
- group: company
  title: ''
  type: News
  url: https://hts.hopper.com/news
- group: company
  title: ''
  type: Newsroom
  url: https://hts.hopper.com/newsroom
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hopper
- group: commercial
  title: ''
  type: Plans
  url: plans/hopper-travel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hopper-travel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hopper-travel-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://hopper.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://hts.hopper.com/newsroom
created: '2026-05-23'
description: Hopper is a travel marketplace and fintech, best known for consumer flight, hotel, car, and homes booking with fintech ancillaries such as Price Freeze, Cancel for Any Reason, and Disruption Assistance for Any Reason. Hopper Technology Solutions (HTS) is the B2B arm that exposes Hopper's e-commerce (Stays, Cars, Packages), fintech ancillaries, loyalty portals, and HTS Assist agentic AI to banks, airlines, and travel providers including Capital One, Air Canada, Virgin Australia, Tripadvisor, Frontier, Wizz Air, and Porter.
finops:
- name: Hopper Travel Finops
  service_category: API
  slug: hopper-travel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hopper-travel.png
layout: provider
modified: '2026-05-23'
name: Hopper
nav: Providers
network: true
overview: 'Hopper publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Marketplace, Fintech, Price Freeze, and Insurance.


  Hopper''s developer surface includes product news, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Hopper Travel Plans Pricing
  plan_count: 1
  slug: hopper-travel-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 2
  name: Hopper Travel Rate Limits
  slug: hopper-travel-rate-limits
score:
  band: emerging
  composite: 16.5
  delta: 0.6
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hopper-travel/refs/heads/main/screenshots/hopper-travel-2026-06-20T182834.png
security:
- kind: domain-security
  name: Hopper Travel Domain Security
  slug: hopper-travel-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hopper-travel
tags:
- Travel
- Marketplace
- Fintech
- Price Freeze
- Insurance
- B2B
- Embedded
- Agentic AI
- Banks
- Airlines
website: https://hopper.com/
---
