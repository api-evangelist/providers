---
aid: google-cloud-tasks
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-tasks/refs/heads/main/apis.yml
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
name: Google Cloud Tasks
tags:
- Asynchronous
- Background Jobs
- Distributed Systems
- Google Cloud
- Queues
- Tasks
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Tasks enables you to manage the execution of large numbers of distributed tasks. Cloud Tasks lets you create and dispatch tasks to worker services running on App Engine or any arbitrary HTTP endpoint, with automatic rate limiting, retry logic, and task deduplication. It provides a fully managed service for asynchronous task execution, allowing you to offload work from your main application and process it reliably in the background.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

