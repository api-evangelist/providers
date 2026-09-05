---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Applied Industrial Technologies Agentic Access
  operation_count: 4
  slug: applied-industrial-technologies-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.applied-industrial-technologies.com/v1
  baseurl_source: spec
  description: Purchase order management
  name: Applied Industrial Technologies Orders API
  slug: applied-industrial-technologies-orders-api
- baseURL: https://api.applied-industrial-technologies.com/v1
  baseurl_source: spec
  description: Industrial product catalog operations
  name: Applied Industrial Technologies Products API
  slug: applied-industrial-technologies-products-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Applied Industrial Technologies Product Catalog Orders API
  slug: open-applied-industrial-technologies-orders-api
- collection_type: open
  name: Applied Industrial Technologies Product Catalog Orders Products API
  slug: open-applied-industrial-technologies-products-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/applied-industrial-technologies-domain-security.yml
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/applied-industrial-technologies-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/applied-industrial-technologies-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applied-industrial-technologies-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appliedindustrialtechnologies-
- group: company
  title: ''
  type: Website
  url: https://www.applied.com
coverage:
  checked: '2026-09-04'
  detail: Applied Industrial Technologies runs a live Azure API Management gateway at api.applied.com — it answers every request with a 54-byte JSON 404 and an Azure Request-Context header — but publishes no developer portal, no API reference and no discovery document, so its integration surface is reachable only through an account team and a signed customer agreement.
  evidence:
  - status: 404
    url: https://api.applied.com/
  - status: 404
    url: https://api.applied.com/openapi.json
  - status: 404
    url: https://www.applied.com/llms.txt
  - status: 403
    url: https://www.applied.com/developers
  - status: 404
    url: https://www.applied.com/.well-known/security.txt
  - status: 0
    url: https://api.applied-industrial-technologies.com/
  reason: customer-only-docs
  state: gated
created: '2026-05-03'
description: 'Applied Industrial Technologies, Inc. (NYSE: AIT) is a Cleveland, Ohio industrial distributor and technical solutions provider, founded in 1923, serving MRO and OEM customers across North America, Australia, New Zealand and Singapore. It distributes bearings, power transmission products, fluid power components, industrial rubber products, linear motion components, specialty flow control, tools and related supplies, and operates engineered fluid power and automation businesses alongside its distribution network. Its customer-facing storefront is applied.com, an SAP Commerce site; the company runs an Azure API Management gateway at api.applied.com but publishes no public developer program, API reference or machine-readable contract.'
examples:
- key_count: 9
  name: Product Example
  slug: product-example
finops:
- name: Applied Industrial Technologies Finops
  service_category: API
  slug: applied-industrial-technologies-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applied-industrial-technologies.png
json_schemas:
- name: Product
  property_count: 9
  slug: product
json_structures:
- name: Product Structure
  property_count: 0
  slug: product-structure
jsonld:
- class_count: 13
  name: Applied Industrial Technologies Context
  property_count: 0
  slug: applied-industrial-technologies-context
layout: provider
modified: '2026-04-19'
name: Applied Industrial Technologies
nav: Providers
network: true
overview: 'Applied Industrial Technologies publishes 2 APIs on the [APIs.io](https://apis.io/) network: Orders API and Products API. Tagged areas include Industrial Distribution, Bearings, Power Transmission, Fluid Power, and Supply Chain.


  The Applied Industrial Technologies catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Applied Industrial Technologies'' developer surface includes authentication and 5 more developer resources.'
plans:
- name: Applied Industrial Technologies Plans Pricing
  plan_count: 0
  slug: applied-industrial-technologies-plans-pricing
press:
- date: '2026-05-25'
  title: Applied Industrial Technologies Q3 Earnings Call Highlights
  url: https://www.marketbeat.com/instant-alerts/applied-industrial-technologies-q3-earnings-call-highlights-2026-04-28/
- date: '2026-05-25'
  title: Applied Industrial emphasizes AI as sales show early ...
  url: https://www.digitalcommerce360.com/2026/01/28/applied-industrial-ai-sales-q2-fy26/
- date: '2026-05-25'
  title: Section Applied Industrial Technologies
  url: https://www.mdpi.com/journal/applsci/sections/applied_industrial_technologies
- date: '2026-05-25'
  title: A Look At Applied Industrial Technologies (AIT) Valuation ...
  url: https://finance.yahoo.com/news/look-applied-industrial-technologies-ait-151001894.html
- date: '2026-05-25'
  title: AIT Applied Industrial Technologies, Inc. Stock Price & ...
  url: https://seekingalpha.com/symbol/AIT
random_paper: 4
rate_limits:
- limit_count: 0
  name: Applied Industrial Technologies Rate Limits
  slug: applied-industrial-technologies-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Applied Industrial Technologies API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: applied-industrial-technologies-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Applied Industrial Technologies API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: applied-industrial-technologies-spectral-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.1
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 28.8
    contract_quality: 26.0
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 0.0
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: falling
security:
- kind: authentication
  name: Applied Industrial Technologies Authentication
  slug: applied-industrial-technologies-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Applied Industrial Technologies Domain Security
  slug: applied-industrial-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: applied-industrial-technologies
tags:
- Industrial Distribution
- Bearings
- Power Transmission
- Fluid Power
- Supply Chain
- Fortune 1000
website: https://www.applied.com
---
