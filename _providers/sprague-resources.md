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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprague-resources-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.spragueenergy.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprague-energy
- group: company
  title: ''
  type: Website
  url: https://www.spragueenergy.com
- group: start
  title: ''
  type: Customer Portal
  url: https://mysprague.com
- group: operate
  title: ''
  type: Contact
  url: https://www.spragueenergy.com/contact-us
- group: company
  title: ''
  type: About
  url: https://www.spragueenergy.com/about-us
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sprague-fuel-order-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sprague-fuel-order-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sprague-resources-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sprague-resources-vocabulary.yml
- group: other
  title: ''
  type: ProductPage
  url: https://www.spragueenergy.com/
created: '2023-01-01'
description: Sprague Resources (operating as Sprague Energy) is one of the largest independent suppliers of energy products and related services in the northeastern United States and Quebec, founded in 1870. The company distributes refined fuel products (heating oil, diesel, gasoline, kerosene, biofuels), natural gas, and electricity to commercial and industrial customers, and operates 20+ port terminal facilities for materials handling. Sprague was acquired by Hartree Partners in 2024 and continues to expand through strategic acquisitions. While Sprague does not publish a public developer API, the company operates SpraguePORT, a digital customer portal for account management, pricing, and order history, and Sprague Real-time for market pricing.
finops:
- name: Sprague Resources Finops
  service_category: API
  slug: sprague-resources-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprague-resources.png
json_schemas:
- name: Sprague Fuel Order
  property_count: 13
  slug: sprague-fuel-order
json_structures:
- name: Sprague Fuel Order Structure
  property_count: 0
  slug: sprague-fuel-order-structure
jsonld:
- class_count: 33
  name: Sprague Resources Context
  property_count: 3
  slug: sprague-resources-context
layout: provider
modified: '2026-07-25'
name: Sprague Resources
nav: Providers
network: true
overview: 'Sprague Resources is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Petroleum, Natural Gas, Fuel Distribution, and Materials Handling.


  The Sprague Resources catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sprague Resources'' developer surface includes engineering blog and 11 more developer resources.'
plans:
- name: Sprague Resources Plans Pricing
  plan_count: 3
  slug: sprague-resources-plans-pricing
press:
- date: '2026-05-25'
  title: Sprague Resources announces acquisition of Coen Energy
  url: https://www.reuters.com/article/world/americas/sprague-resources-announces-acquisition-of-coen-energy-idUSASB0BK3D/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1525287/000152528720000029/form8kq22020.htm
- date: '2026-05-25'
  title: Sprague Resources LP (SRLP) - Revenue
  url: https://companiesmarketcap.com/sprague-resource-lp/revenue/
- date: '2026-05-25'
  title: Adorys Velazquez | People
  url: https://www.bakerbotts.com/people/v/velazquez-adorys/
- date: '2026-05-25'
  title: Sprague Resources LP Announces Cash Distribution for the First ...
  url: https://www.marketscreener.com/quote/stock/SPRAGUE-RESOURCES-LP-14670204/news/Sprague-Resources-LP-Announces-Cash-Distribution-for-the-First-Quarter-of-2022-and-Earnings-Conferen-40140081/
random_paper: 20
rate_limits:
- limit_count: 5
  name: Sprague Resources Rate Limits
  slug: sprague-resources-rate-limits
rules:
- name: Sprague Resources API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: sprague-resources-jsonschema-spectral-rules
score:
  band: emerging
  composite: 26.8
  delta: -6.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 33.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/sprague-resources/refs/heads/main/screenshots/sprague-resources-2026-06-20T194400.png
security:
- kind: domain-security
  name: Sprague Resources Domain Security
  slug: sprague-resources-domain-security
  summary_line: TLSv1.2 · DMARC
slug: sprague-resources
tags:
- Energy
- Petroleum
- Natural Gas
- Fuel Distribution
- Materials Handling
- Northeast
website: https://www.spragueenergy.com
---
