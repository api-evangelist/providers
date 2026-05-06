---
aid: customer-io
url: https://raw.githubusercontent.com/api-evangelist/customer-io/refs/heads/main/apis.yml
apis:
  - aid: customer-io:track-api
    name: Customer.io Track API
    tags:
      - Behavioral Data
      - Customer Data
      - Event Tracking
      - Marketing Automation
      - Messaging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://track.customer.io
    humanURL: https://docs.customer.io/integrations/api/track/
    properties:
      - url: https://docs.customer.io/integrations/api/track/
        type: Documentation
      - url: openapi/customer-io-track-api-openapi.yml
        type: OpenAPI
    description: The Customer.io Track API allows developers to send behavioral data and customer profile information into Customer.io. It provides endpoints for identifying customers, tracking events, managing devices for push notifications, and sending anonymous events. The API uses basic authentication with a Site ID and API key, and accepts JSON request bodies.
  - aid: customer-io:app-api
    name: Customer.io App API
    tags:
      - Broadcasts
      - Campaigns
      - Marketing Automation
      - Messaging
      - Segments
      - Transactional Email
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.customer.io
    humanURL: https://docs.customer.io/integrations/api/app/
    properties:
      - url: https://docs.customer.io/integrations/api/app/
        type: Documentation
      - url: openapi/customer-io-app-api-openapi.yml
        type: OpenAPI
    description: The Customer.io App API enables developers to manage workspace resources and send messages programmatically. It provides endpoints for sending transactional messages, triggering broadcasts, managing customers and segments, retrieving campaign and newsletter data, and exporting customer information.
  - aid: customer-io:pipelines-api
    name: Customer.io Pipelines API
    tags:
      - CDP
      - Customer Data Platform
      - Data Ingestion
      - Marketing Automation
      - Messaging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cdp.customer.io
    humanURL: https://docs.customer.io/integrations/data-in/connections/http-api/
    properties:
      - url: https://docs.customer.io/integrations/data-in/connections/http-api/
        type: Documentation
      - url: openapi/customer-io-pipelines-api-openapi.yml
        type: OpenAPI
    description: The Customer.io Pipelines API is the newer data ingestion interface for getting customer and event data into Customer.io. It follows the Segment spec and supports identify, track, page, screen, group, and alias calls. Customer.io recommends the Pipelines API for new integrations because it is easier to use, supports outbound data integrations and transformations, and is the focus of ongoing development.
common:
  - type: Website
    url: https://customer.io
  - type: Documentation
    url: https://docs.customer.io
  - type: AsyncAPI
    url: asyncapi/customer-io-reporting-webhooks-asyncapi.yml
  - type: JSONSchema
    url: json-schema/customer-io-customer-schema.json
  - type: JSONSchema
    url: json-schema/customer-io-event-schema.json
  - type: JSONSchema
    url: json-schema/customer-io-webhook-payload-schema.json
  - type: JSON-LD
    url: json-ld/customer-io-context.jsonld
  - type: Vocabulary
    url: vocabulary/customer-io-vocabulary.yml
  - type: Rules
    url: rules/customer-io-rules.yml
  - type: Capabilities
    url: capabilities/customer-io-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.20'
created: '2024-01-01'
modified: '2026-04-28'
name: Customer.io
tags:
  - Behavioral Data
  - Broadcasts
  - Campaigns
  - CDP
  - Customer Data
  - Customer Data Platform
  - Data Ingestion
  - Email
  - Event Tracking
  - Marketing Automation
  - Messaging
  - Push Notifications
  - Segments
  - SMS
  - Transactional Email
description: Customer.io is a customer engagement platform that combines a customer data platform, marketing automation, and messaging delivery to send behavior-triggered email, push, SMS, and in-app messages. Its API surface includes the Track API for sending behavioral data and customer profile updates, the App API for managing workspace resources and sending transactional and broadcast messages, the Pipelines API which is a Segment-spec data ingestion interface, and outbound reporting webhooks that deliver message lifecycle events.
---
