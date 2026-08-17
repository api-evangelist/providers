---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Aruba Agentic Access
  operation_count: 19
  slug: aruba-agentic-access
  summary_line: 19 operations · 8 acting
api_count: 11
apis:
- description: REST API for ClearPass Policy Manager providing role- and device-based secure network access control for IoT, BYOD, corporate devices, as well as employees, contractors, and guests across any multiven
  name: Aruba ClearPass API
  slug: aruba-clearpass-api
- description: REST API for AOS-CX switches providing full programmability of switches running the AOS-CX operating system. Supports HTTPS POST, GET, PUT, PATCH, and DELETE methods and includes a built-in Swagger UI
  name: Aruba AOS-CX REST API
  slug: aruba-aos-cx-rest-api
- description: REST API for HPE Aruba Networking EdgeConnect SD-WAN providing programmatic access to Orchestrator and EdgeConnect appliance management, monitoring, and configuration. APIs are available at both the O
  name: Aruba EdgeConnect SD-WAN API
  slug: aruba-edgeconnect-sd-wan-api
- description: REST API for HPE Aruba Networking Fabric Composer, an intelligent software-defined orchestration solution that simplifies and accelerates leaf-spine network provisioning and day-to-day operations acro
  name: Aruba Fabric Composer API
  slug: aruba-fabric-composer-api
- description: API for HPE Aruba Networking User Experience Insight (UXI) providing programmatic access to onboarding tasks such as creating, modifying, or removing groups and assigning sensors, agents, networks, an
  name: Aruba User Experience Insight API
  slug: aruba-user-experience-insight-api
- description: API for AirWave network management platform.
  name: Aruba AirWave API
  slug: aruba-airwave-api
- description: Access point monitoring and management including status, statistics, RF information, and client connectivity.
  name: Aruba Access Points API
  slug: aruba-access-points-api
- description: Device inventory management including listing, searching, and managing devices across the Aruba Central platform.
  name: Aruba Devices API
  slug: aruba-devices-api
- description: Configuration group management for organizing devices, applying templates, and managing group-level settings.
  name: Aruba Groups API
  slug: aruba-groups-api
- description: Network-wide monitoring for clients, networks, gateways, and overall network health metrics.
  name: Aruba Monitoring API
  slug: aruba-monitoring-api
- description: Site and location management for organizing network infrastructure by physical location.
  name: Aruba Sites API
  slug: aruba-sites-api
artifact_total: 141
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aruba Central Access Points API
  slug: open-aruba-access-points-api
- collection_type: open
  name: Aruba Central API
  slug: open-aruba-central-api
- collection_type: open
  name: Aruba Central Access Points Devices API
  slug: open-aruba-devices-api
- collection_type: open
  name: Aruba Central Access Points Groups API
  slug: open-aruba-groups-api
- collection_type: open
  name: Aruba Central Access Points Monitoring API
  slug: open-aruba-monitoring-api
- collection_type: open
  name: Aruba Central Access Points Sites API
  slug: open-aruba-sites-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aruba-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aruba-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aruba-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aruba-a-hewlett-packard-enterprise-company
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.arubanetworks.com
- group: other
  title: ''
  type: Hub
  url: https://devhub.arubanetworks.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aruba
- group: company
  title: ''
  type: Blog
  url: https://blogs.arubanetworks.com/
- group: operate
  title: ''
  type: Support
  url: https://www.arubanetworks.com/support-services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arubanetworks.com/company/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arubanetworks.com/company/legal/privacy-policy/
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.arubanetworks.com/llms.txt
created: '2024-01-01'
description: APIs for HPE Aruba Networking cloud networking, security, and infrastructure solutions including Central, AOS-CX, ClearPass, EdgeConnect SD-WAN, Fabric Composer, and User Experience Insight.
examples:
- key_count: 0
  name: Aruba Central Access Point Detail Example
  slug: aruba-central-access-point-detail-example
- key_count: 21
  name: Aruba Central Access Point Example
  slug: aruba-central-access-point-example
- key_count: 3
  name: Aruba Central Access Point List Response Example
  slug: aruba-central-access-point-list-response-example
