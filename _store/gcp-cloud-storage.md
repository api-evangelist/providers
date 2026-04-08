---
aid: gcp-cloud-storage
url: https://raw.githubusercontent.com/api-evangelist/gcp-cloud-storage/refs/heads/main/apis.yml
apis:
- name: Google Cloud Storage JSON API
  description: RESTful API for interacting with Google Cloud Storage buckets and objects.
  image: https://cloud.google.com/images/storage/storage-icon.svg
  humanURL: https://cloud.google.com/storage/docs/json_api
  baseURL: https://storage.googleapis.com/storage/v1
  properties:
  - type: Documentation
    url: https://cloud.google.com/storage/docs/json_api
  - type: OpenAPI
    url: https://storage.googleapis.com/$discovery/rest?version=v1
  - type: Authentication
    url: https://cloud.google.com/storage/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/storage/pricing
  - type: Quotas
    url: https://cloud.google.com/storage/quotas
  - type: Status
    url: https://status.cloud.google.com/
  - type: TermsOfService
    url: https://cloud.google.com/terms
  - type: APIReference
    url: https://cloud.google.com/storage/docs/json_api/v1
  - type: IAMPermissions
    url: https://cloud.google.com/storage/docs/access-control/iam-json
  - type: Encryption
    url: https://cloud.google.com/storage/docs/encryption
  - type: AccessControl
    url: https://cloud.google.com/storage/docs/access-control/iam
  - type: OpenAPI
    url: openapi/gcp-cloud-storage-json-api-openapi.yml
  contact:
  - type: Support
    url: https://cloud.google.com/storage/docs/getting-support
  - type: Twitter
    url: https://twitter.com/googlecloud
- name: Google Cloud Storage XML API
  description: Amazon S3-compatible XML API for Google Cloud Storage.
  image: https://cloud.google.com/images/storage/storage-icon.svg
  humanURL: https://cloud.google.com/storage/docs/xml-api
  baseURL: https://storage.googleapis.com
  properties:
  - type: Documentation
    url: https://cloud.google.com/storage/docs/xml-api/overview
  - type: Authentication
    url: https://cloud.google.com/storage/docs/authentication/hmackeys
  - type: S3Compatibility
    url: https://cloud.google.com/storage/docs/interoperability
  - type: APIReference
    url: https://cloud.google.com/storage/docs/xml-api/reference-methods
  - type: Headers
    url: https://cloud.google.com/storage/docs/xml-api/reference-headers
  - type: Pricing
    url: https://cloud.google.com/storage/pricing
  - type: Quotas
    url: https://cloud.google.com/storage/quotas
  - type: Status
    url: https://status.cloud.google.com/
  - type: TermsOfService
    url: https://cloud.google.com/terms
  contact:
  - type: Support
    url: https://cloud.google.com/storage/docs/getting-support
  - type: Twitter
    url: https://twitter.com/googlecloud
name: Google Cloud Storage
tags:
- Archival
- Backup
- Blob Storage
- Cloud Storage
- Data
- File Storage
- Gcp
- Google Cloud
- Object Storage
- Storage
type: Contract
image: https://cloud.google.com/images/social-icon-google-cloud-1200-630.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Object storage service offering high durability, availability, and scalability for storing and accessing data on Google Cloud Platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

