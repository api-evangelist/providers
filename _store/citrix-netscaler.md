---
name: Citrix NetScaler
segments:
  - Gateways
description: Citrix NetScaler is an application delivery controller (ADC) that provides load balancing, traffic management, application security, and application acceleration capabilities for web applications and services.
image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
url: https://www.citrix.com/products/citrix-adc/
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.16'
tags:
  - API Gateway
  - Application Delivery Controller
  - Application Security
  - Load Balancing
  - SSL Offloading
  - Traffic Management
  - Web Application Firewall
apis:
  - name: Citrix ADC (NetScaler) NITRO API
    description: The NITRO API provides programmatic access to configure and monitor NetScaler appliances. It supports REST-based operations for comprehensive management of ADC features including load balancing, content switching, SSL, and more.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
    humanURL: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release.html
    baseURL: https://<netscaler-ip>/nitro/v1
    tags:
      - Automation
      - Configuration
      - Monitoring
      - REST API
    properties:
      - type: Documentation
        url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release.html
      - type: OpenAPI
        url: openapi/citrix-netscaler-nitro-openapi.yml
      - type: JSONSchema
        url: json-schema/citrix-netscaler-vserver-schema.json
      - type: JSONLD
        url: json-ld/citrix-netscaler-context.jsonld
      - type: OpenAPI
        url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/api-reference.html
      - type: Authentication
        url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/performing-basic-netscaler-operations.html
      - type: GettingStarted
        url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/before-you-begin.html
      - type: SDK
        url: https://www.citrix.com/downloads/citrix-adc/sdks/
      - type: ChangeLog
        url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/nitro-changes-across-releases/
    contact:
      - type: Support
        url: https://support.citrix.com/
      - type: DeveloperPortal
        url: https://developer-docs.netscaler.com/
  - name: NetScaler ADM NITRO API
    description: The NetScaler Application Delivery Management (ADM) NITRO API provides programmatic access to manage, monitor, and orchestrate multiple NetScaler instances from a centralized platform, covering analytics, configuration audit, and system management.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
    humanURL: https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/
    baseURL: https://<adm-ip>/nitro/v1
    tags:
      - Analytics
      - Management
      - Orchestration
      - REST API
    properties:
      - type: Documentation
        url: https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/
      - type: Authentication
        url: https://developer-docs.netscaler.com/en-us/citrix-adm-nitro-api-reference/configuration/system/Authentication/Authentication.html
    contact:
      - type: Support
        url: https://support.citrix.com/
      - type: DeveloperPortal
        url: https://developer-docs.netscaler.com/
  - name: NetScaler SDX NITRO API
    description: The NetScaler SDX NITRO API provides programmatic access to configure and manage NetScaler SDX appliances via REST interfaces, enabling provisioning and management of multiple virtual NetScaler instances on a single hardware platform.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
    humanURL: https://developer-docs.netscaler.com/en-us/adc-sdx-nitro-api-reference/current-release.html
    baseURL: https://<sdx-ip>/nitro/v1
    tags:
      - Management
      - REST API
      - SDX
      - Virtualization
    properties:
      - type: Documentation
        url: https://developer-docs.netscaler.com/en-us/adc-sdx-nitro-api-reference/current-release.html
      - type: APIReference
        url: https://developer-docs.netscaler.com/en-us/adc-sdx-nitro-api-reference/adc-sdx-nitro-api-reference.html
    contact:
      - type: Support
        url: https://support.citrix.com/
      - type: DeveloperPortal
        url: https://developer-docs.netscaler.com/
  - name: NetScaler Next-Gen API
    description: NetScaler Next-Gen API is a modern declarative RESTful API built on the OpenAPI 3.0 specification that allows developers to programmatically configure NetScaler with an intuitive application-centric interface, abstracting away low-level configuration complexities.
    image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
    humanURL: https://developer-docs.netscaler.com/en-us/nextgen-api.html
    baseURL: https://<netscaler-ip>/
    tags:
      - Application-Centric
      - Declarative
      - OpenAPI
      - REST API
    properties:
      - type: Documentation
        url: https://developer-docs.netscaler.com/en-us/nextgen-api.html
      - type: GettingStarted
        url: https://developer-docs.netscaler.com/en-us/nextgen-api/getting-started-guide.html
      - type: APIReference
        url: https://developer-docs.netscaler.com/en-us/nextgen-api/apis/
    contact:
      - type: Support
        url: https://support.citrix.com/
      - type: DeveloperPortal
        url: https://developer-docs.netscaler.com/
common:
  - type: Portal
    url: https://www.netscaler.com/platform/apis
  - type: Documentation
    url: https://developer-docs.netscaler.com/
  - type: Documentation
    url: https://docs.netscaler.com/
  - type: CLI
    url: https://developer-docs.netscaler.com/en-us/adc-command-reference-int/current-release.html
  - type: Blog
    url: https://www.netscaler.com/blog/
  - type: GitHubRepository
    url: https://github.com/netscaler
  - type: GitHubOrganization
    url: https://github.com/citrix
  - type: Support
    url: https://www.netscaler.com/resources/support
  - type: StatusPage
    url: https://status.cloud.com/
  - type: SignUp
    url: https://onboarding.cloud.com/
  - type: Login
    url: https://citrix.cloud.com/
  - type: PrivacyPolicy
    url: https://www.cloud.com/legal
  - type: TermsOfService
    url: https://www.cloud.com/legal
  - type: X
    url: https://x.com/NetScaler
  - type: LinkedIn
    url: https://www.linkedin.com/company/netscaler
  - type: ReleaseNotes
    url: https://docs.netscaler.com/en-us/citrix-adc/current-release/citrix-adc-release-notes.html
  - type: Features
    data:
      - Load balancing across multiple servers and protocols
      - Content switching for routing traffic based on request attributes
      - SSL offloading and acceleration
      - Web Application Firewall for application security
      - Global Server Load Balancing (GSLB)
      - Application acceleration and optimization
      - API gateway capabilities
      - Health monitoring and auto-scaling
  - type: UseCases
    data:
      - Distributing web traffic across backend servers for high availability
      - Securing applications with WAF and DDoS protection
      - Offloading SSL processing from application servers
      - Routing API traffic through an application delivery controller
      - Managing multi-cloud and hybrid application delivery
  - type: Integrations
    data:
      - Terraform
      - Ansible
      - Kubernetes (Ingress Controller)
      - Citrix Cloud
      - ServiceNow
      - Splunk
properties:
  - type: Capabilities
    url: capabilities/adc-management.yaml
    title: ADC Management Capability
  - type: Capabilities
    url: capabilities/shared/nitro.yaml
    title: NITRO API Shared Definition
include:
  - name: Citrix Developer Portal
    url: https://developer.citrix.com/
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com/
---
