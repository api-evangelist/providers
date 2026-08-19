---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Realtor Agentic Access
  operation_count: 8
  slug: realtor-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 6
apis:
- description: The Realtor.com Connections Plus API provides a direct connection between the Realtor.com lead delivery system and supporting CRM platforms. It enables real estate agents, brokers, and offices to rece
  name: Realtor.com Connections Plus API
  slug: connections-plus-api
- description: The Realtor.com Lead Delivery API is an end-to-end integration layer that delivers real estate leads directly from Realtor.com to third-party CRM systems. It provides faster and more secure lead deliv
  name: Realtor.com Lead Delivery API
  slug: lead-delivery-api
- description: Endpoints for searching and retrieving information about real estate agents and brokers.
  name: realtor Agents API
  slug: realtor-agents-api
- description: Endpoints for retrieving mortgage rates and financial data relevant to real estate transactions.
  name: realtor Finance API
  slug: realtor-finance-api
- description: Endpoints for searching and auto-completing location names, addresses, and geographic areas used as inputs for property searches.
  name: realtor Locations API
  slug: realtor-locations-api
- description: Endpoints for searching, listing, and retrieving detailed property information including for-sale, for-rent, and recently sold listings.
  name: realtor Properties API
  slug: realtor-properties-api
artifact_total: 25
asyncapis:
- description: The Realtor.com Connections Plus API provides a direct connection between the Realtor.com lead delivery system and supporting CRM platforms. It enables real estate agents, brokers, and offices to rece
  name: Realtor.com Connections Plus Events
  slug: realtor-connections-plus-asyncapi
- description: The Realtor.com Lead Delivery API is an end-to-end integration layer that delivers real estate leads directly from Realtor.com to third-party CRM systems. It provides faster and more secure lead deliv
  name: Realtor.com Lead Delivery Events
  slug: realtor-lead-delivery-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Realtor.com Property Data Agents API
  slug: open-realtor-agents-api
- collection_type: open
  name: Realtor.com Property Data Agents Finance API
  slug: open-realtor-finance-api
- collection_type: open
  name: Realtor.com Property Data Agents Locations API
  slug: open-realtor-locations-api
- collection_type: open
  name: Realtor.com Property Data Agents Properties API
  slug: open-realtor-properties-api
- collection_type: open
  name: Realtor.com Property Data API
  slug: open-realtor-property-data
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/realtor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/realtor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/realtor-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.realtor.com/news/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/realtor-com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/realtor-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtor-lead-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/realtor-property-schema.json
description: Realtor.com is an online real estate marketplace operated by Move, Inc., providing home listings, neighborhood information, and tools for buyers, sellers, and renters.
finops:
- name: Realtor Finops
  service_category: Real Estate Data
  slug: realtor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/realtor.png
json_schemas:
- name: Realtor.com Lead
  property_count: 12
  slug: realtor-lead
- name: Realtor.com Property
  property_count: 15
  slug: realtor-property
jsonld:
- class_count: 0
  name: Realtor Context
  property_count: 8
  slug: realtor-context
layout: provider
modified: '2026-05-19'
name: realtor
nav: Providers
network: true
overview: 'realtor publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Realtor.com Connections Plus API, Realtor.com Lead Delivery API, Agents API, and 3 more.


  The realtor catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  realtor''s developer surface includes authentication, engineering blog, and 6 more developer resources.'
plans:
- name: Realtor Plans Pricing
  plan_count: 1
  slug: realtor-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Realtor Rate Limits
  slug: realtor-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: realtor API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: realtor-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: realtor API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: realtor-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.3
  delta: -4.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 11.4
    contract_quality: 67.1
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 11.4
    operational_transparency: 5.3
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/realtor/refs/heads/main/screenshots/realtor-2026-06-20T192649.png
security:
- kind: authentication
  name: Realtor Authentication
  slug: realtor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Realtor Domain Security
  slug: realtor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: realtor
---
