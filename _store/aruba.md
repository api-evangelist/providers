---
aid: aruba
name: Aruba
description: APIs for HPE Aruba Networking cloud networking, security, and infrastructure solutions including Central, AOS-CX, ClearPass, EdgeConnect SD-WAN, Fabric Composer, and User Experience Insight.
image: https://www.arubanetworks.com/assets/img/logo.png
url: https://raw.githubusercontent.com/api-evangelist/aruba/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Cloud
  - Infrastructure
  - Network Management
  - Networking
  - SD-WAN
  - Security
  - Switches
  - Wireless
apis:
  - name: Aruba Central API
    description: RESTful API for managing Aruba Central cloud networking platform, providing unified network management, AI-based analytics, and IoT device security for wired, wireless, and SD-WAN networks. APIs follow the Swagger 2.0 (OpenAPI 2.0) specification.
    image: https://www.arubanetworks.com/assets/img/aruba-central-logo.png
    humanURL: https://developer.arubanetworks.com/central/
    baseURL: https://apigw-prod2.central.arubanetworks.com
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
      - type: OpenAPI
        url: https://developer.arubanetworks.com/central/reference
      - type: Authentication
        url: https://developer.arubanetworks.com/central/docs/api-oauth-access-token
      - type: GettingStarted
        url: https://developer.arubanetworks.com/central/docs/rest-api-getting-started
      - type: SDK
        url: https://github.com/aruba/pycentral
        title: Python SDK
  - name: Aruba ClearPass API
    description: REST API for ClearPass Policy Manager providing role- and device-based secure network access control for IoT, BYOD, corporate devices, as well as employees, contractors, and guests across any multivendor wired, wireless, and VPN infrastructure.
    image: https://www.arubanetworks.com/assets/img/clearpass-logo.png
    humanURL: https://developer.arubanetworks.com/cppm/
    baseURL: https://clearpass.example.com/api
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
      - type: SDK
        url: https://github.com/aruba/pyclearpass
        title: Python SDK
  - name: Aruba AOS-CX REST API
    description: REST API for AOS-CX switches providing full programmability of switches running the AOS-CX operating system. Supports HTTPS POST, GET, PUT, PATCH, and DELETE methods and includes a built-in Swagger UI for API reference and testing.
    humanURL: https://developer.arubanetworks.com/aoscx/
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
      - type: SDK
        url: https://github.com/aruba/pyaoscx
        title: Python SDK
  - name: Aruba EdgeConnect SD-WAN API
    description: REST API for HPE Aruba Networking EdgeConnect SD-WAN providing programmatic access to Orchestrator and EdgeConnect appliance management, monitoring, and configuration. APIs are available at both the Orchestrator level and the Appliance level.
    humanURL: https://developer.arubanetworks.com/edgeconnect/
    tags:
      - Edge Networking
      - Orchestrator
      - SD-WAN
      - WAN Optimization
    properties:
      - type: Documentation
        url: https://developer.arubanetworks.com/edgeconnect/docs/intro
      - type: GettingStarted
        url: https://developer.arubanetworks.com/edgeconnect/docs/whats-new
  - name: Aruba Fabric Composer API
    description: REST API for HPE Aruba Networking Fabric Composer, an intelligent software-defined orchestration solution that simplifies and accelerates leaf-spine network provisioning and day-to-day operations across rack-scale compute and storage infrastructure.
    humanURL: https://developer.arubanetworks.com/afc/
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
    humanURL: https://developer.arubanetworks.com/uxi/
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
      - type: Authentication
        url: https://developer.arubanetworks.com/uxi/docs/generating-managing-access-token
      - type: SDK
        url: https://developer.arubanetworks.com/uxi/docs/installing-python-package
        title: Python SDK
  - name: Aruba AirWave API
    description: API for AirWave network management platform.
    humanURL: https://www.arubanetworks.com/products/network-management-operations/airwave/
    baseURL: https://airwave.example.com/api
    tags:
      - Monitoring
      - Network Management
      - Reporting
    properties:
      - type: Documentation
        url: https://support.hpe.com/techhub/eginfolib/airwave/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: DeveloperPortal
    url: https://developer.arubanetworks.com
  - type: Hub
    url: https://devhub.arubanetworks.com
  - type: GitHubOrganization
    url: https://github.com/aruba
  - type: Blog
    url: https://blogs.arubanetworks.com/
  - type: Support
    url: https://www.arubanetworks.com/support-services/
  - type: TermsOfService
    url: https://www.arubanetworks.com/company/legal/
  - type: PrivacyPolicy
    url: https://www.arubanetworks.com/company/legal/privacy-policy/
  - type: Features
    data:
      - name: Unified Cloud Management
        description: Single pane of glass for managing wired, wireless, and SD-WAN infrastructure across distributed enterprise environments.
      - name: AI-Powered Analytics
        description: Artificial intelligence and machine learning-driven network analytics for proactive troubleshooting and optimization.
      - name: Zero Trust Security
        description: Role-based and device-based access control with ClearPass for IoT, BYOD, and enterprise devices.
      - name: Network Automation
        description: Programmable APIs across all platforms enabling infrastructure-as-code and automated provisioning.
      - name: SD-WAN Orchestration
        description: Centralized management of EdgeConnect SD-WAN appliances with application-aware routing and WAN optimization.
      - name: User Experience Monitoring
        description: Synthetic testing and real-time monitoring of network and application performance from the user perspective.
  - type: UseCases
    data:
      - name: Campus Network Automation
        description: Automate provisioning, monitoring, and troubleshooting of campus wired and wireless networks using Central APIs.
      - name: Branch Office SD-WAN Deployment
        description: Programmatically deploy and manage EdgeConnect SD-WAN appliances across branch offices with centralized orchestration.
      - name: IoT Device Onboarding
        description: Automate secure onboarding and policy assignment for IoT devices using ClearPass APIs.
      - name: Network Health Dashboards
        description: Build custom monitoring dashboards using Central APIs to track device health, client connectivity, and network performance.
      - name: Multi-Site Configuration Management
        description: Manage groups, sites, and device configurations across multiple locations programmatically.
  - type: Integrations
    data:
      - name: Ansible
        description: Ansible modules and playbooks for automating Aruba Central and AOS-CX switch configuration.
      - name: Terraform
        description: Infrastructure-as-code provisioning for Aruba network infrastructure using Terraform providers.
      - name: ServiceNow
        description: Integration with ServiceNow for IT service management and automated incident response.
      - name: Splunk
        description: Log and event forwarding from Aruba infrastructure to Splunk for security analytics and monitoring.
      - name: VMware vSphere
        description: Integration with VMware environments for network-aware virtual infrastructure management.
---
