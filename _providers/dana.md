---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dana Agentic Access
  operation_count: 7
  slug: dana-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 5
apis:
- description: Check inventory availability.
  name: Dana Availability API
  slug: dana-availability-api
- description: Place and manage orders.
  name: Dana Orders API
  slug: dana-orders-api
- description: Search and retrieve part information.
  name: Dana Parts API
  slug: dana-parts-api
- description: Retrieve pricing information.
  name: Dana Pricing API
  slug: dana-pricing-api
- description: Track shipments and delivery status.
  name: Dana Shipping API
  slug: dana-shipping-api
artifact_total: 17
collections:
- collection_type: open
  name: Dana Aftermarket API
  slug: open-dana-aftermarket-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dana-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dana-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dana-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dana-incorporated
- group: company
  title: ''
  type: Website
  url: https://www.dana.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.danaaftermarket.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dana-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dana-vocabulary.yml
created: '2026-03-21'
description: Dana Incorporated is a global supplier of fully integrated drivetrain and electrified propulsion systems for passenger vehicles, commercial trucks, and off-highway equipment. Dana operates a developer portal at developer.danaaftermarket.com offering eight APIs for aftermarket parts search, availability, pricing, ordering, and shipment tracking across its global distribution network.
finops:
- name: Dana Finops
  service_category: Automotive Aftermarket
  slug: dana-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dana.png
json_schemas:
- name: Order
  property_count: 5
  slug: order
- name: Part
  property_count: 9
  slug: part
jsonld:
- class_count: 2
  name: Dana Context
  property_count: 13
  slug: dana-context
layout: provider
modified: '2026-05-19'
name: Dana
nav: Providers
network: true
overview: 'Dana publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Orders API, Parts API, and 2 more. Tagged areas include Aftermarket, Auto Parts, Drivetrain, eCommerce, and Supply Chain.


  The Dana catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dana''s developer surface includes authentication, developer portal, and 6 more developer resources.'
plans:
- name: Dana Plans Pricing
  plan_count: 1
  slug: dana-plans-pricing
press:
- date: '2026-05-25'
  title: Dana named inaugural winner of the EY/Microsoft Digital ...
  url: https://www.prnewswire.com/news-releases/dana-named-inaugural-winner-of-the-eymicrosoft-digital-innovation-award-300251296.html
- date: '2026-05-25'
  title: Dana Holding Corp. 'BB' Corporate Credit Rating A
  url: https://www.spglobal.com/ratings/en/regulatory/article/-/view/type/HTML/id/1170016
- date: '2026-05-25'
  title: 'Dana Holding Corporation: Optimizing Products and Processes ...'
  url: https://www.hpcwire.com/aiwire/2011/06/09/dana_holding_corporation_optimizing_products_and_processes_with_hpc/
- date: '2026-05-25'
  title: Dana Holding Corporation News and Press Releases
  url: https://www.prnewswire.com/news/dana-holding-corporation/?page=2
- date: '2026-05-25'
  title: Dana and Chrysler relations fester as costs rise
  url: https://www.autonews.com/article/20080807/OEM02/308079998/dana-and-chrysler-relations-fester-as-costs-rise/
random_paper: 4
rate_limits:
- limit_count: 1
  name: Dana Rate Limits
  slug: dana-rate-limits
rules:
- name: Dana API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dana-aftermarket-api-rules
- name: Dana API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dana-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.1
  delta: -3.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 67.8
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 21.1
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dana/refs/heads/main/screenshots/dana-2026-06-20T175459.png
security:
- kind: authentication
  name: Dana Authentication
  slug: dana-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Dana Domain Security
  slug: dana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dana
tags:
- Aftermarket
- Auto Parts
- Drivetrain
- eCommerce
- Supply Chain
- Fortune 500
website: https://www.dana.com/
---
