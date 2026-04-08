---
aid: e2open
url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/apis.yml
apis:
- aid: e2open:e2open-supply-chain-api
  name: E2open Supply Chain Platform API
  tags:
  - JSON
  - Logistics
  - REST
  - Supply Chain
  - Trade Management
  - Visibility
  image: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/image.png
  humanURL: https://www.e2open.com/
  baseURL: https://api.e2open.com
  properties:
  - url: https://www.e2open.com/
    type: Documentation
  description: E2open supply chain platform APIs enable supply chain event management, transportation management, customs compliance, and end-to-end shipment visibility. The platform supports REST/JSON, XML, and EDI protocols connecting over 400,000 manufacturing, logistics, channel, and distribution partners, tracking over 12 billion transactions annually.
- aid: e2open:inttra-ocean-api
  name: INTTRA Ocean Execution API
  tags:
  - Booking
  - JSON
  - Logistics
  - Ocean Shipping
  - REST
  - Supply Chain
  - Track and Trace
  image: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/image.png
  humanURL: https://apidocs.inttra.com/
  baseURL: https://api.inttra.com
  properties:
  - url: https://apidocs.inttra.com/
    type: Documentation
  - url: https://apidocs.inttra.com/
    type: Reference
  - url: https://www.inttra.com/services/integration/
    type: GettingStarted
  - url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/openapi/inttra-ocean-execution-openapi.yml
    type: OpenAPI
  description: INTTRA (now part of e2open) provides ocean execution APIs for the world's largest multi-carrier e-commerce platform for global shipping. The RESTful API uses HTTPS with JSON for booking, ocean schedules, rates, and visibility/track and trace products. Authentication requires a token obtained from the identity service before making API requests.
- aid: e2open:e2open-transportation-management-api
  name: E2open Transportation Management API
  tags:
  - Appointment Scheduling
  - Carrier Integration
  - Logistics
  - Supply Chain
  - Transportation
  image: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/image.png
  humanURL: https://marketplace.e2open.com/
  baseURL: https://api.e2open.com
  properties:
  - url: https://marketplace.e2open.com/product/api-implementation/
    type: Documentation
  description: E2open Transportation Management API provides appointment scheduling, carrier integration, and real-time rating capabilities. REST endpoints allow carriers to POST documents, retrieve current rates, manage load stop details, and communicate appointment status updates with supply chain stakeholders.
name: E2Open
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Supply chain software with a connected network and SaaS platform help you seize opportunities, predict disruptions, and drive efficiency and sustainability.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

