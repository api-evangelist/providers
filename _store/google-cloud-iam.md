---
aid: google-cloud-iam
name: Google Cloud IAM
description: Google Cloud Identity and Access Management (IAM) enables fine-grained access control and visibility for managing cloud resources. It provides the ability to create and manage service accounts, roles, and permissions to enforce least-privilege security policies across Google Cloud resources.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-iam/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Access Management
  - Google Cloud
  - IAM
  - Identity
  - Permissions
  - Security
apis:
  - name: Google Cloud IAM API
    description: The Cloud IAM API enables management of identity and access control policies, service accounts, roles, and permissions for Google Cloud resources.
    humanURL: https://cloud.google.com/iam
    baseURL: https://iam.googleapis.com
    tags:
      - IAM
      - Permissions
      - Roles
      - Service Accounts
    properties:
      - type: Documentation
        url: https://cloud.google.com/iam/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/iam/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/iam/docs/quickstarts
      - type: JSONSchema
        url: json-schema/service-account.json
      - type: JSONLDContext
        url: json-ld/context.jsonld
common:
  - type: Portal
    url: https://cloud.google.com/iam
  - type: Getting Started
    url: https://cloud.google.com/iam/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/iam/docs
  - type: Authentication
    url: https://cloud.google.com/iam/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/iam/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/iam/docs/support
  - type: JSONLDContext
    url: json-ld/context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
