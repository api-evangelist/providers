---
aid: commvault
url: https://raw.githubusercontent.com/api-evangelist/commvault/refs/heads/main/apis.yml
apis:
- name: Commvault REST API
  description: The Commvault REST API provides programmatic access to Commvault operations including backup, restore, storage management, and reporting capabilities.
  image: https://www.commvault.com/wp-content/themes/commvault/assets/images/commvault-logo.svg
  humanURL: https://documentation.commvault.com/v11/essential/rest_api_overview.html
  baseURL: https://webserver.commvault.com/webconsole/api
  tags:
  - Backup
  - Data Management
  - REST API
  - Restore
  properties:
  - type: Documentation
    url: https://documentation.commvault.com/v11/essential/rest_api_overview.html
  - type: OpenAPI
    url: https://api.commvault.com/swagger/
  - type: Authentication
    url: https://documentation.commvault.com/v11/essential/rest_api_authentication.html
  - type: Postman Collection
    url: https://documenter.getpostman.com/view/2046098/RW1aHzQg
  - type: OpenAPI
    url: openapi/commvault-rest-openapi.yml
- name: Commvault Command Center API
  description: APIs for managing Commvault Command Center operations, providing centralized management and monitoring capabilities.
  humanURL: https://documentation.commvault.com/2024/essential/command_center_overview.html
  baseURL: https://commandcenter.commvault.com/commandcenter/api
  tags:
  - Command Center
  - Management
  - Monitoring
  properties:
  - type: Documentation
    url: https://documentation.commvault.com/2024/essential/rest_api_command_center.html
  - type: API Reference
    url: https://api.commvault.com/
  - type: OpenAPI
    url: openapi/commvault-command-center-openapi.yml
- name: Commvault Automation API
  description: API for automating Commvault workflows, job scheduling, and policy management.
  humanURL: https://documentation.commvault.com/v11/essential/automation_overview.html
  baseURL: https://webserver.commvault.com/webconsole/api
  tags:
  - Automation
  - Scheduling
  - Workflows
  properties:
  - type: Documentation
    url: https://documentation.commvault.com/v11/essential/rest_api_automation.html
  - type: OpenAPI
    url: openapi/commvault-automation-openapi.yml
name: Commvault
tags:
- Backup
- Cloud Storage
- Data Management
- Data Protection
- Disaster Recovery
- Enterprise Software
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Commvault is a data protection and information management platform that provides backup, recovery, and data management solutions for enterprises.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

