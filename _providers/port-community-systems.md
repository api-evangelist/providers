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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Port Community Systems Agentic Access
  operation_count: 9
  slug: port-community-systems-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 6
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
artifact_total: 19
asyncapis:
- description: Portbase publishes real-time vessel call and cargo events via webhooks to connected port community members. Events notify subscribers of vessel status changes, customs release notifications, and conta
  name: Portbase Vessel Events API
  slug: portbase-vessel-events-asyncapi
collections:
- collection_type: open
  name: Portbase Port Community System API
  slug: open-portbase-port-community
common:
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


  Port Community Systems'' developer surface includes authentication, developer portal, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Port Community Systems Plans Pricing
  plan_count: 3
  slug: port-community-systems-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Port Community Systems Rate Limits
  slug: port-community-systems-rate-limits
rules:
- name: Port Community Systems API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: port-community-systems-asyncapi-spectral-rules
- name: Port Community Systems API Rules
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
  band: developing
  composite: 50.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.6
    developer_ergonomics: 30.4
    discoverability: 67.5
    governance: 52.6
    operational_transparency: 31.6
  previous_composite: 50.8
  schema_version: 0.5
  scored_at: '2026-07-23'
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