- key_count: 15
  name: Aruba Central Client Example
  slug: aruba-central-client-example
- key_count: 3
  name: Aruba Central Client List Response Example
  slug: aruba-central-client-list-response-example
- key_count: 13
  name: Aruba Central Device Example
  slug: aruba-central-device-example
- key_count: 3
  name: Aruba Central Device List Response Example
  slug: aruba-central-device-list-response-example
- key_count: 3
  name: Aruba Central Error Response Example
  slug: aruba-central-error-response-example
- key_count: 11
  name: Aruba Central Gateway Example
  slug: aruba-central-gateway-example
- key_count: 3
  name: Aruba Central Gateway List Response Example
  slug: aruba-central-gateway-list-response-example
- key_count: 2
  name: Aruba Central Group Create Example
  slug: aruba-central-group-create-example
- key_count: 2
  name: Aruba Central Group Detail Example
  slug: aruba-central-group-detail-example
- key_count: 2
  name: Aruba Central Group Example
  slug: aruba-central-group-example
- key_count: 3
  name: Aruba Central Group List Response Example
  slug: aruba-central-group-list-response-example
- key_count: 1
  name: Aruba Central Group Update Example
  slug: aruba-central-group-update-example
- key_count: 5
  name: Aruba Central Network Example
  slug: aruba-central-network-example
- key_count: 3
  name: Aruba Central Network List Response Example
  slug: aruba-central-network-list-response-example
- key_count: 9
  name: Aruba Central Radio Example
  slug: aruba-central-radio-example
- key_count: 8
  name: Aruba Central Site Create Example
  slug: aruba-central-site-create-example
- key_count: 0
  name: Aruba Central Site Detail Example
  slug: aruba-central-site-detail-example
- key_count: 2
  name: Aruba Central Site Device Association Example
  slug: aruba-central-site-device-association-example
- key_count: 11
  name: Aruba Central Site Example
  slug: aruba-central-site-example
- key_count: 3
  name: Aruba Central Site List Response Example
  slug: aruba-central-site-list-response-example
- key_count: 8
  name: Aruba Central Site Update Example
  slug: aruba-central-site-update-example
features:
- description: Single pane of glass for managing wired, wireless, and SD-WAN infrastructure across distributed enterprise environments.
  name: Unified Cloud Management
- description: Artificial intelligence and machine learning-driven network analytics for proactive troubleshooting and optimization.
  name: AI-Powered Analytics
- description: Role-based and device-based access control with ClearPass for IoT, BYOD, and enterprise devices.
  name: Zero Trust Security
- description: Programmable APIs across all platforms enabling infrastructure-as-code and automated provisioning.
  name: Network Automation
- description: Centralized management of EdgeConnect SD-WAN appliances with application-aware routing and WAN optimization.
  name: SD-WAN Orchestration
- description: Synthetic testing and real-time monitoring of network and application performance from the user perspective.
  name: User Experience Monitoring
finops:
- name: Aruba Finops
  service_category: Networking
  slug: aruba-finops
image: https://www.arubanetworks.com/assets/img/logo.png
integrations:
- description: Ansible modules and playbooks for automating Aruba Central and AOS-CX switch configuration.
  name: Ansible
- description: Infrastructure-as-code provisioning for Aruba network infrastructure using Terraform providers.
  name: Terraform
- description: Integration with ServiceNow for IT service management and automated incident response.
  name: ServiceNow
- description: Log and event forwarding from Aruba infrastructure to Splunk for security analytics and monitoring.
  name: Splunk
- description: Integration with VMware environments for network-aware virtual infrastructure management.
  name: VMware vSphere
json_schemas:
- name: AccessPoint
  property_count: 21
  slug: aruba-accesspoint
- name: AccessPointDetail
  property_count: 0
  slug: aruba-accesspointdetail
- name: AccessPointListResponse
  property_count: 3
  slug: aruba-accesspointlistresponse
- name: AccessPointDetail
  property_count: 0
  slug: aruba-central-access-point-detail
- name: AccessPointListResponse
  property_count: 3
  slug: aruba-central-access-point-list-response
