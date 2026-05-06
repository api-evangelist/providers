---
aid: cisco-hardware
name: Cisco Hardware
url: https://raw.githubusercontent.com/api-evangelist/cisco-hardware/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-23'
type: Index
access: 3rd-Party
position: Consumer
specificationVersion: '0.19'
tags:
  - Hardware
  - Infrastructure
  - Networking
  - Routers
  - Switches
description: Cisco Hardware is an aggregated index of programmable interfaces for managing Cisco network and data center hardware, including routers, switches, wireless access points, data center fabric, and unified computing systems. The index covers Cisco Catalyst Center (formerly DNA Center), Meraki cloud-managed devices, IOS XE RESTCONF, ACI APIC, UCS Manager, and Intersight cloud infrastructure management. Cisco hardware APIs are exposed through Cisco DevNet, with sandboxes available for developers to test integrations against live hardware without owning physical devices.
apis:
  - aid: cisco-hardware:catalyst-center-api
    name: Cisco Catalyst Center API
    tags:
      - Automation
      - Catalyst
      - Network Management
      - SDN
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/dna-center/
    properties:
      - url: https://developer.cisco.com/docs/dna-center/
        type: Documentation
      - url: https://developer.cisco.com/docs/dna-center/api/
        type: API Reference
      - url: https://devnetsandbox.cisco.com/
        type: Sandbox
    description: The Cisco Catalyst Center API (formerly Cisco DNA Center) provides programmatic management of Cisco enterprise network infrastructure, including discovery, inventory, provisioning, assurance, software image management, and policy. Authentication uses a basic-auth token exchange that returns a session token used as the X-Auth-Token header for subsequent calls. Responses are JSON.
  - aid: cisco-hardware:meraki-dashboard-api
    name: Cisco Meraki Dashboard API
    tags:
      - Cloud Managed
      - Dashboard
      - Switching
      - Wireless
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.meraki.com/api/v1
    humanURL: https://developer.cisco.com/meraki/
    properties:
      - url: https://developer.cisco.com/meraki/api-latest/
        type: Documentation
      - url: https://api.meraki.com/api/v1/openapiSpec
        type: OpenAPI
      - url: https://developer.cisco.com/meraki/api/getting-started/
        type: Getting Started
    description: The Meraki Dashboard API is a RESTful interface for cloud-managed Meraki hardware including switches, wireless access points, security appliances, cameras, and sensors. Authentication uses an API key passed in the X-Cisco-Meraki-API-Key header. All endpoints return JSON. The API is fully versioned and an OpenAPI specification is published live at the Meraki dashboard URL.
  - aid: cisco-hardware:ios-xe-restconf-api
    name: Cisco IOS XE RESTCONF API
    tags:
      - IOS XE
      - RESTCONF
      - Routers
      - Switches
      - YANG
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/ios-xe/
    properties:
      - url: https://developer.cisco.com/docs/ios-xe/
        type: Documentation
      - url: https://github.com/YangModels/yang/tree/main/vendor/cisco/xe
        type: YANG Models
      - url: https://devnetsandbox.cisco.com/RM/Topology
        type: Sandbox
    description: The IOS XE RESTCONF API exposes Cisco enterprise routers and switches running IOS XE through a model-driven RESTCONF interface that maps directly onto YANG data models. Operations include retrieving device configuration, applying configuration changes, and reading operational state. Authentication uses basic auth and payloads are negotiated as JSON or XML.
  - aid: cisco-hardware:apic-rest-api
    name: Cisco APIC REST API
    tags:
      - ACI
      - APIC
      - Data Center
      - Fabric
      - SDN
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/docs/aci/
    properties:
      - url: https://developer.cisco.com/docs/aci/
        type: Documentation
      - url: https://developer.cisco.com/docs/apic-mim-ref/
        type: API Reference
      - url: https://github.com/datacenter/acitoolkit
        type: SDK
    description: The Cisco APIC REST API manages Application Centric Infrastructure (ACI) data center fabric. The API operates on the ACI Management Information Model and supports tenants, application profiles, endpoint groups, contracts, and fabric infrastructure. Authentication uses login endpoints that return a token cookie used for subsequent object queries and configuration changes.
  - aid: cisco-hardware:intersight-api
    name: Cisco Intersight API
    tags:
      - Cloud Management
      - HyperFlex
      - Infrastructure
      - UCS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://intersight.com/api/v1
    humanURL: https://intersight.com/apidocs/
    properties:
      - url: https://intersight.com/apidocs/introduction/overview/
        type: Documentation
      - url: https://intersight.com/apidocs/downloads/
        type: OpenAPI
      - url: https://github.com/CiscoDevNet/intersight-python
        type: SDK
    description: The Cisco Intersight API is a cloud-based control plane for managing Cisco UCS, HyperFlex, and partner infrastructure. The API follows an OData v4-flavored REST style, uses HTTP signature authentication with API keys, and exposes resource collections for compute, storage, networking, virtualization, and orchestration domains.
  - aid: cisco-hardware:ucs-manager-api
    name: Cisco UCS Manager API
    tags:
      - Compute
      - Data Center
      - Servers
      - UCS
      - XML
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cisco.com/site/ucs-dev-center/
    properties:
      - url: https://developer.cisco.com/docs/ucs-manager/
        type: Documentation
      - url: https://github.com/CiscoUcs/ucsmsdk
        type: SDK
    description: The UCS Manager XML API is the legacy programmatic interface for managing Cisco Unified Computing System blade and rack servers. The API uses an XML over HTTPS request-response model targeting the UCS object model and provides endpoints for chassis discovery, service profile association, firmware management, and policy configuration.
common:
  - type: Portal
    url: https://developer.cisco.com/
  - type: Documentation
    url: https://developer.cisco.com/docs/
  - type: Sandbox
    url: https://devnetsandbox.cisco.com/
  - type: Code Exchange
    url: https://developer.cisco.com/codeexchange/
  - type: Learning
    url: https://developer.cisco.com/learning/
  - type: Support
    url: https://developer.cisco.com/site/support/
  - type: Community
    url: https://community.cisco.com/
  - type: Status
    url: https://status.cisco.com/
  - type: Terms of Service
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software/end_user_license_agreement.html
  - type: Privacy Policy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: JSON-LD
    url: json-ld/cisco-hardware-context.jsonld
  - type: Spectral
    url: rules/cisco-hardware-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cisco-hardware-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
