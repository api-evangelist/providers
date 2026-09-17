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
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-09-16'
api_count: 0
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aijia-home-furnishing-products/refs/heads/main/security/aijia-home-furnishing-products-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aijia-home-furnishing-products-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aijia-home-furnishing-products/refs/heads/main/llms/aijia-home-furnishing-products-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aijia-home-furnishing-products-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.ihomefnt.com/
- group: company
  title: ''
  type: About
  url: https://www.ihomefnt.com/aboutus/
- group: other
  title: ''
  type: X-MobileSite
  url: https://m.ihomefnt.com/allhome/allhomeindex
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/aijia-home-furnishing-products-stock
coverage:
  checked: '2026-09-14'
  detail: 艾佳生活 (ihomefnt.com) sells packaged apartment fit-outs to Chinese consumers through property-developer partnerships and ships only end-user software — a marketing site, a mobile site, a consumer app and a login-only merchant console (艾佳生活商户服务平台) — with no developer portal, no API reference, no SDK and no published contract anywhere; open./developer./docs.ihomefnt.com do not resolve, there is no GitHub organization, and every /.well-known/ path and /llms.txt on both public hosts returns 404 — the one machine-readable description reachable at all is a framework default on its app back-end host, which describes an internal system on a robots-disallowed host and is therefore not treated here as a published contract (see review.yml).
  evidence:
  - status: 200
    url: https://www.ihomefnt.com/
  - status: 404
    url: https://www.ihomefnt.com/openapi.json
  - status: 404
    url: https://www.ihomefnt.com/llms.txt
  - status: 404
    url: https://www.ihomefnt.com/.well-known/agent-card.json
  - status: 404
    url: https://m.ihomefnt.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/ihomefnt
  reason: no-developer-program
  state: none
created: '2026-09-14'
description: Aijia Home Furnishing Products (艾佳生活, operated by 江苏艾佳家居用品有限公司 / Jiangsu Aijia Home Furnishing Products Co., Ltd.) is a Nanjing-based Chinese internet home-furnishing and home-improvement platform, founded in 2015 as a joint venture of Jiangsu Yide Group and Central China (Jianye) Group. It sells a one-stop packaged fit-out for newly delivered apartments — design, hard decoration, soft furnishing, construction, acceptance, delivery and after-sales — plus its 全品家 furniture suites, distributed through property-developer partnerships across 25 Chinese provinces and 500-plus residential projects. It raised a RMB 1 billion Series B led by Tiantu Capital in 2018 at a valuation above USD 1 billion and launched Dramatic Reality (DR), an AI design platform, in 2019. Its public surface is a Chinese-language consumer website, a mobile site, a consumer app and a login-only merchant console; it publishes no developer portal, no API reference and no machine-readable API contract.
image: https://m.ihomefnt.com/public/img/index/icon_LOGO.png
layout: provider
modified: '2026-09-14'
name: Aijia Home Furnishing Products
nav: Providers
network: true
overview: Aijia Home Furnishing Products is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Furnishings, Furniture, Interior Design, and Home Improvement.
plans:
- name: Aijia Home Furnishing Products Plans Pricing
  plan_count: 0
  slug: aijia-home-furnishing-products-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Aijia Home Furnishing Products Rate Limits
  slug: aijia-home-furnishing-products-rate-limits
score:
  band: minimal
  composite: 5.7
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 5.7
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aijia Home Furnishing Products Domain Security
  slug: aijia-home-furnishing-products-domain-security
  summary_line: TLSv1.3
slug: aijia-home-furnishing-products
tags:
- Company
- Home Furnishings
- Furniture
- Interior Design
- Home Improvement
- E-Commerce
- Consumer
- Real-Estate
- China
website: https://www.ihomefnt.com/
---
