---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'The ANELLO device interface: an ASCII sentence protocol (#APIMU, #APIM1, #APGPS, #APHDG, #APINS, #APAHRS output; #APCFG, #APVEH, #APODO, #APPNG, #APECH, #APRST input) plus an RTCM 10403 binary framing'
  name: ANELLO Device Messaging Protocol
  slug: anello-device-messaging-protocol
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anello-photonics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anellophotonics.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs-a1.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs-a1.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs-a1.readthedocs.io/en/latest/communication_messaging.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs-a1.readthedocs.io/en/latest/getting_started_quick.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Anello-Photonics
- group: company
  title: ''
  type: Blog
  url: https://www.anellophotonics.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.anellophotonics.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anellophotonics.com/privacy-policy
- group: other
  title: ''
  type: Downloads
  url: https://www.anellophotonics.com/downloads
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anello-photonics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/anello-photonics-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anello-photonics-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/anello-photonics-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anello-photonics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anello-photonics-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anello-photonics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anello-photonics-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anello-photonics-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anello-photonics-changelog.yml
- group: other
  title: ''
  type: ROSInterface
  url: ros/anello-photonics-ros-interfaces.yml
created: '2026-08-06'
description: 'ANELLO Photonics is a Santa Clara, California company building solid-state, high-precision inertial navigation and sensing products for positioning, navigation and orientation when GNSS is jammed, spoofed, blocked or otherwise unavailable. Its products are powered by SiPhOG (Silicon Photonics Optical Gyroscope), a chip-scale optical gyroscope built on standard semiconductor processes. The developer surface is an embedded one rather than a web API: ANELLO Ground INS, Ground IMU, Maritime INS, Aerial INS, X3 IMU and the Evaluation Kit expose a documented ASCII and RTCM-binary message protocol over RS-232 serial, USB-C and UDP/Ethernet, with a public developer manual, a first-party Python configuration and logging tool, a ROS/ROS2 driver that publishes machine-readable .msg/.srv interface definitions, and PX4/ArduPilot and MAVLink integrations.'
image: https://static1.squarespace.com/static/60404157b68a5453a865f98e/t/6a2742eefb5f0723d0178a9c/1624159401076/social.png?format=1500w
layout: provider
modified: '2026-08-06'
name: ANELLO Photonics
nav: Providers
network: true
overview: 'ANELLO Photonics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Inertial Navigation, Optical Gyroscope, Silicon Photonics, and GNSS.


  ANELLO Photonics'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, changelog, and 15 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 23.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 66.7
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 23.9
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anello-photonics/refs/heads/main/screenshots/anello-photonics-2026-08-07T161404.png
security:
- kind: domain-security
  name: Anello Photonics Domain Security
  slug: anello-photonics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anello-photonics
tags:
- Company
- Inertial Navigation
- Optical Gyroscope
- Silicon Photonics
- GNSS
- GPS-Denied Navigation
- Sensors
- Robotics
- Defense
- Autonomous Vehicles
- Embedded Systems
- IMU
website: https://www.anellophotonics.com/
---
