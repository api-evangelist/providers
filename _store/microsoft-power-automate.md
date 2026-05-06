---
aid: microsoft-power-automate
name: Microsoft Power Automate
description: Microsoft Power Automate is a cloud-based service that helps you create automated workflows between your favorite apps and services to synchronize files, get notifications, collect data, and automate business processes. It supports automated, instant, and scheduled cloud flows, as well as desktop flows for robotic process automation.
image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
url: https://powerautomate.microsoft.com
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Automation
  - Business Process
  - Integration
  - Low-Code
  - Microsoft
  - Power Platform
  - RPA
  - Workflow
apis:
  - name: Power Automate Management API
    description: REST API for managing flows, environments, connections, connectors, and flow permissions in Power Automate. Enables programmatic creation, update, deletion, and lifecycle management of cloud flows.
    image: https://powerautomate.microsoft.com/images/application-logos/svg/powerautomate.svg
    humanURL: https://learn.microsoft.com/en-us/power-automate/web-api
    baseURL: https://api.flow.microsoft.com
    tags:
      - Automation
      - Connectors
      - Environments
      - Flow Management
      - Flows
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-automate/web-api
      - type: OpenAPI
        url: openapi/microsoft-power-automate-management-api.yaml
      - type: JSONSchema
        url: json-schema/power-automate-management-api-flow-schema.json
      - type: JSONSchema
        url: json-schema/power-automate-management-api-environment-schema.json
      - type: JSONSchema
        url: json-schema/power-automate-management-api-flow-run-schema.json
      - type: JSONSchema
        url: json-schema/power-automate-management-api-connector-schema.json
      - type: JSONStructure
        url: json-structure/power-automate-management-api-flow-structure.json
      - type: JSONStructure
        url: json-structure/power-automate-management-api-environment-structure.json
      - type: JSONStructure
        url: json-structure/power-automate-management-api-flow-run-structure.json
      - type: JSONStructure
        url: json-structure/power-automate-management-api-connector-structure.json
      - type: Example
        url: examples/power-automate-management-api-flow-example.json
      - type: Example
        url: examples/power-automate-management-api-environment-example.json
      - type: Example
        url: examples/power-automate-management-api-flow-run-example.json
      - type: Example
        url: examples/power-automate-management-api-connector-example.json
      - type: Authentication
        url: https://learn.microsoft.com/en-us/power-automate/web-api#authentication
      - type: APIReference
        url: https://learn.microsoft.com/en-us/connectors/flowmanagement/
common:
  - type: Portal
    url: https://make.powerautomate.com
  - type: DeveloperPortal
    url: https://learn.microsoft.com/en-us/power-automate/
  - type: Blog
    url: https://powerautomate.microsoft.com/en-us/blog/
  - type: Support
    url: https://powerautomate.microsoft.com/en-us/support/
  - type: StatusPage
    url: https://status.powerplatform.microsoft.com/
  - type: Training
    url: https://learn.microsoft.com/en-us/training/powerplatform/power-automate
  - type: Pricing
    url: https://powerautomate.microsoft.com/en-us/pricing/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: TermsOfService
    url: https://www.microsoft.com/en-us/servicesagreement
  - type: GitHubRepository
    url: https://github.com/microsoft/PowerApps-Samples
  - type: JSON-LD
    url: json-ld/microsoft-power-automate-management-api-context.jsonld
  - type: SpectralRules
    url: rules/microsoft-power-automate-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/flow-automation.yaml
  - type: Vocabulary
    url: vocabulary/microsoft-power-automate-vocabulary.yaml
  - type: Features
    data:
      - name: Automated Cloud Flows
        description: Create event-triggered automations that run when specific events occur.
      - name: Instant Cloud Flows
        description: Start automations on demand with the push of a button.
      - name: Scheduled Cloud Flows
        description: Run automations on a recurring schedule.
      - name: Desktop Flows (RPA)
        description: Automate desktop and legacy application tasks using robotic process automation.
      - name: Copilot Integration
        description: Create flows using natural language descriptions powered by AI.
      - name: 1000+ Connectors
        description: Connect to over 1000 pre-built connectors for Microsoft and third-party services.
      - name: Custom Connectors
        description: Build custom connectors using OpenAPI definitions.
      - name: Flow Templates
        description: Start from pre-built templates for common automation scenarios.
      - name: Approval Workflows
        description: Build approval workflows with built-in support for multi-stage approvals.
      - name: Error Handling
        description: Configure error handling, retry policies, and notifications for flow failures.
  - type: UseCases
    data:
      - name: Email Automation
        description: Automatically process, route, and respond to emails based on content or sender.
      - name: Data Synchronization
        description: Keep data synchronized across multiple systems and applications.
      - name: Approval Processes
        description: Automate business approval workflows across teams and departments.
      - name: Document Processing
        description: Automate document creation, routing, and archival workflows.
      - name: IT Process Automation
        description: Automate IT helpdesk tickets, provisioning, and monitoring workflows.
      - name: Social Media Monitoring
        description: Track brand mentions and automatically respond or alert teams.
  - type: Integrations
    data:
      - name: Microsoft 365
        description: Deep integration with SharePoint, Outlook, Teams, and other Microsoft 365 apps.
      - name: Microsoft Dataverse
        description: Native integration with Dataverse for data storage and management.
      - name: Azure Services
        description: Connect to Azure Logic Apps, Functions, and other Azure services.
      - name: Dynamics 365
        description: Automate business processes within Dynamics 365 CRM and ERP.
      - name: SAP
        description: Connect to SAP systems for enterprise process automation.
      - name: Salesforce
        description: Integrate with Salesforce for CRM automation workflows.
  - type: Solutions
    data:
      - name: Power Automate Premium
        description: Premium plan with advanced connectors, AI Builder, and process mining.
      - name: Power Automate Process
        description: Per-process licensing for unattended RPA and hosted machines.
      - name: Power Automate Hosted
        description: Hosted machine groups for scaling desktop automation.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
