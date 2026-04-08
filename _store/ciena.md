---
aid: ciena
url: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/apis.yml
apis:
- aid: ciena:blue-planet-api
  name: Ciena Blue Planet Open API
  tags:
  - MEF
  - Network Automation
  - Optical
  - SDN
  - Telecom
  - TM Forum
  image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
  humanURL: https://www.blueplanet.com/technology/open-apis.html
  baseURL: https://api.blueplanet.com
  properties:
  - url: https://www.blueplanet.com/technology/open-apis.html
    type: Documentation
  - url: https://developer.blueplanet.com
    type: Portal
  - url: https://www.blueplanet.com/blog
    type: Blog
  - url: https://www.blueplanet.com/support
    type: Support
  - url: https://www.blueplanet.com/contact
    type: Contact
  - url: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/openapi/ciena-blue-planet-openapi.yml
    type: OpenAPI
  description: Ciena Blue Planet provides open APIs for multi-layer SDN network management and automation. The platform supports TM Forum Open APIs, MEF Lifecycle Service Orchestration (LSO) APIs including Legato and Sonata, and integrates with ONAP policy frameworks. APIs enable network topology management, circuit provisioning, performance monitoring, and network operations automation for telecom carriers.
- aid: ciena:mcp-api
  name: Ciena MCP (Manage, Control and Plan) API
  tags:
  - NETCONF
  - Network Management
  - RESTCONF
  - SDN
  - Telecom
  image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
  humanURL: https://software.ciena.com/releasenotes/MCP-DOCS_5.2-217/build/site/mcp-docs/user-guide/Overview.html
  baseURL: https://api.ciena.com
  properties:
  - url: https://software.ciena.com/releasenotes/MCP-DOCS_5.2-217/build/site/mcp-docs/user-guide/Overview.html
    type: Documentation
  description: Ciena's Manage, Control and Plan (MCP) is a multi-layer Software Defined Networking (SDN) and Network Management System (NMS) platform. The MCP REST and RESTCONF APIs enable network-aware management operations for optical and packet networks including topology discovery, circuit provisioning, and performance data retrieval.
- aid: ciena:emulation-cloud-api
  name: Ciena Emulation Cloud API
  tags:
  - Developer Tools
  - SDN
  - Telecom
  - Testing
  image: https://raw.githubusercontent.com/api-evangelist/ciena/refs/heads/main/image.png
  humanURL: https://www.ciena.com/products/emulation-cloud
  baseURL: https://developer.ciena.com
  properties:
  - url: https://www.ciena.com/products/emulation-cloud
    type: Documentation
  - url: https://developer.ciena.com/
    type: Portal
  description: Ciena Emulation Cloud is an open application development environment enabling developers to create, test, and fine-tune custom applications against full API definitions without requiring physical infrastructure. Provides access to complete API documentation, tutorials, and sample code for Ciena network platforms.
name: Ciena
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Open APIs are the enabler sitting atop Blue Planet that transforms the network into an easy-to-use, programmable resource.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

