---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 7.9
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The regionally partitioned HTTP API behind the HungryPanda merchant back office (merchant.hungrypanda.co) and the POS/middleware partner integrations. It carries merchant onboarding and authentication
  name: HungryPanda Merchant & Partner API
  slug: merchant-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hungrypanda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hungrypanda.co/
- group: start
  title: ''
  type: SignUp
  url: https://www.hungrypanda.co/merchants/
- group: operate
  title: ''
  type: Support
  url: https://www.hungrypanda.co/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hungrypanda.co/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fast-leaflet-uk.hungrypanda.co/articleRule?appTypeId=1
- group: company
  title: ''
  type: Blog
  url: https://www.hungrypanda.co/news-center/
- group: auth
  title: ''
  type: Security
  url: https://hpsrc.hungrypanda.co/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hungrypanda-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/hungrypanda-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/hungrypanda-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/hungrypanda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hungrypanda-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: HungryPanda runs a real regionally partitioned merchant/partner ordering API — its own merchant back-office bundle names api-{uk,usa,eur,ca,aus,nzd,jp,kr,sg}-f2e.hungrypanda.co and matching regional gateways — but the only route to it is the merchant application form at hungrypanda.co/merchants/, and every anonymous call to the live API host answers HTTP 200 with {"code":40001} while no host on the estate serves an OpenAPI, GraphQL SDL, WSDL, .proto or any /.well-known/ document.
  evidence:
  - status: 200
    url: https://api-uk-f2e.hungrypanda.co/api/merchant/getCaptchagImage
  - status: 200
    url: https://api-uk-f2e.hungrypanda.co/openapi.json
  - status: 404
    url: https://uk-gateway.hungrypanda.co/v3/api-docs
  - status: 404
    url: https://www.hungrypanda.co/openapi.json
  - status: 200
    url: https://www.hungrypanda.co/merchants/
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: HungryPanda (熊猫外卖) is the largest Asian food delivery platform serving overseas Chinese communities, founded in Nottingham, UK in 2017 and headquartered in London. It operates a marketplace app, a rider delivery network, the Panda Fresh Asian grocery e-commerce platform and the VouchersPanda lifestyle-deals platform across more than 80 cities in ten countries (UK, France, Italy, USA, Canada, Australia, New Zealand, Japan, South Korea and Singapore). Its API surface is a regionally partitioned merchant/partner ordering platform used by POS and middleware integrators — Deliverect, Otter, Neopos, Hubster, Menusifu, Easy Cloud and Redcat — to inject HungryPanda orders into a restaurant point of sale, push order-status updates back, and sync menus. Integration credentials (App Key, Secret Key, ShopID) are issued by HungryPanda on a partner basis; there is no public developer portal, no published specification and no self-service sign-up.
image: https://www.hungrypanda.co/assets/images/logo-400.png
layout: provider
modified: '2026-08-22'
name: HungryPanda
nav: Providers
network: true
overview: 'HungryPanda publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Delivery, Delivery, Marketplace, and Restaurant.


  HungryPanda''s developer surface includes signup flow, support, engineering blog, and 10 more developer resources.'
plans:
- name: Hungrypanda Plans Pricing
  plan_count: 0
  slug: hungrypanda-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Hungrypanda Rate Limits
  slug: hungrypanda-rate-limits
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 34.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hungrypanda/refs/heads/main/screenshots/hungrypanda-2026-09-02T145757.png
security:
- kind: authentication
  name: Hungrypanda Authentication
  slug: hungrypanda-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hungrypanda Domain Security
  slug: hungrypanda-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hungrypanda Vulnerability Disclosure
  slug: hungrypanda-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: hungrypanda
tags:
- Company
- Food Delivery
- Delivery
- Marketplace
- Restaurant
- Grocery
- Logistics
- E-Commerce
- Merchants
- Point-of-Sale
website: https://www.hungrypanda.co/
---
