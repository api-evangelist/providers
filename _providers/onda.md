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
  url: security/onda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drinkonda.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/drinkonda
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/drinkonda/
coverage:
  checked: '2026-08-26'
  detail: Onda sells canned sparkling tequila in 12 oz cans through grocery and liquor retail; its only owned web property, drinkonda.com, is a Shopify storefront that returned HTTP 404 "This store is unavailable" on every path probed, with no api/developer/docs subdomain resolving in DNS.
  evidence:
  - status: 404
    url: https://drinkonda.com/
  - status: 200
    url: https://drinkonda.com/llms.txt
  - status: 200
    url: https://drinkonda.com/robots.txt
  - status: 404
    url: https://drinkonda.com/.well-known/agent-card.json
  - status: 404
    url: https://drinkonda.com/openapi.json
  - status: 0
    url: https://api.drinkonda.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Onda is a ready-to-drink spirits brand that makes canned sparkling tequila — blanco tequila from a woman-owned distillery in Jalisco, Mexico, blended with sparkling water and real fruit juice and sold in 12 oz cans at 5% ABV, 100 calories, zero sugar and naturally gluten free, in lime, blood orange, watermelon and grapefruit. The company was founded in 2019 and launched publicly in July 2020 by Noah Gray (CEO), Max Dworin (COO), Kelli Adams (CCO) and actor-producer Shay Mitchell (Chief Brand Officer). It raised a $5M Series A in 2021 and a $12.5M growth round in 2022 from existing investors including Aria Growth Partners and 25madison, and sells through national grocery, liquor retail and third-party beverage e-commerce alongside its own direct-to-consumer store. NO PUBLIC API SURFACE: Onda is a consumer packaged goods company, not a software vendor — there is no developer program, no API documentation, no SDK and no machine-readable contract of any kind. Its only owned web
  property, drinkonda.com, is a Shopify storefront that on 2026-08-26 returned HTTP 404 "This store is unavailable" on every path probed, with a robots.txt that disallows all crawling and a Shopify-generated /llms.txt that states agent interaction is not possible; the last archived working capture of the storefront is 2026-02-18. Onda appears in the API Evangelist network because it trades on the private secondary market (EquityZen, Nasdaq Private Market), not because it publishes an API.'
layout: provider
modified: '2026-08-26'
name: Onda
nav: Providers
network: true
overview: Onda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consumer Packaged Goods, Beverages, Alcohol, Ready-to-Drink, and Tequila.
random_paper: 19
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Onda Domain Security
  slug: onda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: onda
tags:
- Consumer Packaged Goods
- Beverages
- Alcohol
- Ready-to-Drink
- Tequila
- Direct to Consumer
- E-Commerce
- Retail
- Shopify
website: https://drinkonda.com/
---
