---
aid: cisco
name: Cisco
description: Cisco provides a comprehensive suite of APIs across its networking, security, collaboration, and cloud infrastructure platforms. Through Cisco DevNet, developers can access REST APIs, SDKs, and developer tools for Meraki, Webex, Catalyst Center, ACI, ISE, Intersight, ThousandEyes, SD-WAN, and other Cisco products to automate network operations, build integrations, and extend platform capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cisco/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Collaboration
  - Enterprise
  - Networking
  - Security
  - SD-WAN
apis:
  - aid: cisco:meraki-api
    name: Cisco Meraki Dashboard API
    description: RESTful API for managing Cisco Meraki cloud-managed networking devices including wireless access points, switches, security appliances, and cameras. Supports network configuration, monitoring, and automation at scale.
    humanURL: https://developer.cisco.com/meraki/api-v1/
    baseURL: https://api.meraki.com/api/v1
    tags:
      - Cloud Managed
      - Meraki
      - Network Management
      - REST
    properties:
      - type: Documentation
        url: https://developer.cisco.com/meraki/api-v1/
      - type: APIReference
        url: https://developer.cisco.com/meraki/api-v1/
      - type: GettingStarted
        url: https://developer.cisco.com/meraki/api-v1/getting-started/
      - type: Authentication
        url: https://developer.cisco.com/meraki/api-v1/#!authorization
  - aid: cisco:webex-api
    name: Cisco Webex API
    description: REST API for Webex collaboration platform enabling messaging, meeting management, device control, and administration. Supports bots, integrations, and embedded apps for extending Webex functionality.
    humanURL: https://developer.webex.com/docs/getting-started
    baseURL: https://webexapis.com/v1
    tags:
      - Collaboration
      - Meetings
      - Messaging
      - REST
      - Webex
    properties:
      - type: Documentation
        url: https://developer.webex.com/docs/getting-started
      - type: APIReference
        url: https://developer.webex.com/docs/api/getting-started
      - type: Authentication
        url: https://developer.webex.com/docs/integrations
  - aid: cisco:catalyst-center-api
    name: Cisco Catalyst Center API
    description: REST API for Cisco Catalyst Center (formerly DNA Center), providing intent-based networking capabilities including network design, provisioning, assurance, and policy management for enterprise campus and branch networks.
    humanURL: https://developer.cisco.com/docs/dna-center/
    baseURL: https://sandboxdnac.cisco.com/dna
    tags:
      - Catalyst Center
      - Intent-Based Networking
      - Network Automation
      - REST
    properties:
      - type: Documentation
        url: https://developer.cisco.com/docs/dna-center/
      - type: APIReference
        url: https://developer.cisco.com/docs/dna-center/api/
  - aid: cisco:aci-api
    name: Cisco ACI API
    description: REST API for Cisco Application Centric Infrastructure (ACI) providing programmable access to data center network fabric configuration, policy management, and monitoring through the APIC controller.
    humanURL: https://developer.cisco.com/docs/aci/
    baseURL: https://apic-ip/api
    tags:
      - ACI
      - Data Center
      - Fabric
      - REST
      - SDN
    properties:
      - type: Documentation
        url: https://developer.cisco.com/docs/aci/
      - type: APIReference
        url: https://developer.cisco.com/docs/aci/apic-rest-api-user-guide/
  - aid: cisco:ise-api
    name: Cisco ISE API
    description: REST API for Cisco Identity Services Engine (ISE) enabling network access policy management, guest services, BYOD onboarding, and security group administration for zero-trust network access.
    humanURL: https://developer.cisco.com/docs/identity-services-engine/
    baseURL: https://ise-server/ers
    tags:
      - Identity
      - ISE
      - Network Access
      - REST
      - Security
    properties:
      - type: Documentation
        url: https://developer.cisco.com/docs/identity-services-engine/
      - type: APIReference
        url: https://developer.cisco.com/docs/identity-services-engine/ers-api-reference/
  - aid: cisco:intersight-api
    name: Cisco Intersight API
    description: REST API for Cisco Intersight cloud operations platform providing infrastructure management, workload optimization, and lifecycle automation for Cisco UCS, HyperFlex, and third-party infrastructure.
    humanURL: https://intersight.com/apidocs/introduction/overview/
    baseURL: https://intersight.com/api/v1
    tags:
      - Cloud Operations
      - Infrastructure
      - Intersight
      - REST
    properties:
      - type: Documentation
        url: https://intersight.com/apidocs/introduction/overview/
      - type: APIReference
        url: https://intersight.com/apidocs/apirefs/
  - aid: cisco:sdwan-api
    name: Cisco SD-WAN API
    description: REST API for Cisco SD-WAN (formerly Viptela) providing programmatic access to WAN edge device management, policy configuration, monitoring, and analytics through the vManage controller.
    humanURL: https://developer.cisco.com/docs/sdwan/
    baseURL: https://vmanage-ip/dataservice
    tags:
      - REST
      - SD-WAN
      - WAN
    properties:
      - type: Documentation
        url: https://developer.cisco.com/docs/sdwan/
      - type: APIReference
        url: https://developer.cisco.com/docs/sdwan/api-reference/
  - aid: cisco:thousandeyes-api
    name: Cisco ThousandEyes API
    description: REST API for Cisco ThousandEyes digital experience monitoring platform, providing access to network, application, and internet visibility data for monitoring end-to-end digital experiences.
    humanURL: https://developer.cisco.com/docs/thousandeyes/
    baseURL: https://api.thousandeyes.com/v7
    tags:
      - Digital Experience
      - Monitoring
      - Network Visibility
      - REST
      - ThousandEyes
    properties:
      - type: Documentation
        url: https://developer.cisco.com/docs/thousandeyes/
      - type: APIReference
        url: https://developer.cisco.com/docs/thousandeyes/api-reference/