- name: AccessPoint
  property_count: 21
  slug: aruba-central-access-point
- name: ClientListResponse
  property_count: 3
  slug: aruba-central-client-list-response
- name: Client
  property_count: 15
  slug: aruba-central-client
- name: DeviceListResponse
  property_count: 3
  slug: aruba-central-device-list-response
- name: Device
  property_count: 13
  slug: aruba-central-device
- name: ErrorResponse
  property_count: 3
  slug: aruba-central-error-response
- name: GatewayListResponse
  property_count: 3
  slug: aruba-central-gateway-list-response
- name: Gateway
  property_count: 11
  slug: aruba-central-gateway
- name: GroupCreate
  property_count: 2
  slug: aruba-central-group-create
- name: GroupDetail
  property_count: 2
  slug: aruba-central-group-detail
- name: GroupListResponse
  property_count: 3
  slug: aruba-central-group-list-response
- name: Group
  property_count: 2
  slug: aruba-central-group
- name: GroupUpdate
  property_count: 1
  slug: aruba-central-group-update
- name: NetworkListResponse
  property_count: 3
  slug: aruba-central-network-list-response
- name: Network
  property_count: 5
  slug: aruba-central-network
- name: Radio
  property_count: 9
  slug: aruba-central-radio
- name: SiteCreate
  property_count: 8
  slug: aruba-central-site-create
- name: SiteDetail
  property_count: 0
  slug: aruba-central-site-detail
- name: SiteDeviceAssociation
  property_count: 2
  slug: aruba-central-site-device-association
- name: SiteListResponse
  property_count: 3
  slug: aruba-central-site-list-response
- name: Site
  property_count: 11
  slug: aruba-central-site
- name: SiteUpdate
  property_count: 8
  slug: aruba-central-site-update
- name: Client
  property_count: 15
  slug: aruba-client
- name: ClientListResponse
  property_count: 3
  slug: aruba-clientlistresponse
- name: Aruba Central Device
  property_count: 27
  slug: aruba-device
- name: DeviceListResponse
  property_count: 3
  slug: aruba-devicelistresponse
- name: ErrorResponse
  property_count: 3
  slug: aruba-errorresponse
- name: Gateway
  property_count: 11
  slug: aruba-gateway
- name: GatewayListResponse
  property_count: 3
  slug: aruba-gatewaylistresponse
- name: Group
  property_count: 2
  slug: aruba-group
- name: GroupCreate
  property_count: 2
  slug: aruba-groupcreate
- name: GroupDetail
  property_count: 2
  slug: aruba-groupdetail
- name: GroupListResponse
  property_count: 3
  slug: aruba-grouplistresponse
- name: GroupUpdate
  property_count: 1
  slug: aruba-groupupdate
- name: Network
  property_count: 5
  slug: aruba-network
- name: NetworkListResponse
  property_count: 3
  slug: aruba-networklistresponse
- name: Radio
  property_count: 9
  slug: aruba-radio
- name: Site
  property_count: 11
  slug: aruba-site
- name: SiteCreate
  property_count: 8
  slug: aruba-sitecreate
- name: SiteDetail
  property_count: 0
  slug: aruba-sitedetail
- name: SiteDeviceAssociation
  property_count: 2
  slug: aruba-sitedeviceassociation
- name: SiteListResponse
  property_count: 3
  slug: aruba-sitelistresponse
- name: SiteUpdate
  property_count: 8
  slug: aruba-siteupdate
json_structures:
- name: Aruba Central Access Point Detail Structure
  property_count: 0
  slug: aruba-central-access-point-detail-structure
- name: Aruba Central Access Point List Response Structure
  property_count: 3
  slug: aruba-central-access-point-list-response-structure
- name: Aruba Central Access Point Structure
  property_count: 21
  slug: aruba-central-access-point-structure
- name: Aruba Central Client List Response Structure
  property_count: 3
  slug: aruba-central-client-list-response-structure
- name: Aruba Central Client Structure
  property_count: 15
  slug: aruba-central-client-structure
