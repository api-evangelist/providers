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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aipingji
coverage:
  checked: '2026-09-14'
  detail: Aipingji's operating domain apin.com is now a for-sale parking page at the Chinese domain broker ename.com.cn — the root returns the "您正在访问的域名可以转让 / This domain is for sale" lander and every deeper path, including /openapi.json, /llms.txt, /robots.txt and /.well-known/agent-card.json, returns 403 — so STEP 0b contract discovery had no live first-party host to run against; aipingji.com, aipinji.com and api.aipingji.com do not resolve, there is no GitHub organization or published npm/PyPI package under any spelling of the name, and the company's app has no recorded update since September 2017.
  evidence:
  - status: 200
    url: http://apin.com/
  - status: 0
    url: https://apin.com/
  - status: 403
    url: http://apin.com/openapi.json
  - status: 403
    url: http://apin.com/llms.txt
  - status: 403
    url: http://apin.com/.well-known/agent-card.json
  - status: 403
    url: http://apin.com/.well-known/security.txt
  - status: 0
    url: https://aipingji.com/
  - status: 0
    url: https://api.aipingji.com/
  - status: 0
    url: http://www.belephtro.com/
  - status: 404
    url: https://api.github.com/orgs/aipingji
  - status: 404
    url: https://registry.npmjs.org/aipingji
  - status: 404
    url: https://pypi.org/pypi/aipingji/json
  - status: 404
    url: https://www.linkedin.com/company/aipingji/
  - status: 200
    url: https://equityzen.com/company/aipingji/
  - status: 200
    url: https://www.cbinsights.com/company/aipinji
  reason: defunct
  state: none
created: '2026-09-14'
description: 'Aipingji (爱拼机, also romanized Apin / Aipinji) was a Hangzhou, China travel-technology startup — legal entity 杭州爱拼机网络科技有限公司, incorporated 7 May 2015 in the Binjiang district — that built a C2B "intelligent group-buying" marketplace for discounted international air tickets. Rather than reselling published fares, it aggregated the unsold seat inventory of roughly a thousand Chinese charter operators (包机商), who buy blocks of seats from airlines in advance, and let consumers form 10-15 person buying groups against a specific date until the group filled and tickets were issued, taking a reported 5% commission from the charter operator. The app served 36 destinations from Hangzhou, Shanghai and Nanjing, and the company raised an angel round (Aug 2015, 天使汇), a tens-of-millions-RMB Series A (Apr 2016, led by 耀途资本 with 光合基金 and others), a ¥120M Series B (Jan 2017, 华映资本 and 弘帆资本) and a Series B+ (Jun 2017, 一村资本, 华映资本, Century Capital, Shenxuan Investment). No first-party surface survives:
  the domain cited as its site, apin.com, is now a parked listing offered for sale at ¥199,999 through the Chinese domain broker ename.com.cn and answers 403 on every path but the sale lander, the mobile app''s last recorded update was September 2017, and there is no developer portal, GitHub organization, published package, or API of any kind.'
layout: provider
modified: '2026-09-16'
name: Aipingji
nav: Providers
network: true
overview: Aipingji is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Air Travel, Airline Tickets, and Charter Flights.
random_paper: 7
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aipingji
tags:
- Company
- Travel
- Air Travel
- Airline Tickets
- Charter Flights
- Online Travel Agency
- Marketplace
- Group Buying
- E-Commerce
- China
- Defunct
---
