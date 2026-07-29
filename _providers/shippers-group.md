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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Shippers Group provides third-party logistics services including warehousing, co-packaging, fulfillment, and transportation management. As a national 3PL provider operating across 12 US locations,
  name: The Shippers Group Logistics Operations
  slug: shippers-group-logistics
- description: Kenco Group acquired The Shippers Group in December 2023. Kenco is a leading 3PL provider offering warehousing, distribution, transportation management, and material handling equipment services. Kenco
  name: Kenco Group (Parent Company)
  slug: kenco-group
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippers-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.theshippersgroup.com/
- group: other
  title: ''
  type: Services
  url: https://www.theshippersgroup.com/services/
- group: other
  title: ''
  type: WarehousingServices
  url: https://www.theshippersgroup.com/services/warehousing/
- group: agent
  title: ''
  type: FulfillmentServices
  url: https://www.theshippersgroup.com/services/fulfillment/
- group: other
  title: ''
  type: CoPackagingServices
  url: https://www.theshippersgroup.com/services/co-packaging/
- group: other
  title: ''
  type: TransportationServices
  url: https://www.theshippersgroup.com/services/transportation/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.kencogroup.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-shippers-group/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shippers-group-warehouse-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/shippers-group-warehouse-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/shippers-group-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/shippers-group-warehouse-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shippers-group-vocabulary.yml
created: '2026-05-02'
description: The Shippers Group is a leading national third-party logistics (3PL) company headquartered in Dallas, Texas. Founded in 1901, the company provides warehousing, co-packaging, fulfillment, and transportation management services across 12 locations totaling over 5 million square feet of space. The Shippers Group serves brand leaders and market innovators in industries including food, consumer packaged goods, and retail. The company was acquired by Kenco Group in December 2023. Client integrations are handled via EDI connections and logistics technology partnerships with warehouse management systems and transportation management systems.
examples:
- key_count: 13
  name: Shippers Group Warehouse Example
  slug: shippers-group-warehouse-example
finops:
- name: Shippers Group Finops
  service_category: API
  slug: shippers-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippers-group.png
json_schemas:
- name: Warehouse
  property_count: 13
  slug: shippers-group-warehouse
json_structures:
- name: Shippers Group Warehouse Structure
  property_count: 0
  slug: shippers-group-warehouse-structure
jsonld:
- class_count: 33
  name: Shippers Group Context
  property_count: 2
  slug: shippers-group-context
layout: provider
modified: '2026-05-02'
name: The Shippers Group
nav: Providers
network: true
overview: 'The Shippers Group publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Third-Party Logistics, Warehousing, Fulfillment, Supply Chain, and Transportation Management.


  The The Shippers Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Shippers Group''s developer surface includes code examples and 13 more developer resources.'
plans:
- name: Shippers Group Plans Pricing
  plan_count: 3
  slug: shippers-group-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 5
  name: Shippers Group Rate Limits
  slug: shippers-group-rate-limits
rules:
- name: The Shippers Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shippers-group-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.4
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 31.6
  previous_composite: 34.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Shippers Group Domain Security
  slug: shippers-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippers-group
tags:
- Third-Party Logistics
- Warehousing
- Fulfillment
- Supply Chain
- Transportation Management
- Co-Packaging
- Consumer Packaged Goods
website: https://www.theshippersgroup.com/
---
