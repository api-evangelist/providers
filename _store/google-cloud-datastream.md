---
aid: google-cloud-datastream
name: Google Cloud Datastream
description: Google Cloud Datastream is a serverless change data capture (CDC) and replication service that allows you to synchronize data across heterogeneous databases, storage systems, and applications reliably and with minimal latency.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-datastream/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Change Data Capture
  - Data Replication
  - Google Cloud
  - Streaming
apis:
  - name: Google Cloud Datastream API
    description: The Datastream API enables serverless change data capture and replication. It provides methods to create and manage connection profiles for source and destination databases, configure streams for continuous data replication, and monitor replication status and operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/datastream/docs
    baseURL: https://datastream.googleapis.com
    tags:
      - CDC
      - Replication
      - Streams
    properties:
      - type: Documentation
        url: https://cloud.google.com/datastream/docs/reference/rest
      - type: OpenAPI
        url: openapi/google-cloud-datastream-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/datastream/docs/quickstart
      - type: JSONSchema
        url: json-schema/google-cloud-datastream-stream-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/datastream
  - type: Getting Started
    url: https://cloud.google.com/datastream/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/datastream/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/datastream/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/datastream/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-datastream-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
