---
aid: google-pub-sub
name: Google Pub/Sub
description: Google Cloud Pub/Sub is a fully managed, real-time messaging service that allows you to send and receive messages between independent applications, providing reliable, many-to-many, asynchronous messaging for event ingestion, streaming analytics, and event-driven computing.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Event-Driven
  - Google Cloud
  - Messaging
  - Pub/Sub
  - Streaming
url: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: google-pub-sub:google-pub-sub
    name: Google Pub/Sub
    description: Google Cloud Pub/Sub is a messaging and event ingestion service that provides durable message storage and real-time message delivery for building event-driven systems and streaming data pipelines on Google Cloud Platform.
    humanURL: https://cloud.google.com/pubsub
    tags:
      - Cloud
      - Event-Driven
      - Google Cloud
      - Messaging
      - Pub/Sub
      - Streaming
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/openapi/google-pub-sub-openapi.yml
      - type: AsyncAPI
        url: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/asyncapi/google-pub-sub-asyncapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/json-schema/google-pub-sub-topic.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/google-pub-sub/refs/heads/main/json-schema/google-pub-sub-message.yml
common:
  - type: Website
    url: https://cloud.google.com/pubsub
  - type: Documentation
    url: https://cloud.google.com/pubsub/docs
  - type: Getting Started
    url: https://cloud.google.com/pubsub/docs/quickstarts
  - type: Pricing
    url: https://cloud.google.com/pubsub/pricing
  - type: GitHub
    url: https://github.com/googleapis/google-cloud-go
  - type: Blog
    url: https://cloud.google.com/blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
