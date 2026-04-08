---
aid: google-cloud-storage
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-storage/refs/heads/main/apis.yml
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
name: Google Cloud Storage
tags:
- Buckets
- Cloud
- Google Cloud
- Objects
- Storage
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Storage is a managed service for storing unstructured data such as images, videos, backups, and other binary or text objects. It provides a single API for accessing both simple storage and highly available, globally redundant storage, with automatic data encryption, built-in redundancy, and fine-grained access controls.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

