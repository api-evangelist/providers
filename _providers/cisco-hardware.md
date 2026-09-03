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
    auth_clarity: bearer
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
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Cisco Hardware Agentic Access
  operation_count: 13
  slug: cisco-hardware-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: The Cisco Catalyst Center API (formerly Cisco DNA Center) provides programmatic management of Cisco enterprise network infrastructure, including discovery, inventory, provisioning, assurance, software
  name: Cisco Catalyst Center API
  slug: catalyst-center-api
- description: The IOS XE RESTCONF API exposes Cisco enterprise routers and switches running IOS XE through a model-driven RESTCONF interface that maps directly onto YANG data models. Operations include retrieving d
  name: Cisco IOS XE RESTCONF API
  slug: ios-xe-restconf-api
- description: The Cisco APIC REST API manages Application Centric Infrastructure (ACI) data center fabric. The API operates on the ACI Management Information Model and supports tenants, application profiles, endpoi
  name: Cisco APIC REST API
  slug: apic-rest-api
- description: The UCS Manager XML API is the legacy programmatic interface for managing Cisco Unified Computing System blade and rack servers. The API uses an XML over HTTPS request-response model targeting the UCS
  name: Cisco UCS Manager API
  slug: ucs-manager-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Authentication API from Cisco Hardware — 1 operation(s) for authentication.
  name: Cisco Hardware Authentication API
  slug: cisco-hardware-authentication-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The CommandRunner API from Cisco Hardware — 1 operation(s) for commandrunner.
  name: Cisco Hardware CommandRunner API
  slug: cisco-hardware-commandrunner-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Devices API from Cisco Hardware — 3 operation(s) for devices.
  name: Cisco Hardware Devices API
  slug: cisco-hardware-devices-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Discovery API from Cisco Hardware — 1 operation(s) for discovery.
  name: Cisco Hardware Discovery API
  slug: cisco-hardware-discovery-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Network API from Cisco Hardware — 1 operation(s) for network.
  name: Cisco Hardware Network API
  slug: cisco-hardware-network-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Sites API from Cisco Hardware — 1 operation(s) for sites.
  name: Cisco Hardware Sites API
  slug: cisco-hardware-sites-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The Topology API from Cisco Hardware — 1 operation(s) for topology.
  name: Cisco Hardware Topology API
  slug: cisco-hardware-topology-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication API
  slug: open-cisco-hardware-authentication-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication CommandRunner API
  slug: open-cisco-hardware-commandrunner-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication Devices API
  slug: open-cisco-hardware-devices-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication Discovery API
  slug: open-cisco-hardware-discovery-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication Network API
  slug: open-cisco-hardware-network-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication Sites API
  slug: open-cisco-hardware-sites-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent Authentication Topology API
  slug: open-cisco-hardware-topology-api
- collection_type: open
  name: Cisco Catalyst Center (DNA Center) Intent API
  slug: open-cisco-hardware
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-hardware-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-hardware-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-hardware-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-hardware-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.cisco.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cisco.com/docs/
- group: start
  title: ''
  type: Sandbox
  url: https://devnetsandbox.cisco.com/
- group: build
  title: ''
  type: Code Exchange
  url: https://developer.cisco.com/codeexchange/
- group: learn
  title: ''
  type: Learning
  url: https://developer.cisco.com/learning/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/site/support/
- group: operate
  title: ''
  type: Community
  url: https://community.cisco.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end_user_license_agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cisco-hardware-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/cisco-hardware-rules.yml
created: '2024-01-15'
description: Cisco Hardware is an aggregated index of programmable interfaces for managing Cisco network and data center hardware, including routers, switches, wireless access points, data center fabric, and unified computing systems. The index covers Cisco Catalyst Center (formerly DNA Center), Meraki cloud-managed devices, IOS XE RESTCONF, ACI APIC, UCS Manager, and Intersight cloud infrastructure management. Cisco hardware APIs are exposed through Cisco DevNet, with sandboxes available for developers to test integrations against live hardware without owning physical devices.
finops:
- name: Cisco Hardware Finops
  service_category: API
  slug: cisco-hardware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cisco-hardware.png
jsonld:
- class_count: 19
  name: Cisco Hardware Context
  property_count: 0
  slug: cisco-hardware-context
layout: provider
modified: '2026-08-19'
name: Cisco Hardware
nav: Providers
network: true
overview: 'Cisco Hardware publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, CommandRunner API, Devices API, and 4 more. Tagged areas include Hardware, Infrastructure, Networking, Router, and Switches.


  The Cisco Hardware catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Hardware''s developer surface includes authentication, developer portal, documentation, sandbox, support, and 12 more developer resources.'
plans:
- name: Cisco Hardware Plans Pricing
  plan_count: 3
  slug: cisco-hardware-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Cisco Hardware Rate Limits
  slug: cisco-hardware-rate-limits
rules:
- effective_rule_count: 74
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Cisco Hardware API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 3
  slug: cisco-hardware-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 45.5
    contract_quality: 17.3
    developer_ergonomics: 75.0
    discoverability: 59.3
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-hardware/refs/heads/main/screenshots/cisco-hardware-2026-06-20T174357.png
security:
- kind: authentication
  name: Cisco Hardware Authentication
  slug: cisco-hardware-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cisco Hardware Domain Security
  slug: cisco-hardware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cisco Hardware Vulnerability Disclosure
  slug: cisco-hardware-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cisco-hardware
tags:
- Hardware
- Infrastructure
- Networking
- Router
- Switches
website: https://developer.cisco.com/
---