- name: Aruba Central Device List Response Structure
  property_count: 3
  slug: aruba-central-device-list-response-structure
- name: Aruba Central Device Structure
  property_count: 13
  slug: aruba-central-device-structure
- name: Aruba Central Error Response Structure
  property_count: 3
  slug: aruba-central-error-response-structure
- name: Aruba Central Gateway List Response Structure
  property_count: 3
  slug: aruba-central-gateway-list-response-structure
- name: Aruba Central Gateway Structure
  property_count: 11
  slug: aruba-central-gateway-structure
- name: Aruba Central Group Create Structure
  property_count: 2
  slug: aruba-central-group-create-structure
- name: Aruba Central Group Detail Structure
  property_count: 2
  slug: aruba-central-group-detail-structure
- name: Aruba Central Group List Response Structure
  property_count: 3
  slug: aruba-central-group-list-response-structure
- name: Aruba Central Group Structure
  property_count: 2
  slug: aruba-central-group-structure
- name: Aruba Central Group Update Structure
  property_count: 1
  slug: aruba-central-group-update-structure
- name: Aruba Central Network List Response Structure
  property_count: 3
  slug: aruba-central-network-list-response-structure
- name: Aruba Central Network Structure
  property_count: 5
  slug: aruba-central-network-structure
- name: Aruba Central Radio Structure
  property_count: 9
  slug: aruba-central-radio-structure
- name: Aruba Central Site Create Structure
  property_count: 8
  slug: aruba-central-site-create-structure
- name: Aruba Central Site Detail Structure
  property_count: 0
  slug: aruba-central-site-detail-structure
- name: Aruba Central Site Device Association Structure
  property_count: 2
  slug: aruba-central-site-device-association-structure
- name: Aruba Central Site List Response Structure
  property_count: 3
  slug: aruba-central-site-list-response-structure
- name: Aruba Central Site Structure
  property_count: 11
  slug: aruba-central-site-structure
- name: Aruba Central Site Update Structure
  property_count: 8
  slug: aruba-central-site-update-structure
- name: Aruba Structure
  property_count: 0
  slug: aruba-structure
jsonld:
- class_count: 0
  name: Aruba Central Context
  property_count: 0
  slug: aruba-central-context
- class_count: 0
  name: Aruba Context
  property_count: 8
  slug: aruba-context
layout: provider
modified: '2026-05-19'
name: Aruba
nav: Providers
network: true
overview: 'Aruba publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Access Points API, Devices API, Groups API, and 2 more. Tagged areas include Cloud, Infrastructure, Network Management, Networking, and SD-WAN.


  The Aruba catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Aruba''s developer surface includes authentication, engineering blog, support, and 9 more developer resources.'
plans:
- name: Aruba Plans Pricing
  plan_count: 1
  slug: aruba-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 3
  name: Aruba Rate Limits
  slug: aruba-rate-limits
rules:
- name: Aruba API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aruba-jsonschema-spectral-rules
- name: Aruba API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 10
  slug: aruba-spectral-rules
score:
  band: developing
  composite: 43.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 66.4
    developer_ergonomics: 26.1
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aruba/refs/heads/main/screenshots/aruba-2026-06-20T172454.png
security:
- kind: authentication
  name: Aruba Authentication
  slug: aruba-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Aruba Domain Security
  slug: aruba-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aruba
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- SD-WAN
- Security
- Switches
- Wireless
use_cases:
- description: Automate provisioning, monitoring, and troubleshooting of campus wired and wireless networks using Central APIs.
  name: Campus Network Automation
- description: Programmatically deploy and manage EdgeConnect SD-WAN appliances across branch offices with centralized orchestration.
  name: Branch Office SD-WAN Deployment
- description: Automate secure onboarding and policy assignment for IoT devices using ClearPass APIs.
  name: IoT Device Onboarding
- description: Build custom monitoring dashboards using Central APIs to track device health, client connectivity, and network performance.
  name: Network Health Dashboards
- description: Manage groups, sites, and device configurations across multiple locations programmatically.
  name: Multi-Site Configuration Management
website: https://developer.arubanetworks.com
---
