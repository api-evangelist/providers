---
aid: cisco-nexus
url: https://raw.githubusercontent.com/api-evangelist/cisco-nexus/refs/heads/main/apis.yml
apis:
- name: Cisco NX-API REST
  description: RESTful API for programmatic access to Nexus switches using HTTP/HTTPS.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nx-os/
  baseURL: https://{switch-ip}/api
  tags:
  - CLI
  - Configuration
  - Monitoring
  - REST
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nx-os/#!working-with-nx-api
  - type: OpenAPI
    url: openapi/cisco-nexus-nxapi-rest.yml
  - type: JSONSchema
    url: json-schema/cisco-nexus-interface-schema.json
  - type: JSONLD
    url: json-ld/cisco-nexus-context.jsonld
  - type: Authentication
    url: https://developer.cisco.com/docs/nx-os/#!authentication
  - type: SDK User Guide
    url: https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference/latest/
  - type: Getting Started
    url: https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference/latest/getting-started-with-the-cisco-nexus-3000-and-9000-series-nx-api-rest-sdk/
  - type: Model Reference
    url: https://developer.cisco.com/docs/nexus-model/latest/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NX-API CLI
  description: API that accepts show commands and configuration commands in CLI format.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nx-os/#!working-with-nx-api-cli
  baseURL: https://{switch-ip}/ins
  tags:
  - CLI
  - Configuration
  - Show Commands
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nx-os/#!nx-api-cli
  - type: SDK
    url: https://github.com/CiscoDevNet/nxapi-learning-labs
  - type: Sandbox
    url: https://devnetsandbox.cisco.com/RM/Topology
  - type: Programmability Guide
    url: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/105x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-105x/m-n9k-nx-api-cli-101x.html
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco Nexus Dashboard REST API
  description: Unified API for Nexus Dashboard Insights, Orchestrator, and Fabric Controller.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nexus-dashboard/latest/
  baseURL: https://{nexus-dashboard}/api/v1
  tags:
  - ACI
  - Dashboard
  - Fabric Controller
  - Insights
  - Orchestration
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nexus-dashboard/
  - type: API Reference
    url: https://developer.cisco.com/docs/nexus-dashboard/#!api-reference
  - type: Getting Started
    url: https://developer.cisco.com/docs/nexus-dashboard/latest/getting-started/
  - type: Postman Collection
    url: https://www.postman.com/ciscodevnet/
  - type: Developer Support
    url: https://developer.cisco.com/docs/nexus-dashboard/latest/developer-support/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco Nexus Dashboard Fabric Controller API
  description: REST API for managing and automating Nexus and MDS fabrics including LAN, SAN, and IP Fabric for Media deployments.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nexus-dashboard-fabric-controller/latest/
  baseURL: https://{nexus-dashboard}/appcenter/cisco/ndfc/api/v1
  tags:
  - EVPN
  - Fabric Management
  - LAN
  - NDFC
  - SAN
  - VXLAN
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nexus-dashboard-fabric-controller/latest/
  - type: Getting Started
    url: https://developer.cisco.com/docs/nexus-dashboard-fabric-controller/latest/getting-started/
  - type: Developer Support
    url: https://developer.cisco.com/docs/nexus-dashboard-api-ndfc-1201/developer-support/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco Nexus Dashboard Orchestrator API
  description: API for multi-site orchestration of ACI, Cloud ACI, and DCNM fabrics with policy management and segmentation.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nexus-dashboard-orchestrator/latest/
  baseURL: https://{nexus-dashboard}/appcenter/cisco/ndo/api/v1
  tags:
  - ACI
  - Multi-Site
  - Orchestrator
  - Policy Management
  - Segmentation
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nexus-dashboard-orchestrator/latest/
  - type: Getting Started
    url: https://developer.cisco.com/docs/nexus-dashboard-orchestrator/latest/getting-started/
  - type: Developer Support
    url: https://developer.cisco.com/docs/nexus-dashboard-orchestrator/4-1-1/developer-support/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco Nexus Dashboard Insights API
  description: API for network analytics, telemetry, anomaly detection, and troubleshooting across data center fabrics.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nexus-dashboard-insights/latest/
  baseURL: https://{nexus-dashboard}/appcenter/cisco/ndi/api/v1
  tags:
  - Analytics
  - Anomaly Detection
  - Insights
  - Telemetry
  - Troubleshooting
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nexus-dashboard-insights/latest/
  - type: Getting Started
    url: https://developer.cisco.com/docs/nexus-dashboard-insights/latest/getting-started/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco DCNM REST API
  description: Data Center Network Manager API for managing Nexus fabric deployments.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/data-center-network-manager/
  baseURL: https://{dcnm-server}/rest
  tags:
  - DCNM
  - EVPN
  - Fabric Management
  - VXLAN
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/data-center-network-manager/
  - type: API Guide
    url: https://www.cisco.com/c/en/us/support/cloud-systems-management/prime-data-center-network-manager/products-programming-reference-guides-list.html
  - type: Use Cases
    url: https://developer.cisco.com/docs/data-center-network-manager/#!use-cases
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NETCONF/YANG API
  description: Model-driven API using YANG data models for Nexus devices.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nx-os/#!working-with-netconf
  baseURL: netconf://{switch-ip}:830
  tags:
  - Automation
  - Model-Driven
  - NETCONF
  - YANG
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nx-os/#!working-with-netconf
  - type: YANG Models
    url: https://github.com/YangModels/yang/tree/master/vendor/cisco/nx
  - type: Tutorial
    url: https://developer.cisco.com/learning/labs/tags/Nexus/
  - type: Model-Driven Programming
    url: https://developer.cisco.com/docs/nx-os/model-driven-programming-model-driven-programming/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NX-OS RESTCONF API
  description: HTTP-based protocol for configuring YANG-defined data on Nexus switches supporting XML and JSON payload encodings.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-106x/chapter-2.html
  baseURL: https://{switch-ip}/restconf
  tags:
  - HTTP
  - Model-Driven
  - RESTCONF
  - YANG
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-106x/chapter-2.html
  - type: YANG Models
    url: https://github.com/YangModels/yang/tree/master/vendor/cisco/nx
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NX-OS gNMI/gRPC API
  description: gRPC Network Management Interface for streaming telemetry and configuration management on Nexus switches.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-106x/m-gnmi.html
  baseURL: grpc://{switch-ip}:50051
  tags:
  - gNMI
  - gRPC
  - Model-Driven
  - Streaming
  - Telemetry
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/106x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-106x/m-gnmi.html
  - type: Telemetry Proto
    url: https://github.com/CiscoDevNet/nx-telemetry-proto
  - type: Telemetry Collector
    url: https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/telemetry_collector/
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NX-OS Model-Driven Telemetry API
  description: Streaming telemetry interface for real-time operational data collection from Nexus switches using YANG models.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/102x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-release-102x/m-n9k-model-driven-telemetry-101x.html
  baseURL: grpc://{switch-ip}:50051
  tags:
  - Dial-Out
  - Monitoring
  - Streaming
  - Telemetry
  - YANG
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/td/docs/dcn/nx-os/nexus9000/102x/programmability/cisco-nexus-9000-series-nx-os-programmability-guide-release-102x/m-n9k-model-driven-telemetry-101x.html
  - type: Telemetry Proto
    url: https://github.com/CiscoDevNet/nx-telemetry-proto
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
- name: Cisco NX-OS Python SDK API
  description: Python Software Development Kit for programmatic access to Nexus 9000 Series switch modules including interfaces, VLANs, ACLs, and routes.
  image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
  humanURL: https://developer.cisco.com/docs/nx-os/cisco-nexus-9000-series-python-sdk-user-guide-and-api-reference/
  baseURL: https://{switch-ip}
  tags:
  - Automation
  - On-Box
  - Python
  - SDK
  properties:
  - type: Documentation
    url: https://developer.cisco.com/docs/nx-os/cisco-nexus-9000-series-python-sdk-user-guide-and-api-reference/
  - type: GitHub Repository
    url: https://github.com/CiscoDevNet/NX-SDK
  contact:
  - FN: Cisco DevNet Support
    email: support@cisco.com
    url: https://developer.cisco.com/site/support/
name: Cisco Nexus Dashboard
tags:
- Data Center
- Infrastructure
- Network Automation
- Networking
- SDN
- Switches
type: Contract
image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing and monitoring Cisco Nexus data center switches and network infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

