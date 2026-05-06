---
aid: google-cloud-firestore
name: Google Cloud Firestore
description: Google Cloud Firestore is a flexible, scalable NoSQL cloud database for mobile, web, and server development. It keeps data in sync across client apps through real-time listeners and offers offline support for mobile and web, enabling responsive apps that work regardless of network latency or internet connectivity. Firestore supports ACID transactions, automatic multi-region data replication, and strong consistency guarantees.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-firestore/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Database
  - Documents
  - Google Cloud
  - NoSQL
  - Real-Time
apis:
  - name: Cloud Firestore API
    description: The Cloud Firestore API provides RESTful access to create, read, update, and delete documents in Firestore databases. It supports structured queries with filters, ordering, and pagination, as well as batch operations and transactions. The API also enables database management, index configuration, and collection group queries for flexible data modeling and retrieval patterns.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/firestore/docs
    baseURL: https://firestore.googleapis.com/v1
    tags:
      - Collections
      - Documents
      - NoSQL
      - Queries
    properties:
      - type: Documentation
        url: https://cloud.google.com/firestore/docs/reference/rest
      - type: OpenAPI
        url: openapi/cloud-firestore-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/firestore/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/firestore/docs/quickstart
      - type: JSONSchema
        url: json-schema/document-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/firestore
  - type: Getting Started
    url: https://cloud.google.com/firestore/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/firestore/docs
  - type: Authentication
    url: https://cloud.google.com/firestore/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/firestore/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/firestore/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-firestore-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
