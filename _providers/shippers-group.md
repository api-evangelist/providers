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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-04'
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
overview: 'The Shippers Group publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Third Party Logistics, Warehousing, Fulfillment, Supply Chain, and Transportation Management.


  The The Shippers Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Shippers Group''s developer surface includes code examples and 13 more developer resources.'
plans:
- name: Shippers Group Plans Pricing
  plan_count: 3
  slug: shippers-group-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Shippers Group Rate Limits
  slug: shippers-group-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: The Shippers Group API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: shippers-group-jsonschema-spectral-rules
score:
  band: emerging
  composite: 19.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 17.3
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 19.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Shippers Group Domain Security
  slug: shippers-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippers-group
tags:
- Third Party Logistics
- Warehousing
- Fulfillment
- Supply Chain
- Transportation Management
- Co-Packaging
- Consumer Packaged Goods
website: https://www.theshippersgroup.com/
---
