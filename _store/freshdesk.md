---
aid: freshdesk
url: https://raw.githubusercontent.com/api-evangelist/freshdesk/refs/heads/main/apis.yml
apis:
- aid: freshdesk:rest-api
  name: Freshdesk REST API
  tags:
  - Agents
  - Companies
  - Contacts
  - Customer Support
  - Helpdesk
  - Tickets
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://yourdomain.freshdesk.com/api/v2
  humanURL: https://developers.freshdesk.com/api/
  properties:
  - url: https://developers.freshdesk.com/api/
    type: Documentation
  - url: openapi/freshdesk-rest-api-openapi.yml
    type: OpenAPI
  description: The Freshdesk REST API (v2) provides programmatic access to helpdesk data and operations within Freshdesk, a customer support platform by Freshworks. It exposes endpoints for managing tickets, contacts, companies, agents, groups, conversations, products, email configurations, SLA policies, and business hours. The API uses JSON for request and response payloads, supports API key-based authentication, and follows RESTful conventions for CRUD operations.
- aid: freshdesk:webhook-api
  name: Freshdesk Webhook API
  tags:
  - Automation
  - Customer Support
  - Events
  - Notifications
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://support.freshdesk.com/support/solutions/folders/272646
  properties:
  - url: https://support.freshdesk.com/support/solutions/folders/272646
    type: Documentation
  - url: asyncapi/freshdesk-webhook-api-asyncapi.yml
    type: AsyncAPI
  description: The Freshdesk Webhook API enables real-time communication between Freshdesk and external systems by sending HTTP POST requests when specific events occur within the helpdesk. Webhooks can be triggered by ticket creation, updates, status changes, and other support events, allowing developers to build event-driven integrations without polling the REST API.
- aid: freshdesk:app-sdk
  name: Freshdesk App SDK
  tags:
  - Apps
  - Extensions
  - Marketplace
  - Plugins
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://developers.freshdesk.com/
  properties:
  - url: https://developers.freshdesk.com/
    type: Documentation
  - url: https://developers.freshworks.com/docs/app-sdk/v3.0/support_ticket/rest-apis/
    type: Documentation
  description: The Freshdesk App SDK allows developers to build custom applications that extend the functionality of the Freshdesk helpdesk platform. Backed by a Platform-as-a-Service infrastructure that includes a data store and serverless runtimes, the SDK provides tools for creating front-end interfaces using the Crayons component library and server-side logic through serverless apps.
name: Freshdesk
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Freshdesk API.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

