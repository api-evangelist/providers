---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 9
  human_in_the_loop: 2
  name: Cisco Nexus Agentic Access
  operation_count: 18
  slug: cisco-nexus-agentic-access
  summary_line: 18 operations · 9 acting · 2 human-in-the-loop
api_count: 16
apis:
- description: API that accepts show commands and configuration commands in CLI format.
  name: Cisco NX-API CLI
  slug: cisco-nx-api-cli
- description: Unified API for Nexus Dashboard Insights, Orchestrator, and Fabric Controller.
  name: Cisco Nexus Dashboard REST API
  slug: cisco-nexus-dashboard-rest-api
- description: REST API for managing and automating Nexus and MDS fabrics including LAN, SAN, and IP Fabric for Media deployments.
  name: Cisco Nexus Dashboard Fabric Controller API
  slug: cisco-nexus-dashboard-fabric-controller-api
- description: API for multi-site orchestration of ACI, Cloud ACI, and DCNM fabrics with policy management and segmentation.
  name: Cisco Nexus Dashboard Orchestrator API
  slug: cisco-nexus-dashboard-orchestrator-api
- description: API for network analytics, telemetry, anomaly detection, and troubleshooting across data center fabrics.
  name: Cisco Nexus Dashboard Insights API
  slug: cisco-nexus-dashboard-insights-api
- description: Data Center Network Manager API for managing Nexus fabric deployments.
  name: Cisco DCNM REST API
  slug: cisco-dcnm-rest-api
- description: Model-driven API using YANG data models for Nexus devices.
  name: Cisco NETCONF/YANG API
  slug: cisco-netconfyang-api
- description: HTTP-based protocol for configuring YANG-defined data on Nexus switches supporting XML and JSON payload encodings.
  name: Cisco NX-OS RESTCONF API
  slug: cisco-nx-os-restconf-api
- description: gRPC Network Management Interface for streaming telemetry and configuration management on Nexus switches.
  name: Cisco NX-OS gNMI/gRPC API
  slug: cisco-nx-os-gnmigrpc-api
- description: Streaming telemetry interface for real-time operational data collection from Nexus switches using YANG models.
  name: Cisco NX-OS Model-Driven Telemetry API
  slug: cisco-nx-os-model-driven-telemetry-api
- description: Python Software Development Kit for programmatic access to Nexus 9000 Series switch modules including interfaces, VLANs, ACLs, and routes.
  name: Cisco NX-OS Python SDK API
  slug: cisco-nx-os-python-sdk-api
- description: Session authentication and token management via aaaLogin and aaaLogout
  name: Cisco Nexus Dashboard Authentication API
  slug: cisco-nexus-authentication-api
- description: Physical interface configuration and operational state using the l1PhysIf managed object class (DN sys/intf/phys-[id])
  name: Cisco Nexus Dashboard Interfaces API
  slug: cisco-nexus-interfaces-api
- description: IPv4 and IPv6 static route configuration using ipv4Route/ipv6Route managed objects and BGP protocol management using bgpEntity hierarchy
  name: Cisco Nexus Dashboard Routing API
  slug: cisco-nexus-routing-api
- description: Top-level system information and feature management via topSystem and fmEntity managed objects
  name: Cisco Nexus Dashboard System API
  slug: cisco-nexus-system-api
- description: VLAN bridge domain management using the l2BD managed object class (DN sys/bd/bd-[vlan-id]) and SVI interface configuration using sviIf
  name: Cisco Nexus Dashboard VLANs API
  slug: cisco-nexus-vlans-api
artifact_total: 165
collections:
- collection_type: open
  name: Cisco NX-API REST
  slug: open-cisco-nexus-nxapi-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cisco-nexus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cisco-nexus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cisco-nexus-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cisco.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.cisco.com/tag/nexus/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CiscoDevNet
- group: learn
  title: ''
  type: Training
  url: https://developer.cisco.com/learning/labs/tags/Nexus/
