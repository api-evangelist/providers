---
aid: google-cloud-build
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-build/refs/heads/main/apis.yml
apis:
- name: Cloud Build API
  description: The Cloud Build API provides programmatic access to create, manage, and monitor builds on Google Cloud. Developers can use the API to trigger builds from source code, manage build triggers that automatically start builds when source code changes, view build logs and results, manage worker pools for custom build environments, and configure build connections to source repositories.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/build/docs
  baseURL: https://cloudbuild.googleapis.com
  tags:
  - Builds
  - Source Repositories
  - Triggers
  - Worker Pools
  properties:
  - type: Documentation
    url: https://cloud.google.com/build/docs/api/reference/rest
  - type: OpenAPI
    url: openapi/cloud-build-api-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/build/docs/api/reference/rest#authentication
  - type: JSONSchema
    url: json-schema/google-cloud-build-build-schema.json
name: Google Cloud Build
tags:
- Build Automation
- CI/CD
- Container Build
- Continuous Delivery
- Continuous Integration
- DevOps
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Build is a fully managed continuous integration and continuous delivery (CI/CD) platform that lets you build, test, and deploy software quickly across all languages and frameworks. It executes builds on Google Cloud infrastructure, supports building from source code repositories, creating container images, and deploying to various Google Cloud targets including GKE, Cloud Run, and App Engine.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

