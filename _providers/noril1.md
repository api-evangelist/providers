---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: '@nori/sdk — robot-local teleoperation SDK. Connects to a Nori robot over WebRTC, receives video and telemetry, and drives it from the browser via the RemoteTeleop client. Signaling over the reference '
  name: Nori Teleoperation SDK
  slug: nori-teleoperation-sdk
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.norirobotics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.norirobotics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.norirobotics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.norirobotics.com/sdk/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.norirobotics.com/guide/
- group: operate
  title: ''
  type: Support
  url: https://docs.norirobotics.com/troubleshooting/getting-help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nori-Robotics
- group: other
  title: ''
  type: X
  url: https://x.com/NoriRobotics
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/dH8DwTpYD
- group: build
  title: ''
  type: Packages
  url: packages/noril1-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/noril1-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/noril1-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/noril1-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/noril1-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/noril1-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/noril1-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/noril1-domain-security.yml
created: '2026-07-17'
description: 'Nori (Nori Robotics) is a Y Combinator (Summer 2026) hard-tech company in San Francisco building affordable bimanual humanoid home robots — the NORI L2, a sub-$1,300 wheeled robot with dual Z-axis lift arms that autonomously handles household chores like loading dishes, making beds, food prep, and cleaning, with multiple units able to collaborate on coordinated tasks. Beyond the hardware, Nori publishes a developer surface: the @nori/sdk robot-local teleoperation SDK connects to a robot over WebRTC to stream video and telemetry and drive it from the browser in ~20 lines, with all safety mechanisms (clamping, watchdog, E-STOP, motor torque lifecycle) enforced on the robot''s control daemon. The SDK targets the nori-protocol v1 wire format (NDJSON over a WebRTC data channel to the daemon on port 7777), is Apache-2.0 licensed, and is distributed to a small set of collaborating developers as a tarball rather than on public npm.'
image: https://docs.norirobotics.com/nori-logo.png
layout: provider
modified: '2026-07-20'
name: Nori
nav: Providers
network: true
overview: 'Nori publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Humanoid Robots, Teleoperation, and SDK.


  Nori''s developer surface includes documentation, API reference, getting-started guide, support, and 13 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 17.5
  provenance:
    conformance: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noril1/refs/heads/main/screenshots/noril1-2026-08-07T185516.png
security:
- kind: domain-security
  name: Noril1 Domain Security
  slug: noril1-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: noril1
tags:
- Company
- Robotics
- Humanoid Robots
- Teleoperation
- SDK
- WebRTC
- Hardware
- Home Automation
- Developer Tools
- Y Combinator
website: https://www.norirobotics.com/
---
