---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.8
  scored_at: '2026-11-06'
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
  description: The Devices API from Cisco Hardware — 3 operation(s) for devices.
  name: Cisco Hardware Devices API
  slug: cisco-hardware-devices-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The administered API from Cisco Hardware — 4 operation(s) for administered.
  name: Cisco Hardware Administered API
  slug: cisco-hardware-administered-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The appliance API from Cisco Hardware — 122 operation(s) for appliance.
  name: Cisco Hardware Appliance API
  slug: cisco-hardware-appliance-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The camera API from Cisco Hardware — 29 operation(s) for camera.
  name: Cisco Hardware Camera API
  slug: cisco-hardware-camera-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The campusGateway API from Cisco Hardware — 17 operation(s) for campusgateway.
  name: Cisco Hardware Campus Gateway API
  slug: cisco-hardware-campusgateway-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The cellularGateway API from Cisco Hardware — 16 operation(s) for cellulargateway.
  name: Cisco Hardware Cellular Gateway API
  slug: cisco-hardware-cellulargateway-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The insight API from Cisco Hardware — 4 operation(s) for insight.
  name: Cisco Hardware Insight API
  slug: cisco-hardware-insight-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The licensing API from Cisco Hardware — 8 operation(s) for licensing.
  name: Cisco Hardware Licensing API
  slug: cisco-hardware-licensing-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The networks API from Cisco Hardware — 75 operation(s) for networks.
  name: Cisco Hardware Networks API
  slug: cisco-hardware-networks-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The organizations API from Cisco Hardware — 182 operation(s) for organizations.
  name: Cisco Hardware Organizations API
  slug: cisco-hardware-organizations-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The sensor API from Cisco Hardware — 13 operation(s) for sensor.
  name: Cisco Hardware Sensor API
  slug: cisco-hardware-sensor-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The sm API from Cisco Hardware — 43 operation(s) for sm.
  name: Cisco Hardware Sm API
  slug: cisco-hardware-sm-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The spaces API from Cisco Hardware — 2 operation(s) for spaces.
  name: Cisco Hardware Spaces API
  slug: cisco-hardware-spaces-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The switch API from Cisco Hardware — 56 operation(s) for switch.
  name: Cisco Hardware Switch API
  slug: cisco-hardware-switch-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The wireless API from Cisco Hardware — 113 operation(s) for wireless.
  name: Cisco Hardware Wireless API
  slug: cisco-hardware-wireless-api
- baseURL: https://api.meraki.com/api/v1
  baseurl_source: declared
  description: The wirelessController API from Cisco Hardware — 15 operation(s) for wirelesscontroller.
  name: Cisco Hardware Wireless Controller API
  slug: cisco-hardware-wirelesscontroller-api
artifact_total: 37
collections:
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
- group: commercial
  href: https://artifacts.apis.io/cisco-hardware/plans/cisco-hardware-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cisco-hardware-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cisco-hardware/rate-limits/cisco-hardware-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cisco-hardware-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cisco-hardware/finops/cisco-hardware-finops.yml
  title: ''
  type: FinOps
  url: finops/cisco-hardware-finops.yml
- group: other
  href: https://artifacts.apis.io/cisco-hardware/capabilities/cisco-hardware-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cisco-hardware-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.cisco.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/cisco/
- group: agent
  href: https://artifacts.apis.io/cisco-hardware/agentic-access/cisco-hardware-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-hardware-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cisco-hardware/security/cisco-hardware-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cisco-hardware-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cisco-hardware/security/cisco-hardware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cisco-hardware-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cisco-hardware/authentication/cisco-hardware-authentication.yml
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
  href: https://artifacts.apis.io/cisco-hardware/json-ld/cisco-hardware-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cisco-hardware-context.jsonld
- group: design
  href: https://artifacts.apis.io/cisco-hardware/rules/cisco-hardware-rules.yml
  title: ''
  type: Spectral
  url: rules/cisco-hardware-rules.yml
created: '2024-01-15'
description: Cisco Hardware is an aggregated index of programmable interfaces for managing Cisco network and data center hardware, including routers, switches, wireless access points, data center fabric, and unified computing systems. The index covers Cisco Catalyst Center (formerly DNA Center), Meraki cloud-managed devices, IOS XE RESTCONF, ACI APIC, UCS Manager, and Intersight cloud infrastructure management. Cisco hardware APIs are exposed through Cisco DevNet, with sandboxes available for developers to test integrations against live hardware without owning physical devices.
finops:
- has_sources: false
  method: generated
  name: Cisco Hardware Finops
  primary_unit: request
  service_category: API
  slug: cisco-hardware-finops
  template: true
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
overview: 'Cisco Hardware publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Devices API, Administered API, Appliance API, and 17 more. Tagged areas include Hardware, Infrastructure, Networking, Router, and Switches.


  The Cisco Hardware catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cisco Hardware''s developer surface includes authentication, developer portal, documentation, sandbox, support, and 17 more developer resources.'
plans:
- name: Cisco Hardware Plans Pricing
  plan_count: 3
  slug: cisco-hardware-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Cisco Hardware Rate Limits
  slug: cisco-hardware-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 74
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
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 56.1
    developer_ergonomics: 75.0
    discoverability: 57.1
    operational_transparency: 34.2
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 66.7
      total: 24
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cisco-hardware/cisco-hardware-2026-06-20T174357.png
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
website: https://www.cisco.com/
---
