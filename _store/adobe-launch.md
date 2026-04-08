---
aid: adobe-launch
url: https://raw.githubusercontent.com/api-evangelist/adobe-launch/refs/heads/main/apis.yml
apis:
- name: Adobe Launch Reactor API
  description: The Reactor API allows you to programmatically manage all resources for Adobe Experience Platform Tags, including properties, data elements, rules, extensions, library builds, and environments. It follows the JSON API specification for request and response formatting.
  baseURL: https://reactor.adobe.io
  humanURL: https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/overview
  image: https://www.adobe.com/content/dam/cc/icons/adobe-corporate-logo.svg
  tags:
  - Automation
  - Data Collection
  - Marketing Technology
  - Tag Management
  properties:
  - type: Documentation
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/overview
  - type: Reference
    url: https://developer.adobe.com/experience-platform-apis/references/reactor/
  - type: Authentication
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/getting-started
  - type: Getting Started
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/api/getting-started
  - type: PostmanCollection
    url: https://github.com/adobe/reactor-postman
  - type: SDKs
    url: https://www.npmjs.com/package/@adobe/reactor-sdk
  - type: Change Log
    url: https://experienceleague.adobe.com/en/docs/experience-platform/release-notes/latest
  - type: OpenAPI
    url: openapi/reactor-api.yml
  - type: JSONSchema
    url: json-schema/property.json
  - type: JSONSchema
    url: json-schema/rule.json
  - type: JSONSchema
    url: json-schema/data-element.json
  - type: JSONSchema
    url: json-schema/extension.json
  - type: JSONSchema
    url: json-schema/library.json
  - type: JSONSchema
    url: json-schema/build.json
  - type: JSONLD
    url: json-ld/context.jsonld
  contact:
  - type: Support
    url: https://experienceleague.adobe.com/?support-solution=Experience+Platform
- name: Adobe Launch Extension API
  description: API for developing custom extensions for Adobe Experience Platform Tags, allowing developers to create integrations with third-party tools and services. Extensions are the building blocks of tags and consist of library modules and views.
  baseURL: https://reactor.adobe.io
  humanURL: https://experienceleague.adobe.com/en/docs/experience-platform/tags/extension-dev/overview
  image: https://www.adobe.com/content/dam/cc/icons/adobe-corporate-logo.svg
  tags:
  - Development
  - Extensions
  - Integrations
  - Tag Management
  properties:
  - type: Documentation
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/extension-dev/overview
  - type: SDKs
    url: https://www.npmjs.com/package/@adobe/reactor-scaffold
  - type: Client Libraries
    url: https://www.npmjs.com/package/@adobe/reactor-sandbox
  - type: OpenAPI
    url: openapi/extension-api.yml
  - type: JSONSchema
    url: json-schema/extension.json
  - type: JSONLD
    url: json-ld/context.jsonld
  contact:
  - type: Support
    url: https://experienceleague.adobe.com/?support-solution=Experience+Platform
- name: Adobe Experience Platform Event Forwarding API
  description: Event forwarding allows you to send collected event data to destinations for server-side processing using the Adobe Experience Platform Edge Network. It decreases web page weight by moving tasks from the client to Adobe servers.
  baseURL: https://reactor.adobe.io
  humanURL: https://experienceleague.adobe.com/en/docs/experience-platform/tags/event-forwarding/overview
  image: https://www.adobe.com/content/dam/cc/icons/adobe-corporate-logo.svg
  tags:
  - Data Collection
  - Edge Network
  - Event Forwarding
  - Server Side
  properties:
  - type: Documentation
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/event-forwarding/overview
  - type: Getting Started
    url: https://experienceleague.adobe.com/en/docs/experience-platform/tags/event-forwarding/getting-started
  - type: OpenAPI
    url: openapi/event-forwarding-api.yml
  - type: JSONLD
    url: json-ld/context.jsonld
  contact:
  - type: Support
    url: https://experienceleague.adobe.com/?support-solution=Experience+Platform
- name: Adobe Experience Platform Data Collection API
  description: The Data Collection APIs provide endpoints for sending data directly to the Adobe Experience Platform Edge Network, including the Edge Network API for authenticated and non-authenticated data ingestion and the Media Edge API for media tracking data.
  baseURL: https://edge.adobedc.net
  humanURL: https://developer.adobe.com/data-collection-apis/docs/
  image: https://www.adobe.com/content/dam/cc/icons/adobe-corporate-logo.svg
  tags:
  - Analytics
  - Data Collection
  - Data Ingestion
  - Edge Network
  properties:
  - type: Documentation
    url: https://developer.adobe.com/data-collection-apis/docs/
  - type: Getting Started
    url: https://developer.adobe.com/data-collection-apis/docs/getting-started/
  - type: Authentication
    url: https://developer.adobe.com/data-collection-apis/docs/getting-started/authentication
  - type: OpenAPI
    url: openapi/data-collection-api.yml
  - type: JSONLD
    url: json-ld/context.jsonld
  contact:
  - type: Support
    url: https://experienceleague.adobe.com/?support-solution=Experience+Platform
name: Adobe Launch
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Adobe Launch, now known as Adobe Experience Platform Tags, is a next-generation tag management system that unifies the client-side marketing ecosystem by empowering developers to build integrations on a robust, extensible platform that partners, clients, and the broader industry can build on and contribute to.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

