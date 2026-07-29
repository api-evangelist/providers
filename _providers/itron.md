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
- acting_count: 8
  human_in_the_loop: 0
  name: Itron Agentic Access
  operation_count: 13
  slug: itron-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 11
apis:
- description: Partner-gated platform for building purpose-built applications that execute on Itron-DI-enabled electric meters at the grid edge. Itron describes DI as moving "grid analysis, decision-making and contr
  name: Itron Distributed Intelligence (DI) Platform
  slug: itron-distributed-intelligence-di-platform
- description: The IC platform combines Itron's IPv6-enabled RF mesh Network Platform with a Control Platform that manages the lifecycle of connected devices. Itron describes it as "an open, standards-based IPv6-ena
  name: Itron Intelligent Connectivity (IC) Platform
  slug: itron-intelligent-connectivity-ic-platform
- description: REST-based OData 4.0 query API exposing the Itron Analytics data warehouse for Itron Enterprise Edition / IA Platform tenants. Authentication uses a JWT obtained from the Itron Identity Service with a
  name: Itron Analytics Data Warehouse API
  slug: itron-analytics-data-warehouse-api
- description: REST/JSON API that enables utility customer portals to enroll consumers into Distributed Intelligence (DI) programs by forwarding requests into the Itron Enterprise Application Center (EAC) and orches
  name: Itron Third-Party Gateway API
  slug: itron-third-party-gateway-api
