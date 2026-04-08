---
aid: dell-servers
url: https://raw.githubusercontent.com/api-evangelist/dell-servers/refs/heads/main/apis.yml
apis:
- name: iDRAC REST API
  description: Integrated Dell Remote Access Controller REST API for server management, monitoring, and configuration. The iDRAC RESTful API builds upon the DMTF Redfish standard to provide a comprehensive interface for out-of-band server lifecycle management of Dell PowerEdge servers.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{idrac-ip}/redfish/v1
  humanURL: https://www.dell.com/support/kbdoc/en-us/000178045/redfish-api-with-dell-integrated-remote-access-controller
  tags:
  - BMC
  - Hardware Monitoring
  - Redfish
  - Server Management
  properties:
  - type: Documentation
    url: https://www.dell.com/support/kbdoc/en-us/000178045/redfish-api-with-dell-integrated-remote-access-controller
  - type: OpenAPI
    url: https://downloads.dell.com/manuals/common/dellemc-idrac-redfish-openapi.yaml
  - type: Authentication
    url: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v4.x-series/idrac9_4.00.00.00_redfishapiguide_pub/redfish-authentication-and-authorization?guid=guid-d572792f-afd2-499a-bf12-38a6778b9bbc&lang=en-us
  - type: Getting Started
    url: https://developer.dell.com/apis/2978/versions/5.xx/docs/1.0Intro.md
  - type: GitHub Repository
    url: https://github.com/dell/iDRAC-Redfish-Scripting
- name: Dell OpenManage Enterprise API
  description: REST API for centralized management of Dell EMC servers, chassis, and storage. OpenManage Enterprise provides a comprehensive console for discovery, inventory, monitoring, and lifecycle management of Dell PowerEdge infrastructure at scale.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{ome-server}/api
  humanURL: https://www.dell.com/support/kbdoc/en-us/000175879/support-for-openmanage-enterprise
  tags:
  - Automation
  - Enterprise Management
  - Monitoring
  - Orchestration
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/dell-openmanage-enterprise/ome_p_api_guide/preface?guid=guid-82bcb773-392d-43a4-bdfa-431dd06a06f4&lang=en-us
  - type: API Reference
    url: https://{ome-server}/api/docs
  - type: Swagger UI
    url: https://{ome-server}/api/swagger-ui
  - type: GitHub Repository
    url: https://github.com/dell/OpenManage-Enterprise
- name: Dell OpenManage Enterprise Modular API
  description: RESTful API for managing Dell PowerEdge MX7000 modular chassis and its components including compute sleds, network devices, IOMs, and storage. OME-Modular shares a common codebase with OpenManage Enterprise and supports multi-chassis management with up to 20 chassis per group.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{omem-server}/api
  humanURL: https://www.dell.com/support/manuals/en-us/openmanage-enterprise-modular/omem_2.00.00_api/openmanage-enterprise-modular-edition?guid=guid-fe459ff7-030b-4375-a6d5-9f0ab2278946&lang=en-us
  tags:
  - Chassis Management
  - Modular Infrastructure
  - Multi-Chassis
  - PowerEdge MX
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/openmanage-enterprise-modular/omem_2.00.00_api/openmanage-enterprise-modular-edition?guid=guid-fe459ff7-030b-4375-a6d5-9f0ab2278946&lang=en-us
  - type: GitHub Repository
    url: https://github.com/dell/OpenManage-Enterprise
- name: Dell OpenManage Enterprise Power Manager API
  description: RESTful API for monitoring and managing power consumption, thermal conditions, and energy costs across Dell PowerEdge server infrastructure. Power Manager is a plug-in to the OpenManage Enterprise console that provides power policies, capping, and reporting capabilities.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{ome-server}/api
  humanURL: https://developer.dell.com/apis/5708/versions/3.0/docs/0.1%20Introduction-to-PMP-API.md
  tags:
  - Data Center
  - Energy Efficiency
  - Power Management
  - Thermal Monitoring
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/openmanage-enterprise-power-manager/pmp_3.1_apiguide/about-this-document
- name: Dell OpenManage Enterprise SupportAssist API
  description: RESTful API for the OpenManage Enterprise SupportAssist plug-in that enables proactive and predictive monitoring of Dell PowerEdge servers. SupportAssist automates support case creation and parts dispatch for servers with ProSupport and ProSupport Plus entitlements.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{ome-server}/api
  humanURL: https://developer.dell.com/apis/2848/versions/1.2
  tags:
  - Alerting
  - Predictive Analytics
  - Proactive Monitoring
  - Support
  properties:
  - type: Documentation
    url: https://developer.dell.com/apis/2848/versions/1.2
