---
aid: sap-integration-suite
url: https://raw.githubusercontent.com/api-evangelist/sap-integration-suite/refs/heads/main/apis.yml
apis:
- aid: sap-integration-suite:sap-integration-suite
  name: SAP Integration Suite API
  description: The SAP Integration Suite API provides programmatic access to manage integration flows, APIs, artifacts, and runtime operations on the SAP Integration Suite platform hosted on SAP Business Technology Platform.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-documentation
  tags:
  - Cloud Integration
  - Integration
  - SAP BTP
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-documentation
  - type: Reference
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
- aid: sap-integration-suite:sap-cloud-integration
  name: SAP Cloud Integration API
  description: The SAP Cloud Integration API (also known as the Process Integration Runtime API) allows developers to deploy, monitor, and manage integration flows and artifacts on SAP Integration Suite. It provides OData and REST endpoints for runtime monitoring, message processing logs, and artifact lifecycle management.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/cloud-integration
  baseURL: https://api.sap.com/api/CloudIntegrationAPI
  tags:
  - Cloud Integration
  - Integration Flows
  - OData
  - Runtime Monitoring
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/cloud-integration
  - type: Reference
    url: https://api.sap.com/api/CloudIntegrationAPI/overview
  - type: Authentication
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
- aid: sap-integration-suite:sap-api-management
  name: SAP API Management API
  description: The SAP API Management API enables programmatic management of APIs, products, applications, and developer portals within SAP Integration Suite. It supports creating and publishing API proxies, managing rate plans, and administering the full API lifecycle.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
  baseURL: https://api.sap.com/api/APIMgmt
  tags:
  - API Gateway
  - API Management
  - API Proxy
  - Developer Portal
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
  - type: Reference
    url: https://api.sap.com/api/APIMgmt/overview
  - type: Getting Started
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/getting-started-with-api-management
- aid: sap-integration-suite:sap-integration-advisor
  name: SAP Integration Advisor API
  description: The SAP Integration Advisor API provides access to the library of message implementation guidelines (MIGs) and mapping guidelines (MAGs) used to simplify B2B and A2A integration scenarios. It supports querying and managing integration content in the Integration Advisor capability.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-advisor-capability
  tags:
  - B2B Integration
  - Integration Advisor
  - Message Mapping
  - MIG
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-advisor-capability
  - type: Reference
    url: https://api.sap.com/api/IntegrationAdvisor/overview
- aid: sap-integration-suite:sap-open-connectors
  name: SAP Open Connectors API
  description: The SAP Open Connectors API (formerly Cloud Elements) provides a unified REST interface to connect to over 160 third-party cloud applications using pre-built connectors. It normalizes disparate API endpoints into consistent resource models for faster integration development.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/open-connectors-capability
  baseURL: https://api.openconnectors.ext.hana.ondemand.com
  tags:
  - Cloud Connectors
  - Open Connectors
  - Third-Party Integration
  - Unified API
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/open-connectors-capability
  - type: Reference
    url: https://api.sap.com/api/OpenConnectors/overview
- aid: sap-integration-suite:sap-trading-partner-management
  name: SAP Trading Partner Management API
  description: The SAP Trading Partner Management API supports the setup and management of B2B trading partner relationships, agreements, and communication channels within SAP Integration Suite. It enables automation of partner onboarding and maintenance of EDI and AS2 communication profiles.
  humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/trading-partner-management-capability
  tags:
  - AS2
  - B2B
  - EDI
  - Trading Partner Management
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/trading-partner-management-capability
  - type: Reference
    url: https://api.sap.com/api/TradingPartnerManagement/overview
- aid: sap-integration-suite:sap-event-mesh
  name: SAP Event Mesh API
  description: The SAP Event Mesh API provides access to the event brokering service within SAP Business Technology Platform that enables applications to communicate through asynchronous events. It supports publishing and subscribing to events across SAP and third-party applications using industry-standard messaging protocols.
  humanURL: https://help.sap.com/docs/event-mesh
  baseURL: https://enterprise-messaging.cfapps.sap.hana.ondemand.com
  tags:
  - Asynchronous
  - Event Mesh
  - Messaging
  - Pub/Sub
  properties:
  - type: Documentation
    url: https://help.sap.com/docs/event-mesh
  - type: Reference
    url: https://api.sap.com/api/SAPEventMesh/overview
name: SAP Integration Suite
tags:
- API Management
- Cloud Integration
- Enterprise Integration
- iPaaS
- SAP
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: SAP Integration Suite is an enterprise integration platform as a service (iPaaS) that connects applications, processes, and people across cloud and on-premises environments. It includes capabilities for Cloud Integration, API Management, Integration Advisor, Open Connectors, and Trading Partner Management as part of SAP Business Technology Platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

