---
aid: citrix-netscaler
url: https://raw.githubusercontent.com/api-evangelist/citrix-netscaler/refs/heads/main/apis.yml
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
  - type: SDKs
    url: https://www.citrix.com/downloads/citrix-adc/sdks/
  - type: Terraform Provider
    url: https://registry.terraform.io/providers/citrix/citrixadc/latest/docs
  - type: Change Log
    url: https://developer-docs.netscaler.com/en-us/adc-nitro-api/current-release/nitro-changes-across-releases/
  contact:
  - type: Support
    url: https://support.citrix.com/
  - type: Developer Portal
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
  - type: Developer Portal
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
  - type: API Reference
    url: https://developer-docs.netscaler.com/en-us/adc-sdx-nitro-api-reference/adc-sdx-nitro-api-reference.html
  contact:
  - type: Support
    url: https://support.citrix.com/
  - type: Developer Portal
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
  - type: API Reference
    url: https://developer-docs.netscaler.com/en-us/nextgen-api/apis/
  - type: Product Page
    url: https://www.netscaler.com/platform/next-gen-api
  contact:
  - type: Support
    url: https://support.citrix.com/
  - type: Developer Portal
    url: https://developer-docs.netscaler.com/
name: Citrix NetScaler
tags:
- API Gateway
- Application Delivery Controller
- Application Security
- Load Balancing
- SSL Offloading
- Traffic Management
- Web Application Firewall
type: Contract
image: https://www.citrix.com/content/dam/citrix/en_us/images/logos/citrix-logo.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Citrix NetScaler is an application delivery controller (ADC) that provides load balancing, traffic management, application security, and application acceleration capabilities for web applications and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

