---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Nokia Netact Agentic Access
  operation_count: 9
  slug: nokia-netact-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.nokia-netact.example.com
  baseurl_source: declared
  description: Network element configuration read and write
  name: Nokia NetAct Configuration Management API
  slug: nokia-netact-configuration-management-api
- baseURL: https://api.nokia-netact.example.com
  baseurl_source: declared
  description: Alarm monitoring and lifecycle management
  name: Nokia NetAct Fault Management API
  slug: nokia-netact-fault-management-api
- baseURL: https://api.nokia-netact.example.com
  baseurl_source: declared
  description: KPI and PM counter retrieval
  name: Nokia NetAct Performance Management API
  slug: nokia-netact-performance-management-api
- baseURL: https://api.nokia-netact.example.com
  baseurl_source: declared
  description: Network topology discovery and navigation
  name: Nokia NetAct Topology API
  slug: nokia-netact-topology-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nokia NetAct Network Management Northbound Interface Configuration Management API
  slug: open-nokia-netact-configuration-management-api
- collection_type: open
  name: Nokia NetAct Network Management Northbound Interface Configuration Management Fault Management API
  slug: open-nokia-netact-fault-management-api
- collection_type: open
  name: Nokia NetAct Network Management Northbound Interface API
  slug: open-nokia-netact-nbi
- collection_type: open
  name: Nokia NetAct Network Management Northbound Interface Configuration Management Performance Management API
  slug: open-nokia-netact-performance-management-api
- collection_type: open
  name: Nokia NetAct Network Management Northbound Interface Configuration Management Topology API
  slug: open-nokia-netact-topology-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/nokia-netact-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nokia-netact-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nokia-netact-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nokia-netact-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nokia-netact-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.nokia.com/
- group: company
  title: ''
  type: Website
  url: https://www.nokia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nokia.com/networks/products/netact/
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/openapi/nokia-netact-nbi-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-schema/nokia-netact-network-element-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/json-ld/nokia-netact-context.jsonld
created: '2026-03-18'
description: Nokia NetAct is a network management system that enables operators to monitor, configure, and optimize multi-vendor mobile networks across radio, transport, and core domains. The northbound interface exposes REST APIs for OSS/BSS integration including topology, performance, fault, and configuration management.
finops:
- name: Nokia Netact Finops
  service_category: API
  slug: nokia-netact-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nokia-netact.png
json_schemas:
- name: Nokia NetAct Network Element
  property_count: 11
  slug: nokia-netact-network-element
jsonld:
- class_count: 8
  name: Nokia Netact Context
  property_count: 14
  slug: nokia-netact-context
layout: provider
modified: '2026-05-19'
name: Nokia NetAct
nav: Providers
network: true
overview: 'Nokia NetAct publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Configuration Management API, Fault Management API, Performance Management API, and 1 more. Tagged areas include Network Management, OSS, SNMP, and Telecom.


  The Nokia NetAct catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nokia NetAct''s developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Nokia Netact Plans Pricing
  plan_count: 3
  slug: nokia-netact-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Nokia Netact Rate Limits
  slug: nokia-netact-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nokia NetAct API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nokia-netact-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 61.3
    catalog_earned_first_party: 0.0
    catalog_gap: 53.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 64.2
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 33.9
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
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nokia-netact/refs/heads/main/screenshots/nokia-netact-2026-06-20T190353.png
security:
- kind: authentication
  name: Nokia Netact Authentication
  slug: nokia-netact-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Nokia Netact Domain Security
  slug: nokia-netact-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nokia Netact Vulnerability Disclosure
  slug: nokia-netact-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nokia-netact
tags:
- Network Management
- OSS
- SNMP
- Telecom
website: https://www.nokia.com/
---