- group: start
  title: ''
  type: Sandbox
  url: https://devnetsandbox.cisco.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.cisco.com/site/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cisco.com/
- group: build
  title: ''
  type: CodeExamples
  url: https://developer.cisco.com/codeexchange/
created: '2024'
description: APIs for managing and monitoring Cisco Nexus data center switches and network infrastructure.
examples:
- key_count: 6
  name: Cisco Nexus Authenticateuser Example
  slug: cisco-nexus-authenticateuser-example
- key_count: 6
  name: Cisco Nexus Configurefeatures Example
  slug: cisco-nexus-configurefeatures-example
- key_count: 6
  name: Cisco Nexus Configurephysicalinterface Example
  slug: cisco-nexus-configurephysicalinterface-example
- key_count: 6
  name: Cisco Nexus Configurestaticroute Example
  slug: cisco-nexus-configurestaticroute-example
- key_count: 6
  name: Cisco Nexus Configuresviinterface Example
  slug: cisco-nexus-configuresviinterface-example
- key_count: 6
  name: Cisco Nexus Createvlan Example
  slug: cisco-nexus-createvlan-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Aaa Login Response Example
  slug: cisco-nexus-nxapi-rest-aaa-login-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Bd Entity Payload Example
  slug: cisco-nexus-nxapi-rest-bd-entity-payload-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Bgp Dom Example
  slug: cisco-nexus-nxapi-rest-bgp-dom-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Bgp Entity Example
  slug: cisco-nexus-nxapi-rest-bgp-entity-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Bgp Entity Response Example
  slug: cisco-nexus-nxapi-rest-bgp-entity-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Bgp Inst Example
  slug: cisco-nexus-nxapi-rest-bgp-inst-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Bgp Peer Example
  slug: cisco-nexus-nxapi-rest-bgp-peer-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Error Response Example
  slug: cisco-nexus-nxapi-rest-error-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Fm Entity Payload Example
  slug: cisco-nexus-nxapi-rest-fm-entity-payload-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Im Data Response Example
  slug: cisco-nexus-nxapi-rest-im-data-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Interface Entity Payload Example
  slug: cisco-nexus-nxapi-rest-interface-entity-payload-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Ipv4 Inst Payload Example
  slug: cisco-nexus-nxapi-rest-ipv4-inst-payload-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Ipv4 Nexthop Example
  slug: cisco-nexus-nxapi-rest-ipv4-nexthop-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Ipv4 Route Example
  slug: cisco-nexus-nxapi-rest-ipv4-route-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Ipv4 Route List Response Example
  slug: cisco-nexus-nxapi-rest-ipv4-route-list-response-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Ipv4 Route Response Example
  slug: cisco-nexus-nxapi-rest-ipv4-route-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest L1 Phys If Example
  slug: cisco-nexus-nxapi-rest-l1-phys-if-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest L2 Bd Example
  slug: cisco-nexus-nxapi-rest-l2-bd-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Physical Interface List Response Example
  slug: cisco-nexus-nxapi-rest-physical-interface-list-response-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Physical Interface Response Example
  slug: cisco-nexus-nxapi-rest-physical-interface-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Svi If Example
  slug: cisco-nexus-nxapi-rest-svi-if-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Svi If Payload Example
  slug: cisco-nexus-nxapi-rest-svi-if-payload-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Svi Interface Response Example
  slug: cisco-nexus-nxapi-rest-svi-interface-response-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Top System Example
  slug: cisco-nexus-nxapi-rest-top-system-example
- key_count: 1
  name: Cisco Nexus Nxapi Rest Top System Payload Example
  slug: cisco-nexus-nxapi-rest-top-system-payload-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Top System Response Example
  slug: cisco-nexus-nxapi-rest-top-system-response-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Vlan Bridge Domain List Response Example
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-list-response-example
- key_count: 2
  name: Cisco Nexus Nxapi Rest Vlan Bridge Domain Response Example
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-response-example
features:
- description: RESTful access to the NX-OS Data Management Engine object model for switch configuration and operational state through managed objects.
  name: DME Object Model REST API
