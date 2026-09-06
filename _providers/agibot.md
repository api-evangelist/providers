---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The AimDK protocol is AgiBot's first-party Protocol Buffers definition of its robots' interfaces, published as the aimrt_protocol repository of Link-U OS. It defines 33 gRPC services and 175 RPCs acro
  name: AimDK Protocol (Link-U OS Robot Interface)
  slug: aimdk-protocol
- description: AimDK_X2 is the published secondary-development SDK for the AgiBot X2 humanoid. It exposes the robot to Python and C++ programs through five documented interface modules — a control module (motion mod
  name: AimDK_X2 SDK
  slug: aimdk-x2
- description: The AGIBOT online store implements the Universal Commerce Protocol (UCP) for agent-driven commerce and exposes a live, anonymous, hosted Model Context Protocol endpoint. A JSON-RPC 2.0 tools/list call
  name: AGIBOT Store Agent Commerce API (UCP / MCP)
  slug: store-commerce
artifact_total: 9
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Link-U-OS/aimrt_protocol/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agibot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agibot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agibot.com/DOCS/OS
- group: docs
  title: ''
  type: Documentation
  url: https://www.agibot.com/filepage/282.html
- group: docs
  title: ''
  type: APIReference
  url: https://x2-aimdk.agibot.com/en/latest/Interface/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://x2-aimdk.agibot.com/en/latest/quick_start/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgibotTech
- group: company
  title: ''
  type: Blog
  url: https://www.agibot.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.agibot.com/Contact/Business
- group: commercial
  title: ''
  type: Pricing
  url: https://store.agibot.com/collections/all
- group: start
  title: ''
  type: Login
  url: https://store-account.agibot.com/authentication/oauth/authorize
- group: commercial
  title: ''
  type: TermsOfService
  url: https://store.agibot.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agibot.com/AGIBOT%20Website%20Privacy%20Policy.pdf
- group: other
  title: ''
  type: Protobuf
  url: grpc/agibot-aimdk-protocol-index.yml
- group: build
  title: ''
  type: Packages
  url: packages/agibot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agibot-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agibot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agibot-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agibot-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agibot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agibot-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agibot-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agibot-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agibot-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agibot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/agibot-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/agibot-changelog.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/agibot-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/agibot-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agibot-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/agibot-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/agibot-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: 'AgiBot (AGIBOT Innovation (Shanghai) Technology Co., Ltd., known in Chinese as Zhiyuan Robotics / 智元机器人) is a Shanghai-based embodied-intelligence company founded in 2023 that designs and mass-produces humanoid and wheeled service robots — the Expedition A2/A3 full-size humanoids, the X1/X2 open-source bipeds, the Genie G1/G2 and D1 series, the C5, and the OmniHand dexterous hands. Its developer surface is not a public web API but a robotics contract stack: AimRT, an in-house C++20 runtime and middleware compatible with ROS 2, gRPC, HTTP, MQTT, Zenoh and Iceoryx; Link-U OS, an open-source embodied operating system; and the AimDK protocol, a first-party Protocol Buffers definition of the robot itself — hardware abstraction (hands, arms, audio, lights, neck, battery management, cameras, temperature, emergency stop), motion control, kinematics, force control, teleoperation and a health-and-diagnostics service. AgiBot also publishes the AgiBot World dataset, the Genie Sim simulation
  platform, and runs an online store that implements the Universal Commerce Protocol with a live hosted MCP endpoint for agent-driven purchasing.'
image: https://www.agibot.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: AgiBot MCP Server
  slug: agibot-mcp-server
modified: '2026-08-06'
name: AgiBot
nav: Providers
network: true
overview: 'AgiBot publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Humanoid Robots, Embodied AI, and Artificial Intelligence.


  AgiBot''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 27 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agibot Rate Limits
  slug: agibot-rate-limits
scopes:
- name: Agibot Scopes
  scope_count: 0
  slug: agibot-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 80.4
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 44.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agibot/refs/heads/main/screenshots/agibot-2026-08-07T161032.png
security:
- kind: authentication
  name: Agibot Authentication
  slug: agibot-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agibot Domain Security
  slug: agibot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agibot Vulnerability Disclosure
  slug: agibot-vulnerability-disclosure
  summary_line: contact published
slug: agibot
tags:
- Company
- Robotics
- Humanoid Robots
- Embodied AI
- Artificial Intelligence
- Manufacturing
- Hardware
- Middleware
- ROS 2
- gRPC
- Protocol Buffers
- Simulation
- Machine-Learning
- Open-Source
- MCP
- Agentic Commerce
- China
website: https://www.agibot.com/
---
