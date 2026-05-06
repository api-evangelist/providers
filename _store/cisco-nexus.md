---
name: Cisco Nexus Dashboard
description: APIs for managing and monitoring Cisco Nexus data center switches and network infrastructure.
image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
url: https://developer.cisco.com/site/nexus/
created: '2024'
modified: '2026-04-19'
tags:
  - Data Center
  - Infrastructure
  - Network Automation
  - Networking
  - SDN
  - Switches
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
      - type: Authentication
        url: https://developer.cisco.com/docs/nx-os/#!authentication
      - type: SDK
        url: https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference/latest/
      - type: GettingStarted
        url: https://developer.cisco.com/docs/cisco-nexus-3000-and-9000-series-nx-api-rest-sdk-user-guide-and-api-reference/latest/getting-started-with-the-cisco-nexus-3000-and-9000-series-nx-api-rest-sdk/
      - type: APIReference
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
      - type: APIReference
        url: https://developer.cisco.com/docs/nexus-dashboard/#!api-reference
      - type: GettingStarted
        url: https://developer.cisco.com/docs/nexus-dashboard/latest/getting-started/
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
      - type: GettingStarted
        url: https://developer.cisco.com/docs/nexus-dashboard-fabric-controller/latest/getting-started/
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
      - type: GettingStarted
        url: https://developer.cisco.com/docs/nexus-dashboard-orchestrator/latest/getting-started/
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
      - type: GettingStarted
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
      - type: UseCases
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
      - type: GitHubRepository
        url: https://github.com/YangModels/yang/tree/master/vendor/cisco/nx
      - type: Tutorials
        url: https://developer.cisco.com/learning/labs/tags/Nexus/
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
      - type: GitHubRepository
        url: https://github.com/CiscoDevNet/nx-telemetry-proto
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
      - type: GitHubRepository
        url: https://github.com/CiscoDevNet/NX-SDK
    contact:
      - FN: Cisco DevNet Support
        email: support@cisco.com
        url: https://developer.cisco.com/site/support/
common:
  - type: DeveloperPortal
    url: https://developer.cisco.com/
  - type: GitHubOrganization
    url: https://github.com/CiscoDevNet
  - type: Training
    url: https://developer.cisco.com/learning/labs/tags/Nexus/
  - type: Sandbox
    url: https://devnetsandbox.cisco.com/
  - type: Support
    url: https://developer.cisco.com/site/support/
  - type: StatusPage
    url: https://status.cisco.com/
  - type: CodeExamples
    url: https://developer.cisco.com/codeexchange/
  - type: Features
    data:
      - name: DME Object Model REST API
        description: RESTful access to the NX-OS Data Management Engine object model for switch configuration and operational state through managed objects.
      - name: VLAN and SVI Management
        description: Create, modify, and delete VLAN bridge domains and Switch Virtual Interfaces for Layer 2 and Layer 3 networking.
      - name: Interface Configuration
        description: Programmatically configure physical Ethernet interfaces including speed, duplex, MTU, switchport mode, and VLAN assignment.
      - name: BGP Routing Management
        description: Configure and monitor BGP routing protocol including neighbors, route policies, and address families.
      - name: Static Route Management
        description: Create and manage IPv4 static routes across VRFs with next-hop specifications and route preferences.
      - name: Feature Management
        description: Enable and disable NX-OS features programmatically including interface-vlan, BGP, OSPF, and LACP.
      - name: Streaming Telemetry
        description: Real-time operational data collection using gNMI/gRPC and model-driven telemetry with YANG models.
      - name: Multi-Site Orchestration
        description: Unified policy management and orchestration across multiple ACI, Cloud ACI, and DCNM fabrics.
  - type: UseCases
    data:
      - name: Data Center Network Automation
        description: Automate switch configuration, VLAN provisioning, and routing changes across large-scale data center fabrics.
      - name: Network Monitoring and Analytics
        description: Collect real-time telemetry data from Nexus switches for performance monitoring, anomaly detection, and capacity planning.
      - name: Multi-Site Fabric Management
        description: Orchestrate network policies and connectivity across geographically distributed data center fabrics.
      - name: Infrastructure as Code
        description: Define and manage network infrastructure configurations using YANG models, NETCONF, and RESTCONF for version-controlled deployments.
      - name: Compliance and Auditing
        description: Programmatically verify switch configurations against security baselines and generate compliance reports.
  - type: Integrations
    data:
      - name: Ansible
        description: Automate Nexus switch configuration using Ansible NX-OS modules and playbooks for declarative network management.
      - name: Terraform
        description: Provision and manage Cisco ACI and Nexus infrastructure using the Terraform Cisco provider.
      - name: Cisco ACI
        description: Application Centric Infrastructure integration for policy-driven network automation with Nexus 9000 switches.
      - name: Splunk
        description: Forward NX-OS streaming telemetry and syslog data to Splunk for network analytics and SIEM integration.
      - name: ServiceNow
        description: Integrate Nexus Dashboard events and alerts with ServiceNow ITSM for automated incident management.
  - type: NaftikoCapability
    url: capabilities/switch-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
