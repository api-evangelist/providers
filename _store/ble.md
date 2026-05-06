---
aid: ble
name: BLE
description: Bluetooth Low Energy (BLE), also known as Bluetooth Smart, is a wireless personal area network technology designed and marketed by the Bluetooth Special Interest Group (Bluetooth SIG). Aimed at IoT and embedded applications, BLE provides reduced power consumption while maintaining similar communication range to classic Bluetooth. The specification is managed by the Bluetooth SIG and covers the full protocol stack including the Generic Attribute Profile (GATT), Generic Access Profile (GAP), and the various service and characteristic specifications used for device interoperability.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - BLE
  - Bluetooth
  - Embedded
  - IoT
  - Protocols
  - Standards
  - Wireless
url: https://raw.githubusercontent.com/api-evangelist/ble/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: ble:bluetooth-core-specification
    name: Bluetooth Core Specification
    description: The Bluetooth Core Specification defines the complete Bluetooth wireless communication protocol stack including BLE (LE) and Classic Bluetooth. The current stable version is Bluetooth 6.0. The specification covers the Physical Layer, Link Layer, HCI, L2CAP, SM, GAP, and GATT layers, as well as LE Audio, Isochronous Channels, and Direction Finding extensions.
    humanURL: https://www.bluetooth.com/specifications/specs/core60/
    tags:
      - BLE
      - Bluetooth
      - Core Specification
      - Protocols
      - Standards
    properties:
      - type: Documentation
        url: https://www.bluetooth.com/specifications/specs/
      - type: Specification
        url: https://www.bluetooth.com/specifications/specs/core60/
      - type: JSONSchema
        url: json-schema/ble-gatt-service-schema.json
      - type: JSONSchema
        url: json-schema/ble-advertising-packet-schema.json
      - type: JSONStructure
        url: json-structure/ble-gatt-service-structure.json
      - type: JSONStructure
        url: json-structure/ble-advertising-packet-structure.json
      - type: JSONLD
        url: json-ld/ble-context.jsonld
      - type: Example
        url: examples/ble-heart-rate-service-example.json
      - type: Example
        url: examples/ble-advertising-packet-example.json
  - aid: ble:gatt-specification
    name: GATT and Assigned Numbers
    description: The Generic Attribute Profile (GATT) defines the framework for data transfer between Bluetooth LE devices. The Bluetooth SIG maintains assigned numbers for services, characteristics, and descriptors that enable interoperable implementations. GATT services include Battery Service, Heart Rate, Device Information, Health Thermometer, and many other standardized profiles.
    humanURL: https://www.bluetooth.com/specifications/assigned-numbers/
    tags:
      - BLE
      - GATT
      - IoT
      - Profiles
      - Standards
    properties:
      - type: Documentation
        url: https://www.bluetooth.com/specifications/assigned-numbers/
      - type: Specification
        url: https://www.bluetooth.com/specifications/assigned-numbers/
  - aid: ble:mesh-networking
    name: Bluetooth Mesh Networking
    description: Bluetooth Mesh enables many-to-many device communications and is particularly suited for IoT applications that require large-scale device networks, including building automation, industrial IoT, and smart city infrastructure.
    humanURL: https://www.bluetooth.com/specifications/specs/mesh-profile/
    tags:
      - BLE
      - IoT
      - Mesh
      - Networking
      - Standards
    properties:
      - type: Documentation
        url: https://www.bluetooth.com/specifications/specs/mesh-profile/
      - type: Specification
        url: https://www.bluetooth.com/specifications/specs/mesh-profile/
common:
  - type: Website
    url: https://www.bluetooth.com/
  - type: Documentation
    url: https://www.bluetooth.com/develop-with-bluetooth/
  - type: Specification
    url: https://www.bluetooth.com/specifications/specs/
  - type: Training
    url: https://www.bluetooth.com/develop-with-bluetooth/training/
  - type: Community
    url: https://www.bluetooth.com/develop-with-bluetooth/
  - type: SDK
    url: https://www.bluetooth.com/develop-with-bluetooth/developer-resources/
    title: Developer Tools and SDKs
  - type: Conformance
    url: https://www.bluetooth.com/develop-with-bluetooth/qualification-listing/
  - type: SpectralRules
    url: rules/ble-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/ble-gatt-capability.yaml
  - type: Vocabulary
    url: vocabulary/ble-vocabulary.yaml
  - type: Features
    data:
      - name: Low Energy Protocol Stack
        description: BLE defines a complete protocol stack from Physical Layer through Application, enabling ultra-low-power wireless communication for IoT and wearable devices.
      - name: Generic Attribute Profile (GATT)
        description: GATT defines a client/server model for data exchange using services and characteristics, enabling standardized device interoperability across vendors.
      - name: Generic Access Profile (GAP)
        description: GAP controls connections and advertising in BLE, defining how devices discover each other and establish connections.
      - name: Advertising and Scanning
        description: BLE advertising allows devices to broadcast data without requiring a connection, enabling beacons, proximity sensing, and asset tracking.
      - name: LE Audio
        description: Bluetooth 5.2+ LE Audio introduces LC3 codec, Auracast broadcast audio, and hearing aid profiles for next-generation wireless audio applications.
      - name: Direction Finding
        description: Bluetooth 5.1+ Direction Finding supports Angle of Arrival (AoA) and Angle of Departure (AoD) for indoor positioning and real-time location.
      - name: Bluetooth Mesh
        description: The Bluetooth Mesh specification enables many-to-many communications for large-scale IoT deployments in buildings, industry, and infrastructure.
  - type: UseCases
    data:
      - name: Wearable Health Devices
        description: BLE powers fitness trackers, smartwatches, heart rate monitors, and medical wearables using standardized GATT health profiles.
      - name: Proximity Beacons
        description: BLE beacons broadcast advertising packets for proximity detection, indoor positioning, and contextual notifications in retail and logistics.
      - name: Smart Home Automation
        description: BLE Mesh enables smart lighting, HVAC control, and security systems in residential and commercial building automation.
      - name: Industrial IoT
        description: BLE provides wireless sensor connectivity for industrial monitoring, predictive maintenance, and asset tracking applications.
      - name: Healthcare Monitoring
        description: BLE medical devices including glucose meters, blood pressure monitors, and pulse oximeters use standardized health profiles for mobile integration.
  - type: Integrations
    data:
      - name: Apple Core Bluetooth
        description: iOS and macOS Core Bluetooth framework provides native BLE central and peripheral role implementation for Apple platform apps.
      - name: Android Bluetooth API
        description: Android Bluetooth API provides BLE central and peripheral support for Android application development.
      - name: Zephyr RTOS
        description: The Zephyr Project includes a full BLE stack (Zephyr BT) for embedded and IoT firmware development.
      - name: NRF Connect SDK
        description: Nordic Semiconductor's nRF Connect SDK provides BLE and Bluetooth mesh implementation for nRF52 and nRF53 series SoCs.
      - name: Web Bluetooth API
        description: The W3C Web Bluetooth API enables browser-based applications to communicate with BLE devices via JavaScript.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