- description: Legacy web-service surface for Itron Enterprise Edition (IEE) Meter Data Management. Documented as a mix of WCF services (with annotated WSDL and XSD files shipped in the installation's `bin\ServiceMe
  name: Itron IEE Web Services
  slug: itron-iee-web-services
- description: Itron describes Consumer Energy Stream as a data product that allows electricity meter consumption data "from a consumer's meter to stream to an Itron-authenticated receiver over the consumer's intern
  name: Itron Consumer Energy Stream (CES) API
  slug: itron-consumer-energy-stream-ces-api
- description: GenX is the marketing umbrella under which Itron positions next-generation grid-edge solutions for developer partners; Starfish Studio is a related sandbox/prototyping surface for IoT solution builder
  name: Itron GenX / Starfish Studio
  slug: itron-genx-starfish-studio
- description: Reusable sensor-shape templates for devices.
  name: Itron Device Templates API
  slug: itron-device-templates-api
- description: Device registration, lookup, and querying.
  name: Itron Devices API
  slug: itron-devices-api
- description: Time-series sensor observation ingest and query.
  name: Itron Observations API
  slug: itron-observations-api
- description: OAuth 2.0 token issuance for browser-suitable, short-lived bearer tokens.
  name: Itron Tokens API
  slug: itron-tokens-api
artifact_total: 30
collections:
- collection_type: open
  name: Itron Starfish Data Platform API
  slug: open-starfish-data-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/itron-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itron-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itron-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://na.itron.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://na.itron.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.itrontotal.com/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://customer.itron.com/
- group: start
  title: ''
  type: Signup
  url: https://partner.itron.com/flow/af4b0f91-1acd-4c07-9425-7fb4c31ac22b
- group: auth
  title: ''
  type: Authentication
  url: https://docs.itrontotal.com/IAPlatform/Cloud/AdminPortal/help/Content/DataWarehouseAPI.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/silverspringnetworks
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/silverspringnetworks/starfish-js
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/silverspringnetworks/developer_program
- group: company
  title: ''
  type: Blog
  url: https://na.itron.com/w
- group: company
  title: ''
  type: Newsroom
  url: https://na.itron.com/na/company/newsroom
- group: company
  title: ''
  type: Partners
  url: https://na.itron.com/partners
- group: other
  title: ''
  type: Customers
  url: https://na.itron.com/who-we-serve
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itron-inc/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ItronInc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/itroninc
- group: other
  title: ''
  type: Glossary
  url: https://apps.itron.com/ItronGlossary/
- group: company
  title: ''
  type: Investors
  url: https://investors.itron.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/itron-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/itron-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/itron-finops.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/itron-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/itron-context.jsonld
created: '2026-05-22'
description: 'Itron, Inc. (NASDAQ: ITRI) is a Liberty Lake, Washington–based industrial technology company providing smart-meter, grid-edge, and IoT infrastructure to electric, gas, and water utilities and cities. Itron''s self-described mission is "Creating a more resourceful world" and the company reports 7,700+ customers in 100+ countries with 310M+ communicating endpoints delivered and 112M+ endpoints under management. The Itron developer surface is partner-gated rather than self-serve, centered on three platform families: (1) Distributed Intelligence (DI) — purpose-built apps that run at the grid edge on Itron smart meters; (2) Intelligent Connectivity (IC) — an IPv6/RF-mesh network platform (Itron Networks, formerly Cisco IoT FAN); and (3) the Starfish / Itron Networked Solutions Data Platform — a REST API + JavaScript SDK for device management and observation data, inherited from the Silver Spring Networks acquisition. A separate Data Warehouse OData API serves the Itron Analytics
  product, a Third-Party Gateway REST API bridges utility customer portals into DI enrollment, and legacy IEE web services (WCF/SOAP) and Consumer Energy Stream (CES) APIs document the Itron Enterprise Edition stack. Public OpenAPI/AsyncAPI artifacts are not published — access to specs, SDKs, and sandboxes is brokered through partner.itron.com after program acceptance. The developer.itron.com hostname now redirects to na.itron.com/developers/.'
examples:
- key_count: 3
  name: Starfish Device Template Example
  slug: starfish-device-template-example
- key_count: 1
  name: Starfish List Devices Example
  slug: starfish-list-devices-example
- key_count: 4
  name: Starfish Post Observation Example
  slug: starfish-post-observation-example
- key_count: 2
  name: Starfish Query Observations Example
  slug: starfish-query-observations-example
- key_count: 2
  name: Starfish Token Request Example
  slug: starfish-token-request-example
finops:
- name: Itron Finops
  service_category: ''
  slug: itron-finops
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/api-evangelist-icon.jpg
json_schemas:
- name: Itron Starfish Device
  property_count: 6
  slug: starfish-device
- name: Itron Starfish Device Template
  property_count: 3
  slug: starfish-device-template
- name: Itron Starfish Observation
  property_count: 4
  slug: starfish-observation
json_structures:
- name: Starfish Data Platform Structure
  property_count: 0
  slug: starfish-data-platform-structure
jsonld:
- class_count: 29
  name: Itron Context
  property_count: 0
  slug: itron-context
layout: provider
modified: '2026-05-23'
name: Itron
nav: Providers
network: true
overview: 'Itron publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Device Templates API, Devices API, Observations API, and 1 more. Tagged areas include Itron, Utilities, Smart Meters, Smart Grid, and Smart Cities.


  The Itron catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Itron''s developer surface includes authentication, developer portal, documentation, signup flow, engineering blog, YouTube channel, and 21 more developer resources.'
plans:
- name: Itron Plans Pricing
  plan_count: 4
  slug: itron-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 5
  name: Itron Rate Limits
  slug: itron-rate-limits
rules:
- name: Itron API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: itron-jsonschema-spectral-rules
- name: Itron API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: starfish-data-platform-rules
score:
  band: developing
  composite: 46.9
  delta: -8.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 66.9
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 55.6
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
    score: 23.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/itron/refs/heads/main/screenshots/itron-2026-06-20T183633.png
security:
- kind: authentication
  name: Itron Authentication
  slug: itron-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Itron Domain Security
  slug: itron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: itron
tags:
- Itron
- Utilities
- Smart Meters
- Smart Grid
- Smart Cities
- Internet Of Things
- IoT
- Energy
- Water
- Gas
- Electricity
- Distributed Intelligence
- Grid Edge
- AMI
- AMR
- RF Mesh
- IPv6
- OData
- Industrial IoT
- Fortune 1000
- NASDAQ ITRI
website: https://na.itron.com/developers/
---
