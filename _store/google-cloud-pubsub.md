---
name: Google Cloud Pub/Sub
description: Google Cloud Pub/Sub is a fully managed, real-time messaging service that allows you to send and receive messages between independent applications. It provides reliable, many-to-many, asynchronous messaging that decouples senders and receivers.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-pubsub/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Event-Driven
  - Google Cloud
  - Messaging
  - Pub/Sub
apis:
  - name: Google Cloud Pub/Sub API
    description: The Cloud Pub/Sub API provides reliable, many-to-many, asynchronous messaging between applications. It allows you to create and manage topics for publishing messages, create subscriptions for consuming messages, and handle message acknowledgment and delivery.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/pubsub/docs
    baseURL: https://pubsub.googleapis.com
    tags:
      - Messaging
      - Subscriptions
      - Topics
    properties:
      - type: Documentation
        url: https://cloud.google.com/pubsub/docs/reference/rest
      - type: OpenAPI
        url: openapi/google-cloud-pubsub-openapi.yml
      - type: JSONSchema
        url: json-schema/google-cloud-pubsub-topic-schema.json
common:
  - type: GettingStarted
    url: https://cloud.google.com/pubsub/docs/quickstarts
  - type: Pricing
    url: https://cloud.google.com/pubsub/pricing
  - type: JSON-LD
    url: json-ld/google-cloud-pubsub-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
