---
aid: google-cloud-artifact-registry
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-artifact-registry/refs/heads/main/apis.yml
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
name: Google Cloud Artifact Registry
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
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Artifact Registry is a centralized repository for storing and managing container images, language packages, and build dependencies. It supports Docker, Maven, npm, Python, Go, Helm, and OS packages with integrated vulnerability scanning, IAM-based access control, and VPC Service Controls for supply chain security.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

