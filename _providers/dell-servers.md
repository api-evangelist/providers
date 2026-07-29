---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Dell Servers Agentic Access
  operation_count: 47
  slug: dell-servers-agentic-access
  summary_line: 47 operations · 8 acting · 1 human-in-the-loop
api_count: 27
apis:
- description: RESTful API for managing Dell PowerEdge MX7000 modular chassis and its components including compute sleds, network devices, IOMs, and storage. OME-Modular shares a common codebase with OpenManage Ente
  name: Dell OpenManage Enterprise Modular API
  slug: dell-servers-openmanage-enterprise-modular
- description: RESTful API for monitoring and managing power consumption, thermal conditions, and energy costs across Dell PowerEdge server infrastructure. Power Manager is a plug-in to the OpenManage Enterprise con
  name: Dell OpenManage Enterprise Power Manager API
  slug: dell-servers-openmanage-enterprise-power-manager
- description: RESTful API for the OpenManage Enterprise SupportAssist plug-in that enables proactive and predictive monitoring of Dell PowerEdge servers. SupportAssist automates support case creation and parts disp
  name: Dell OpenManage Enterprise SupportAssist API
  slug: dell-servers-openmanage-enterprise-supportassist
- description: RESTful API for the OpenManage Integration for VMware vCenter (OMIVV), enabling automation of Dell PowerEdge server management within VMware environments. The API is compliant with OpenAPI Specificati
  name: Dell OpenManage Integration for VMware vCenter API
  slug: dell-servers-openmanage-integration-vmware-vcenter
- description: Server-Sent Events (SSE) streaming API for real-time telemetry data from Dell PowerEdge servers via iDRAC. Provides continuous metric reports including power statistics, CPU and memory metrics, therma
  name: Dell iDRAC Telemetry Streaming API
  slug: dell-servers-idrac-telemetry-streaming
- description: Standards-based interface for remote deployment, configuration, and updates of Dell PowerEdge servers. Lifecycle Controller Remote Services supports WSMAN and Redfish management interfaces for bare-me
  name: Dell Lifecycle Controller Remote Services API
  slug: dell-servers-lifecycle-controller-remote-services
- description: Command-line interface for Dell Remote Access Controller Administration. RACADM provides local and remote command-line access to iDRAC for scripting and automating server configuration, monitoring, an
  name: Dell RACADM CLI
  slug: dell-servers-racadm
- description: Web Services Management API for Dell server hardware management. WSMan provides a SOAP-based interface for managing server configuration, BIOS, RAID, NIC, and HBA settings on Dell PowerEdge servers th
  name: Dell WSMan API
  slug: dell-servers-wsman
- description: User account management and role-based access control
  name: Dell Servers Accounts API
  slug: dell-servers-accounts-api
- description: Alert monitoring, acknowledgment, and management
  name: Dell Servers Alerts API
  slug: dell-servers-alerts-api
- description: Console configuration including network, time, and proxy settings
  name: Dell Servers Application Settings API
  slug: dell-servers-application-settings-api
- description: Physical enclosure resources including power supplies, thermal sensors, and physical component inventory
  name: Dell Servers Chassis API
  slug: dell-servers-chassis-api
- description: Server configuration templates and compliance baselines
  name: Dell Servers Configuration API
  slug: dell-servers-configuration-api
- description: Device inventory, status, and hardware details for managed servers
  name: Dell Servers Devices API
  slug: dell-servers-devices-api
- description: Network discovery configuration and job management
  name: Dell Servers Discovery API
  slug: dell-servers-discovery-api
- description: Event subscriptions and server-sent events configuration
  name: Dell Servers Event Service API
  slug: dell-servers-event-service-api
- description: Firmware catalog management, compliance, and update operations
  name: Dell Servers Firmware API
  slug: dell-servers-firmware-api
- description: Device group management for organizing servers and infrastructure
  name: Dell Servers Groups API
  slug: dell-servers-groups-api
- description: Job creation, scheduling, and status tracking
  name: Dell Servers Jobs API
  slug: dell-servers-jobs-api
- description: Management controller resources for iDRAC configuration, networking, and remote services
  name: Dell Servers Managers API
  slug: dell-servers-managers-api
- description: Report definitions and execution
  name: Dell Servers Reports API
  slug: dell-servers-reports-api
- description: Redfish service root and metadata
  name: Dell Servers Service Root API
  slug: dell-servers-service-root-api
- description: Authentication session creation and management
  name: Dell Servers Sessions API
  slug: dell-servers-sessions-api
- description: Computer system resources including hardware inventory, health status, power state, and BIOS configuration
  name: Dell Servers Systems API
  slug: dell-servers-systems-api
- description: Asynchronous task tracking and lifecycle job management
  name: Dell Servers Task Service API
  slug: dell-servers-task-service-api
