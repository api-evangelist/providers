---
aid: google-cloud-secret-manager
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-secret-manager/refs/heads/main/apis.yml
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
name: Google Cloud Secret Manager
tags:
- Configuration
- Credentials
- Google Cloud
- Key Management
- Secrets
- Security
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. It provides a central place to manage, access, and audit secrets across Google Cloud with automatic versioning, IAM-based access control, and audit logging.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

