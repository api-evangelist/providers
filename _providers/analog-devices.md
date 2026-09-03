---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-09-02'
api_count: 4
apis:
- description: The libiio library provides a cross-platform C API for interfacing with Linux Industrial I/O (IIO) devices including ADCs, DACs, and RF transceivers. It supports local and remote device access via a n
  name: Analog Devices libiio API
  slug: libiio-api
- description: PyADI-IIO provides Python interfaces for ADI hardware with IIO drivers, enabling Python developers to interact with ADI evaluation boards and production hardware. It abstracts libiio with device-speci
  name: Analog Devices PyADI-IIO Python API
  slug: pyadi-iio-api
- description: CodeFusion Studio is ADI's embedded software development environment built on Visual Studio Code for ADI microcontrollers and DSPs. It provides graphical system configuration, code generation, debuggi
  name: Analog Devices CodeFusion Studio
  slug: codefusion-studio
- description: 'The ADI 3D Time-of-Flight SDK (libaditof, and the ADCAM application layer built on it) drives ADI depth cameras from a host. Its network connection is defined by a published proto3 contract, in which '
  name: Analog Devices 3D Time-of-Flight SDK
  slug: aditof-sdk
artifact_total: 30
common:
- group: company
  title: ''
  type: Website
  url: https://www.analog.com/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/analog-devices-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/analog-devices
- group: start
  title: ''
  type: Portal
  url: https://www.analog.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.analog.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.analog.com/en/software.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/analogdevicesinc
- group: company
  title: ''
  type: Blog
  url: https://www.analog.com/en/resources/analog-dialogue.html
- group: operate
  title: ''
  type: Support
  url: https://ez.analog.com/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/analog-devices-iio-device-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/analog-devices-iio-context-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/analog-devices-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/analog-devices-vocabulary.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/analog-devices-spectral-rules.yml
- group: build
  title: ''
  type: Packages
  url: packages/analog-devices-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/analog-devices-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/analog-devices-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/analog-devices-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/analog-devices-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/analog-devices-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/analog-devices-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/analog-devices-cli.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/analog-devices-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/analog-devices-data-model.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/analog-devices-aditof-network.proto
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/analog-devices-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://analogdevicesinc.github.io/ltspice-reference/llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/analog-devices-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/analog-devices-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/analog-devices-finops.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.analog.com/docs/codefusion-studio/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.analog.com/documentation
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.analog.com/en/who-we-are/legal-and-risk-oversight/data-privacy/privacy-policy.html
created: '2026-05-03'
description: Analog Devices (ADI) is a global semiconductor company designing high-performance analog, mixed-signal, and digital signal processing integrated circuits for industrial, communications, automotive, and consumer markets. ADI provides developer tools through its CodeFusion Studio embedded development environment and the ADI Developer Portal. ADI's APIs are primarily embedded software APIs for microcontrollers and DSPs via the libiio library for Linux Industrial I/O devices, pyadi-iio Python interfaces, and security APIs within the ADI Assure Trusted Edge Security Architecture. The company also maintains the no-OS driver library for bare-metal embedded systems.
features:
- description: libiio library for accessing Linux Industrial I/O devices over USB, network, and local interfaces.
  name: Linux IIO Interface
- description: PyADI-IIO provides Pythonic device-specific APIs for ADI transceivers, converters, and sensors.
  name: Python Hardware Interfaces
- description: ADI Assure security APIs for hardware root of trust, secure boot, and cryptographic operations.
  name: Embedded Security APIs
- description: Bare-metal C drivers for ADI ICs without requiring an operating system.
  name: No-OS Drivers
- description: VS Code-based IDE for ADI MCUs and DSPs with graphical configuration and code generation.
  name: CodeFusion Studio
- description: Active contributor to Linux kernel IIO subsystem, Zephyr RTOS, and other open source projects.
  name: Open Source Ecosystem
finops:
- name: Analog Devices Finops
  service_category: Semiconductors
  slug: analog-devices-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/analog-devices.png
integrations:
- description: ADI actively contributes drivers to the Linux kernel IIO framework.
  name: Linux Kernel IIO Subsystem