- name: Dell OpenManage Integration for VMware vCenter API
  description: RESTful API for the OpenManage Integration for VMware vCenter (OMIVV), enabling automation of Dell PowerEdge server management within VMware environments. The API is compliant with OpenAPI Specification 3.0.0 and supports firmware updates, inventory, and monitoring tasks.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{omivv-server}/api
  humanURL: https://www.dell.com/support/manuals/en-us/openmanage-integration-vmware-vcenter/omivv_5.4_api/overview
  tags:
  - Server Management
  - vCenter Integration
  - Virtualization
  - VMware
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/openmanage-integration-vmware-vcenter/omivv_5.4_api/overview
  - type: GitHub Repository
    url: https://github.com/dell/omivv
- name: Dell iDRAC Telemetry Streaming API
  description: Server-Sent Events (SSE) streaming API for real-time telemetry data from Dell PowerEdge servers via iDRAC. Provides continuous metric reports including power statistics, CPU and memory metrics, thermal sensor data, NIC statistics, and PSU metrics using the Redfish TelemetryService.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{idrac-ip}/redfish/v1/SSE
  humanURL: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v4.x-series/idrac9_4.00.00.00_redfishapiguide_pub/server-sent-events?guid=guid-fc87fd01-2cff-4ae0-9714-1bd712bb5ce3&lang=en-us
  tags:
  - Monitoring
  - Server-Sent Events
  - Streaming
  - Telemetry
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v4.x-series/idrac9_4.00.00.00_redfishapiguide_pub/server-sent-events?guid=guid-fc87fd01-2cff-4ae0-9714-1bd712bb5ce3&lang=en-us
  - type: GitHub Repository
    url: https://github.com/dell/iDRAC-Telemetry-Reference-Tools
- name: Dell Lifecycle Controller Remote Services API
  description: Standards-based interface for remote deployment, configuration, and updates of Dell PowerEdge servers. Lifecycle Controller Remote Services supports WSMAN and Redfish management interfaces for bare-metal provisioning and one-to-many operating system deployments.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{idrac-ip}/wsman
  humanURL: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v3.4-series/idrac_3.40.40.40_lc_re_qsg/about-lifecycle-controller-api?guid=guid-f7bcc1d3-46c1-4ec3-9a45-0f33d734585c&lang=en-us
  tags:
  - Deployment
  - Lifecycle Management
  - Provisioning
  - Remote Services
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v3.4-series/idrac_3.40.40.40_lc_re_qsg/about-lifecycle-controller-api?guid=guid-f7bcc1d3-46c1-4ec3-9a45-0f33d734585c&lang=en-us
- name: Dell RACADM CLI
  description: Command-line interface for Dell Remote Access Controller Administration. RACADM provides local and remote command-line access to iDRAC for scripting and automating server configuration, monitoring, and management tasks.
  image: https://www.dell.com/favicon.ico
  humanURL: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v3.x-series/idrac9_racadm_pub/
  tags:
  - Automation
  - CLI
  - Remote Management
  - Scripting
  properties:
  - type: Documentation
    url: https://www.dell.com/support/manuals/en-us/idrac9-lifecycle-controller-v3.x-series/idrac9_racadm_pub/
- name: Dell WSMan API
  description: Web Services Management API for Dell server hardware management. WSMan provides a SOAP-based interface for managing server configuration, BIOS, RAID, NIC, and HBA settings on Dell PowerEdge servers through iDRAC.
  image: https://www.dell.com/favicon.ico
  baseURL: https://{idrac-ip}/wsman
  humanURL: https://www.dell.com/support/kbdoc/en-us/000178046/how-to-use-the-wsman-interface-on-idrac
  tags:
  - Hardware Management
  - Legacy
  - Web Services
  - WSMan
  properties:
  - type: Documentation
    url: https://www.dell.com/support/kbdoc/en-us/000178046/how-to-use-the-wsman-interface-on-idrac
  - type: Profile Catalog
    url: https://downloads.dell.com/solutions/dell-management-solution-resources/
  - type: GitHub Repository
    url: https://github.com/dell/DellPEWSMANTools
name: Dell Servers
tags:
- Hardware
- Infrastructure
- Management
- Monitoring
- Servers
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing and monitoring Dell PowerEdge servers and infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