- description: Create, modify, and delete VLAN bridge domains and Switch Virtual Interfaces for Layer 2 and Layer 3 networking.
  name: VLAN and SVI Management
- description: Programmatically configure physical Ethernet interfaces including speed, duplex, MTU, switchport mode, and VLAN assignment.
  name: Interface Configuration
- description: Configure and monitor BGP routing protocol including neighbors, route policies, and address families.
  name: BGP Routing Management
- description: Create and manage IPv4 static routes across VRFs with next-hop specifications and route preferences.
  name: Static Route Management
- description: Enable and disable NX-OS features programmatically including interface-vlan, BGP, OSPF, and LACP.
  name: Feature Management
- description: Real-time operational data collection using gNMI/gRPC and model-driven telemetry with YANG models.
  name: Streaming Telemetry
- description: Unified policy management and orchestration across multiple ACI, Cloud ACI, and DCNM fabrics.
  name: Multi-Site Orchestration
finops:
- name: Cisco Nexus Finops
  service_category: Data Center Networking
  slug: cisco-nexus-finops
image: https://www.cisco.com/c/en/us/products/switches/nexus-series-switches/index.jpg
integrations:
- description: Automate Nexus switch configuration using Ansible NX-OS modules and playbooks for declarative network management.
  name: Ansible
- description: Provision and manage Cisco ACI and Nexus infrastructure using the Terraform Cisco provider.
  name: Terraform
- description: Application Centric Infrastructure integration for policy-driven network automation with Nexus 9000 switches.
  name: Cisco ACI
- description: Forward NX-OS streaming telemetry and syslog data to Splunk for network analytics and SIEM integration.
  name: Splunk
- description: Integrate Nexus Dashboard events and alerts with ServiceNow ITSM for automated incident management.
  name: ServiceNow
json_schemas:
- name: AaaLoginResponse
  property_count: 2
  slug: cisco-nexus-aaaloginresponse
- name: BdEntityPayload
  property_count: 1
  slug: cisco-nexus-bdentitypayload
- name: BgpDom
  property_count: 1
  slug: cisco-nexus-bgpdom
- name: BgpEntity
  property_count: 2
  slug: cisco-nexus-bgpentity
- name: BgpEntityResponse
  property_count: 2
  slug: cisco-nexus-bgpentityresponse
- name: BgpInst
  property_count: 1
  slug: cisco-nexus-bgpinst
- name: BgpPeer
  property_count: 1
  slug: cisco-nexus-bgppeer
- name: ErrorResponse
  property_count: 1
  slug: cisco-nexus-errorresponse
- name: FmEntityPayload
  property_count: 1
  slug: cisco-nexus-fmentitypayload
- name: ImDataResponse
  property_count: 2
  slug: cisco-nexus-imdataresponse
- name: Cisco Nexus NX-API REST Interface Schema
  property_count: 0
  slug: cisco-nexus-interface
- name: InterfaceEntityPayload
  property_count: 1
  slug: cisco-nexus-interfaceentitypayload
- name: Ipv4InstPayload
  property_count: 1
  slug: cisco-nexus-ipv4instpayload
- name: Ipv4Nexthop
  property_count: 1
  slug: cisco-nexus-ipv4nexthop
- name: Ipv4Route
  property_count: 2
  slug: cisco-nexus-ipv4route
- name: Ipv4RouteListResponse
  property_count: 2
  slug: cisco-nexus-ipv4routelistresponse
- name: Ipv4RouteResponse
  property_count: 2
  slug: cisco-nexus-ipv4routeresponse
- name: L1PhysIf
  property_count: 1
  slug: cisco-nexus-l1physif
- name: L2BD
  property_count: 1
  slug: cisco-nexus-l2bd
- name: AaaLoginResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-aaa-login-response
- name: BdEntityPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bd-entity-payload
- name: BgpDom
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-dom
- name: BgpEntityResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-bgp-entity-response
- name: BgpEntity
  property_count: 2
  slug: cisco-nexus-nxapi-rest-bgp-entity