common:
  - type: Portal
    url: https://developer.cisco.com/
  - type: Documentation
    url: https://developer.cisco.com/docs/
  - type: GettingStarted
    url: https://developer.cisco.com/learning/
  - type: Blog
    url: https://blogs.cisco.com/developer
  - type: GitHubOrganization
    url: https://github.com/CiscoDevNet
  - type: Support
    url: https://developer.cisco.com/site/support/
  - type: TermsOfService
    url: https://www.cisco.com/c/en/us/about/legal/cloud-and-software.html
  - type: PrivacyPolicy
    url: https://www.cisco.com/c/en/us/about/legal/privacy-full.html
  - type: Sandbox
    url: https://developer.cisco.com/site/sandbox/
  - type: Training
    url: https://developer.cisco.com/certification/
  - type: YouTube
    url: https://www.youtube.com/ciscodevnet
  - type: X
    url: https://twitter.com/CiscoDevNet
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/cisco
  - type: Features
    data:
      - 'Cisco (Networking + Security + Collaboration): hundreds of services across Networking + Security'
      - 'Detailed pricing: see https://www.cisco.com/c/en/us/products/index.html'
      - 'Service: Meraki Dashboard API'
      - 'Service: Catalyst Center API'
      - 'Service: DNA Center API'
      - 'Service: Webex API'
      - 'Service: Webex Calling'
      - 'Service: Cisco Secure Endpoint API'
      - 'Service: Umbrella API'
      - 'Service: AppDynamics API'
      - 'Service: ThousandEyes API'
      - 'Service: Cisco Intersight API'
    sources:
      - https://www.cisco.com/c/en/us/products/index.html
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Network Configuration Management
        description: Automate network device configuration changes across thousands of devices using APIs and templates.
      - name: Security Policy Automation
        description: Programmatically manage access control policies, security groups, and compliance enforcement.
      - name: Collaboration Integration
        description: Build bots, integrations, and custom applications on the Webex platform for team collaboration.
      - name: Cloud Infrastructure Management
        description: Manage hybrid cloud infrastructure with Intersight APIs for lifecycle management and workload optimization.
      - name: Network Monitoring and Analytics
        description: Collect and analyze network telemetry data for performance monitoring and troubleshooting.
  - type: Integrations
    data:
      - name: Ansible
        description: Network automation modules for Cisco platforms including IOS, NX-OS, ACI, and Meraki.
      - name: Terraform
        description: Terraform providers for Cisco ACI, Intersight, Meraki, and other platforms for infrastructure as code.
      - name: ServiceNow
        description: ITSM integration for automated incident management and change control with Cisco platforms.
      - name: Splunk
        description: Security and network analytics integration for log aggregation and threat detection.
      - name: Python
        description: Python SDKs and libraries for all major Cisco platforms including Meraki, Webex, and ACI.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
