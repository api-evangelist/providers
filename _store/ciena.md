---
aid: ciena
name: Ciena
description: Ciena Corporation is a global networking equipment, software, and services vendor focused on optical and packet networking, SDN, and service automation. This index covers Ciena's open APIs across the Blue Planet automation platform, the Ciena MCP (Manage, Control, and Plan) NMS, and the Emulation Cloud developer environment, exposing TM Forum Open APIs, MEF Lifecycle Service Orchestration (LSO) APIs (Legato, Sonata), and ONAP-aligned policy controls for telecom carriers and managed service providers.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - MEF
  - NETCONF
  - Network Automation
  - Network Management
  - Optical
  - RESTCONF
  - SDN
  - Telecom
  - TM Forum
created: '2025-02-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: ciena:blue-planet-api
    name: Ciena Blue Planet Open API
    description: Ciena Blue Planet provides open APIs for multi-layer SDN network management and automation. The platform supports TM Forum Open APIs, MEF Lifecycle Service Orchestration (LSO) APIs including Legato and Sonata, and integrates with ONAP policy frameworks. APIs enable network topology management, circuit provisioning, performance monitoring, and network operations automation for telecom carriers.
    image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
    humanURL: https://www.blueplanet.com/technology/open-apis.html
    baseURL: https://api.blueplanet.com/bpocore/market/api/v1
    tags:
      - MEF
      - Network Automation
      - Optical
      - SDN
      - Telecom
      - TM Forum
    properties:
      - type: Documentation
        url: https://www.blueplanet.com/technology/open-apis.html
      - type: Portal
        url: https://developer.blueplanet.com
      - type: Blog
        url: https://www.blueplanet.com/blog
      - type: Support
        url: https://www.blueplanet.com/support
      - type: Contact
        url: https://www.blueplanet.com/contact
      - type: OpenAPI
        url: openapi/ciena-blue-planet-openapi.yml
  - aid: ciena:mcp-api
    name: Ciena MCP (Manage, Control and Plan) API
    description: Ciena's Manage, Control and Plan (MCP) is a multi-layer Software Defined Networking (SDN) and Network Management System (NMS) platform. The MCP REST and RESTCONF APIs enable network-aware management operations for optical and packet networks including topology discovery, circuit provisioning, configuration management, and performance data retrieval.
    image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
    humanURL: https://software.ciena.com/releasenotes/MCP-DOCS_5.2-217/build/site/mcp-docs/user-guide/Overview.html
    baseURL: https://api.ciena.com/mcp
    tags:
      - NETCONF
      - Network Management
      - RESTCONF
      - SDN
      - Telecom
    properties:
      - type: Documentation
        url: https://software.ciena.com/releasenotes/MCP-DOCS_5.2-217/build/site/mcp-docs/user-guide/Overview.html
  - aid: ciena:emulation-cloud-api
    name: Ciena Emulation Cloud API
    description: Ciena Emulation Cloud is an open application development environment enabling developers to create, test, and fine-tune custom applications against full API definitions without requiring physical infrastructure. Provides access to complete API documentation, tutorials, and sample code for Ciena network platforms.
    image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
    humanURL: https://www.ciena.com/products/emulation-cloud
    baseURL: https://developer.ciena.com
    tags:
      - Developer Tools
      - SDN
      - Telecom
      - Testing
    properties:
      - type: Documentation
        url: https://www.ciena.com/products/emulation-cloud
      - type: Portal
        url: https://developer.ciena.com/
common:
  - type: Website
    url: https://www.ciena.com/
  - type: DeveloperPortal
    url: https://developer.ciena.com/
  - type: Portal
    url: https://developer.blueplanet.com
  - type: Documentation
    url: https://www.blueplanet.com/technology/open-apis.html
  - type: Blog
    url: https://www.blueplanet.com/blog
  - type: Support
    url: https://www.blueplanet.com/support
  - type: PrivacyPolicy
    url: https://www.ciena.com/about/corporate-governance/privacy-policy
  - type: TermsOfService
    url: https://www.ciena.com/customers/terms-and-conditions
  - type: Community
    url: https://my.ciena.com/CienaPortal/s/blue-planet
  - type: GitHubOrg
    url: https://git.blueplanet.com
  - type: OpenAPI
    url: openapi/ciena-blue-planet-openapi.yml
  - type: JSONLDContext
    url: json-ld/ciena-context.jsonld
  - type: JSONSchema
    url: json-schema/ciena-network-service-schema.json
  - type: Spectral
    url: spectral/ciena-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/ciena-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
