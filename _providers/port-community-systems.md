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
  score: 23.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Port Community Systems Agentic Access
  operation_count: 9
  slug: port-community-systems-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- description: The International Port Community Systems Association (IPCSA) represents Port Community System operators and Maritime Single Window operators worldwide. Member PCS platforms provide APIs for customs de
  name: IPCSA Port Community Systems API
  slug: ipcsa
- description: Cargo manifest declarations
  name: Port Community Systems CargoManifests API
  slug: port-community-systems-cargomanifests-api
- description: Container tracking and inspection
  name: Port Community Systems Containers API
  slug: port-community-systems-containers-api
- description: Import and export customs filings
  name: Port Community Systems CustomsDeclarations API
  slug: port-community-systems-customsdeclarations-api
- description: Dangerous goods declarations
  name: Port Community Systems HazardousCargo API
  slug: port-community-systems-hazardouscargo-api
- description: Vessel arrival and departure notifications
  name: Port Community Systems VesselCalls API
  slug: port-community-systems-vesselcalls-api
artifact_total: 25
asyncapis:
- description: Portbase publishes real-time vessel call and cargo events via webhooks to connected port community members. Events notify subscribers of vessel status changes, customs release notifications, and conta
  name: Portbase Vessel Events API
  slug: portbase-vessel-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Portbase Port Community System CargoManifests API
  slug: open-port-community-systems-cargomanifests-api
- collection_type: open
  name: Portbase Port Community System CargoManifests Containers API
  slug: open-port-community-systems-containers-api
- collection_type: open
  name: Portbase Port Community System CargoManifests CustomsDeclarations API
  slug: open-port-community-systems-customsdeclarations-api
- collection_type: open
  name: Portbase Port Community System CargoManifests HazardousCargo API
  slug: open-port-community-systems-hazardouscargo-api
- collection_type: open
  name: Portbase Port Community System CargoManifests VesselCalls API
  slug: open-port-community-systems-vesselcalls-api
- collection_type: open
  name: Portbase Port Community System API
  slug: open-portbase-port-community
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/port-community-systems-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/port-community-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/port-community-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/port-community-systems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/port-community-systems-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.ipcsa.international/
- group: start
  title: ''
  type: Portal
  url: https://www.ipcsa.international/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ipcsa.international/
- group: company
  title: ''
  type: Blog
  url: https://www.portbase.com/en/news-knowledge/
created: '2026-03-18'
description: Port Community Systems (PCS) are neutral and open electronic platforms enabling intelligent and secure exchange of information between public and private stakeholders to optimise, manage, and automate efficient port and logistics processes through a single submission of data.
finops:
- name: Port Community Systems Finops
  service_category: API
  slug: port-community-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/port-community-systems.png
json_schemas:
- name: Portbase Vessel Call
  property_count: 20
  slug: portbase-vessel-call
jsonld:
- class_count: 0
  name: Portbase Context
  property_count: 30
  slug: portbase-context
layout: provider
modified: '2026-05-19'
name: Port Community Systems
nav: Providers
network: true
overview: 'Port Community Systems publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CargoManifests API, Containers API, CustomsDeclarations API, and 2 more. Tagged areas include Maritime, Port, Logistics, Customs, and Cargo.


  The Port Community Systems catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Port Community Systems'' developer surface includes authentication, developer portal, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Port Community Systems Plans Pricing
  plan_count: 3
  slug: port-community-systems-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Port Community Systems Rate Limits
  slug: port-community-systems-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Port Community Systems API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: port-community-systems-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Port Community Systems API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: port-community-systems-jsonschema-spectral-rules
scopes:
- name: Port Community Systems Scopes
  scope_count: 4
  slug: port-community-systems-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 55.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 74.2
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 37.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/port-community-systems/refs/heads/main/screenshots/port-community-systems-2026-06-20T191927.png
security:
- kind: authentication
  name: Port Community Systems Authentication
  slug: port-community-systems-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Port Community Systems Domain Security
  slug: port-community-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: port-community-systems
tags:
- Maritime
- Port
- Logistics
- Customs
- Cargo
- Shipping
website: https://www.ipcsa.international/
---
