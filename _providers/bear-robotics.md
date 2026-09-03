---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Bear Robotics Agentic Access
  operation_count: 23
  slug: bear-robotics-agentic-access
  summary_line: 23 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The on-robot gRPC service for direct local control of a Bear robot, used where the cloud is not in the path. 23 RPCs covering drive/twist commands, odometry, battery and robot status, missions, settin
  name: Bear Base API
  slug: bear-base-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Carti-specific operations
  name: Bear Robotics Carti API
  slug: bear-robotics-carti-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Fleet-level operations
  name: Bear Robotics Fleet Management API
  slug: bear-robotics-fleet-management-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Low-level endpoints for robot pose and localization
  name: Bear Robotics Localization & Navigation API
  slug: bear-robotics-localization-navigation-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Operations for fetching and setting location and map settings
  name: Bear Robotics Locations & Maps API
  slug: bear-robotics-locations-maps-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Basic mission-related operations
  name: Bear Robotics Mission API
  slug: bear-robotics-mission-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Queries for real-time robot status data
  name: Bear Robotics Robot Status API
  slug: bear-robotics-robot-status-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: System-level operations and Queries for static robot configurations
  name: Bear Robotics Robot System API
  slug: bear-robotics-robot-system-api
- baseURL: https://api.bearrobotics.ai
  baseurl_source: declared
  description: Servi-specific operations
  name: Bear Robotics Servi API
  slug: bear-robotics-servi-api
artifact_total: 23
asyncapis:
- description: ''
  name: Bear Robotics Webhooks
  slug: bear-robotics-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bear Cloud Carti API
  slug: open-bear-robotics-carti-api
- collection_type: open
  name: API Collection
  slug: open-bear-robotics-cloud-v1-3-postman-collection
- collection_type: open
  name: Bear Cloud Fleet Management API
  slug: open-bear-robotics-fleet-management-api
- collection_type: open
  name: Bear Cloud Localization & Navigation API
  slug: open-bear-robotics-localization-navigation-api
- collection_type: open
  name: Bear Cloud Locations & Maps API
  slug: open-bear-robotics-locations-maps-api
- collection_type: open
  name: Bear Cloud Mission API
  slug: open-bear-robotics-mission-api
- collection_type: open
  name: Bear Cloud Robot Status API
  slug: open-bear-robotics-robot-status-api
- collection_type: open
  name: Bear Cloud Robot System API
  slug: open-bear-robotics-robot-system-api
- collection_type: open
  name: Bear Cloud Servi API
  slug: open-bear-robotics-servi-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bear-robotics-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.bearrobotics.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.api.bearrobotics.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.api.bearrobotics.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.api.bearrobotics.ai/v1.3/resources/RestAPI/
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.api.bearrobotics.ai/guides/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bearrobotics-public
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/44195110/2sBXwto8ex
- group: company
  title: ''
  type: Blog
  url: https://www.bearrobotics.ai/blog
- group: start
  title: ''
  type: Login
  url: https://universe.bearrobotics.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bearrobotics.ai/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bearrobotics.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/bear-robotics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bear-robotics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bear-robotics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bear-robotics-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/bear-robotics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bear-robotics-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bear-robotics-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bear-robotics-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/bear-robotics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bear-robotics-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/v1/bear-robotics-services-cloud-api_service.proto
- group: other
  title: ''
  type: Overlay
  url: overlays/bear-robotics-cloud-overlay.yaml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bear-robotics-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bear-robotics-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bear-robotics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bear-robotics-domain-security.yml
created: '2026-08-06'
description: 'Bear Robotics builds AI-driven autonomous mobile robots for hospitality and service environments — the Servi family (Servi, Servi Plus, Servi Q, Servi Clean) for restaurants, senior living, hotels and hospitals, the Carti cargo line for warehouses and factories, and Kinisi — all managed through the Bear Universe cloud fleet platform. Founded in 2017 by former Google engineer John Ha, headquartered in Redwood City, California, and now majority-owned by LG Electronics. Bear publishes a genuinely open, gRPC-first third-party developer surface: the Bear Cloud API (39 RPCs, 27 unary and 12 server-streaming) for creating missions, streaming robot state and managing fleets, plus an on-robot Bear Base API for direct local control. The Protobuf definitions are published under MPL-2.0 in a public GitHub organization, an OpenAPI 3.0.3 document covers the transcoded REST projection, and v1.3 added outbound webhooks. API keys are issued through an account manager rather than self-serve
  signup.'
image: http://static1.squarespace.com/static/652cbb3fb1f91809d4610dc0/t/6a3dc3f863ff8c5ce8254bd0/1782432760376/og-bear-robotics-default.webp?format=1500w
layout: provider
modified: '2026-08-06'
name: Bear Robotics
nav: Providers
network: true
overview: 'Bear Robotics publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Carti API, Fleet Management API, Localization & Navigation API, and 5 more. Tagged areas include Robotics, Autonomous Mobile Robots, Fleet Management, Hospitality, and Food Service.


  The Bear Robotics catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Bear Robotics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, and 23 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 57.4
    developer_ergonomics: 66.1
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 44.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bear-robotics/refs/heads/main/screenshots/bear-robotics-2026-08-07T162236.png
security:
- kind: authentication
  name: Bear Robotics Authentication
  slug: bear-robotics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bear Robotics Domain Security
  slug: bear-robotics-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: bear-robotics
tags:
- Robotics
- Autonomous Mobile Robots
- Fleet Management
- Hospitality
- Food Service
- Logistics
- gRPC
- Protobuf
- Webhook
- Internet of Things
- Company
website: https://www.bearrobotics.ai/
---
