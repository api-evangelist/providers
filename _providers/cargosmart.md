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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Cargosmart Agentic Access
  operation_count: 8
  slug: cargosmart-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: Container booking management
  name: CargoSmart Bookings API
  slug: cargosmart-bookings-api
- description: Container tracking and event history
  name: CargoSmart Containers API
  slug: cargosmart-containers-api
- description: Shipping documentation
  name: CargoSmart Documents API
  slug: cargosmart-documents-api
- description: Shipment visibility and status
  name: CargoSmart Shipments API
  slug: cargosmart-shipments-api
- description: Vessel position and schedule
  name: CargoSmart Vessels API
  slug: cargosmart-vessels-api
artifact_total: 25
asyncapis:
- description: 'The CargoSmart Shipment Events API delivers real-time event notifications for container movements, shipment milestones, and vessel arrivals/departures via webhooks or server-sent events. Subscribe to '
  name: CargoSmart Shipment Events API
  slug: cargosmart-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CargoSmart Shipment Tracking Bookings API
  slug: open-cargosmart-bookings-api
- collection_type: open
  name: CargoSmart Shipment Tracking Bookings Containers API
  slug: open-cargosmart-containers-api
- collection_type: open
  name: CargoSmart Shipment Tracking Bookings Documents API
  slug: open-cargosmart-documents-api
- collection_type: open
  name: CargoSmart Shipment Tracking API
  slug: open-cargosmart-shipment-tracking
- collection_type: open
  name: CargoSmart Shipment Tracking Bookings Shipments API
  slug: open-cargosmart-shipments-api
- collection_type: open
  name: CargoSmart Shipment Tracking Bookings Vessels API
  slug: open-cargosmart-vessels-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/cargosmart-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cargosmart-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cargosmart-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cargosmart-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cargosmart-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cargosmart.com
- group: start
  title: ''
  type: Portal
  url: https://www.cargosmart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cargosmart.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/openapi/cargosmart-shipment-tracking-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/asyncapi/cargosmart-events-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-schema/cargosmart-container-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-schema/cargosmart-booking-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/json-ld/cargosmart-context.jsonld
- group: other
  title: ''
  type: GSBN
  url: https://www.gsbn.trade/
- group: other
  title: ''
  type: IQAX
  url: https://www.iqax.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cargosmart-limited/
created: '2025-01-15'
description: CargoSmart (now operating as IQAX) is a global shipment management software provider that gives shippers, consignees, freight forwarders, and logistics service providers ocean freight booking, container tracking, vessel scheduling, and shipping documentation tools across multiple ocean carriers. CargoSmart co-founded the Global Shipping Business Network (GSBN), a blockchain-based data exchange for carriers, terminals, banks, and customs authorities, and exposes its APIs so trading partners can embed booking, visibility, schedule, and documentation workflows directly into TMS, ERP, and supply-chain platforms.
finops:
- name: Cargosmart Finops
  service_category: Shipment Management Platform
  slug: cargosmart-finops
json_schemas:
- name: CargoSmart Container Booking
  property_count: 14
  slug: cargosmart-booking
- name: CargoSmart Container Tracking
  property_count: 12
  slug: cargosmart-container
jsonld:
- class_count: 0
  name: Cargosmart Context
  property_count: 6
  slug: cargosmart-context
layout: provider
modified: '2026-05-19'
name: CargoSmart
nav: Providers
network: true
overview: 'CargoSmart publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Containers API, Documents API, and 2 more. Tagged areas include Booking, Container, Documentation, GSBN, and IQAX.


  The CargoSmart catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  CargoSmart''s developer surface includes authentication, developer portal, documentation, and 13 more developer resources.'
plans:
- name: Cargosmart Plans Pricing
  plan_count: 1
  slug: cargosmart-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Cargosmart Rate Limits
  slug: cargosmart-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: CargoSmart API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: cargosmart-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: CargoSmart API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cargosmart-jsonschema-spectral-rules
scopes:
- name: Cargosmart Scopes
  scope_count: 4
  slug: cargosmart-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 63.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 13.6
    contract_quality: 68.1
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargosmart/refs/heads/main/screenshots/cargosmart-2026-06-20T174010.png
security:
- kind: authentication
  name: Cargosmart Authentication
  slug: cargosmart-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Cargosmart Domain Security
  slug: cargosmart-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
slug: cargosmart
tags:
- Booking
- Container
- Documentation
- GSBN
- IQAX
- Logistics
- Maritime
- Ocean Freight
- Schedule
- Shipping
- Supply Chain
- Tracking
- Visibility
- Vessel
website: https://www.cargosmart.com
---
