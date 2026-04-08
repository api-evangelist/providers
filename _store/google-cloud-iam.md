---
aid: google-cloud-iam
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-iam/refs/heads/main/apis.yml
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
name: Google Cloud IAM
tags:
- Access Management
- Google Cloud
- IAM
- Identity
- Permissions
- Security
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Identity and Access Management (IAM) enables fine-grained access control and visibility for managing cloud resources. It provides the ability to create and manage service accounts, roles, and permissions to enforce least-privilege security policies across Google Cloud resources.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

