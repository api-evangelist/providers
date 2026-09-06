---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Cabela's offers an online storefront for hunting, fishing, camping, and outdoor gear, along with store locator, customer service, and loyalty program pages. No public developer API is currently docume
  name: Cabela's
  slug: cabelas-website
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cabelas-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cabelas-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.cabelas.com
- group: other
  title: ''
  type: Parent Company
  url: https://www.basspro.com
- group: other
  title: ''
  type: Store Locator
  url: https://stores.cabelas.com
- group: operate
  title: ''
  type: Support
  url: https://help.cabelas.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cabelas.com/shop/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cabelas.com/shop/en/terms-and-conditions
coverage:
  checked: '2026-09-05'
  detail: 'Cabela''s runs a consumer storefront and a Shelf.io-hosted help centre and nothing developer-facing behind them: api., developer., dev., apis., status. and trust.cabelas.com have no DNS records at all, /openapi.json and every /.well-known/ path return genuine app-router 404s on www.cabelas.com, and the provider''s own llms.txt on help.cabelas.com indexes roughly 140 published FAQ articles without a single developer, API or integration topic among them.'
  evidence:
  - status: 404
    url: https://www.cabelas.com/openapi.json
  - status: 404
    url: https://www.cabelas.com/.well-known/agent-card.json
  - status: 404
    url: https://www.cabelas.com/.well-known/api-catalog
  - status: 200
    url: https://help.cabelas.com/llms.txt
  - status: 404
    url: https://stores.cabelas.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-03-23'
description: Cabela's is a specialty retailer of hunting, fishing, camping, and outdoor recreation merchandise, operating retail stores and an e-commerce platform. Cabela's is a subsidiary of Bass Pro Shops following the 2017 acquisition, and continues to operate under its own brand with retail locations and a consumer-facing web storefront.
finops:
- name: Cabelas Finops
  service_category: API
  slug: cabelas-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cabelas.png
layout: provider
modified: '2026-09-05'
name: Cabela's
nav: Providers
network: true
overview: 'Cabela''s publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Retail, Outdoor, Hunting, Fishing, and Camping.


  Cabela''s'' developer surface includes support and 7 more developer resources.'
plans:
- name: Cabelas Plans Pricing
  plan_count: 0
  slug: cabelas-plans-pricing
press:
- date: '2026-05-25'
  title: Bass Pro Shops acquires Cabela's in $5.5-billion transaction
  url: https://www.knopnews2.com/content/news/Bass-Pro-Shops-acquires-Cabelas-395635171.html
- date: '2026-05-25'
  title: Privacy Policy Summary
  url: https://www.cabelas.com/b/privacy-policy-summary
- date: '2026-05-25'
  title: Bass Pro Shops Sells 11 Cabela's Stores for $324.3 Million
  url: https://www.grandviewoutdoors.com/news/bass-pro-shops-sells-11-cabelas-stores-for-324-3-million
- date: '2026-05-25'
  title: Sportsman's Warehouse Acquired by Bass Pro Parent
  url: https://www.mytotalretail.com/article/sportsmans-warehouse-acquired-by-bass-pro-shops-cabelas-parent-company/
- date: '2026-05-25'
  title: B+E Brokers $324 million Cabela's Sale-leaseback ...
  url: https://www.24-7pressrelease.com/press-release/463191/be-brokers-324-million-cabelas-sale-leaseback-through-proprietary-digital-platform
random_paper: 1
rate_limits:
- limit_count: 0
  name: Cabelas Rate Limits
  slug: cabelas-rate-limits
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cabelas/refs/heads/main/screenshots/cabelas-2026-06-20T173836.png
security:
- kind: domain-security
  name: Cabelas Domain Security
  slug: cabelas-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cabelas
tags:
- Retail
- Outdoor
- Hunting
- Fishing
- Camping
- E-Commerce
- Company
- Fortune 1000
website: https://www.cabelas.com
---