- description: ADI maintains hardware support for ADI MCUs in the Zephyr real-time operating system.
  name: Zephyr RTOS
- description: Integration with GNU Radio for software-defined radio applications using ADI transceivers.
  name: GNU Radio
- description: MathWorks toolbox support for ADI hardware for signal processing prototyping.
  name: MATLAB/Simulink
- description: CodeFusion Studio is built as a VS Code extension for embedded development.
  name: Microsoft Visual Studio Code
json_schemas:
- name: IIOContext
  property_count: 5
  slug: analog-devices-iio-context
- name: IIODevice
  property_count: 5
  slug: analog-devices-iio-device
jsonld:
- class_count: 5
  name: Analog Devices Context
  property_count: 6
  slug: analog-devices-context
layout: provider
modified: '2026-09-02'
name: Analog Devices
nav: Providers
network: true
overview: 'Analog Devices publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Embedded Systems, Hardware, IoT, Semiconductors, and Signal Processing.


  The Analog Devices catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Analog Devices'' developer surface includes developer portal, documentation, engineering blog, support, authentication, changelog, CLI, and 27 more developer resources.'
plans:
- name: Analog Devices Plans Pricing
  plan_count: 1
  slug: analog-devices-plans-pricing
press:
- date: '2026-05-25'
  title: Engineering the Foundation of Physical AI
  url: https://www.analog.com/en/ai.html
- date: '2026-05-25'
  title: Analog Devices to Acquire Empower Semiconductor ...
  url: https://www.prnewswire.com/news-releases/analog-devices-to-acquire-empower-semiconductor-expanding-its-next-generation-high-density-power-portfolio-for-the-ai-era-302776701.html
- date: '2026-05-25'
  title: '2026: The Year Intelligence Gets Physical'
  url: https://www.analog.com/en/newsroom/press-releases/2026/2-9-2026-the-year-intelligence-gets-physical.html
- date: '2026-05-25'
  title: Analog Devices to Buy Empower Semiconductor for $1.5 ...
  url: https://www.wsj.com/business/deals/analog-devices-to-buy-empower-semiconductor-for-1-5-billion-bcbe4d3d
- date: '2026-05-25'
  title: Q1 2026 Analog Devices Inc Earnings Call EVENT DATE/TIME
  url: https://investor.analog.com/static-files/6040f10c-669c-487e-bfa8-60eb1db6c369
random_paper: 3
rate_limits:
- limit_count: 2
  name: Analog Devices Rate Limits
  slug: analog-devices-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Analog Devices API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: analog-devices-jsonschema-spectral-rules
- effective_rule_count: 4
  extends: []
  name: Analog Devices API Rules
  rule_count: 4
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 0
  slug: analog-devices-spectral-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 26
    catalog_gap: 51.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 16.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 43.2
    contract_quality: 10.7
    developer_ergonomics: 75.0
    discoverability: 81.5
    governance: 43.2
    operational_transparency: 23.7
  previous_composite: 22.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/analog-devices/refs/heads/main/screenshots/analog-devices-2026-08-07T161354.png
security:
- kind: authentication
  name: Analog Devices Authentication
  slug: analog-devices-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Analog Devices Domain Security
  slug: analog-devices-domain-security
  summary_line: TLSv1.3 · DMARC
slug: analog-devices
tags:
- Embedded Systems
- Hardware
- IoT
- Semiconductors
- Signal Processing
- Fortune 1000
use_cases:
- description: High-accuracy data acquisition from ADI ADCs and sensors using libiio or PyADI-IIO.
  name: Precision Measurement
- description: Control of RF transceivers like ADRV9002 and AD9361 for SDR and communications applications.
  name: RF and Communications
- description: Integration of ADI industrial ICs into factory automation and process control systems.
  name: Industrial Automation
- description: Building secure edge devices with hardware root of trust using ADI Assure security APIs.
  name: Secure IoT Devices
- description: Developing motor drive applications using ADI ADSP processors and evaluation kits.
  name: Motor Control
website: https://www.analog.com/
---
