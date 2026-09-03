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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Aspentech Agentic Access
  operation_count: 6
  slug: aspentech-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- description: 'AspenTech provides process optimization and simulation software for energy, chemicals, and manufacturing industries. The aspenONE platform APIs enable access to process simulation models, performance '
  name: AspenTech aspenONE API
  slug: aspenone-api
- description: The AspenTech Inmation Simple Call Interface (SCI) API provides a simplified HTTP interface for communicating with the Inmation industrial data platform. Designed for straightforward read/write access
  name: AspenTech Inmation Simple Call Interface (SCI) API
  slug: inmation-sci-api
- baseURL: http://hostname:8002
  baseurl_source: declared
  description: Read and write process data points
  name: AspenTech Data API
  slug: aspentech-data-api
- baseURL: http://hostname:8002
  baseurl_source: declared
  description: Historical time-series data access
  name: AspenTech Historical API
  slug: aspentech-historical-api
- baseURL: http://hostname:8002
  baseurl_source: declared
  description: Configuration item management
  name: AspenTech Items API
  slug: aspentech-items-api
- baseURL: http://hostname:8002
  baseurl_source: declared
  description: System information and health
  name: AspenTech System API
  slug: aspentech-system-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AspenTech Inmation Web Data API
  slug: open-aspentech-data-api
- collection_type: open
  name: AspenTech Inmation Web Data Historical API
  slug: open-aspentech-historical-api
- collection_type: open
  name: AspenTech Inmation Web API
  slug: open-aspentech-inmation-web
- collection_type: open
  name: AspenTech Inmation Web Data Items API
  slug: open-aspentech-items-api
- collection_type: open
  name: AspenTech Inmation Web Data System API
  slug: open-aspentech-system-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aspentech-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aspentech-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aspentech-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aspen-technology
- group: start
  title: AspenTech Website
  type: Portal
  url: https://www.aspentech.com/
- group: start
  title: Developer Knowledge Center
  type: Portal
  url: https://dev.knowledgecenter.aspentech.com/
- group: docs
  title: Documentation
  type: Documentation
  url: https://dev.knowledgecenter.aspentech.com/
- group: start
  title: Getting Started Guides
  type: GettingStarted
  url: https://www.aspentech.com/en/getting-started-guides
- group: operate
  title: Technical Support
  type: Support
  url: https://esupport.aspentech.com/
- group: docs
  title: Inmation Web API OpenAPI
  type: OpenAPI
  url: openapi/_original/aspentech-inmation-web-openapi.yml
- group: docs
  title: Data Item JSON Schema
  type: JSONSchema
  url: json-schema/aspentech-dataitem-schema.json
- group: design
  title: AspenTech JSON-LD Context
  type: JSONLD
  url: json-ld/aspentech-context.jsonld
created: '2024-01-15'
description: AspenTech (Aspen Technology, Inc.) is a global leader in industrial software for asset optimization across the energy, chemicals, and manufacturing industries. AspenTech provides process simulation, optimization, and industrial IoT platforms including the aspenONE suite and Inmation industrial data platform. The Inmation platform provides Web API and Simple Call Interface (SCI) APIs for external applications to interact with industrial IoT and time-series process data via HTTP and WebSocket interfaces. AspenTech serves refineries, petrochemical plants, power generation facilities, and other industrial operations worldwide.
features:
- description: The Inmation platform provides industrial-grade time-series data management, process data connectivity, and real-time analytics for manufacturing and energy operations.
  name: Inmation Industrial IoT Platform
- description: aspenONE suite provides high-fidelity process simulation for design, optimization, and operational decision support in chemical plants, refineries, and energy facilities.
  name: Process Simulation
- description: WebSocket interface in the Inmation Web API enables real-time streaming of process data, alarm states, and operational events to external applications.
  name: WebSocket Real-Time Data
- description: Tools for monitoring asset health, predicting maintenance needs, and optimizing equipment performance across industrial operations.
  name: Asset Performance Management
- description: APIs for integrating AI and machine learning models with process data to enable predictive analytics and autonomous optimization.
  name: AI/ML Integration
finops:
- name: Aspentech Finops
  service_category: Industrial Software / Process Optimization
  slug: aspentech-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aspentech.png
json_schemas:
- name: AspenTech Inmation Data Item
  property_count: 13
  slug: aspentech-dataitem
jsonld:
- class_count: 0
  name: Aspentech Context
  property_count: 3
  slug: aspentech-context
layout: provider
modified: '2026-05-19'
name: AspenTech
nav: Providers
network: true
overview: 'AspenTech publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Data API, Historical API, Items API, and 1 more. Tagged areas include Industrial IoT, Process Optimization, Manufacturing, Energy, and Chemicals.


  The AspenTech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AspenTech''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Aspentech Plans Pricing
  plan_count: 1
  slug: aspentech-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: Aspentech Rate Limits
  slug: aspentech-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AspenTech API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aspentech-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 9.8
    contract_quality: 59.5
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 35.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/screenshots/aspentech-2026-06-20T172502.png
security:
- kind: authentication
  name: Aspentech Authentication
  slug: aspentech-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Aspentech Domain Security
  slug: aspentech-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aspentech
tags:
- Industrial IoT
- Process Optimization
- Manufacturing
- Energy
- Chemicals
- Time Series
use_cases:
- description: Operations technology teams integrate the Inmation Web API with business intelligence tools, historian systems, and enterprise applications to access real-time and historical process data.
  name: Process Data Integration
- description: Engineering teams use aspenONE simulation APIs to build digital twins of process plants for operations optimization and scenario analysis.
  name: Digital Twin Development
- description: Control systems engineers use the Inmation API to build custom alarm management dashboards and analytics for industrial operations.
  name: Alarm Management
- description: Refineries and petrochemical plants use AspenTech APIs to connect optimization models with real-time operations for energy efficiency.
  name: Energy Optimization
website: https://www.aspentech.com/
---
