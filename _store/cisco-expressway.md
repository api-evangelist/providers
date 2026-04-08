---
aid: cisco-expressway
url: https://raw.githubusercontent.com/api-evangelist/cisco-expressway/refs/heads/main/apis.yml
apis:
- name: Cisco Expressway Configuration API
  description: RESTful API for configuring and managing Cisco Expressway systems including zones, search rules, transforms, DNS, NTP, and system settings. Uses JSON Schema version 4 for request and response schemas.
  image: https://www.cisco.com/c/dam/en/us/products/collateral/unified-communications/expressway-series/datasheet-c78-733751.jpg
  humanURL: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
  baseURL: https://expressway.example.com/api/provisioning
  tags:
  - Configuration
  - Management
  - Provisioning
  - REST
  - Unified Communications
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
  - type: Reference
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-programming-reference-guides-list.html
  - type: Authentication
    url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
  - type: Getting Started
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html
  - type: Change Log
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-release-notes-list.html
  - type: OpenAPI
    url: openapi/cisco-expressway-configuration-api-openapi.yml
  - type: JSONSchema
    url: json-schema/cisco-expressway-zone-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-search-rule-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-transform-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-system-status-schema.json
  - type: JSONLD
    url: json-ld/cisco-expressway-context.jsonld
  contact:
  - FN: Cisco TAC
    email: tac@cisco.com
    X-twitter: CiscoUC
- name: Cisco Expressway Status API
  description: RESTful API for retrieving status information, alarms, call history, licensing status, upgrade status, and system health metrics from Cisco Expressway. Endpoints follow the pattern /api/status/common/ for items common between Expressway-E and Expressway-C.
  image: https://www.cisco.com/c/dam/en/us/products/collateral/unified-communications/expressway-series/datasheet-c78-733751.jpg
  humanURL: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
  baseURL: https://expressway.example.com/api/status
  tags:
  - Alarms
  - Health Check
  - Licensing
  - Monitoring
  - Status
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-2/rest-api/exwy_b_cisco-expressway-rest-api-summary-guide--x142/exwy_m_using-the-expressway-rest-api.html
  - type: Reference
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-programming-reference-guides-list.html
  - type: Getting Started
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-installation-and-configuration-guides-list.html
  - type: Change Log
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-release-notes-list.html
  - type: OpenAPI
    url: openapi/cisco-expressway-status-api-openapi.yml
  - type: JSONSchema
    url: json-schema/cisco-expressway-alarm-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-call-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-registration-schema.json
  - type: JSONSchema
    url: json-schema/cisco-expressway-system-status-schema.json
  - type: JSONLD
    url: json-ld/cisco-expressway-context.jsonld
  contact:
  - FN: Cisco TAC
    email: tac@cisco.com
- name: Cisco Expressway SNMP API
  description: SNMP-based monitoring and management interface for Cisco Expressway providing access to system metrics, alarms, and configuration data. Supports SNMP versions v2c and v3 for secure network management integration.
  humanURL: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-technical-reference-list.html
  baseURL: snmp://expressway.example.com:161
  tags:
  - Metrics
  - Monitoring
  - Network Management
  - SNMP
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-technical-reference-list.html
  - type: Reference
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-technical-reference-list.html
  - type: Change Log
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-release-notes-list.html
- name: Cisco Expressway XML API
  description: Legacy XML-based API for configuration and status retrieval on Cisco Expressway systems. Uses HTTP Basic Authentication over HTTPS for secure access to system configuration and management functions.
  humanURL: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-programming-reference-guides-list.html
  baseURL: https://expressway.example.com/xmlapi
  tags:
  - Configuration
  - Legacy
  - Management
  - XML
  properties:
  - type: Documentation
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-programming-reference-guides-list.html
  - type: Authentication
    url: https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/expressway/admin_guide/X14-0/exwy_b_cisco-expressway-administrator-guide/exwy_m_managing-security.html
  - type: Change Log
    url: https://www.cisco.com/c/en/us/support/unified-communications/expressway-series/products-release-notes-list.html
name: Cisco Expressway
tags:
- Collaboration
- Firewall Traversal
- H.323
- Session Border Controller
- SIP
- Unified Communications
- Video Conferencing
type: Contract
image: https://www.cisco.com/c/en/us/products/unified-communications/expressway-series/index.html
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API definitions for Cisco Expressway, a session border controller and firewall traversal solution for Unified Communications that provides secure remote and mobile access for collaboration workloads including video, voice, content, and presence.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

