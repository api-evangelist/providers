---
aid: google-cloud-deploy
name: Google Cloud Deploy
description: Google Cloud Deploy is a managed continuous delivery service that automates the deployment of applications to Google Cloud target environments such as GKE, Cloud Run, and Anthos. It provides an opinionated delivery pipeline that promotes releases through a series of target environments with approval gates, rollback capabilities, and deployment verification, enabling safe and repeatable software delivery workflows.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-deploy/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Continuous Delivery
  - Deployment
  - DevOps
  - Kubernetes
  - Pipeline
  - Release Management
apis:
  - name: Cloud Deploy API
    description: The Cloud Deploy API provides programmatic access to manage delivery pipelines, targets, releases, and rollouts for continuous delivery workflows. Developers can use the API to create and manage delivery pipelines that define the progression of releases through target environments, create releases from build artifacts, promote releases between targets, approve rollouts, and manage rollback operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/deploy/docs
    baseURL: https://clouddeploy.googleapis.com
    tags:
      - Delivery Pipelines
      - Releases
      - Rollouts
      - Targets
    properties:
      - type: Documentation
        url: https://cloud.google.com/deploy/docs/api/reference/rest
      - type: OpenAPI
        url: openapi/cloud-deploy-api-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/deploy/docs/api/reference/rest#authentication
      - type: JSONSchema
        url: json-schema/google-cloud-deploy-release-schema.json
common:
  - type: Portal
    url: https://cloud.google.com/deploy
  - type: Getting Started
    url: https://cloud.google.com/deploy/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/deploy/docs
  - type: Authentication
    url: https://cloud.google.com/deploy/docs/api/reference/rest#authentication
  - type: Pricing
    url: https://cloud.google.com/deploy/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Console
    url: https://console.cloud.google.com/deploy
  - type: CLI
    url: https://cloud.google.com/sdk/gcloud/reference/deploy
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/deploy/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-deploy-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
