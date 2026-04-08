---
aid: google-cloud-workflows
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-workflows/refs/heads/main/apis.yml
apis:
- name: Google Cloud Workflows API
  description: The Workflows API allows you to create, update, delete, and execute workflows. Workflows orchestrate calls to HTTP-based APIs including Google Cloud services, and manage execution state, retries, and error handling automatically.
  humanURL: https://cloud.google.com/workflows/docs
  baseURL: https://workflows.googleapis.com
  tags:
  - Orchestration
  - Serverless
  - Workflows
  properties:
  - type: Documentation
    url: https://cloud.google.com/workflows/docs/reference/rest
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Getting Started
    url: https://cloud.google.com/workflows/docs/quickstarts
  - type: JSONSchema
    url: json-schema/json-schema.yml
name: Google Cloud Workflows
tags:
- Automation
- Google Cloud
- Integration
- Orchestration
- Serverless
- Workflows
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Workflows is a serverless orchestration service that lets you combine Google Cloud services and APIs into flexible, automated workflows. Workflows manages the order of execution, including handling retries, waiting, and polling, and ensures reliable execution despite hardware and networking interruptions. It supports conditional logic, subworkflows, and connectors to integrate with other Google Cloud products.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

