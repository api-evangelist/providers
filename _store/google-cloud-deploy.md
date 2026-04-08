---
aid: google-cloud-deploy
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-deploy/refs/heads/main/apis.yml
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
name: Google Cloud Deploy
tags:
- Continuous Delivery
- Deployment
- DevOps
- Kubernetes
- Pipeline
- Release Management
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Deploy is a managed continuous delivery service that automates the deployment of applications to Google Cloud target environments such as GKE, Cloud Run, and Anthos. It provides an opinionated delivery pipeline that promotes releases through a series of target environments with approval gates, rollback capabilities, and deployment verification, enabling safe and repeatable software delivery workflows.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

