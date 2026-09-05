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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The Bluetooth Core Specification defines the complete Bluetooth wireless communication protocol stack including BLE (LE) and Classic Bluetooth. The current stable version is Bluetooth 6.0. The specifi
  name: Bluetooth Core Specification
  slug: bluetooth-core-specification
- description: The Generic Attribute Profile (GATT) defines the framework for data transfer between Bluetooth LE devices. The Bluetooth SIG maintains assigned numbers for services, characteristics, and descriptors t
  name: GATT and Assigned Numbers
  slug: gatt-specification
- description: Bluetooth Mesh enables many-to-many device communications and is particularly suited for IoT applications that require large-scale device networks, including building automation, industrial IoT, and s
  name: Bluetooth Mesh Networking
  slug: mesh-networking
artifact_total: 34
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ble-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ble-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bluetooth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bluetooth.com/develop-with-bluetooth/
- group: docs
  title: ''
  type: Specification
  url: https://www.bluetooth.com/specifications/specs/
- group: learn
  title: ''
  type: Training
  url: https://www.bluetooth.com/develop-with-bluetooth/training/
- group: operate
  title: ''
  type: Community
  url: https://www.bluetooth.com/develop-with-bluetooth/
- group: build
  title: Developer Tools and SDKs
  type: SDKs
  url: https://www.bluetooth.com/develop-with-bluetooth/developer-resources/
- group: design
  title: ''
  type: Conformance
  url: https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/
- group: design
  title: ''
  type: SpectralRules
  url: rules/ble-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ble-vocabulary.yaml
created: '2025-01-01'
description: Bluetooth Low Energy (BLE), also known as Bluetooth Smart, is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG). Aimed at IoT and embedded applications, BLE provides reduced power consumption while maintaining similar communication range to classic Bluetooth. The specification is managed by the Bluetooth SIG and covers the full protocol stack including the Generic Attribute Profile (GATT), Generic Access Profile (GAP), and the various service and characteristic specifications used for device interoperability.
examples:
- key_count: 8
  name: Ble Advertising Packet Example
  slug: ble-advertising-packet-example
- key_count: 4
  name: Ble Heart Rate Service Example
  slug: ble-heart-rate-service-example
features:
- description: BLE defines a complete protocol stack from Physical Layer through Application, enabling ultra-low-power wireless communication for IoT and wearable devices.
  name: Low Energy Protocol Stack
- description: GATT defines a client/server model for data exchange using services and characteristics, enabling standardized device interoperability across vendors.
  name: Generic Attribute Profile (GATT)
- description: GAP controls connections and advertising in BLE, defining how devices discover each other and establish connections.
  name: Generic Access Profile (GAP)
- description: BLE advertising allows devices to broadcast data without requiring a connection, enabling beacons, proximity sensing, and asset tracking.
  name: Advertising and Scanning
- description: Bluetooth 5.2+ LE Audio introduces LC3 codec, Auracast broadcast audio, and hearing aid profiles for next-generation wireless audio applications.
  name: LE Audio
- description: Bluetooth 5.1+ Direction Finding supports Angle of Arrival (AoA) and Angle of Departure (AoD) for indoor positioning and real-time location.
  name: Direction Finding
- description: The Bluetooth Mesh specification enables many-to-many communications for large-scale IoT deployments in buildings, industry, and infrastructure.
  name: Bluetooth Mesh
finops:
- name: Ble Finops
  service_category: API
  slug: ble-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ble.png
integrations:
- description: iOS and macOS Core Bluetooth framework provides native BLE central and peripheral role implementation for Apple platform apps.
  name: Apple Core Bluetooth
- description: Android Bluetooth API provides BLE central and peripheral support for Android application development.
  name: Android Bluetooth API
- description: The Zephyr Project includes a full BLE stack (Zephyr BT) for embedded and IoT firmware development.
  name: Zephyr RTOS
- description: Nordic Semiconductor's nRF Connect SDK provides BLE and Bluetooth mesh implementation for nRF52 and nRF53 series SoCs.
  name: NRF Connect SDK
- description: The W3C Web Bluetooth API enables browser-based applications to communicate with BLE devices via JavaScript.
  name: Web Bluetooth API
json_schemas:
- name: BLE Advertising Packet
  property_count: 8
  slug: ble-advertising-packet
- name: BLE GATT Service
  property_count: 4
  slug: ble-gatt-service
json_structures:
- name: Ble Advertising Packet Structure
  property_count: 0
  slug: ble-advertising-packet-structure
- name: Ble Gatt Service Structure
  property_count: 0
  slug: ble-gatt-service-structure
jsonld:
- class_count: 11
  name: Ble Context
  property_count: 0
  slug: ble-context
layout: provider
modified: '2026-04-21'
name: BLE
nav: Providers
network: true
overview: 'BLE publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include BLE, Bluetooth, Embedded, IoT, and Protocols.


  The BLE catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  BLE''s developer surface includes documentation, training material, and 9 more developer resources.'
plans:
- name: Ble Plans Pricing
  plan_count: 3
  slug: ble-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Ble Rate Limits
  slug: ble-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: BLE API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ble-jsonschema-spectral-rules
- effective_rule_count: 5
  extends: []
  name: BLE API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 5
  slug: ble-spectral-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 70.3
    catalog_earned_first_party: 0.0
    catalog_gap: 44.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 30.7
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 7.9
  previous_composite: 25.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ble/refs/heads/main/screenshots/ble-2026-06-20T173347.png
security:
- kind: domain-security
  name: Ble Domain Security
  slug: ble-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ble Vulnerability Disclosure
  slug: ble-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ble
tags:
- BLE
- Bluetooth
- Embedded
- IoT
- Protocols
- Standards
- Wireless
use_cases:
- description: BLE powers fitness trackers, smartwatches, heart rate monitors, and medical wearables using standardized GATT health profiles.
  name: Wearable Health Devices
- description: BLE beacons broadcast advertising packets for proximity detection, indoor positioning, and contextual notifications in retail and logistics.
  name: Proximity Beacons
- description: BLE Mesh enables smart lighting, HVAC control, and security systems in residential and commercial building automation.
  name: Smart Home Automation
- description: BLE provides wireless sensor connectivity for industrial monitoring, predictive maintenance, and asset tracking applications.
  name: Industrial IoT
- description: BLE medical devices including glucose meters, blood pressure monitors, and pulse oximeters use standardized health profiles for mobile integration.
  name: Healthcare Monitoring
website: https://www.bluetooth.com/
---
