---
access_model:
  confidence: high
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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Iec Cim Agentic Access
  operation_count: 8
  slug: iec-cim-agentic-access
  summary_line: 8 operations
api_count: 7
apis:
- description: The IEC CIM 61970 standard defines the Common Information Model for energy management systems (EMS), enabling data exchange for power system network models, measurements, and topology across transmiss
  name: IEC CIM 61970 Energy Management API
  slug: iec-cim-61970-ems-api
- description: The IEC CIM AMI (Advanced Metering Infrastructure) APIs from AMI head-end systems provide smart meter readings, interval data, usage points, and demand response signals using CIM XML data models compl
  name: IEC CIM AMI Smart Meter API
  slug: iec-cim-ami-smart-meter-api
- description: Customer service agreements and locations
  name: iec-cim Customers API
  slug: iec-cim-customers-api
- description: Meters and interval readings (IEC 61968-9 AMI)
  name: iec-cim Metering API
  slug: iec-cim-metering-api
- description: Distribution network equipment – transformers, switches, lines, conductors
  name: iec-cim Network Assets API
  slug: iec-cim-network-assets-api
- description: Outage events and management
  name: iec-cim Outages API
  slug: iec-cim-outages-api
- description: Maintenance and construction work orders
  name: iec-cim Work Orders API
  slug: iec-cim-work-orders-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: IEC CIM 61968 Distribution Management API
  slug: open-iec-cim-61968-distribution
- collection_type: open
  name: IEC CIM 61968 Distribution Management Customers API
  slug: open-iec-cim-customers-api
- collection_type: open
  name: IEC CIM 61968 Distribution Management Customers Metering API
  slug: open-iec-cim-metering-api
- collection_type: open
  name: IEC CIM 61968 Distribution Management Customers Network Assets API
  slug: open-iec-cim-network-assets-api
- collection_type: open
  name: IEC CIM 61968 Distribution Management Customers Outages API
  slug: open-iec-cim-outages-api
- collection_type: open
  name: IEC CIM 61968 Distribution Management Customers Work Orders API
  slug: open-iec-cim-work-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iec-cim-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iec-cim-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iec-cim-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/iec-cim-scopes.yml
description: IEC Common Information Model (CIM) is an international standard developed by the International Electrotechnical Commission for representing electrical power system data and facilitating data exchange between applications.
finops:
- name: Iec Cim Finops
  service_category: API
  slug: iec-cim-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iec-cim.png
json_schemas:
- name: IEC CIM Asset
  property_count: 15
  slug: iec-cim-asset
jsonld:
- class_count: 20
  name: Iec Cim Context
  property_count: 18
  slug: iec-cim-context
layout: provider
modified: '2026-05-19'
name: iec-cim
nav: Providers
network: true
overview: 'iec-cim publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Metering API, Network Assets API, and 2 more.


  The iec-cim catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  iec-cim''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Iec Cim Plans Pricing
  plan_count: 3
  slug: iec-cim-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Iec Cim Rate Limits
  slug: iec-cim-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: iec-cim API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iec-cim-jsonschema-spectral-rules
scopes:
- name: Iec Cim Scopes
  scope_count: 2
  slug: iec-cim-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 62.2
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Iec Cim Authentication
  slug: iec-cim-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Iec Cim Domain Security
  slug: iec-cim-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iec-cim
---
