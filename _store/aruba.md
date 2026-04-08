---
aid: aruba
url: https://raw.githubusercontent.com/api-evangelist/aruba/refs/heads/main/apis.yml
apis:
- name: Aruba Central API
  description: RESTful API for managing Aruba Central cloud networking platform, providing unified network management, AI-based analytics, and IoT device security for wired, wireless, and SD-WAN networks. APIs follow the Swagger 2.0 (OpenAPI 2.0) specification.
  image: https://www.arubanetworks.com/assets/img/aruba-central-logo.png
  humanUrl: https://developer.arubanetworks.com/central/
  baseUrl: https://apigw-prod2.central.arubanetworks.com
  tags:
  - Analytics
  - Cloud Management
  - Monitoring
  - Network Automation
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/central/docs
  - type: OpenAPI
    url: openapi/aruba-central-api.yml
  - type: JSONSchema
    url: json-schema/aruba-device-schema.json
  - type: JSONLD
    url: json-ld/aruba-context.jsonld
  - type: OpenAPI
    url: https://developer.arubanetworks.com/central/reference
  - type: Authentication
    url: https://developer.arubanetworks.com/central/docs/api-oauth-access-token
  - type: GettingStarted
    url: https://developer.arubanetworks.com/central/docs/rest-api-getting-started
  - type: APIGateway
    url: https://developer.arubanetworks.com/central/docs/api-gateway
  - type: Webhooks
    url: https://developer.arubanetworks.com/central/docs/webhooks-getting-started
  - type: StreamingAPI
    url: https://developer.arubanetworks.com/central/docs/streaming-api-getting-started
  - type: Ansible
    url: https://developer.arubanetworks.com/central/docs/ansible-getting-started
  - type: PythonSDK
    url: https://github.com/aruba/pycentral
- name: Aruba ClearPass API
  description: REST API for ClearPass Policy Manager providing role- and device-based secure network access control for IoT, BYOD, corporate devices, as well as employees, contractors, and guests across any multivendor wired, wireless, and VPN infrastructure.
  image: https://www.arubanetworks.com/assets/img/clearpass-logo.png
  humanUrl: https://developer.arubanetworks.com/cppm/
  baseUrl: https://clearpass.example.com/api
  tags:
  - Authentication
  - Authorization
  - Network Access Control
  - Policy Management
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/cppm/docs
  - type: APIReference
    url: https://developer.arubanetworks.com/cppm/reference
  - type: GettingStarted
    url: https://developer.arubanetworks.com/cppm/docs/getting-started-with-the-clearpass-policy-manager-api
  - type: PythonSDK
    url: https://github.com/aruba/pyclearpass
- name: Aruba AOS-CX REST API
  description: REST API for AOS-CX switches providing full programmability of switches running the AOS-CX operating system. Supports HTTPS POST, GET, PUT, PATCH, and DELETE methods and includes a built-in Swagger UI for API reference and testing.
  humanUrl: https://developer.arubanetworks.com/aoscx/
  tags:
  - Infrastructure
  - Network Automation
  - Programmability
  - Switches
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/aoscx/docs/introduction
  - type: APIReference
    url: https://developer.arubanetworks.com/aoscx/docs/additional-resources-1
  - type: SwaggerUI
    url: https://developer.arubanetworks.com/hpe-aruba-networking-aoscx/docs/aos-cx-swagger-ui
  - type: PythonSDK
    url: https://github.com/aruba/pyaoscx
- name: Aruba EdgeConnect SD-WAN API
  description: REST API for HPE Aruba Networking EdgeConnect SD-WAN providing programmatic access to Orchestrator and EdgeConnect appliance management, monitoring, and configuration. APIs are available at both the Orchestrator level and the Appliance level.
  humanUrl: https://developer.arubanetworks.com/edgeconnect/
  tags:
  - Edge Networking
  - Orchestrator
  - Sd-Wan
  - Wan Optimization
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/edgeconnect/docs/intro
  - type: APIEndpoints
    url: https://developer.arubanetworks.com/edgeconnect/docs/aruba-orchestrator-and-edgeconnect-api-endpoints
  - type: GettingStarted
    url: https://developer.arubanetworks.com/edgeconnect/docs/whats-new
  - type: MakingRequests
    url: https://developer.arubanetworks.com/edgeconnect/docs/making-api-requests
- name: Aruba Fabric Composer API
  description: REST API for HPE Aruba Networking Fabric Composer, an intelligent software-defined orchestration solution that simplifies and accelerates leaf-spine network provisioning and day-to-day operations across rack-scale compute and storage infrastructure.
  humanUrl: https://developer.arubanetworks.com/afc/
  tags:
  - Data Center
  - Fabric
  - Leaf-Spine
  - Orchestration
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/afc/docs/about
  - type: GettingStarted
    url: https://developer.arubanetworks.com/afc/docs/getting-started-with-the-afc-api
  - type: APIReference
    url: https://developer.arubanetworks.com/aruba-fabric-composer/reference/getping
- name: Aruba User Experience Insight API
  description: API for HPE Aruba Networking User Experience Insight (UXI) providing programmatic access to onboarding tasks such as creating, modifying, or removing groups and assigning sensors, agents, networks, and service tests to groups.
  humanUrl: https://developer.arubanetworks.com/uxi/
  tags:
  - Monitoring
  - Network Testing
  - Sensors
  - User Experience
  properties:
  - type: Documentation
    url: https://developer.arubanetworks.com/uxi/docs/user-experience-insight-overview
  - type: GettingStarted
    url: https://developer.arubanetworks.com/uxi/docs/getting-started-with-onboarding-api
  - type: OnboardingAPI
    url: https://developer.arubanetworks.com/uxi/docs/onboarding-api
  - type: MakingAPICalls
    url: https://developer.arubanetworks.com/uxi/docs/making-api-calls
  - type: Authentication
    url: https://developer.arubanetworks.com/uxi/docs/generating-managing-access-token
  - type: PythonSDK
    url: https://developer.arubanetworks.com/uxi/docs/installing-python-package
- name: Aruba AirWave API
  description: API for AirWave network management platform.
  humanUrl: https://www.arubanetworks.com/products/network-management-operations/airwave/
  baseUrl: https://airwave.example.com/api
  tags:
  - Monitoring
  - Network Management
  - Reporting
  properties:
  - type: Documentation
    url: https://support.hpe.com/techhub/eginfolib/airwave/
name: Aruba
tags:
- Cloud
- Infrastructure
- Network Management
- Networking
- Sd-Wan
- Security
- Switches
- Wireless
type: Contract
image: https://www.arubanetworks.com/assets/img/logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for HPE Aruba Networking cloud networking, security, and infrastructure solutions including Central, AOS-CX, ClearPass, EdgeConnect SD-WAN, Fabric Composer, and User Experience Insight.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

