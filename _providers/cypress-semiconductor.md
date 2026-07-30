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
api_count: 6
apis:
- description: ModusToolbox is Infineon's modern embedded development ecosystem and the successor to Cypress' PSoC Creator. It is a collection of GUI and non-GUI tools, libraries, configurators, board support packag
  name: ModusToolbox Software Ecosystem
  slug: modustoolbox
- description: The PSoC Hardware Abstraction Layer (HAL) and Peripheral Driver Library (PDL) are the C-language embedded APIs developers use to program Cypress-originated PSoC 4, PSoC 6, and PSoC Edge microcontrolle
  name: PSoC HAL and Peripheral Driver Library (PDL)
  slug: psoc-hal
- description: AIROC Bluetooth is the Infineon-rebranded Cypress WICED Bluetooth and Bluetooth LE software stack and SDK, supporting CYW20xxx, CYW43xxx, and AIROC combo Bluetooth/Wi-Fi parts inherited from the Cypre
  name: AIROC Bluetooth (formerly WICED)
  slug: airoc-bluetooth
- description: AIROC Wi-Fi is the Infineon-rebranded Cypress WICED Wi-Fi stack and SDK, including the Wi-Fi Host Driver (WHD) and connectivity middleware that drives CYW43xxx and CYW55xxx Wi-Fi chipsets originally d
  name: AIROC Wi-Fi (formerly WICED)
  slug: airoc-wifi
- description: CapSense is Cypress' (now Infineon's) capacitive touch sensing technology, exposed to firmware developers as a ModusToolbox middleware library and Device Configurator personality. CapSense supports bu
  name: CapSense Capacitive Touch Library
  slug: capsense
- description: TRAVEO T2G is the automotive Arm Cortex-M microcontroller family inherited from Cypress, now developed under Infineon. Developers program TRAVEO T2G via ModusToolbox using a dedicated PDL, HAL, and BS
  name: TRAVEO T2G Automotive Microcontroller SDK
  slug: traveo-t2g
artifact_total: 38
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cypress-semiconductor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cypress-semiconductor-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.infineon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://softwaretools.infineon.com/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.infineon.com/modustoolbox/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Infineon
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cypresssemiconductorco
- group: operate
  title: ''
  type: Support
  url: https://community.infineon.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infineon-technologies
- group: company
  title: ''
  type: Blog
  url: https://community.infineon.com/t5/Blogs/ct-p/Blogs
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.infineon.com/cms/en/about-infineon/company/acquisitions/cypress/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cypress-semiconductor-modustoolbox-application-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cypress-semiconductor-board-support-package-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cypress-semiconductor-capsense-configuration-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cypress-semiconductor-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cypress-semiconductor-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/cypress-semiconductor-rules.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cypress-semiconductor-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cypress-semiconductor-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cypress-semiconductor-finops.yml
- group: company
  title: ''
  type: News
  url: https://www.infineon.com/cms/en/product/memories/nor-flash/
description: Cypress Semiconductor was a US-based semiconductor company known for its PSoC programmable system-on-chip microcontrollers, WICED Wi-Fi and Bluetooth connectivity stacks, NOR Flash memory, CapSense capacitive touch sensing, and Traveo automotive microcontrollers. Infineon Technologies completed its $9.4 billion acquisition of Cypress on April 16, 2020, and Cypress now operates as a wholly owned subsidiary of Infineon. The former Cypress product lines (PSoC, AIROC formerly WICED, NOR Flash, CapSense, Traveo) remain in active development under Infineon branding, and the cypress.com domain redirects to infineon.com. The former Cypress developer surface — including PSoC Creator (legacy) and the modern ModusToolbox embedded development ecosystem — is now hosted on the Infineon GitHub organization (github.com/Infineon) which contains 2,143 public repositories spanning code examples, board support packages, HAL libraries, middleware, and configurators for PSoC, AIROC, Traveo, XMC,
  and AURIX device families. The original Cypress GitHub organization (github.com/cypresssemiconductorco) has been wound down to four placeholder repos that redirect users to the Infineon org. Cypress' APIs are predominantly embedded software APIs (C/C++ HAL, PDL, middleware libraries) rather than HTTP/REST surfaces, consumed by firmware engineers via ModusToolbox, Eclipse, and Visual Studio Code workflows.
features:
- description: Cypress' flagship PSoC 4, PSoC 6, and PSoC Edge Arm Cortex-M MCUs with configurable analog and digital fabric, now produced under Infineon.
  name: PSoC Programmable System-on-Chip
- description: Rebranded WICED Wi-Fi and Bluetooth combo silicon (CYW43xxx, CYW20xxx, CYW55xxx) with ModusToolbox middleware.
  name: AIROC Wireless Connectivity
- description: Capacitive sensing IP for buttons, sliders, and proximity, with SmartSense auto-tuning and a dedicated Configurator GUI.
  name: CapSense Capacitive Touch
