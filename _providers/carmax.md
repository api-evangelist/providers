---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: The CarMax Store Locations API, discussed publicly on the CarMax Engineering Blog, exposes details about all CarMax store locations including addresses, hours, services offered, and geographic metadat
  name: CarMax Store Locations API
  slug: store-locations-api
- description: 'The CarMax Vehicle Inventory API exposes details about all used vehicles currently in CarMax''s nationwide inventory, including year/make/model, trim, mileage, price, exterior and interior attributes, '
  name: CarMax Vehicle Inventory API
  slug: vehicle-inventory-api
- description: The CarMax Vehicle Search Server-Driven UI API controls the search filters and list layouts presented across carmax.com and CarMax's mobile apps. It was rewritten approximately three years prior to Ma
  name: CarMax Vehicle Search Server-Driven UI API
  slug: vehicle-search-sdui-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carmax-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CarMax
- group: company
  title: ''
  type: Website
  url: https://www.carmax.com/
- group: other
  title: ''
  type: Stores
  url: https://www.carmax.com/stores
- group: other
  title: ''
  type: Cars
  url: https://www.carmax.com/cars
- group: other
  title: ''
  type: Finance
  url: https://www.carmax.com/finance
- group: other
  title: ''
  type: Sell Your Car
  url: https://www.carmax.com/sell-my-car
- group: company
  title: ''
  type: Engineering Blog
  url: https://medium.com/carmax-engineering-blog
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/carmax-engineering-blog
- group: company
  title: ''
  type: Careers
  url: https://jobs.carmax.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.carmax.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.carmax.com/customer-service
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carmax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carmax.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carmax
- group: other
  title: ''
  type: X
  url: https://x.com/CarMax
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CarMax
created: '2026-03-21'
description: 'CarMax (NYSE: KMX) is the largest retailer of used cars in the United States, operating an omnichannel business that spans brick-and-mortar stores, carmax.com online purchasing, home delivery, financing, appraisals, and trade-ins. CarMax does not publish a public developer portal, but its engineering organization operates an extensive internal API program built around distinct API roles (Data Access Layer, Business Logic Layer, Server-Driven UI, Backend for Frontend). Public-facing APIs documented by the CarMax Engineering Blog include a Store Locations API and a Vehicle Inventory API, and CarMax has publicly discussed a Server-Driven UI API that controls vehicle search filters across web and mobile. Partner and syndication integrations are handled case by case rather than through a self-service portal.'
finops:
- name: Carmax Finops
  service_category: Auto Retail / Vehicle Inventory
  slug: carmax-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carmax.png
layout: provider
modified: '2026-04-23'
name: CarMax
nav: Providers
network: true
overview: 'CarMax publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Financing, Auto Retail, Appraisals, Automotive, and Omnichannel.


  CarMax''s developer surface includes engineering blog and 16 more developer resources.'
plans:
- name: Carmax Plans Pricing
  plan_count: 1
  slug: carmax-plans-pricing
press:
- date: '2026-05-25'
  title: CarMax Partners with AI Technology Company UVeye ...
  url: https://media.carmax.com/press-releases/news-release/2023/CarMax-Partners-with-AI-Technology-Company-UVeye-on-Vehicle-Assessment-Technology-for-Wholesale-Vehicles/default.aspx
- date: '2026-05-25'
  title: CarMax Launches First-of-Its-Kind Car Shopping and ...
  url: https://media.carmax.com/press-releases/news-release/2026/CarMax-Launches-First-of-Its-Kind-Car-Shopping-and-Selling-Experience-in-ChatGPT-App-Store/default.aspx
- date: '2026-05-25'
  title: CarMax Launches AI-Powered Used Vehicle Shopping App
  url: https://www.linkedin.com/posts/autofinancenews_carmaxlauncheschatgpt-apptoenable-nationwide-activity-7435824109525204993-An4v
- date: '2026-05-25'
  title: CarMax aims to up its customer experience under new CEO
  url: https://www.constellationr.com/insights/news/carmax-aims-its-customer-experience-under-new-ceo
- date: '2026-05-25'
  title: CarMax Partners with UVeye to Automate Inspections at ...
  url: https://uveye.com/carmax-partners-with-uveye/
random_paper: 66
rate_limits:
- limit_count: 1
  name: Carmax Rate Limits
  slug: carmax-rate-limits
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carmax/refs/heads/main/screenshots/carmax-2026-06-20T174010.png
security:
- kind: domain-security
  name: Carmax Domain Security
  slug: carmax-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: carmax
tags:
- Auto Financing
- Auto Retail
- Appraisals
- Automotive
- Omnichannel
- Retail
- Server-Driven UI
- Used Cars
- Vehicle Inventory
- VIN Lookup
- Fortune 500
website: https://www.carmax.com/
---
