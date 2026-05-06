---
name: Google Cloud Transfer Service
description: Google Cloud Storage Transfer Service enables seamless data movement across object and file storage systems, including transfers from Amazon S3, Azure Blob Storage, or Cloud Storage to Cloud Storage, and from on-premises storage to Cloud Storage. It is optimized for large-scale transfers involving terabytes or petabytes of data.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-transfer-service/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - Azure
  - Cloud Storage
  - Data Transfer
  - Migration
  - S3
  - Storage
apis:
  - name: Storage Transfer API
    description: The Storage Transfer API provides programmatic access to Google Cloud Storage Transfer Service for creating, managing, and monitoring data transfer jobs between cloud storage systems and on-premises storage. Developers can use the API to schedule transfers, configure transfer options, manage agent pools for on-premises transfers, and monitor transfer operation status and progress.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/storage-transfer/docs
    baseURL: https://storagetransfer.googleapis.com
    tags:
      - Data Transfer
      - Scheduling
      - Storage
      - Transfer Jobs
    properties:
      - type: Documentation
        url: https://cloud.google.com/storage-transfer/docs/reference/rest
      - type: OpenAPI
        url: openapi/storage-transfer-api-openapi.yml
      - type: JSONSchema
        url: json-schema/google-cloud-transfer-service-job-schema.json
common:
  - type: GettingStarted
    url: https://cloud.google.com/storage-transfer/docs/create-transfers
  - type: Pricing
    url: https://cloud.google.com/storage-transfer/pricing
  - type: JSON-LD
    url: json-ld/google-cloud-transfer-service-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