- description: Telemetry metric definitions and metric report management
  name: Dell Servers Telemetry Service API
  slug: dell-servers-telemetry-service-api
- description: Firmware update operations and firmware inventory
  name: Dell Servers Update Service API
  slug: dell-servers-update-service-api
arazzos:
- description: Assemble a chassis health report from chassis, power, and thermal reads.
  name: Dell Servers Chassis Health Report
  slug: dell-servers-chassis-health-report-workflow
- description: Read the update service, list firmware versions, and poll active tasks.
  name: Dell Servers Firmware Inventory and Task Audit
  slug: dell-servers-firmware-inventory-tasks-workflow
- description: Inspect the iDRAC manager, its virtual media, and its log services.
  name: Dell Servers iDRAC Manager Overview
  slug: dell-servers-manager-overview-workflow
- description: Find a critical alert, read its detail, then read the source device.
  name: Dell Servers OpenManage Alert Triage
  slug: dell-servers-ome-alert-triage-workflow
- description: Read a managed device and pull its detailed hardware inventory.
  name: Dell Servers OpenManage Device Inventory Deep Dive
  slug: dell-servers-ome-device-inventory-workflow
- description: Create a discovery configuration, watch its job, then list discovered devices.
  name: Dell Servers OpenManage Device Discovery
  slug: dell-servers-ome-discovery-workflow
- description: List firmware catalogs and read their compliance baselines.
  name: Dell Servers OpenManage Firmware Compliance Check
  slug: dell-servers-ome-firmware-compliance-workflow
- description: Check firmware baselines, run an update job, and poll it to completion.
  name: Dell Servers OpenManage Firmware Update Job
  slug: dell-servers-ome-firmware-update-job-workflow
- description: Find a device group, list its member devices, then read one device.
  name: Dell Servers OpenManage Group Device Expansion
  slug: dell-servers-ome-group-devices-workflow
- description: Authenticate to OpenManage Enterprise and list managed server devices.
  name: Dell Servers OpenManage Session and Device Listing
  slug: dell-servers-ome-session-list-devices-workflow
- description: Pick a configuration template, run a deploy job, and poll it to completion.
  name: Dell Servers OpenManage Template Deployment Job
  slug: dell-servers-ome-template-deploy-job-workflow
- description: Issue a power action on a system and poll until the power state settles.
  name: Dell Servers Power Action with State Polling
  slug: dell-servers-power-action-poll-workflow
- description: Open a Redfish session and list systems using the session token.
  name: Dell Servers Redfish Session Bootstrap
  slug: dell-servers-redfish-session-bootstrap-workflow
- description: Read a system, set a pending BIOS boot override, then power-cycle it.
  name: Dell Servers Set Boot Device and Reset
  slug: dell-servers-set-boot-and-reset-workflow
- description: Collect system, storage, network, and BIOS detail for one server.
  name: Dell Servers System Hardware Inventory
  slug: dell-servers-system-inventory-workflow
- description: Discover metric reports and subscribe to telemetry events.
  name: Dell Servers Telemetry Subscription Setup
  slug: dell-servers-telemetry-subscription-workflow
artifact_total: 83
collections:
- collection_type: postman
  name: Dell Servers Dell iDRAC Redfish REST API
  slug: postman-dell-servers-idrac-redfish
- collection_type: postman
  name: Dell Servers Dell OpenManage Enterprise API
  slug: postman-dell-servers-openmanage-enterprise
- collection_type: open
  name: Dell Servers Dell iDRAC Redfish REST API
  slug: open-dell-servers-idrac-redfish
- collection_type: open
  name: Dell Servers Dell OpenManage Enterprise API
  slug: open-dell-servers-openmanage-enterprise
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dell-servers-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dell-servers-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dell-servers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dell-servers-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/dell-servers/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-chassis-health-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-firmware-inventory-tasks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-manager-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-alert-triage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-device-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-firmware-compliance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-firmware-update-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-group-devices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-session-list-devices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-ome-template-deploy-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-power-action-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-redfish-session-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-set-boot-and-reset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-system-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/dell-servers-telemetry-subscription-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.dell.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v6.x-series/smog_26.0/idrac-restful-apis-redfish-standards-based?guid=guid-476c6603-818e-4e2e-82f0-699bde0c3a3c&lang=en-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.dell.com/support/product-details/en-us/product/dell-openmanage-enterprise/resources/manuals
- group: operate
  title: ''
  type: Support
  url: https://www.dell.com/support
- group: operate
  title: ''
  type: Community
  url: https://www.dell.com/community/
- group: company
  title: ''
  type: Blog
  url: https://www.dell.com/community/en/topics/developer-blogs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://i.dell.com/sites/csdocuments/Legal_Docs/en/us/api-terms-of-use_en.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dell.com/en-us/lp/legal/policies-privacy