- name: BgpInst
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-inst
- name: BgpPeer
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-peer
- name: ErrorResponse
  property_count: 1
  slug: cisco-nexus-nxapi-rest-error-response
- name: FmEntityPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-fm-entity-payload
- name: ImDataResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-im-data-response
- name: InterfaceEntityPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-interface-entity-payload
- name: Ipv4InstPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-ipv4-inst-payload
- name: Ipv4Nexthop
  property_count: 1
  slug: cisco-nexus-nxapi-rest-ipv4-nexthop
- name: Ipv4RouteListResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route-list-response
- name: Ipv4RouteResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route-response
- name: Ipv4Route
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route
- name: L1PhysIf
  property_count: 1
  slug: cisco-nexus-nxapi-rest-l1-phys-if
- name: L2BD
  property_count: 1
  slug: cisco-nexus-nxapi-rest-l2-bd
- name: PhysicalInterfaceListResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-physical-interface-list-response
- name: PhysicalInterfaceResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-physical-interface-response
- name: SviIfPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-svi-if-payload
- name: SviIf
  property_count: 1
  slug: cisco-nexus-nxapi-rest-svi-if
- name: SviInterfaceResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-svi-interface-response
- name: TopSystemPayload
  property_count: 1
  slug: cisco-nexus-nxapi-rest-top-system-payload
- name: TopSystemResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-top-system-response
- name: TopSystem
  property_count: 1
  slug: cisco-nexus-nxapi-rest-top-system
- name: VlanBridgeDomainListResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-list-response
- name: VlanBridgeDomainResponse
  property_count: 2
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-response
- name: PhysicalInterfaceListResponse
  property_count: 2
  slug: cisco-nexus-physicalinterfacelistresponse
- name: PhysicalInterfaceResponse
  property_count: 2
  slug: cisco-nexus-physicalinterfaceresponse
- name: SviIf
  property_count: 1
  slug: cisco-nexus-sviif
- name: SviIfPayload
  property_count: 1
  slug: cisco-nexus-sviifpayload
- name: SviInterfaceResponse
  property_count: 2
  slug: cisco-nexus-sviinterfaceresponse
- name: TopSystem
  property_count: 1
  slug: cisco-nexus-topsystem
- name: TopSystemPayload
  property_count: 1
  slug: cisco-nexus-topsystempayload
- name: TopSystemResponse
  property_count: 2
  slug: cisco-nexus-topsystemresponse
- name: VlanBridgeDomainListResponse
  property_count: 2
  slug: cisco-nexus-vlanbridgedomainlistresponse
- name: VlanBridgeDomainResponse
  property_count: 2
  slug: cisco-nexus-vlanbridgedomainresponse
