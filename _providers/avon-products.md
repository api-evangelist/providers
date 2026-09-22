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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.avonworldwide.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/avon/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avon-products/refs/heads/main/security/avon-products-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avon-products-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avon-products/refs/heads/main/plans/avon-products-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avon-products-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avon-products/refs/heads/main/rate-limits/avon-products-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/avon-products-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avon-products/refs/heads/main/llms/avon-products-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avon-products-llms.txt
coverage:
  checked: '2026-09-18'
  detail: Avon Products is a direct-selling beauty manufacturer whose corporate site avonworldwide.com has no developer, API or docs page; its old corporate domain avon-products.com is a GoDaddy for-sale parking page and developer.avon.com no longer resolves, while the only Avon-branded contract found — a Springfox Swagger at api.avon.com — is served by The Avon Company (Avon North America, LG H&H until Regent's September 2026 purchase), a separate company since 2016, and so is not this provider's.
  evidence:
  - status: 307
    url: https://www.avon-products.com/lander
  - status: 403
    url: https://www.avonworldwide.com/
  - status: 200
    url: https://api.avon.com/swagger-resources
  - status: 404
    url: https://www.linkedin.com/company/avon-products/
  reason: not-a-software-company
  state: none
created: '2026-01-01'
description: Avon Products is a global manufacturer and marketer of beauty and related products, primarily distributed through a network of independent sales representatives. Founded in 1886 and headquartered in Northampton, UK as Avon International, it was owned by Natura &Co from 2020 until Regent acquired it in January 2026; its corporate site is avonworldwide.com. The North American business (avon.com) was separated in 2016 and has been run as a distinct company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/avon-products.png
layout: provider
modified: '2026-09-18'
name: Avon Products
nav: Providers
network: true
overview: Avon Products is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Beauty, E-Commerce, Retail, and Direct Sales.
plans:
- name: Avon Products Plans Pricing
  plan_count: 0
  slug: avon-products-plans-pricing
press:
- date: ''
  title: Avon Sells Guangzhou Manufacturing Site to LG
  url: https://www.cosmeticsandtoiletries.com/news/companies/news/21842509/avon-sells-guangzhou-manufacturing-site-to-lg
- date: ''
  title: Avon to bring AI into supply chain
  url: https://cosmeticsbusiness.com/avon-to-bring-ai-into-supply-chain
- date: ''
  title: Avon Products, Inc. Takes Steps to Address Debt and ...
  url: https://www.prnewswire.com/news-releases/avon-products-inc-takes-steps-to-address-debt-and-legacy-liabilities-in-us-court-process-302220491.html
- date: ''
  title: Avon's algorithm-powered app delivers personalized ...
  url: https://www.marketingdive.com/news/avons-algorithm-powered-app-delivers-personalized-makeup-tips/540925/
- date: ''
  title: Avon announces partnership to deliver global training ...
  url: https://www.newswire.ca/news-releases/avon-announces-partnership-to-deliver-global-training-platform-for-independent-sales-representatives-897384276.html
random_paper: 1
rate_limits:
- limit_count: 0
  name: Avon Products Rate Limits
  slug: avon-products-rate-limits
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/avon-products/refs/heads/main/screenshots/avon-products-2026-07-25T202009.png
security:
- kind: domain-security
  name: Avon Products Domain Security
  slug: avon-products-domain-security
  summary_line: TLSv1.3
slug: avon-products
tags:
- Fortune 500
- Beauty
- E-Commerce
- Retail
- Direct Sales
- Consumer Goods
website: https://www.avonworldwide.com
---
