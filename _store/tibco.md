---
name: TIBCO
segments:
  - iPaaS
description: APIs and services provided by TIBCO Software Inc., a global leader in integration, API management, and analytics software.
image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
url: https://www.tibco.com
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.18'
tags:
  - Analytics
  - API Management
  - Cloud
  - Enterprise Software
  - Integration
  - Messaging
  - Real-Time Data
apis:
  - name: TIBCO Cloud Integration API
    description: API for TIBCO Cloud Integration platform enabling application integration, API management, and business process automation.
    image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
    humanURL: https://integration.cloud.tibco.com/
    baseURL: https://integration.cloud.tibco.com/api/v1
    tags:
      - Cloud
      - Integration
      - iPaaS
    properties:
      - type: Documentation
        url: https://integration.cloud.tibco.com/docs/
      - type: OpenAPI
        url: https://integration.cloud.tibco.com/docs/api/openapi.json
      - type: Authentication
        url: https://integration.cloud.tibco.com/docs/authentication
      - type: OpenAPI
        url: openapi/tibco-cloud-integration-openapi.yml
  - name: TIBCO Mashery API Management
    description: API management platform for designing, building, securing, and analyzing APIs.
    image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
    humanURL: https://www.tibco.com/products/api-management
    baseURL: https://api.mashery.com
    tags:
      - Analytics
      - API Management
      - Security
    properties:
      - type: Documentation
        url: https://developer.mashery.com/docs
      - type: OpenAPI
        url: https://developer.mashery.com/io-docs
      - type: Portal
        url: https://developer.mashery.com
      - type: OpenAPI
        url: openapi/tibco-mashery-openapi.yml
  - name: TIBCO BusinessEvents API
    description: Complex event processing and decision management API for real-time business operations.
    image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
    humanURL: https://www.tibco.com/products/tibco-businessevents
    baseURL: https://api.tibco.com/businessevents/v1
    tags:
      - Decision Management
      - Event Processing
      - Real-Time
    properties:
      - type: Documentation
        url: https://docs.tibco.com/products/tibco-businessevents
      - type: SDK
        url: https://docs.tibco.com/products/tibco-businessevents/sdk
      - type: OpenAPI
        url: openapi/tibco-businessevents-openapi.yml
  - name: TIBCO Messaging API
    description: Enterprise messaging API supporting EMS (Enterprise Message Service) and FTL (Fast Transport Layer).
    image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
    humanURL: https://www.tibco.com/products/tibco-enterprise-message-service
    baseURL: https://messaging.cloud.tibco.com/api/v1
    tags:
      - JMS
      - Messaging
      - Publish-Subscribe
    properties:
      - type: Documentation
        url: https://docs.tibco.com/products/tibco-enterprise-message-service
      - type: Protocol
        url: https://docs.tibco.com/products/tibco-enterprise-message-service/protocol-reference
      - type: AsyncAPI
        url: asyncapi/tibco-messaging-asyncapi.yml
  - name: TIBCO Spotfire Analytics API
    description: Analytics and data visualization API for embedded analytics and automated workflows.
    image: https://www.tibco.com/sites/tibco/files/media_entity/2021-04/TIBCO-logo.svg
    humanURL: https://www.tibco.com/products/tibco-spotfire
    baseURL: https://spotfire.cloud.tibco.com/api/rest/v1
    tags:
      - Analytics
      - Business Intelligence
      - Visualization
    properties:
      - type: Documentation
        url: https://docs.tibco.com/products/tibco-spotfire/latest
      - type: API Reference
        url: https://docs.tibco.com/pub/spotfire_server/latest/doc/api/TIB_sfire_server_tsas_admin_api/index.html
      - type: JavaScript API
        url: https://docs.tibco.com/pub/spotfire/latest/doc/api/TIB_sfire-jsapi/index.html
      - type: OpenAPI
        url: openapi/tibco-spotfire-openapi.yml
common:
  - type: Portal
    url: https://developer.tibco.com
  - type: Documentation
    url: https://docs.tibco.com
  - type: Support
    url: https://support.tibco.com
  - type: Status
    url: https://status.tibco.com
  - type: Blog
    url: https://www.tibco.com/blog
  - type: GitHub
    url: https://github.com/tibco
  - type: LinkedIn
    url: https://www.linkedin.com/company/tibco
  - type: Twitter
    url: https://twitter.com/tibco
  - type: Terms of Service
    url: https://www.tibco.com/legal/terms-of-use
  - type: Privacy Policy
    url: https://www.tibco.com/legal/privacy
  - type: JSON-LD
    url: json-ld/tibco-context.jsonld
  - type: JSONSchema
    url: json-schema/tibco-integration-app-schema.json
  - type: JSONSchema
    url: json-schema/tibco-api-service-schema.json
  - type: Spectral
    url: rules/tibco-rules.yml
  - type: Vocabulary
    url: vocabulary/tibco-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
