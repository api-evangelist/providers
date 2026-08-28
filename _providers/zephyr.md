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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The Zephyr kernel C API exposes scheduling, threading, synchronization, memory management, and timer services for real-time embedded applications. It is the foundation that device drivers and applicat
  name: Zephyr RTOS Kernel API
  slug: zephyr-kernel-api
- description: The Zephyr device driver subsystem exposes a uniform device model across GPIO, I2C, SPI, UART, ADC, sensors, displays, networking, USB, Bluetooth, and many other peripheral classes, configured through
  name: Zephyr Device Driver API
  slug: zephyr-device-driver-api
- description: The Zephyr networking stack exposes BSD-like sockets, TLS/DTLS, MQTT, CoAP, LWM2M, HTTP, WebSocket, gRPC, and connectivity layers including IPv4/IPv6, Wi-Fi, Thread, OpenThread, Matter, and BLE.
  name: Zephyr Networking API
  slug: zephyr-networking-api
artifact_total: 8
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/zephyrproject-rtos/zephyr/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zephyr-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-zephyr-project
- group: start
  title: ''
  type: Portal
  url: https://www.zephyrproject.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zephyrproject.org/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zephyrproject.org/apidoc/latest/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zephyrproject.org/latest/develop/getting_started/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zephyrproject-rtos
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zephyrproject-rtos/zephyr
- group: build
  title: ''
  type: SDKs
  url: https://github.com/zephyrproject-rtos/sdk-ng
- group: build
  title: ''
  type: CLI
  url: https://github.com/zephyrproject-rtos/west
- group: company
  title: ''
  type: Blog
  url: https://www.zephyrproject.org/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.zephyrproject.org/latest/releases/index.html
- group: learn
  title: ''
  type: Training
  url: https://www.zephyrproject.org/training-partner-program/
- group: other
  title: ''
  type: Events
  url: https://www.zephyrproject.org/events/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.zephyrproject.org/latest/security/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linuxfoundation.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linuxfoundation.org/privacy-policy/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/zephyr-context.jsonld
- group: other
  title: ''
  type: Resources
  url: vocabulary/zephyr-vocabulary.yml
created: '2026-03-16'
description: The Zephyr Project is a Linux Foundation project that delivers a small, scalable, secure, and open-source real-time operating system (RTOS) for resource-constrained embedded devices. Zephyr supports 1000+ boards across ARM Cortex, RISC-V, ARC, x86, Xtensa, and other architectures, ships with a C kernel, device drivers, networking stacks (BLE, Wi-Fi, Thread, Matter), security subsystems, and is supported by a meta-tool (west), an SDK (sdk-ng), and a broad ecosystem of training partners and commercial silicon and module vendors.
finops:
- name: Zephyr Finops
  service_category: API
  slug: zephyr-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zephyr.png
jsonld:
- class_count: 18
  name: Zephyr Context
  property_count: 0
  slug: zephyr-context
layout: provider
modified: '2026-05-03'
name: Zephyr Project
nav: Providers
network: true
overview: 'Zephyr Project publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded, IoT, Linux Foundation, RTOS, and Open-Source.


  The Zephyr Project catalog on APIs.io includes 1 JSON-LD context.


  Zephyr Project''s developer surface includes developer portal, documentation, API reference, getting-started guide, CLI, engineering blog, release notes, and 13 more developer resources.'
plans:
- name: Zephyr Plans Pricing
  plan_count: 3
  slug: zephyr-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Zephyr Rate Limits
  slug: zephyr-rate-limits
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 10.7
    developer_ergonomics: 54.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 32.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zephyr/refs/heads/main/screenshots/zephyr-2026-06-20T201826.png
security:
- kind: domain-security
  name: Zephyr Domain Security
  slug: zephyr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zephyr
tags:
- Embedded
- IoT
- Linux Foundation
- RTOS
- Open-Source
- Edge
website: https://www.zephyrproject.org/
---