- group: company
  title: ''
  type: Website
  url: https://www.dell.com/en-us/lp/dt/open-manage
- group: build
  title: ''
  type: GitHub
  url: https://github.com/dell
- group: build
  title: ''
  type: SDKs
  url: https://developer.dell.com/apis/
- group: start
  title: ''
  type: Signup
  url: https://developer.dell.com/
- group: start
  title: ''
  type: Login
  url: https://developer.dell.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dell-servers-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dell-servers-vocabulary.yml
created: '2024-01-01'
description: APIs for managing and monitoring Dell PowerEdge servers and infrastructure, including the iDRAC Redfish out-of-band management interface, OpenManage Enterprise centralized console and its modular, power, support, and VMware integrations, telemetry streaming, the Lifecycle Controller, RACADM, and the legacy WSMan interface.
finops:
- name: Dell Servers Finops
  service_category: Hardware Infrastructure
  slug: dell-servers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dell-servers.png
json_schemas:
- name: Alert
  property_count: 11
  slug: dell-servers-alert
- name: Bios
  property_count: 4
  slug: dell-servers-bios
- name: Chassis
  property_count: 13
  slug: dell-servers-chassis
- name: ComputerSystem
  property_count: 19
  slug: dell-servers-computersystem
- name: ComputerSystemCollection
  property_count: 5
  slug: dell-servers-computersystemcollection
- name: ConfigTemplate
  property_count: 9
  slug: dell-servers-configtemplate
- name: Device
  property_count: 15
  slug: dell-servers-device
- name: DiscoveryConfigGroup
  property_count: 4
  slug: dell-servers-discoveryconfiggroup
- name: EventSubscription
  property_count: 4
  slug: dell-servers-eventsubscription
- name: FirmwareBaseline
  property_count: 5
  slug: dell-servers-firmwarebaseline
- name: FirmwareCatalog
  property_count: 6
  slug: dell-servers-firmwarecatalog
- name: Group
  property_count: 9
  slug: dell-servers-group
- name: InventoryDetail
  property_count: 2
  slug: dell-servers-inventorydetail
- name: Job
  property_count: 9
  slug: dell-servers-job
- name: JobRequest
  property_count: 4
  slug: dell-servers-jobrequest
- name: Manager
  property_count: 7
  slug: dell-servers-manager
- name: Power
  property_count: 3
  slug: dell-servers-power
- name: ReportDefinition
  property_count: 5
  slug: dell-servers-reportdefinition
- name: ResetAction
  property_count: 1
  slug: dell-servers-resetaction
- name: ResourceCollection
  property_count: 5
  slug: dell-servers-resourcecollection
- name: ResourceLink
  property_count: 1
  slug: dell-servers-resourcelink
- name: ServiceRoot
  property_count: 14
  slug: dell-servers-serviceroot
- name: Status
  property_count: 3
  slug: dell-servers-status
- name: Thermal
  property_count: 3
  slug: dell-servers-thermal
json_structures:
- name: Dell Servers Structure
  property_count: 0
  slug: dell-servers-structure
jsonld:
- class_count: 10
  name: Dell Servers Context
  property_count: 12
  slug: dell-servers-context
layout: provider
modified: '2026-05-19'
name: Dell Servers
nav: Providers
network: true
overview: 'Dell Servers publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Alerts API, Application Settings API, and 16 more. Tagged areas include Hardware, Infrastructure, Management, Monitoring, and Servers.


  The Dell Servers catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Dell Servers'' developer surface includes authentication, developer portal, getting-started guide, documentation, support, engineering blog, GitHub presence, and 29 more developer resources.'
plans:
- name: Dell Servers Plans Pricing
  plan_count: 3
  slug: dell-servers-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 3
  name: Dell Servers Rate Limits
  slug: dell-servers-rate-limits
rules:
- name: Dell Servers API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dell-servers-idrac-redfish-rules
- name: Dell Servers API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dell-servers-jsonschema-spectral-rules
- name: Dell Servers API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: dell-servers-openmanage-enterprise-rules
score:
  band: strong
  composite: 59.7
  delta: -4.5
  facets:
    commercial_clarity: 73.7
    contract_quality: 66.9
    developer_ergonomics: 56.5
    discoverability: 59.3
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 64.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/screenshots/dell-servers-2026-06-20T175900.png
security:
- kind: authentication
  name: Dell Servers Authentication
  slug: dell-servers-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dell Servers Domain Security
  slug: dell-servers-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dell Servers Vulnerability Disclosure
  slug: dell-servers-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: dell-servers
tags:
- Hardware
- Infrastructure
- Management
- Monitoring
- Servers
website: https://www.dell.com/en-us/lp/dt/open-manage
---
