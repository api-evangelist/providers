---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dana Agentic Access
  operation_count: 7
  slug: dana-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.danaaftermarket.com
  baseurl_source: declared
  description: Check inventory availability.
  name: Dana Availability API
  slug: dana-availability-api
- baseURL: https://api.danaaftermarket.com
  baseurl_source: declared
  description: Place and manage orders.
  name: Dana Orders API
  slug: dana-orders-api
- baseURL: https://api.danaaftermarket.com
  baseurl_source: declared
  description: Search and retrieve part information.
  name: Dana Parts API
  slug: dana-parts-api
- baseURL: https://api.danaaftermarket.com
  baseurl_source: declared
  description: Retrieve pricing information.
  name: Dana Pricing API
  slug: dana-pricing-api
- baseURL: https://api.danaaftermarket.com
  baseurl_source: declared
  description: Track shipments and delivery status.
  name: Dana Shipping API
  slug: dana-shipping-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dana Aftermarket API
  slug: open-dana-aftermarket-api
- collection_type: open
  name: Dana Aftermarket Availability API
  slug: open-dana-availability-api
- collection_type: open
  name: Dana Aftermarket Availability Orders API
  slug: open-dana-orders-api
- collection_type: open
  name: Dana Aftermarket Availability Parts API
  slug: open-dana-parts-api
- collection_type: open
  name: Dana Aftermarket Availability Pricing API
  slug: open-dana-pricing-api
- collection_type: open
  name: Dana Aftermarket Availability Shipping API
  slug: open-dana-shipping-api
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
overview: 'Dana publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Orders API, Parts API, and 2 more. Tagged areas include Aftermarket, Auto Parts, Drivetrain, E-Commerce, and Supply Chain.


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
random_paper: 5
rate_limits:
- limit_count: 1
  name: Dana Rate Limits
  slug: dana-rate-limits
rules:
- effective_rule_count: 46
  extends:
  - spectral:oas
  name: Dana API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dana-aftermarket-api-rules
- effective_rule_count: 5
  extends: []
  name: Dana API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: dana-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 85.0
    catalog_earned_first_party: 0.0
    catalog_gap: 30.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 69.7
    contract_quality: 58.5
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 69.7
    operational_transparency: 5.3
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- E-Commerce
- Supply Chain
- Fortune 500
website: https://www.dana.com/
---
