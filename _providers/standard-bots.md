---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.2
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'On-robot REST API (served by the RO1 control box on /api/v1, Bearer-token auth) for controlling arm position and motion, the gripper/end-effector, cameras, routines, teleoperation, the recorder, I/O, '
  name: RO1 Robotics REST API
  slug: ro1-robotics-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/standard-bots-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://standardbots.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://standardbots.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.standardbots.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.standardbots.com/docs/rest-api/
- group: operate
  title: ''
  type: Support
  url: https://standardbots.com/support
- group: company
  title: ''
  type: Blog
  url: https://standardbots.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/standardbots
- group: start
  title: ''
  type: Login
  url: https://admin.standardbots.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://standardbots.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://standardbots.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/standard-bots-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/standard-bots-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/standard-bots-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/standard-bots-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/standard-bots-error-codes.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/standard-bots-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/standard-bots-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/standard-bots-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/standard-bots-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/standard-bots-sandbox.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/standard-bots-external-control.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/standard-bots-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Standard Bots designs and builds AI-native industrial robotic arms — the RO1 family (Spark, Core/RO1, Thor, and the Bolt beta) — designed and assembled in the USA for machine tending, welding, palletizing, pick & place, and inspection. The robots ship with a developer platform, "StandardOS", that exposes a Bearer-token REST API served on the robot control box (/api/v1) for controlling arm motion, the gripper/end-effector, cameras, routines, teleoperation, recording, I/O and fault recovery. Alongside the REST API, Standard Bots publishes an official Python SDK (PyPI: standardbots), a realtime protobuf external-control streaming channel, and a ROS2 bridge (Cyclone DDS) with MoveIt and Modbus tooling — making the RO1 programmable both for high-level orchestration and low-latency realtime control.'
image: https://assets-global.website-files.com/63d925b46a84dec214bc0bbd/6408ee2c083a0474a480124a_OG%20Image-Home.jpg
layout: provider
modified: '2026-07-21'
name: Standard Bots
nav: Providers
network: true
overview: 'Standard Bots publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Industrial Automation, Robotic Arm, and Manufacturing.


  Standard Bots'' developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 18 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 44.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 29.6
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/standard-bots/refs/heads/main/screenshots/standard-bots-2026-09-02T160741.png
security:
- kind: authentication
  name: Standard Bots Authentication
  slug: standard-bots-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Standard Bots Domain Security
  slug: standard-bots-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: standard-bots
tags:
- Company
- Robotics
- Industrial Automation
- Robotic Arm
- Manufacturing
- Artificial Intelligence
- Machine Tending
- Developer API
- ROS 2
- Physical AI
website: https://standardbots.com
---
