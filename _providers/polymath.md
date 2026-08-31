---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 4
  name: Polymath Agentic Access
  operation_count: 37
  slug: polymath-agentic-access
  summary_line: 37 operations · 18 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: The CANBus API from Polymath Robotics — 1 operation(s) for canbus.
  name: Polymath Robotics CANBus API
  slug: polymath-canbus-api
- description: The filesystem API from Polymath Robotics — 3 operation(s) for filesystem.
  name: Polymath Robotics filesystem API
  slug: polymath-filesystem-api
- description: Contains UUID endpoint that can be used to health check the robot
  name: Polymath Robotics Health Check API
  slug: polymath-health-check-api
- description: The Livekit API from Polymath Robotics — 4 operation(s) for livekit.
  name: Polymath Robotics Livekit API
  slug: polymath-livekit-api
- description: All endpoints related to interacting with Robot's media resources
  name: Polymath Robotics Media API
  slug: polymath-media-api
- description: The ros API from Polymath Robotics — 1 operation(s) for ros.
  name: Polymath Robotics ros API
  slug: polymath-ros-api
- description: The systemd API from Polymath Robotics — 1 operation(s) for systemd.
  name: Polymath Robotics systemd API
  slug: polymath-systemd-api
- description: Endpoints for managing control leases
  name: Polymath Robotics Teleop Control API
  slug: polymath-teleop-control-api
- description: All endpoints related to interacting with Robot's autonomy operations here
  name: Polymath Robotics Vehicle Autonomy API
  slug: polymath-vehicle-autonomy-api
- description: All endpoints related to interacting with Robot's vehicle operations here
  name: Polymath Robotics Vehicle Operations API
  slug: polymath-vehicle-operations-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polymath API Service CANBus API
  slug: open-polymath-canbus-api
- collection_type: open
  name: Polymath API Service CANBus filesystem API
  slug: open-polymath-filesystem-api
- collection_type: open
  name: Polymath API Service CANBus Health Check API
  slug: open-polymath-health-check-api
- collection_type: open
  name: Polymath API Service CANBus Livekit API
  slug: open-polymath-livekit-api
- collection_type: open
  name: Polymath API Service CANBus Media API
  slug: open-polymath-media-api
- collection_type: open
  name: Polymath API Service CANBus ros API
  slug: open-polymath-ros-api
- collection_type: open
  name: Polymath API Service CANBus systemd API
  slug: open-polymath-systemd-api
- collection_type: open
  name: Polymath API Service CANBus Teleop Control API
  slug: open-polymath-teleop-control-api
- collection_type: open
  name: Polymath API Service CANBus Vehicle Autonomy API
  slug: open-polymath-vehicle-autonomy-api
- collection_type: open
  name: Polymath API Service CANBus Vehicle Operations API
  slug: open-polymath-vehicle-operations-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/polymath-synapse-v2-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://synapse.docs.polymathrobotics.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://synapse.docs.polymathrobotics.dev/docs/reference
- group: docs
  title: ''
  type: APIReference
  url: https://synapse.docs.polymathrobotics.dev/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://synapse.docs.polymathrobotics.dev/docs/guides/authentication
- group: company
  title: ''
  type: Blog
  url: https://www.polymathrobotics.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@polymathrobotics.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polymathrobotics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polymathrobotics.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polymathrobotics.com/legal/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.polymathrobotics.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/polymathrobotics/caladan_examples
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polymath-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polymath-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/polymath-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/polymath-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polymath-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/polymath-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polymath-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polymath-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/polymath-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polymath-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Polymath Robotics builds general autonomy and safety software for off-highway and industrial vehicles such as tractors, loaders, dozers, and mining trucks. Its Synapse REST API lets developers command a real or simulated Polymath-powered vehicle: sending GPS and relative waypoints, issuing motion and vehicle commands, reading combined autonomy, navigation, and vehicle feedback, managing exclusive teleoperation control leases, and streaming media over LiveKit. Caladan, its browser-based simulation environment, lets teams build and test autonomous behaviors in Python without ROS, Gazebo, or Linux before deploying to physical machines. Founded in 2021 (YC S22), San Francisco.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polymath.png
layout: provider
mcp_servers:
- description: ''
  name: Polymath Robotics MCP Server
  slug: polymath-robotics-mcp-server
modified: '2026-07-20'
name: Polymath Robotics
nav: Providers
network: true
overview: 'Polymath Robotics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CANBus API, filesystem API, Health Check API, and 7 more. Tagged areas include Robotics, Autonomy, Industrial Vehicles, Off-Highway, and Machine-Learning.


  Polymath Robotics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Polymath Authentication
  slug: polymath-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Polymath Domain Security
  slug: polymath-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polymath
tags:
- Robotics
- Autonomy
- Industrial Vehicles
- Off-Highway
- Machine-Learning
- Simulation
- Teleoperation
- Automation
- Artificial Intelligence
- Unmanned Vehicles
website: https://www.polymathrobotics.com/
---
