---
aid: google-cloud-eventarc
name: Google Cloud Eventarc
description: Google Cloud Eventarc is a fully managed eventing service that allows you to build event-driven architectures by routing events from Google Cloud services, SaaS applications, and custom sources to target destinations. Eventarc supports both standard and advanced editions, providing scalable, serverless event routing with built-in security, authorization, observability, and error handling.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-eventarc/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Event-Driven
  - Events
  - Google Cloud
  - Messaging
  - Serverless
  - Triggers
apis:
  - name: Google Cloud Eventarc API
    description: The Eventarc API enables you to create and manage event triggers, channels, and channel connections for routing events between providers and subscribers. It supports CloudEvents-compliant event delivery to Cloud Run, Cloud Functions, GKE, and Workflows targets.
    humanURL: https://cloud.google.com/eventarc/docs
    baseURL: https://eventarc.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/eventarc/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/eventarc/docs/quickstarts
      - type: JSONSchema
        url: json-schema/json-schema.yml
    tags:
      - Event-Driven Architecture
      - Events
      - Triggers
common:
  - type: Portal
    url: https://cloud.google.com/eventarc
  - type: Getting Started
    url: https://cloud.google.com/eventarc/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/eventarc/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/eventarc/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/eventarc/docs/support
  - type: JSONLD
    url: json-ld/json-ld.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
