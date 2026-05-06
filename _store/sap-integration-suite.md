---
aid: sap-integration-suite
name: SAP Integration Suite
description: SAP Integration Suite is an enterprise integration platform as a service (iPaaS) that connects applications, processes, and people across cloud and on-premises environments. It includes capabilities for Cloud Integration, API Management, Integration Advisor, Open Connectors, Trading Partner Management, and Event Mesh as part of SAP Business Technology Platform (BTP). It enables seamless connectivity between SAP and non-SAP systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Cloud Integration
  - Enterprise Integration
  - Event Mesh
  - iPaaS
  - SAP
  - SAP BTP
url: https://raw.githubusercontent.com/api-evangelist/sap-integration-suite/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: sap-integration-suite:sap-cloud-integration
    name: SAP Cloud Integration API
    description: The SAP Cloud Integration API (Process Integration Runtime API) allows developers to deploy, monitor, and manage integration flows and artifacts on SAP Integration Suite. It provides OData V2 endpoints for runtime monitoring, message processing logs, artifact lifecycle management, integration package management, and service endpoint discovery.
    humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/cloud-integration
    baseURL: https://{host}/api/v1
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
      - type: OpenAPI
        url: openapi/sap-integration-suite-cloud-integration-openapi.yml
      - type: JSONSchema
        url: json-schema/sap-integration-suite-integration-package-schema.json
      - type: JSONSchema
        url: json-schema/sap-integration-suite-message-processing-log-schema.json
      - type: JSONLD
        url: json-ld/sap-integration-suite-context.jsonld
      - type: Authentication
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
  - aid: sap-integration-suite:sap-api-management
    name: SAP API Management API
    description: The SAP API Management API enables programmatic management of APIs, products, applications, and developer portals within SAP Integration Suite. It supports creating and publishing API proxies, managing rate plans, administering the full API lifecycle, configuring policies, and managing developer portal content. Built on REST and OData principles.
    humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
    baseURL: https://{api-portal-host}/apiportal/api/1.0
    tags:
      - API Gateway
      - API Management
      - API Proxy
      - Developer Portal
      - OData
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/api-management-capability
      - type: Reference
        url: https://api.sap.com/api/APIMgmt/overview
      - type: OpenAPI
        url: openapi/sap-integration-suite-api-management-openapi.yml
      - type: JSONLD
        url: json-ld/sap-integration-suite-context.jsonld
      - type: Authentication
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
  - aid: sap-integration-suite:sap-integration-advisor
    name: SAP Integration Advisor API
    description: The SAP Integration Advisor API provides access to the library of message implementation guidelines (MIGs) and mapping guidelines (MAGs) used to simplify B2B and A2A integration scenarios. It supports querying and managing integration content including type systems, business context, and codelists in the Integration Advisor capability.
    humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-advisor-capability
    baseURL: https://{host}/api
    tags:
      - B2B Integration
      - EDI
      - Integration Advisor
      - Mapping Guidelines
      - Message Implementation Guidelines
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/integration-advisor-capability
      - type: Reference
        url: https://api.sap.com/api/IntegrationAdvisor/overview
      - type: Authentication
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
  - aid: sap-integration-suite:sap-open-connectors
    name: SAP Open Connectors API
    description: The SAP Open Connectors API (formerly Cloud Elements) provides a unified REST interface to connect to over 160 third-party cloud applications using pre-built connectors. It normalizes disparate API endpoints into consistent resource models for faster integration development. Connectors are available for CRM, ERP, marketing, storage, and collaboration platforms.
    humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/open-connectors-capability
    baseURL: https://api.openconnectors.ext.hana.ondemand.com
    tags:
      - Cloud Connectors
      - Normalization
      - Open Connectors
      - Third-Party Integration
      - Unified API
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/open-connectors-capability
      - type: Reference
        url: https://api.sap.com/api/OpenConnectors/overview
      - type: Authentication
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/open-connectors-capability
  - aid: sap-integration-suite:sap-trading-partner-management
    name: SAP Trading Partner Management API
    description: The SAP Trading Partner Management API supports setup and management of B2B trading partner relationships, agreements, and communication channels within SAP Integration Suite. It enables automation of partner onboarding, maintenance of EDI and AS2 communication profiles, and management of certificates and agreements.
    humanURL: https://help.sap.com/docs/integration-suite/sap-integration-suite/trading-partner-management-capability
    baseURL: https://{host}/api
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
      - type: Authentication
        url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
  - aid: sap-integration-suite:sap-event-mesh
    name: SAP Event Mesh API
    description: The SAP Event Mesh API provides access to the event brokering service within SAP Business Technology Platform that enables applications to communicate through asynchronous events. It supports publishing and subscribing to events across SAP and third-party applications using CloudEvents standard and AMQP/MQTT/HTTP protocols.
    humanURL: https://help.sap.com/docs/event-mesh
    baseURL: https://enterprise-messaging.cfapps.sap.hana.ondemand.com
    tags:
      - Asynchronous
      - CloudEvents
      - Event Mesh
      - Messaging
      - Pub/Sub
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/event-mesh
      - type: Reference
        url: https://api.sap.com/api/SAPEventMesh/overview
      - type: Authentication
        url: https://help.sap.com/docs/event-mesh/sap-event-mesh/authentication-and-authorization
  - aid: sap-integration-suite:sap-integration-suite-advanced-event-mesh
    name: SAP Integration Suite Advanced Event Mesh API
    description: The SAP Integration Suite Advanced Event Mesh (AEM) REST API provides management capabilities for event brokers, message queues, topic subscriptions, and event broker services. It enables programmatic management of messaging infrastructure including creation and monitoring of event brokers and messaging services.
    humanURL: https://help.pubsub.em.services.cloud.sap/Cloud/cloud-rest-api-lp.htm
    baseURL: https://api.solacecloud.com/api/v2
    tags:
      - Advanced Event Mesh
      - Broker Management
      - Event Streaming
      - Messaging
      - REST
    properties:
      - type: Documentation
        url: https://help.pubsub.em.services.cloud.sap/Cloud/cloud-rest-api-lp.htm
      - type: Reference
        url: https://api.sap.com/package/SAPIIntegrationSuiteAdvancedEventMesh/rest
      - type: Authentication
        url: https://help.pubsub.em.services.cloud.sap/Cloud/ght_use_rest_api_services.htm
