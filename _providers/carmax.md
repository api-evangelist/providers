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
  band: agent-aware
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-05'
api_count: 4
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
- description: On 2026-02-27 CarMax became the first U.S. auto retailer with an app in the OpenAI ChatGPT App Store, putting its nationwide inventory of more than 45,000 vehicles and its instant-offer tool inside th
  name: CarMax in ChatGPT
  slug: chatgpt-app
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carmax-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/carmax-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.carmax.com/responsible-disclosure
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/carmax-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carmax-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/carmax-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carmax-llms.txt
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
  url: https://www.carmax.com/car-financing
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
  url: https://careers.carmax.com/
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.carmax.com/
- group: operate
  title: ''
  type: Support
  url: https://www.carmax.com/help-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.carmax.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.carmax.com/privacy-policy
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
mcp_servers:
- description: ''
  name: CarMax in ChatGPT
  slug: carmax-in-chatgpt
modified: '2026-09-05'
name: CarMax
nav: Providers
network: true
overview: 'CarMax publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Auto Financing, Auto Retail, Appraisals, Automotive, and Omnichannel.


  CarMax''s developer surface includes engineering blog, support, and 21 more developer resources.'
plans:
- name: Carmax Plans Pricing
  plan_count: 0
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
random_paper: 6
rate_limits:
- limit_count: 0
  name: Carmax Rate Limits
  slug: carmax-rate-limits
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 16.7
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carmax/refs/heads/main/screenshots/carmax-2026-06-20T174010.png
security:
- kind: domain-security
  name: Carmax Domain Security
  slug: carmax-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Carmax Vulnerability Disclosure
  slug: carmax-vulnerability-disclosure
  summary_line: Hackerone
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
