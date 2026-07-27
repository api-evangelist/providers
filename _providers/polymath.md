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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 18
  human_in_the_loop: 4
  name: Polymath Agentic Access
  operation_count: 37
  slug: polymath-agentic-access
  summary_line: 37 operations · 18 acting · 4 human-in-the-loop
api_count: 10
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
artifact_total: 14
common:
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
  name: polymath-mcp.yml
  slug: polymath-mcpyml
modified: '2026-07-20'
name: Polymath Robotics
nav: Providers
network: true
overview: 'Polymath Robotics publishes 10 APIs on the [APIs.io](https://apis.io/) network, including CANBus API, filesystem API, Health Check API, and 7 more. Tagged areas include Robotics, Autonomy, Industrial Vehicles, Off-Highway, and Machine Learning.


  Polymath Robotics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 15 more developer resources.'
random_paper: 62
score:
  band: thin
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 52.1
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 42.7
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Machine Learning
- Simulation
- Teleoperation
- Automation
- Artificial Intelligence
- Unmanned Vehicles
website: https://www.polymathrobotics.com/
---
