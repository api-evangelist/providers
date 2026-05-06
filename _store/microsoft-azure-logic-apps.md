---
name: Azure Logic Apps
description: Azure Logic Apps is a cloud platform for creating and running automated workflows that integrate apps, data, services, and systems. It provides a visual designer and over 400 connectors to build event-driven, scheduled, and on-demand integrations.
image: https://azure.microsoft.com/svghandler/logic-apps/
url: https://azure.microsoft.com/en-us/services/logic-apps/
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Automation
  - Azure
  - Integration
  - iPaaS
  - Workflow
apis:
  - name: Azure Logic Apps REST API
    description: Programmatic management of Azure Logic Apps automated workflows including workflow definitions, triggers, actions, runs, integration accounts, and connectors.
    image: https://azure.microsoft.com/svghandler/logic-apps/
    humanURL: https://learn.microsoft.com/en-us/rest/api/logic/
    baseURL: https://management.azure.com
    tags:
      - Automation
      - Integration
      - Workflow
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/logic-apps/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/logic/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/azure/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/logic-apps/quickstart-create-first-logic-app-workflow
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
      - type: SDK
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/mgmt-logic-readme
        title: Python SDK
      - type: SDK
        url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/resourcemanager.logic-readme
        title: .NET SDK
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/logic-apps/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/logic-apps/
  - type: StatusPage
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Features
    data:
      - name: Visual Workflow Designer
        description: Build workflows visually using a drag-and-drop designer in the Azure portal or Visual Studio Code.
      - name: 400+ Connectors
        description: Connect to hundreds of SaaS apps, databases, file systems, and Azure services with prebuilt connectors.
      - name: Event-Driven Triggers
        description: Start workflows from HTTP requests, scheduled timers, file changes, or events from connected services.
      - name: B2B Integration
        description: Process EDI, AS2, X12, and EDIFACT messages with integration accounts for partner-to-partner workflows.
      - name: Stateful and Stateless Workflows
        description: Run long-running stateful workflows or short-lived stateless workflows for low-latency scenarios.
      - name: Hybrid Connectivity
        description: Connect to on-premises data sources using on-premises data gateways and integration service environments.
  - type: UseCases
    data:
      - name: Enterprise Application Integration
        description: Connect SaaS apps, databases, and on-premises systems for end-to-end business process automation.
      - name: B2B and EDI Processing
        description: Exchange business documents with partners using industry-standard EDI protocols.
      - name: Event-Driven Automation
        description: Trigger workflows based on events from Azure services, third-party APIs, or scheduled timers.
      - name: Data Transformation
        description: Transform and route data between systems using built-in mapping and conversion capabilities.
  - type: Integrations
    data:
      - name: Azure Functions
        description: Invoke Azure Functions from workflows for custom code execution.
      - name: Azure Service Bus
        description: Send and receive messages through Azure Service Bus queues and topics.
      - name: Office 365
        description: Integrate with Outlook, SharePoint, OneDrive, and Teams using Office 365 connectors.
      - name: Salesforce
        description: Connect to Salesforce CRM for record creation, updates, and event-driven workflows.
      - name: Azure API Management
        description: Expose and manage workflow endpoints through Azure API Management.
---
