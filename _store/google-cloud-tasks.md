---
aid: google-cloud-tasks
name: Google Cloud Tasks
description: Google Cloud Tasks enables you to manage the execution of large numbers of distributed tasks. Cloud Tasks lets you create and dispatch tasks to worker services running on App Engine or any arbitrary HTTP endpoint, with automatic rate limiting, retry logic, and task deduplication. It provides a fully managed service for asynchronous task execution, allowing you to offload work from your main application and process it reliably in the background.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-tasks/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Asynchronous
  - Background Jobs
  - Distributed Systems
  - Google Cloud
  - Queues
  - Tasks
apis:
  - name: Google Cloud Tasks API
    description: The Cloud Tasks API allows you to create and manage task queues, enqueue tasks for asynchronous processing, and configure retry and rate limiting policies. Tasks can target App Engine handlers or any HTTP endpoint.
    humanURL: https://cloud.google.com/tasks/docs
    baseURL: https://cloudtasks.googleapis.com
    tags:
      - Asynchronous Processing
      - Queues
      - Tasks
    properties:
      - type: Documentation
        url: https://cloud.google.com/tasks/docs/reference/rest
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: Authentication
        url: https://cloud.google.com/docs/authentication
      - type: Getting Started
        url: https://cloud.google.com/tasks/docs/quickstart
      - type: JSONSchema
        url: json-schema/json-schema.yml
common:
  - type: Portal
    url: https://cloud.google.com/tasks
  - type: Getting Started
    url: https://cloud.google.com/tasks/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/tasks/docs
  - type: Authentication
    url: https://cloud.google.com/docs/authentication
  - type: Pricing
    url: https://cloud.google.com/tasks/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/tasks/docs/support
  - type: JSONLD
    url: json-ld/json-ld.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
