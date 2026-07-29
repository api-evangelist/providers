---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The AGL Application Framework provides APIs for managing applications on the AGL platform including installation, lifecycle management, permission enforcement, and inter-application communication. App
  name: AGL Application Framework API
  slug: agl-application-framework-api
- description: 'AGL uses SOME/IP (Scalable service-Oriented MiddlewarE over IP) via the vSomeIP library for vehicle service communication. This enables microservice communication between ECUs over Ethernet using the '
  name: AGL VSOMEIP Service API
  slug: vsomeip-service-api
- description: The AGL SoDeV (Software Defined Vehicle) reference platform provides APIs for software-defined vehicle architectures that decouple software from hardware. SoDeV builds on Zephyr RTOS and meta-AGL laye
  name: AGL SoDeV Software Defined Vehicle API
  slug: sodev-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automotive-grade-linux-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.automotivelinux.org/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/automotive-grade-linux
- group: company
  title: ''
  type: Website
  url: https://www.automotivelinux.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.automotivelinux.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/automotive-grade-linux
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/automotive-grade-linux/meta-agl-monorepo
created: '2026-03-16'
description: Automotive Grade Linux (AGL) is a collaborative open source project under the Linux Foundation that develops a unified software platform for connected vehicles. AGL brings together automakers (Toyota, Honda, Mercedes-Benz), suppliers, and technology companies to build an open Linux-based software stack for in-vehicle infotainment, instrument clusters, telematics, and software-defined vehicle (SoDeV) architectures. The platform decouples software from hardware enabling rapid automotive application development.
features:
- description: AGL uses the Yocto Project and OpenEmbedded build framework with meta-AGL layers for creating customized embedded Linux distributions targeting automotive hardware platforms including Renesas R-Car and Raspberry Pi.
  name: Yocto-Based Build System
- description: Service-oriented in-vehicle communication using the SOME/IP protocol via vSomeIP for microservice architectures across ECUs over automotive Ethernet networks.
  name: SOME/IP Vehicle Services
- description: AGL SoDeV reference platform for decoupling software from hardware, enabling flexible, updatable in-vehicle software architectures using Zephyr RTOS and container-based application isolation.
  name: Software Defined Vehicle (SoDeV)
- description: OTA update framework for delivering software updates to AGL-based in-vehicle systems without physical access, supporting fleet-wide update management.
  name: Over-The-Air Updates
- description: Wayland/Weston-based display framework for in-vehicle infotainment and digital instrument cluster applications with automotive-grade display requirements.
  name: IVI and Instrument Cluster Support
finops:
- name: Automotive Grade Linux Finops
  service_category: API
  slug: automotive-grade-linux-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/automotive-grade-linux.png
integrations:
- description: Integration with the COVESA Vehicle Signal Specification (VSS) for standardized access to vehicle sensor and actuator data.
  name: COVESA Vehicle Signal Specification
- description: Integration with Eclipse KUKSA for vehicle signal API abstraction enabling portable in-vehicle application development.
  name: Eclipse KUKSA
- description: AGL SoDeV integrates Zephyr RTOS for safety-critical microcontroller domains within software-defined vehicle architectures.
  name: Zephyr RTOS
- description: Primary hardware reference platform support for Renesas R-Car SoCs used in production automotive IVI and cluster systems.
  name: Renesas R-Car Platforms
layout: provider
modified: '2026-04-19'
name: Automotive Grade Linux
nav: Providers
network: true
overview: 'Automotive Grade Linux publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Connected Vehicles, Embedded Linux, In-Vehicle Infotainment, and IoT.


  Automotive Grade Linux''s developer surface includes engineering blog, documentation, and 5 more developer resources.'
plans:
- name: Automotive Grade Linux Plans Pricing
  plan_count: 3
  slug: automotive-grade-linux-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Automotive Grade Linux Rate Limits
  slug: automotive-grade-linux-rate-limits
score:
  band: emerging
  composite: 21.3
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automotive-grade-linux/refs/heads/main/screenshots/automotive-grade-linux-2026-06-20T172702.png
security:
- kind: domain-security
  name: Automotive Grade Linux Domain Security
  slug: automotive-grade-linux-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: automotive-grade-linux
tags:
- Automotive
- Connected Vehicles
- Embedded Linux
- In-Vehicle Infotainment
- IoT
- Linux Foundation
- Open Source
- Software Defined Vehicles
use_cases:
- description: Develop navigation, media, and connectivity applications for automotive head units using AGL application framework APIs and the Wayland display system.
  name: In-Vehicle Infotainment Development
- description: Build telematics, V2X communication, and cloud connectivity capabilities on AGL-based vehicle computing platforms.
  name: Connected Car Platform
- description: Design vehicle software architectures that decouple application software from hardware using AGL SoDeV as the foundation platform.
  name: Software Defined Vehicle Architecture
- description: Create digital instrument cluster applications for speedometers, tachometers, and ADAS status displays using AGL display APIs.
  name: Instrument Cluster Applications
website: https://www.automotivelinux.org
---
