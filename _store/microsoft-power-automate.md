---
aid: microsoft-power-automate
url: https://raw.githubusercontent.com/api-evangelist/microsoft-power-automate/refs/heads/main/apis.yml
apis:
- name: Power Automate Management API
  description: REST API for managing flows, connections, and environments in Power Automate.
  image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
  humanURL: https://powerautomate.microsoft.com
  baseURL: https://api.flow.microsoft.com
  tags:
  - Automation
  - Flows
  - Management
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-automate/web-api
  - type: OpenAPI
    url: https://learn.microsoft.com/en-us/rest/api/power-automate/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/power-automate/web-api#authentication
  - type: Pricing
    url: https://powerautomate.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://powerautomate.microsoft.com/en-us/terms-of-use/
- name: Power Automate Connectors API
  description: API for creating and managing custom connectors in Power Automate.
  image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
  humanURL: https://learn.microsoft.com/en-us/connectors/
  baseURL: https://api.flow.microsoft.com/providers/Microsoft.PowerApps/apis
  tags:
  - Connectors
  - Custom Connectors
  - Integration
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/
  - type: OpenAPI
    url: https://learn.microsoft.com/en-us/connectors/custom-connectors/define-openapi-definition
  - type: Connector Reference
    url: https://learn.microsoft.com/en-us/connectors/connector-reference/
- name: Power Automate Desktop API
  description: API for interacting with Power Automate Desktop for robotic process automation.
  image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
  humanURL: https://powerautomate.microsoft.com/en-us/desktop/
  baseURL: https://api.flow.microsoft.com
  tags:
  - Desktop Automation
  - Robotic Process Automation
  - RPA
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/power-automate/desktop-flows/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/power-automate/desktop-flows/introduction
name: Microsoft Power Automate
tags:
- Automation
- Business Process
- Integration
- Low-Code
- Microsoft
- RPA
- Workflow
type: Contract
image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Power Automate is a service that helps you create automated workflows between your favorite apps and services to synchronize files, get notifications, collect data, and more.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

