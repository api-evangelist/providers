---
aid: google-cloud-container-registry
name: Google Cloud Container Registry
description: Google Cloud Container Registry is a private Docker image storage service on Google Cloud Platform. It provides secure, private Docker image storage with integration into Google Cloud CI/CD pipelines, vulnerability scanning, and access control. Note that Container Registry has been superseded by Artifact Registry as the recommended container registry for Google Cloud.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-container-registry/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - CI/CD
  - Containers
  - Docker
  - Google Cloud
  - Images
  - Registries
  - Storage
apis:
  - name: Google Cloud Container Registry API
    description: The Container Registry API provides access to store, manage, and secure Docker container images. It supports pushing and pulling images, managing image tags, and integrating with vulnerability scanning and binary authorization services.
    humanURL: https://cloud.google.com/container-registry/docs
    baseURL: https://containerregistry.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/container-registry/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/container-registry/docs/access-control
      - type: Getting Started
        url: https://cloud.google.com/container-registry/docs/quickstart
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://cloud.google.com/container-registry
  - type: Getting Started
    url: https://cloud.google.com/container-registry/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/container-registry/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/container-registry/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/container-registry/docs/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
