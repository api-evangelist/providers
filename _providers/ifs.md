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
- acting_count: 0
  human_in_the_loop: 0
  name: Ifs Agentic Access
  operation_count: 7
  slug: ifs-agentic-access
  summary_line: 7 operations
api_count: 7
apis:
- description: 'IFS Field Service Management APIs enable work order management, scheduling optimization, technician dispatch, parts inventory, and mobile workforce coordination for energy, manufacturing, and telecom '
  name: IFS Field Service Management API
  slug: ifs-field-service-management-api
- description: IFS Enterprise Asset Management APIs provide integration with asset lifecycle management, maintenance planning, work order execution, and predictive maintenance workflows for industrial and infrastruc
  name: IFS Enterprise Asset Management API
  slug: ifs-enterprise-asset-management-api
- description: IFS Enterprise Service Management APIs enable IT service management, service catalog, incident management, and CMDB integration for enterprise IT and shared service organizations using the IFS Cloud p
  name: IFS Enterprise Service Management API
  slug: ifs-enterprise-service-management-api
- description: General ledger, vouchers, and financial entities
  name: IFS Finance API
  slug: ifs-finance-api
- description: Parts and inventory management
  name: IFS Inventory API
  slug: ifs-inventory-api
- description: Purchase orders and supplier management
  name: IFS Procurement API
  slug: ifs-procurement-api
- description: Maintenance work orders and job management
  name: IFS Work Orders API
  slug: ifs-work-orders-api
artifact_total: 18
collections:
- collection_type: open
  name: IFS Cloud ERP API
  slug: open-ifs-cloud-erp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ifs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ifs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ifs-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ifs-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ifs
- group: company
  title: ''
  type: Blog
  url: https://blog.ifs.com/feed/
description: IFS is a global enterprise software company providing cloud ERP, enterprise asset management, field service management, and enterprise service management platforms. APIs enable integration with IFS Cloud across manufacturing, energy, aerospace, defense, and service industries. IFS is headquartered in Linköping, Sweden with operations in over 90 countries.
finops:
- name: Ifs Finops
  service_category: Enterprise Software
  slug: ifs-finops
image: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/image.png
json_schemas:
- name: IFS Work Order
  property_count: 17
  slug: ifs-work-order
jsonld:
- class_count: 19
  name: Ifs Context
  property_count: 14
  slug: ifs-context
layout: provider
modified: '2026-04-28'
name: IFS
nav: Providers
network: true
overview: 'IFS publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Finance API, Inventory API, Procurement API, and 1 more. Tagged areas include ERP, Field Service, Asset Management, Manufacturing, and Energy.


  The IFS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  IFS''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Ifs Plans Pricing
  plan_count: 1
  slug: ifs-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 1
  name: Ifs Rate Limits
  slug: ifs-rate-limits
rules:
- name: IFS API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ifs-jsonschema-spectral-rules
scopes:
- name: Ifs Scopes
  scope_count: 2
  slug: ifs-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.0
  delta: -3.5
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.3
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 45.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ifs/refs/heads/main/screenshots/ifs-2026-06-20T183215.png
security:
- kind: authentication
  name: Ifs Authentication
  slug: ifs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Ifs Domain Security
  slug: ifs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ifs
tags:
- ERP
- Field Service
- Asset Management
- Manufacturing
- Energy
- Cloud
---
