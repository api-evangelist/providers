---
aid: google-cloud-scheduler
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-scheduler/refs/heads/main/apis.yml
apis:
- name: Google Cloud Scheduler API
  description: The Cloud Scheduler API allows you to create, configure, and manage scheduled jobs that execute on a recurring basis. Jobs can target HTTP endpoints, Pub/Sub topics, or App Engine applications with configurable retry policies and scheduling intervals.
  humanURL: https://cloud.google.com/scheduler/docs
  baseURL: https://cloudscheduler.googleapis.com
  properties:
  - type: OpenAPI
    url: openapi/openapi.yml
  - type: JSONSchema
    url: json-schema/json-schema.yml
  tags:
  - Automation
  - Cron Jobs
  - Scheduler
name: Google Cloud Scheduler
tags:
- Automation
- Cron
- Google Cloud
- Jobs
- Scheduler
- Scheduling
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It allows you to schedule virtually any job, including batch, big data jobs, cloud infrastructure operations, and more. Cloud Scheduler reliably sends requests to HTTP endpoints, Pub/Sub topics, or App Engine applications on a recurring schedule, with automatic retries in case of failure and configurable retry policies.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

