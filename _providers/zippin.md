---
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: The Zippin Gateway is Zippin's integration/API framework for its checkout-free store platform — the surface retailers and partners use to connect payment gateways, loyalty and gift providers, campus c
  name: Zippin Gateway
  slug: zippin-gateway
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zippin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getzippin.com/
- group: company
  title: ''
  type: About
  url: https://www.getzippin.com/about
- group: operate
  title: ''
  type: Support
  url: https://support.getzippin.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.getzippin.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.getzippin.com/blog/rss.xml
- group: start
  title: ''
  type: Login
  url: https://dashboard.getzippin.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getzippin.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getzippin.com/en/retailer-terms
- group: company
  title: ''
  type: Partners
  url: https://www.getzippin.com/partners
- group: company
  title: ''
  type: Careers
  url: https://www.getzippin.com/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.getzippin.com/whitepapers
- group: company
  title: ''
  type: Newsroom
  url: https://www.getzippin.com/press-and-resources
- group: commercial
  title: ''
  type: Plans
  url: plans/zippin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zippin-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zippin-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zippin-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/zippin-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zippin-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Zippin markets the "Zippin Gateway" API framework but publishes no developer portal, no API reference and no machine-readable contract anywhere; the live host api.getzippin.com answers every path under /v1 — including paths that cannot exist — with an HTTP 401 authentication_error, and the only public description of the API is a single retailer help-center article saying it is "a standard rest API with a nested JSON payload".
  evidence:
  - status: 401
    url: https://api.getzippin.com/v1
  - status: 404
    url: https://api.getzippin.com/openapi.json
  - status: 401
    url: https://api.getzippin.com/v1/zippin-negative-control-7f3ab91c
  - status: 403
    url: https://support.getzippin.com/hc/en-us/articles/14978971623828-Reports-Dashboard-and-API-pulls
  - status: 200
    url: https://support.getzippin.com/api/v2/help_center/en-us/articles/14978971623828.json
  reason: customer-only-docs
  state: gated
created: '2026-09-05'
description: Zippin (vCognition Technologies Inc.) builds a checkout-free, cashierless retail platform that uses computer vision, sensor fusion and machine learning to let shoppers enter a store with an app, credit card or campus credential, take what they want and leave without a checkout line. The company sells store formats including the Zippin Retrofit, Zippin Lane, Zippin Walk-Up, Micromarket Lite and Zippin Outdoors, and operates in stadiums, arenas, airports, hotels, theme parks, college campuses and convenience retail. Its integration surface is the Zippin Gateway, an API framework the company says connects the platform to more than 25 third-party systems — payment gateways, loyalty and gift programs, campus card providers, inventory systems, POS and self-service beverage hardware — alongside a Store Dashboard whose Reports Dashboard data can also be pulled through a REST API with nested JSON payloads. Founded by veterans of Amazon and SRI, Zippin is headquartered in San Francisco.
image: https://www.getzippin.com/hs-fs/hubfs/zippinlogocolor-266x68.png
layout: provider
modified: '2026-09-05'
name: Zippin
nav: Providers
network: true
overview: 'Zippin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Retail Technology, Checkout Free, and Cashierless.


  Zippin''s developer surface includes support, engineering blog, and 17 more developer resources.'
plans:
- name: Zippin Plans Pricing
  plan_count: 0
  slug: zippin-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Zippin Rate Limits
  slug: zippin-rate-limits
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Zippin Domain Security
  slug: zippin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zippin
tags:
- Company
- Retail
- Retail Technology
- Checkout Free
- Cashierless
- Computer Vision
- Artificial Intelligence
- Machine Learning
- Point of Sale
- Payments
- Loyalty
- Inventory
- Sports Venues
- Airports
- Higher Education
website: https://www.getzippin.com/
---
