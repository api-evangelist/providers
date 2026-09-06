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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aak.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aak.com/about-AAK/data-privacy-information/
- group: company
  title: ''
  type: Blog
  url: https://www.aak.com/news-and-media/news/
coverage:
  checked: '2026-09-05'
  detail: AAK AB manufactures plant-based oils and fats for food and industrial customers and sells a physical ingredient through a co-development sales model, so there is nothing to expose programmatically — aak.com carries no developer, API or integration section anywhere in its navigation, every named /.well-known/ and contract path returns 404 on both aak.com and www.aak.com, api/developer/developers/docs/portal/my hostnames are all NXDOMAIN, and no GitHub organization for the company exists.
  evidence:
  - status: 200
    url: https://www.aak.com/
  - status: 404
    url: https://www.aak.com/.well-known/security.txt
  - status: 404
    url: https://www.aak.com/openapi.json
  - status: 404
    url: https://www.aak.com/.well-known/agent-card.json
  - status: 404
    url: https://www.aak.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'AAK AB is a Swedish producer of value-adding plant-based oils and fats, headquartered in Malmö and listed on Nasdaq Stockholm (ticker AAK) in the Food & Beverage large-cap segment. It was formed in 2005 through the merger of Denmark''s Aarhus United and Sweden''s Karlshamns AB, and describes more than 150 years of combined experience in specialty vegetable oils. The company employs roughly 4,000 people across 19 production facilities, 25 regional sales offices and 16 Customer Innovation Centers, and works through a co-development model with customers in chocolate and confectionery, bakery, dairy and ice cream, plant-based foods, special nutrition, foodservice and retail, personal care, animal nutrition, candles and technical products such as fatty acids and glycerine. Its product is a physical industrial ingredient, not software: no developer program, public API, SDK, developer portal, machine-readable contract or GitHub organization could be found, and no api/developer/docs/portal
  hostname resolves under aak.com.'
image: https://www.aak.com/globalassets/adobestock_463258443_web.jpg
layout: provider
modified: '2026-09-05'
name: AAK
nav: Providers
network: true
overview: 'AAK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Ingredients, Vegetable Oils, and Fats.


  AAK''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Aak Domain Security
  slug: aak-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aak
tags:
- Company
- Food and Beverage
- Ingredients
- Vegetable Oils
- Fats
- Manufacturing
- Chemicals
- Consumer Goods
- Agriculture
- Sweden
website: https://www.aak.com/
---
