---
aid: varonis
url: https://raw.githubusercontent.com/api-evangelist/varonis/refs/heads/main/apis.yml
apis:
- name: Varonis Data Security Platform API
  description: API for integrating with Varonis Data Security Platform to manage data security policies, access permissions, and threat detection.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://www.varonis.com/products/data-security-platform
  baseURL: https://api.varonis.com
  tags:
  - Access Control
  - Data Security
  - Permissions
  properties:
  - type: Documentation
    url: https://docs.varonis.com/api
  - type: OpenAPI
    url: https://api.varonis.com/openapi.json
  - type: Authentication
    url: https://docs.varonis.com/api/authentication
- name: Varonis DatAlert API
  description: API for accessing threat detection and incident response capabilities from Varonis DatAlert. Provides endpoints for retrieving alerts, managing alert status, adding notes to alerts, and accessing alerted events for investigation and threat hunting.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://www.varonis.com/products/datalert
  baseURL: https://api.varonis.com/datalert
  tags:
  - Incident Response
  - Security Alerts
  - Threat Detection
  properties:
  - type: Documentation
    url: https://docs.varonis.com/api/datalert
  - type: Alerts
    url: https://docs.varonis.com/api/datalert/alerts
- name: Varonis Data Classification API
  description: API for automated data classification and sensitive data discovery across cloud and on-premises data stores.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://www.varonis.com/products/data-classification
  baseURL: https://api.varonis.com/classification
  tags:
  - Data Classification
  - Data Discovery
  - Sensitive Data
  properties:
  - type: Documentation
    url: https://docs.varonis.com/api/classification
  - type: SDK
    url: https://github.com/varonis/classification-sdk
- name: Varonis DataPrivilege API
  description: REST and SOAP API for integrating Varonis DataPrivilege with IAM and ITSM solutions. Enables synchronization of managed data, execution and reporting on access requests and access control changes, and automation of entitlement reviews and self-service access workflows.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://www.varonis.com/products/dataprivilege
  baseURL: https://api.varonis.com
  tags:
  - Access Governance
  - Entitlement Reviews
  - Identity Management
  - Self-Service Access
  properties:
  - type: Documentation
    url: https://www.varonis.com/blog/introducing-gdpr-patterns-and-dataprivilege-api
- name: Varonis Reports API
  description: API for accessing and exporting Varonis report data. Allows integration with business intelligence systems to send data-centric insights and reports for further analysis to streamline business and security operations.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://help.varonis.com/s/
  baseURL: https://api.varonis.com
  tags:
  - Analytics
  - Business Intelligence
  - Reports
  properties:
  - type: Documentation
    url: https://help.varonis.com/s/
- name: Varonis Commit API
  description: API for executing permission and group membership changes through the Varonis Commit Engine. Exposes the capability to change permissions and group membership programmatically as part of automated remediation workflows.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://help.varonis.com/s/
  baseURL: https://api.varonis.com
  tags:
  - Access Control
  - Permissions
  - Remediation
  properties:
  - type: Documentation
    url: https://help.varonis.com/s/
- name: Varonis MCP Server
  description: Model Context Protocol server that interfaces with Varonis APIs, allowing AI clients such as ChatGPT, Claude, and GitHub Copilot to access and orchestrate the Varonis Data Security Platform using natural language. Enables complex workflows including alert retrieval, access remediation, and compliance reporting.
  image: https://www.varonis.com/favicon.ico
  humanURL: https://www.varonis.com/blog/mcp-server
  baseURL: https://api.varonis.com
  tags:
  - AI Integration
  - Automation
  - MCP
  - Natural Language
  properties:
  - type: Documentation
    url: https://www.varonis.com/blog/mcp-server
  - type: SDKs
    url: https://www.npmjs.com/package/@varonis/mcp
name: Varonis
tags:
- Cloud Security
- Compliance
- Data Analytics
- Data Governance
- Data Security
- Threat Detection
type: Contract
image: https://www.varonis.com/favicon.ico
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Varonis is a pioneer in data security and analytics, specializing in software for data security, governance, threat detection and response. The company provides solutions for protecting enterprise data across cloud and on-premises environments.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

