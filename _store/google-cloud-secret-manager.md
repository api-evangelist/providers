---
aid: google-cloud-secret-manager
name: Google Cloud Secret Manager
description: Google Cloud Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. It provides a central place to manage, access, and audit secrets across Google Cloud with automatic versioning, IAM-based access control, and audit logging.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-secret-manager/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Configuration
  - Credentials
  - Google Cloud
  - Key Management
  - Secrets
  - Security
apis:
  - name: Google Cloud Secret Manager API
    description: The Secret Manager API enables creating, managing, and accessing secrets and their versions, providing secure storage for sensitive configuration data and credentials.
    humanURL: https://cloud.google.com/secret-manager
    baseURL: https://secretmanager.googleapis.com
    tags:
      - Configuration
      - Secrets
      - Security
      - Versions
    properties:
      - type: Documentation
        url: https://cloud.google.com/secret-manager/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/secret-manager/docs/quickstart
      - type: JSONSchema
        url: json-schema/secret.json
      - type: JSONLDContext
        url: json-ld/context.jsonld
common:
  - type: Portal
    url: https://cloud.google.com/secret-manager
  - type: Getting Started
    url: https://cloud.google.com/secret-manager/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/secret-manager/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/secret-manager/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/secret-manager/docs/support
  - type: JSONLDContext
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
