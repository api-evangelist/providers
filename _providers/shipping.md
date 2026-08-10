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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-08-10'
api_count: 3
apis:
- description: Shipping.com provides a marketplace and intelligence platform for the ocean freight and logistics industry. The platform aggregates freight rates from major carriers and provides rate comparison, mark
  name: Shipping.com Rate Intelligence Platform
  slug: shipping-platform
- description: The Freightos Baltic Index is the global benchmark for container freight rates, providing weekly assessments of freight rates across major trade lanes. The FBX provides spot market freight rate data f
  name: Freightos Baltic Index (FBX)
  slug: freightos-baltic-index
- description: The World Bank provides commodity price data including shipping-related indices such as the Baltic Dry Index (BDI) and fuel prices that affect freight rates. This data is used for freight market analy
  name: World Bank Commodity Markets Data
  slug: world-bank-commodity-markets
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipping-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipping.com/
- group: company
  title: ''
  type: Blog
  url: https://www.shipping.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipping-com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shipping-rate-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/shipping-rate-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/shipping-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/shipping-rate-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shipping-vocabulary.yml
created: '2026-05-02'
description: Shipping.com is a shipping intelligence and marketplace platform that provides inside information on the best deals across the shipping industry worldwide. The platform enables carriers, shippers, and third-party logistics companies (3PLs) to access reduced shipping rates, improve revenue opportunities, and optimize transportation supply chain operations. Shipping.com is headquartered in New York City and connects members of the transportation and logistics industry with competitive pricing and market intelligence across all major ocean freight trade lanes.
examples:
- key_count: 14
  name: Shipping Rate Example
  slug: shipping-rate-example
finops:
- name: Shipping Finops
  service_category: API
  slug: shipping-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipping.png
json_schemas:
- name: Shipping Rate
  property_count: 14
  slug: shipping-rate
json_structures:
- name: Shipping Rate Structure
  property_count: 0
  slug: shipping-rate-structure
jsonld:
- class_count: 31
  name: Shipping Context
  property_count: 4
  slug: shipping-context
layout: provider
modified: '2026-05-02'
name: Shipping.com
nav: Providers
network: true
overview: 'Shipping.com publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Freight, Logistics, Transportation, and Marketplace.


  The Shipping.com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shipping.com''s developer surface includes engineering blog, code examples, and 7 more developer resources.'
plans:
- name: Shipping Plans Pricing
  plan_count: 3
  slug: shipping-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Shipping Rate Limits
  slug: shipping-rate-limits
rules:
- name: Shipping.com API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shipping-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 2.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 30.4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Shipping Domain Security
  slug: shipping-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipping
tags:
- Shipping
- Freight
- Logistics
- Transportation
- Marketplace
- Rate Intelligence
- Ocean Freight
- Supply Chain
website: https://www.shipping.com/
---
