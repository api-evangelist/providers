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
common:
  - url: https://www.e2open.com/
    type: Website
  - url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/openapi/inttra-ocean-execution-openapi.yml
    type: OpenAPI
  - url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/json-schema/e2open-shipment-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/e2open/refs/heads/main/json-ld/e2open-context.jsonld
    type: JSONLDContext
  - url: https://apidocs.inttra.com/
    type: Portal
  - url: https://www.e2open.com/e2open-network-connectivity/
    type: Documentation
  - url: https://www.e2open.com/privacy-policy/
    type: PrivacyPolicy
  - url: https://www.inttra.com/legal/
    type: TermsOfService
  - url: https://marketplace.e2open.com/
    type: GettingStarted
  - url: https://knowledge.e2open.com/knowledgecenter/inttra-resources/
    type: Support
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-04-28'
specificationVersion: '0.19'
description: Supply chain software with a connected network and SaaS platform help you seize opportunities, predict disruptions, and drive efficiency and sustainability.
---
