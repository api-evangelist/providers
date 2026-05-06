---
aid: vertiv
name: Vertiv
description: Vertiv is a global provider of critical digital infrastructure and continuity solutions for data centers and communication networks. The company delivers power management, thermal management, IT management software (DCIM), and infrastructure monitoring solutions through brands including Geist (DCIM and PDU monitoring), Avocent (IT management and KVM), and Liebert (UPS and thermal). Vertiv's software platforms expose REST APIs for integrating with third-party systems, automation workflows, and data center management platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Critical Infrastructure
  - Data Center
  - DCIM
  - Infrastructure Monitoring
  - Power Management
  - UPS
url: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vertiv:environet-alert-rest-api
    name: Vertiv Environet Alert REST API
    description: The Vertiv Environet Alert Public REST API provides programmatic access to Vertiv's DCIM monitoring platform for data centers. The API enables retrieval of device data, sensor readings, environmental metrics, alerts, alarms, circuit information, rack details, and asset management data. Authentication uses HTTP Basic credentials (POST x-www-form-urlencoded). The API supports integration with third-party DCIM, ITSM, and automation platforms.
    humanURL: https://www.vertiv.com/en-us/products-catalog/monitoring-control-and-management/software/vertiv-environet-alert/
    tags:
      - Alerts
      - Asset Management
      - DCIM
      - Environmental Monitoring
      - Infrastructure Monitoring
      - Sensors
    properties:
      - type: Documentation
        url: https://www.vertiv.com/48ea2d/globalassets/products/monitoring-control-and-management/software/vertiv-environet-alert-public-rest-api-v1-guide-sl-70596.pdf
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/openapi/vertiv-environet-alert-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/json-schema/vertiv-alarm-schema.json
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/capabilities/dcim-monitoring.yaml
      - type: SpectralRuleset
        url: https://raw.githubusercontent.com/api-evangelist/vertiv/refs/heads/main/rules/vertiv-environet-rules.yml
  - aid: vertiv:avocent-adx-ecosystem-api
    name: Vertiv Avocent ADX Ecosystem API
    description: The Vertiv Avocent ADX Ecosystem API provides REST API access for managing IT infrastructure through the Avocent ADX Management Platform. The API supports device management, KVM session management, user administration, and configuration of server management functions including the MP1000 Management Platform.
    humanURL: https://www.vertiv.com/en-us/products-catalog/monitoring-control-and-management/digital-infrastructure-solutions/vertiv-avocent-mp1000-management-platform/
    tags:
      - Avocent
      - IT Management
      - KVM
      - Server Management
    properties:
      - type: Documentation
        url: https://www.vertiv.com/4a648a/globalassets/shared/vertiv-avocent-adx-ecosystem-api-guide.pdf
  - aid: vertiv:avocent-dsview-api
    name: Vertiv Avocent DSView API
    description: The Vertiv Avocent DSView Solution REST API enables launching of KVM, serial, and virtual viewer sessions to managed devices. The API provides programmatic control of session management, device inventory, and user access workflows for the DSView centralized management platform.
    humanURL: https://www.vertiv.com/en-us/products/monitoring-control--management/vertiv-avocent-dsview-solution/
    tags:
      - Avocent
      - DSView
      - IT Management
      - KVM
      - Session Management
    properties:
      - type: Documentation
        url: https://www.vertiv.com/48ee3b/globalassets/products/monitoring-control-and-management/digital-infrastructure-solutions/vertiv-avocent-dsview-solution/vertiv-avocent-dsview-api-tech-note_aug-2023.pdf
  - aid: vertiv:geist-pdu-rest-api
    name: Vertiv Geist PDU REST API
    description: The Vertiv Geist Power Distribution Unit (PDU) REST API provides programmatic control of Geist intelligent rack PDUs. The API supports outlet power control (on/off with delay), outlet configuration, device information retrieval, and energy monitoring. Authentication uses token- based auth via POST to the auth endpoint.
    humanURL: https://www.geistglobal.com/open-api-and-software-integration
    tags:
      - Energy Monitoring
      - Outlet Control
      - PDU
      - Power Distribution
      - Power Management
    properties:
      - type: Documentation
        url: https://www.geistglobal.com/open-api-and-software-integration
  - aid: vertiv:avocent-acs-api
    name: Vertiv Avocent ACS800/8000 REST API
    description: The Vertiv Avocent ACS800/8000 Advanced Console System native RESTful API provides programmatic access to serial console server management. The API supports device configuration, port management, user administration, and session management for out-of-band management of network infrastructure.
    humanURL: https://www.vertiv.com/en-us/products/monitoring-control--management/avocent-embedded-management-systems/
    tags:
      - Avocent
      - Console Server
      - Out-of-Band Management
      - Serial Console
    properties:
      - type: Documentation
        url: https://www.vertiv.com/48ea81/globalassets/shared/avocent-acs8008000-application-programming-interface_0.pdf
common:
  - url: https://www.vertiv.com/
    name: Vertiv
    type: Website
    description: Vertiv's main website providing information on critical digital infrastructure solutions for data centers.
  - url: https://www.vertiv.com/en-us/products-catalog/monitoring-control-and-management/
    name: Vertiv Monitoring and Management
    type: Documentation
    description: Vertiv's portfolio of monitoring, control, and management solutions including DCIM, power management, and IT infrastructure tools.
  - url: https://www.geistglobal.com/
    name: Vertiv Geist
    type: Website
    description: Geist brand site for Vertiv's DCIM, intelligent PDU, and environmental monitoring solutions.
  - url: https://www.geistglobal.com/open-api-and-software-integration
    name: Geist Open API and Software Integration
    type: Documentation
    description: Documentation for Geist/Vertiv REST API integrations and third-party software connections.
  - url: https://www.vertiv.com/en-us/support/software-downloads/
    name: Vertiv Software Downloads
    type: Downloads
    description: Software downloads for Vertiv monitoring and management applications including Power Assist, Power Insight, and Environet.
  - url: https://www.vertiv.com/en-us/support/
    name: Vertiv Support
    type: Support
    description: Vertiv support portal for documentation, firmware updates, and technical assistance.
  - url: https://github.com/enp-isit
    name: Vertiv IS/IT GitHub
    type: GitHubOrganization
    description: Vertiv IS/IT GitHub organization for internal software development.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