- description: Arm Cortex-M-based automotive microcontrollers for body, cluster, and gateway ECUs, developed via ModusToolbox.
  name: TRAVEO T2G Automotive MCUs
- description: High-reliability and high-bandwidth NOR Flash memory families with serial, QSPI, and HyperBus interfaces.
  name: Semper / HyperFlash NOR Memory
- description: Cross-platform tools, BSPs, HAL/PDL libraries, middleware, and configurators that replaced Cypress PSoC Creator and WICED Studio.
  name: ModusToolbox Development Ecosystem
- description: 2,143 public repositories on the Infineon GitHub org including 87+ ModusToolbox-tagged repos, mtb-example-* code examples, and BSP packages.
  name: Open Source Reference Code
finops:
- name: Cypress Semiconductor Finops
  service_category: Semiconductors
  slug: cypress-semiconductor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cypress-semiconductor.png
integrations:
- description: ModusToolbox ships a VS Code extension as a primary supported IDE for embedded development.
  name: Visual Studio Code
- description: ModusToolbox integrates with Eclipse via the Eclipse IDE for ModusToolbox distribution.
  name: Eclipse IDE
- description: ModusToolbox project export supports IAR EWARM for Arm Cortex-M PSoC targets.
  name: IAR Embedded Workbench
- description: PSoC 6 and AIROC parts have Arm Mbed OS targets, enabling Mbed-based application development.
  name: Arm Mbed OS
- description: Infineon contributes board support for PSoC 6 and PSoC Edge to the Zephyr RTOS project.
  name: Zephyr RTOS
- description: An Infineon-maintained PSoC 6 / PSoC Edge port of MicroPython enables Python-based prototyping.
  name: MicroPython
- description: Arduino cores exist for XMC (XMC-for-Arduino) and PSoC 6 (arduino-core-psoc6) on the Infineon GitHub org.
  name: Arduino
- description: Cypress was a launch partner for Amazon FreeRTOS; the amazon-freertos repository remains in the legacy Cypress GitHub org.
  name: Amazon FreeRTOS
json_schemas:
- name: ModusToolbox Board Support Package
  property_count: 8
  slug: cypress-semiconductor-board-support-package
- name: CapSense Configuration
  property_count: 4
  slug: cypress-semiconductor-capsense-configuration
- name: ModusToolbox Application
  property_count: 9
  slug: cypress-semiconductor-modustoolbox-application
jsonld:
- class_count: 34
  name: Cypress Semiconductor Context
  property_count: 10
  slug: cypress-semiconductor-context
layout: provider
modified: '2026-07-25'
name: Cypress Semiconductor
nav: Providers
network: true
overview: 'Cypress Semiconductor publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Bluetooth, CapSense, Embedded Systems, and Hardware.


  The Cypress Semiconductor catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cypress Semiconductor''s developer surface includes developer portal, documentation, support, engineering blog, product news, and 16 more developer resources.'
plans:
- name: Cypress Semiconductor Plans Pricing
  plan_count: 1
  slug: cypress-semiconductor-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Cypress Semiconductor Rate Limits
  slug: cypress-semiconductor-rate-limits
rules:
- name: Cypress Semiconductor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cypress-semiconductor-jsonschema-spectral-rules
- name: Cypress Semiconductor API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 7
  slug: cypress-semiconductor-rules
score:
  band: thin
  composite: 37.0
  delta: -5.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 17.7
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 42.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cypress-semiconductor/refs/heads/main/screenshots/cypress-semiconductor-2026-06-20T175414.png
security:
- kind: domain-security
  name: Cypress Semiconductor Domain Security
  slug: cypress-semiconductor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cypress Semiconductor Vulnerability Disclosure
  slug: cypress-semiconductor-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cypress-semiconductor
tags:
- Acquired
- Bluetooth
- CapSense
- Embedded Systems
- Hardware
- Infineon
- IoT
- Microcontrollers
- NOR Flash
- PSoC
- Semiconductor
- WiFi
use_cases:
- description: Building Wi-Fi and Bluetooth-connected IoT endpoints on PSoC 6 + AIROC silicon using ModusToolbox middleware.
  name: Connected IoT Devices
- description: Designing capacitive touch buttons, sliders, and proximity surfaces with CapSense on PSoC microcontrollers.
  name: Touch and HMI Interfaces
- description: Programming TRAVEO T2G microcontrollers for body, cluster, and gateway electronic control units.
  name: Automotive ECU Development
- description: Using PSoC and XMC parts together in factory automation, motor drive, and industrial sensing applications.
  name: Industrial Microcontrollers
- description: Leveraging PSoC 6 dual-core (Cortex-M4 + Cortex-M0+) architecture and OPTIGA Trust for root-of-trust IoT designs.
  name: Secured Embedded Applications
- description: Building USB-C PD controllers and chargers on Infineon's PD MCU family with ModusToolbox.
  name: USB-C Power Delivery
website: https://softwaretools.infineon.com/welcome
---