json_structures:
- name: Cisco Nexus Nxapi Rest Aaa Login Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-aaa-login-response-structure
- name: Cisco Nexus Nxapi Rest Bd Entity Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bd-entity-payload-structure
- name: Cisco Nexus Nxapi Rest Bgp Dom Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-dom-structure
- name: Cisco Nexus Nxapi Rest Bgp Entity Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-bgp-entity-response-structure
- name: Cisco Nexus Nxapi Rest Bgp Entity Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-bgp-entity-structure
- name: Cisco Nexus Nxapi Rest Bgp Inst Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-inst-structure
- name: Cisco Nexus Nxapi Rest Bgp Peer Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-bgp-peer-structure
- name: Cisco Nexus Nxapi Rest Error Response Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-error-response-structure
- name: Cisco Nexus Nxapi Rest Fm Entity Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-fm-entity-payload-structure
- name: Cisco Nexus Nxapi Rest Im Data Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-im-data-response-structure
- name: Cisco Nexus Nxapi Rest Interface Entity Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-interface-entity-payload-structure
- name: Cisco Nexus Nxapi Rest Ipv4 Inst Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-ipv4-inst-payload-structure
- name: Cisco Nexus Nxapi Rest Ipv4 Nexthop Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-ipv4-nexthop-structure
- name: Cisco Nexus Nxapi Rest Ipv4 Route List Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route-list-response-structure
- name: Cisco Nexus Nxapi Rest Ipv4 Route Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route-response-structure
- name: Cisco Nexus Nxapi Rest Ipv4 Route Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-ipv4-route-structure
- name: Cisco Nexus Nxapi Rest L1 Phys If Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-l1-phys-if-structure
- name: Cisco Nexus Nxapi Rest L2 Bd Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-l2-bd-structure
- name: Cisco Nexus Nxapi Rest Physical Interface List Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-physical-interface-list-response-structure
- name: Cisco Nexus Nxapi Rest Physical Interface Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-physical-interface-response-structure
- name: Cisco Nexus Nxapi Rest Svi If Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-svi-if-payload-structure
- name: Cisco Nexus Nxapi Rest Svi If Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-svi-if-structure
- name: Cisco Nexus Nxapi Rest Svi Interface Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-svi-interface-response-structure
- name: Cisco Nexus Nxapi Rest Top System Payload Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-top-system-payload-structure
- name: Cisco Nexus Nxapi Rest Top System Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-top-system-response-structure
- name: Cisco Nexus Nxapi Rest Top System Structure
  property_count: 1
  slug: cisco-nexus-nxapi-rest-top-system-structure
- name: Cisco Nexus Nxapi Rest Vlan Bridge Domain List Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-list-response-structure
- name: Cisco Nexus Nxapi Rest Vlan Bridge Domain Response Structure
  property_count: 2
  slug: cisco-nexus-nxapi-rest-vlan-bridge-domain-response-structure
- name: Cisco Nexus Structure
  property_count: 0
  slug: cisco-nexus-structure
jsonld:
- class_count: 3
  name: Cisco Nexus Context
  property_count: 15
  slug: cisco-nexus-context
- class_count: 0
  name: Cisco Nexus Nxapi Rest Context
  property_count: 0
  slug: cisco-nexus-nxapi-rest-context
layout: provider
modified: '2026-05-19'
name: Cisco Nexus Dashboard
nav: Providers
network: true
overview: 'Cisco Nexus Dashboard publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Interfaces API, Routing API, and 2 more. Tagged areas include Data Center, Infrastructure, Network Automation, Networking, and SDN.


  The Cisco Nexus Dashboard catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Cisco Nexus Dashboard''s developer surface includes authentication, engineering blog, training material, sandbox, support, code examples, and 5 more developer resources.'
plans:
- name: Cisco Nexus Plans Pricing
  plan_count: 1
  slug: cisco-nexus-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Cisco Nexus Rate Limits
  slug: cisco-nexus-rate-limits
rules:
- name: Cisco Nexus Dashboard API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: cisco-nexus-jsonschema-spectral-rules
- name: Cisco Nexus Dashboard API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: cisco-nexus-spectral-rules
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 70.1
    developer_ergonomics: 32.6
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 51.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cisco-nexus/refs/heads/main/screenshots/cisco-nexus-2026-06-20T174359.png
security:
- kind: authentication
  name: Cisco Nexus Authentication
  slug: cisco-nexus-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cisco Nexus Domain Security
  slug: cisco-nexus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cisco-nexus
tags:
- Data Center
- Infrastructure
- Network Automation
- Networking
- SDN
- Switches
use_cases:
- description: Automate switch configuration, VLAN provisioning, and routing changes across large-scale data center fabrics.
  name: Data Center Network Automation
- description: Collect real-time telemetry data from Nexus switches for performance monitoring, anomaly detection, and capacity planning.
  name: Network Monitoring and Analytics
- description: Orchestrate network policies and connectivity across geographically distributed data center fabrics.
  name: Multi-Site Fabric Management
- description: Define and manage network infrastructure configurations using YANG models, NETCONF, and RESTCONF for version-controlled deployments.
  name: Infrastructure as Code
- description: Programmatically verify switch configurations against security baselines and generate compliance reports.
  name: Compliance and Auditing
website: https://developer.cisco.com/
---
