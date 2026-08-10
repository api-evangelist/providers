---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: Real-time freight and shipment visibility. Lets a shipper, broker, or 3PL create, update, monitor, and stop tracking sessions on loads directly from a TMS or ERP and receive location, order-status, tr
  name: Descartes MacroPoint Visibility API
  slug: descartes-macropoint-visibility-api
- description: Intelligent carrier sourcing and capacity matching. An Import API pushes available-capacity and load data into MacroPoint Capacity, and an Export API returns carrier matches back into the customer's s
  name: Descartes MacroPoint Capacity Integration API
  slug: descartes-macropoint-capacity-api
- description: Carrier-facing integration for the MacroPoint Visibility network. Lets carriers and telematics/ELD providers supply location updates as lat/long coordinate sets or addresses, plus load event updates (
  name: Descartes MacroPoint Carrier Integration API
  slug: descartes-macropoint-carrier-api
- description: Trade content and classification for customs and regulatory compliance. Delivers Harmonized System (HS) codes and product classification, current tariff and duty rates and preferential-tariff details,
  name: Descartes CustomsInfo Trade Content API
  slug: descartes-customsinfo-trade-content-api
- description: Programmatic access to Descartes Datamyne's global import/export trade data - bill-of-lading and customs records, trade flows, and company/commodity intelligence - for embedding market and supply chai
  name: Descartes Datamyne Global Trade Data API
  slug: descartes-datamyne-trade-data-api
- description: Real-time B2B connectivity over the Descartes Global Logistics Network, complementing traditional EDI. Provides synchronous request/response integrations for marketplace connectivity (exchanging listi
  name: Descartes B2B API Connectivity
  slug: descartes-b2b-api-connectivity
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/descartes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.descartes.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.descartes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.macropoint.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/descartes-systems-group
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/macropoint-telematics
- group: commercial
  title: ''
  type: Plans
  url: plans/descartes-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/descartes-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/descartes-finops.yml
created: '2026-07-05'
description: 'The Descartes Systems Group is a global logistics and supply chain software company whose cloud-based Global Logistics Network connects manufacturers, distributors, carriers, brokers, and freight forwarders. Descartes delivers its capabilities across a large family of products - real-time freight visibility and carrier sourcing (Descartes MacroPoint), customs and regulatory compliance and trade content (Descartes CustomsInfo, NetCHB), global trade intelligence (Descartes Datamyne), routing and mobile, and B2B connectivity and messaging. Descartes exposes APIs on a per-product basis: the MacroPoint visibility, capacity, and carrier integration APIs are publicly documented (customer credentials required), while trade content, trade data, and B2B connectivity APIs are provisioned through the Descartes API portal or a sales/contract engagement. Most API access is customer/partner-gated rather than open self-service signup.'
finops:
- name: Descartes Finops
  service_category: Logistics and Supply Chain Software
  slug: descartes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/descartes.png
layout: provider
modified: '2026-07-05'
name: Descartes Systems Group
nav: Providers
network: true
overview: 'Descartes Systems Group publishes 1 API on the [APIs.io](https://apis.io/) network: Descartes MacroPoint Carrier Integration API. Tagged areas include Logistics, Supply Chain, Freight Visibility, Shipment Tracking, and Customs Compliance.


  Descartes Systems Group''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Descartes Plans Pricing
  plan_count: 4
  slug: descartes-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 4
  name: Descartes Rate Limits
  slug: descartes-rate-limits
score:
  band: emerging
  composite: 22.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 22.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/descartes/refs/heads/main/screenshots/descartes-2026-07-25T211743.png
security:
- kind: domain-security
  name: Descartes Domain Security
  slug: descartes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: descartes
tags:
- Logistics
- Supply Chain
- Freight Visibility
- Shipment Tracking
- Customs Compliance
- Global Trade
- Trade Content
- Carrier Sourcing
website: https://www.descartes.com
---
