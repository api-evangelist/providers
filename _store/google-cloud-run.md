---
aid: google-cloud-run
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-run/refs/heads/main/apis.yml
apis:
- name: Google Cloud Run Admin API
  description: The Cloud Run Admin API deploys and manages user-provided container images as serverless services. It allows you to create, update, and delete services and revisions, manage traffic routing between revisions, and configure domain mappings and IAM policies.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/run/docs
  baseURL: https://run.googleapis.com
  tags:
  - Containers
  - Serverless
  properties:
  - type: Documentation
    url: https://cloud.google.com/run/docs/reference/rest
  - type: OpenAPI
    url: openapi/google-cloud-run-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/run/docs/quickstarts
  - type: JSONSchema
    url: json-schema/google-cloud-run-service-schema.json
name: Google Cloud Run
tags:
- Cloud Run
- Containers
- Google Cloud
- Serverless
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Run is a fully managed serverless platform that enables you to run stateless containers that are invocable via HTTP requests. It abstracts away infrastructure management so you can focus on building applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

