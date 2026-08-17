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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Oracle Transportation Management Agentic Access
  operation_count: 9
  slug: oracle-transportation-management-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 5
apis:
- description: Oracle Transportation Management Data Export REST API facilitates table-centric data extraction and integration with external systems for reporting, analytics, and data warehouse use cases.
  name: Oracle Transportation Management Data Export REST API
  slug: oracle-transportation-management-data-export-rest-api
- description: Carrier master data
  name: Oracle Transportation Management Carriers API
  slug: oracle-transportation-management-carriers-api
- description: Location master data
  name: Oracle Transportation Management Locations API
  slug: oracle-transportation-management-locations-api
- description: Rate records and freight costs
  name: Oracle Transportation Management Rates API
  slug: oracle-transportation-management-rates-api
- description: Shipment order management
  name: Oracle Transportation Management ShipmentOrders API
  slug: oracle-transportation-management-shipmentorders-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Transportation Management Business Object Resources REST API
  slug: open-oracle-otm-business-objects
- collection_type: open
  name: Oracle Transportation Management Business Object Resources REST Carriers API
  slug: open-oracle-transportation-management-carriers-api
- collection_type: open
  name: Oracle Transportation Management Business Object Resources REST Carriers Locations API
  slug: open-oracle-transportation-management-locations-api
- collection_type: open
  name: Oracle Transportation Management Business Object Resources REST Carriers Rates API
  slug: open-oracle-transportation-management-rates-api
- collection_type: open
  name: Oracle Transportation Management Business Object Resources REST Carriers ShipmentOrders API
  slug: open-oracle-transportation-management-shipmentorders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-transportation-management-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-transportation-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-transportation-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-transportation-management-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.oracle.com/en/cloud/saas/transport-management/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/logistics-cloud-suite/index.html
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/scm/transportation-management/
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/portal/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/scm/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.oracle.com/developer/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/oracle-otm-business-objects-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/oracle-otm-shipment-order-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/oracle-otm-context.jsonld
created: '2024-01-01'
description: Oracle Transportation Management (OTM) is a logistics platform delivered as part of Oracle Fusion Cloud Transportation and Global Trade Management. OTM APIs provide programmatic access to shipment orders, carriers, lanes, rates, transportation plans, and logistics data, plus table-centric data export for integration with reporting, analytics, and data warehouse systems.
finops:
- name: Oracle Transportation Management Finops
  service_category: API
  slug: oracle-transportation-management-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-transportation-management.png
json_schemas:
- name: Oracle OTM Shipment Order
  property_count: 17
  slug: oracle-otm-shipment-order
jsonld:
- class_count: 0
  name: Oracle Otm Context
  property_count: 24
  slug: oracle-otm-context
layout: provider
modified: '2026-05-19'
name: Oracle Transportation Management
nav: Providers
network: true
overview: 'Oracle Transportation Management publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Locations API, Rates API, and 1 more. Tagged areas include Logistics, Transportation, Freight, Supply Chain, and Shipping.


  The Oracle Transportation Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Transportation Management''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 12 more developer resources.'
plans:
- name: Oracle Transportation Management Plans Pricing
  plan_count: 3
  slug: oracle-transportation-management-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Oracle Transportation Management Rate Limits
  slug: oracle-transportation-management-rate-limits
rules:
- name: Oracle Transportation Management API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: oracle-transportation-management-jsonschema-spectral-rules
scopes:
- name: Oracle Transportation Management Scopes
  scope_count: 2
  slug: oracle-transportation-management-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: developing
  composite: 47.4
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 63.4
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-transportation-management/refs/heads/main/screenshots/oracle-transportation-management-2026-06-20T191148.png
security:
- kind: authentication
  name: Oracle Transportation Management Authentication
  slug: oracle-transportation-management-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Oracle Transportation Management Domain Security
  slug: oracle-transportation-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-transportation-management
tags:
- Logistics
- Transportation
- Freight
- Supply Chain
- Shipping
- Global Trade
- Oracle
website: https://www.oracle.com/scm/transportation-management/
---
