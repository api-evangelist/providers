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
    agentic_commerce: false
    auth_clarity: negotiable
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
  score: 22.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Oracle Transportation Management Agentic Access
  operation_count: 9
  slug: oracle-transportation-management-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: Oracle Transportation Management Data Export REST API facilitates table-centric data extraction and integration with external systems for reporting, analytics, and data warehouse use cases.
  name: Oracle Transportation Management Data Export REST API
  slug: oracle-transportation-management-data-export-rest-api
- baseURL: https://{host}/GC3/glog.integration.servlet.WMServlet/otm/rest/v1
  baseurl_source: declared
  description: Carrier master data
  name: Oracle Transportation Management Carriers API
  slug: oracle-transportation-management-carriers-api
- baseURL: https://{host}/GC3/glog.integration.servlet.WMServlet/otm/rest/v1
  baseurl_source: declared
  description: Location master data
  name: Oracle Transportation Management Locations API
  slug: oracle-transportation-management-locations-api
- baseURL: https://{host}/GC3/glog.integration.servlet.WMServlet/otm/rest/v1
  baseurl_source: declared
  description: Rate records and freight costs
  name: Oracle Transportation Management Rates API
  slug: oracle-transportation-management-rates-api
- baseURL: https://{host}/GC3/glog.integration.servlet.WMServlet/otm/rest/v1
  baseurl_source: declared
  description: Shipment order management
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-transportation-management-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
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
modified: '2026-08-21'
name: Oracle Transportation Management
nav: Providers
network: true
overview: 'Oracle Transportation Management publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Carriers API, Locations API, Rates API, and 1 more. Tagged areas include Logistics, Transportation, Freight, Supply Chain, and Shipping.


  The Oracle Transportation Management catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oracle Transportation Management''s developer surface includes authentication, developer portal, documentation, support, engineering blog, and 14 more developer resources.'
plans:
- name: Oracle Transportation Management Plans Pricing
  plan_count: 3
  slug: oracle-transportation-management-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Oracle Transportation Management Rate Limits
  slug: oracle-transportation-management-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle Transportation Management API Rules
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
  composite: 42.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.3
    catalog_earned_first_party: 0.0
    catalog_gap: 62.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 61.7
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
