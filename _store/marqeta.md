---
aid: marqeta
url: https://raw.githubusercontent.com/api-evangelist/marqeta/refs/heads/main/apis.yml
apis:
- aid: marqeta:core-api
  name: Marqeta Core API
  tags:
  - Card Issuing
  - Fintech
  - Payment Processing
  - Payments
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://sandbox-api.marqeta.com/v3
  humanURL: https://www.marqeta.com/docs/core-api/introduction
  properties:
  - url: https://www.marqeta.com/docs/core-api/introduction
    type: Documentation
  - url: openapi/marqeta-core-api-openapi.yml
    type: OpenAPI
  description: The Marqeta Core API is a RESTful interface that enables developers to build and manage card payment programs programmatically. It provides endpoints for creating and managing cardholders, issuing physical and virtual cards, defining spending controls, and retrieving transaction data. The API supports use cases including prepaid cards, expense management, earned wage access, and buy now pay later programs. Authentication uses HTTP Basic Auth, and the API communicates using JSON over HTTPS.
- aid: marqeta:diva-api
  name: Marqeta DiVA API
  tags:
  - Analytics
  - Data
  - Fintech
  - Reporting
  - REST
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://diva-api.marqeta.com/data/v2
  humanURL: https://www.marqeta.com/docs/diva-api/introduction
  properties:
  - url: https://www.marqeta.com/docs/diva-api/introduction
    type: Documentation
  - url: openapi/marqeta-diva-api-openapi.yml
    type: OpenAPI
  description: The Marqeta DiVA (Data insights, Visualization, and Analytics) API is a RESTful interface that provides programmatic access to production data from a Marqeta card program. It surfaces the data behind Marqeta's reporting and analytics tools, enabling developers to retrieve large datasets in JSON or CSV format. The API supports filtering, sorting, aggregation, and pagination for customized responses.
- aid: marqeta:webhooks
  name: Marqeta Webhooks
  tags:
  - Events
  - Fintech
  - Notifications
  - Real-Time
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://your-server.example.com/webhooks
  humanURL: https://www.marqeta.com/docs/developer-guides/webhooks-landing-page
  properties:
  - url: https://www.marqeta.com/docs/developer-guides/webhooks-landing-page
    type: Documentation
  - url: asyncapi/marqeta-webhooks-asyncapi.yml
    type: AsyncAPI
  description: Marqeta Webhooks deliver real-time event notifications to a developer- configured endpoint when specific events occur within a card program. Each program supports up to five active webhook configurations, and events cover card transactions, authorizations, declines, and other platform activity. Webhook payloads are delivered as HTTP POST requests in JSON format to the receiving endpoint. This allows applications to respond immediately to card activity without polling the Core API for updates.
name: Marqeta
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Marqeta is a modern card issuing platform that empowers innovators to build configurable payment cards and provides issuer processor services to power digital banking, financial services, and commerce.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

