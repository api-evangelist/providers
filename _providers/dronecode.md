---
access_model:
  confidence: high
  label: Free and open source · no account, no key, no quota
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - license
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-06'
api_count: 4
apis:
- description: PX4 is the open source flight control firmware the Dronecode Foundation stewards — the software running on the vehicle that MAVLink and MAVSDK talk to. It exposes no network API of its own; its progra
  name: PX4 Autopilot
  slug: dronecode-api
- description: MAVSDK is the Dronecode Foundation's programmable interface to any MAVLink vehicle, and the only surface in the estate with a full machine-readable contract. 38 protobuf services and 387 RPCs cover ar
  name: MAVSDK gRPC API
  slug: mavsdk
- description: MAVLink is the message-level interoperability standard for drones, and the Dronecode Foundation publishes it. The contract is the dialect XML — 19 files including common.xml, standard.xml, minimal.xml
  name: MAVLink Protocol
  slug: mavlink
- description: 'The only HTTP API the Foundation itself hosts, and the one its RFC 9727 /.well-known/api-catalog advertises. The discovery root is anonymous and lists 74 routes across 7 namespaces; the wp/v2 content '
  name: dronecode.org WordPress REST API
  slug: dronecode-org-rest
artifact_total: 16
common:
- group: company
  title: ''
  type: Website
  url: https://www.dronecode.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dronecode.org/projects/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.px4.io/
- group: docs
  title: ''
  type: APIReference
  url: https://mavsdk.mavlink.io/main/en/cpp/api_reference/index.html
- group: start
  title: ''
  type: Quickstart
  url: https://mavsdk.mavlink.io/main/en/python/quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://discuss.px4.io/
- group: operate
  title: ''
  type: Community
  url: https://lists.dronecode.org/groups
- group: company
  title: ''
  type: Blog
  url: https://dronecode.org/feed/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Dronecode
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mavlink
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/PX4
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dronecode-foundation
- group: commercial
  title: ''
  type: Pricing
  url: https://dronecode.org/membership/
- group: start
  title: ''
  type: SignUp
  url: https://discuss.px4.io/signup
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://dronecode.org/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dronecode.org/privacy-policy/
- group: commercial
  title: ''
  type: Plans
  url: plans/dronecode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dronecode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dronecode-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dronecode-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dronecode-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/dronecode-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/dronecode-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dronecode-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dronecode-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dronecode-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dronecode-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dronecode-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dronecode-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dronecode-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/dronecode-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dronecode-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dronecode-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dronecode-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dronecode-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dronecode-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/dronecode-api-catalog.json
created: '2026-03-16'
description: 'The Dronecode Foundation is a vendor-neutral Linux Foundation collaborative project and the home of the open source flight stack the drone industry runs on: PX4 Autopilot, the MAVLink communication protocol, MAVSDK, QGroundControl and the Pixhawk hardware standards. Its machine-readable surface is a gRPC one — MAVSDK-Proto publishes 38 protobuf services and 387 RPCs covering arming, takeoff, missions, geofencing, telemetry, camera, gimbal and parameter control — alongside the MAVLink dialect XML and the component-metadata JSON Schemas that define how vehicles describe themselves. Nothing is hosted: the consumer runs mavsdk_server themselves, and every contract, SDK and firmware is free and open source.'
finops:
- name: Dronecode Finops
  service_category: API
  slug: dronecode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dronecode.png
json_schemas:
- name: Dronecode Mavlink Component Metadata Actuators.Schema
  property_count: 6
  slug: dronecode-mavlink-component-metadata-actuators.schema
- name: Dronecode Mavlink Component Metadata General.Schema
  property_count: 6
  slug: dronecode-mavlink-component-metadata-general.schema
- name: Dronecode Mavlink Component Metadata Parameter.Schema
  property_count: 3
  slug: dronecode-mavlink-component-metadata-parameter.schema
- name: Dronecode Mavlink Component Metadata Peripherals.Schema
  property_count: 2
  slug: dronecode-mavlink-component-metadata-peripherals.schema
- name: Dronecode Mavlink Component Metadata Translation.Schema
  property_count: 1
  slug: dronecode-mavlink-component-metadata-translation.schema
layout: provider
mcp_servers:
- description: Derived candidate tool list. Dronecode publishes no MCP server — deployment.mode is none.
  name: MCP candidate (no server published)
  slug: mcp-candidate-no-server-published
modified: '2026-09-06'
name: Dronecode Foundation
nav: Providers
network: true
overview: 'Dronecode Foundation publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Drones, UAV, Robotics, MAVLink, and PX4.


  Dronecode Foundation''s developer surface includes documentation, API reference, quickstart, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Dronecode Plans Pricing
  plan_count: 0
  slug: dronecode-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Dronecode Rate Limits
  slug: dronecode-rate-limits
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 35.8
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 40.0
    developer_ergonomics: 68.5
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 11.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.19.0
  scored_at: '2026-09-06'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dronecode/refs/heads/main/screenshots/dronecode-2026-06-20T180242.png
security:
- kind: authentication
  name: Dronecode Authentication
  slug: dronecode-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Dronecode Domain Security
  slug: dronecode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dronecode Vulnerability Disclosure
  slug: dronecode-vulnerability-disclosure
  summary_line: Hackerone
slug: dronecode
tags:
- Drones
- UAV
- Robotics
- MAVLink
- PX4
- Autopilot
- Aerial Robotics
- gRPC
- Open Source
- Linux Foundation
website: https://www.dronecode.org/
---
