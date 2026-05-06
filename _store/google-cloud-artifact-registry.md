---
aid: google-cloud-artifact-registry
name: Google Cloud Artifact Registry
description: Google Cloud Artifact Registry is a centralized repository for storing and managing container images, language packages, and build dependencies. It supports Docker, Maven, npm, Python, Go, Helm, and OS packages with integrated vulnerability scanning, IAM-based access control, and VPC Service Controls for supply chain security.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-artifact-registry/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Artifacts
  - Containers
  - Docker
  - Google Cloud
  - Packages
  - Registries
  - Repositories
  - Security
  - Supply Chain
apis:
  - name: Google Cloud Artifact Registry API
    description: The Artifact Registry API provides programmatic access to create and manage repositories, upload and download artifacts, manage packages and versions, and configure IAM policies for artifact storage across multiple formats including Docker images, language packages, and OS packages.
    humanURL: https://cloud.google.com/artifact-registry/docs
    baseURL: https://artifactregistry.googleapis.com
    properties:
      - type: Documentation
        url: https://cloud.google.com/artifact-registry/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/artifact-registry/docs/access-control
      - type: Getting Started
        url: https://cloud.google.com/artifact-registry/docs/quickstarts
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLDContext
        url: json-ld/json-ld.yml
common:
  - type: Portal
    url: https://cloud.google.com/artifact-registry
  - type: Getting Started
    url: https://cloud.google.com/artifact-registry/docs/quickstarts
  - type: Documentation
    url: https://cloud.google.com/artifact-registry/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/artifact-registry/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/artifact-registry/docs/support
  - type: JSONLDContext
    url: json-ld/json-ld.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
