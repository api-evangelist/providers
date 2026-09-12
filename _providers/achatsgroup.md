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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: http://achatsgroup.co.kr/
- group: operate
  title: ''
  type: Support
  url: http://achatsgroup.co.kr/default/01/menu02.php
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AchatsGroup
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/achats-group
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/achatsgroup
- group: auth
  title: ''
  type: DomainSecurity
  url: security/achatsgroup-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/achatsgroup-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/achatsgroup-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/achatsgroup-llms.txt
coverage:
  checked: '2026-09-06'
  detail: Achats Group manufactures and sells physical consumer goods — Cellomon sprays, ND247 hangover drinks, Biotreat and BringB — through rented Cafe24 storefronts and a Naver Smart Store, and its own achatsgroup.co.kr is an unedited purchased Cafe24 template still carrying the vendor's demo pages, so there is no product an API could front; every contract-discovery and /.well-known/ path on all four company hosts returned 404, and api./docs./developer. subdomains only appear to exist because the domain answers DNS for every label and serves the same 709-byte homepage on each.
  evidence:
  - status: 404
    url: http://achatsgroup.co.kr/openapi.json
  - status: 404
    url: http://achatsgroup.co.kr/.well-known/agent-card.json
  - status: 200
    url: http://api.achatsgroup.co.kr/
  - status: 404
    url: https://cellomon.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: 'Achats Group (아샤그룹) is a South Korean media-commerce company founded in February 2017 and led by CEO Vivian Eun Young Lee, with offices in Pangyo (Seongnam) and Magok (Seoul). It manufactures and sells everyday consumer goods — sanitizing and deodorizing sprays, foot care, living care, health drinks and cosmetics — under its own brands Cellomon, ND247 / Neverdie, Biotreat and BringB, marketing them through short-form video and social advertising that routes buyers into its own Cafe24 storefronts and a Naver Smart Store. Public records put total funding near USD 6.2 million through a Series B. It is a direct-to-consumer consumer-goods business, not a software vendor: as of 2026-09-06 achatsgroup.co.kr is a Cafe24-hosted brochure site still carrying unedited pages from its purchased template, with no developer portal, no API documentation, no SDK and no machine-readable API contract, and the brand storefronts are hosted Cafe24 malls whose only /api path is Cafe24''s own.'
image: http://achatsgroup.co.kr/default/img/images/logo.png
layout: provider
modified: '2026-09-06'
name: Achats Group
nav: Providers
network: true
overview: 'Achats Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Goods, Media Commerce, E-Commerce, and Direct to Consumer.


  Achats Group''s developer surface includes support and 8 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.0
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 6.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Achatsgroup Domain Security
  slug: achatsgroup-domain-security
  summary_line: no transport/DNS hardening detected
slug: achatsgroup
tags:
- Company
- Consumer Goods
- Media Commerce
- E-Commerce
- Direct to Consumer
- Cosmetics
- Health and Beauty
- Retail
- Cafe24
- South Korea
website: http://achatsgroup.co.kr/
---