common:
  - type: Portal
    url: https://api.sap.com/
  - type: Documentation
    url: https://help.sap.com/docs/integration-suite
  - type: Website
    url: https://www.sap.com/products/technology-platform/integration-suite.html
  - type: Getting Started
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/what-is-sap-integration-suite
  - type: Authentication
    url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
  - type: Blog
    url: https://blogs.sap.com/tags/73554900100700002542/
  - type: Community
    url: https://community.sap.com/topics/integration-suite
  - type: Support
    url: https://support.sap.com/en/product/support-by-product/73554900100700002542.html
  - type: Status
    url: https://www.sap.com/about/trust-center/cloud-service-status.html
  - type: GitHub Organization
    url: https://github.com/SAP-samples
  - type: Terms of Service
    url: https://www.sap.com/about/agreements/policies/cloud-platform.html
  - type: Privacy Policy
    url: https://www.sap.com/about/legal/privacy.html
  - type: YouTube
    url: https://www.youtube.com/@SAPTechnology
  - type: Pricing
    url: https://www.sap.com/products/technology-platform/integration-suite/pricing.html
  - type: Tutorials
    url: https://developers.sap.com/tutorial-navigator.html?tag=software-product%3Atechnology-platform%2Fsap-integration-suite
  - type: Vocabulary
    url: vocabulary/sap-integration-suite-vocabulary.yml
  - type: Capabilities
    url: capabilities/integration-lifecycle.yaml
  - type: SpectralRules
    url: rules/sap-integration-suite-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
