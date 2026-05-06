---
aid: google-cloud-storage
name: Google Cloud Storage
description: Google Cloud Storage is a managed service for storing unstructured data such as images, videos, backups, and other binary or text objects. It provides a single API for accessing both simple storage and highly available, globally redundant storage, with automatic data encryption, built-in redundancy, and fine-grained access controls.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-storage/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Buckets
  - Cloud
  - Google Cloud
  - Objects
  - Storage
apis:
  - name: Cloud Storage JSON API
    description: The Cloud Storage JSON API is a RESTful interface for managing data in Google Cloud Storage. It allows you to create and manage buckets, upload and download objects, manage access controls, and configure lifecycle policies. The API supports resumable uploads, object versioning, and customer-managed encryption keys for comprehensive cloud storage management.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/storage/docs
    baseURL: https://storage.googleapis.com/storage/v1
    tags:
      - Buckets
      - Objects
      - Storage
    properties:
      - type: Documentation
        url: https://cloud.google.com/storage/docs/json_api
      - type: OpenAPI
        url: openapi/cloud-storage-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/storage/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/storage/docs/quickstarts
      - type: JSONSchema
        url: json-schema/bucket-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/storage
  - type: Getting Started
    url: https://cloud.google.com/storage/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/storage/docs
  - type: Authentication
    url: https://cloud.google.com/storage/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/storage/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/storage/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-storage-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
