---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/countrydelight/llms/countrydelight-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/countrydelight-llms.txt
- group: company
  title: ''
  type: Website
  url: https://countrydelight.in/
- group: company
  title: ''
  type: About
  url: https://countrydelight.in/story
- group: operate
  title: ''
  type: Support
  url: https://countrydelight.in/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://countrydelight.in/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://countrydelight.in/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://countrydelight.in/privacy-policy
- group: other
  href: https://artifacts.apis.io/countrydelight/hosts/countrydelight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/countrydelight-hosts.yml
- group: auth
  href: https://artifacts.apis.io/countrydelight/security/countrydelight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/countrydelight-domain-security.yml
coverage:
  checked: '2026-11-04'
  detail: Country Delight is a consumer D2C dairy/grocery brand; countrydelight.in serves a product site with no developer portal, no API reference, and no machine-readable contract. /graphql, /api and /.well-known/ai-plugin.json all return the same ~70KB SPA HTML shell (catch-all, not real endpoints); developer./docs./developers. subdomains do not resolve.
  evidence:
  - status: 200
    url: https://countrydelight.in/graphql
  - status: 200
    url: https://countrydelight.in/api
  - status: 200
    url: https://countrydelight.in/.well-known/ai-plugin.json
  - status: 0
    url: https://developer.countrydelight.in/
  - status: 0
    url: https://docs.countrydelight.in/
  - status: 200
    url: https://countrydelight.in/robots.txt
  - status: 200
    url: https://countrydelight.in/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Country Delight is an Indian direct-to-consumer subscription grocery brand, owned and operated by Beejapuri Dairy Private Limited, that delivers farm-fresh milk, dairy products (paneer, curd, ghee), fresh fruits and vegetables, pulses, atta and cereals, eggs, bread, oils and other everyday staples to subscribers' doorsteps by 7 AM every morning. Founded in 2015 in Gurugram, Haryana by co-founders Chakradhar Gade and Nitin Kaushal, the service runs entirely through a mobile-app-based subscription model with daily or weekly deliveries across Delhi-NCR, Mumbai, Pune, Bangalore, Chennai, Hyderabad, Chandigarh, Jaipur, Kolkata, Lucknow and other Indian cities. It is a consumer-facing dairy and grocery service — not a developer platform — and publishes no public API, developer portal or machine-readable contract.
image: https://countrydelight.in/assets/img/Logo_instory.png
layout: provider
modified: '2026-11-04'
name: Country Delight
nav: Providers
network: true
overview: 'Country Delight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery Delivery, Dairy, Milk, and Direct to Consumer.


  Country Delight''s developer surface includes support and 8 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Countrydelight Domain Security
  slug: countrydelight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: countrydelight
tags:
- Company
- Grocery Delivery
- Dairy
- Milk
- Direct to Consumer
- Consumer
- Food and Beverage
- Subscription
- India
- Consumer Goods
website: https://countrydelight.in/
---
