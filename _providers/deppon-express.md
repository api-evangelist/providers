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
api_count: 1
apis:
- description: 'The Deppon Open Platform (德邦开放平台) is Deppon''s enterprise integration hub, exposing logistics system-integration APIs to contracted partners: order service (下单/订单) interfaces, standard track/tracking ('
  name: Deppon Open Platform
  slug: deppon-open-platform
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deppon-express-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deppon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dpopen.deppon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dpopen.deppon.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deppon-express-llms.txt
created: '2026-07-17'
description: Deppon Express (德邦快递), operated by Deppon Logistics Co., Ltd., is a major Chinese express delivery and logistics provider specializing in large-parcel (heavy/bulky) express, less-than-truckload freight, full-truckload, air freight, warehousing, supply chain, and cross-border services. Founded from Cui's Freight Company (1996) and incorporated in 2009, it became part of the JD Logistics group in 2022 and ranks among China's largest express carriers by market share. For developers and enterprise partners, Deppon runs the Deppon Open Platform (德邦开放平台, established 2015) at dpopen.deppon.com, offering system-integration APIs for order creation, standard track/tracking queries, and electronic waybill (面单) printing, with access granted to contracted monthly-settlement customers.
image: https://www.deppon.com/cms/console/sites/favicon.ico
layout: provider
modified: '2026-07-18'
name: Deppon Express
nav: Providers
network: true
overview: 'Deppon Express publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Logistics, Express Delivery, and Shipping.


  Deppon Express'' developer surface includes documentation and 4 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deppon-express/refs/heads/main/screenshots/deppon-express-2026-07-25T211747.png
security:
- kind: domain-security
  name: Deppon Express Domain Security
  slug: deppon-express-domain-security
  summary_line: TLSv1.3
slug: deppon-express
tags:
- Company
- Consumer
- Logistics
- Express Delivery
- Shipping
- Freight
- Supply Chain
- Tracking
- E-Commerce
- China
website: https://www.deppon.com/
---
