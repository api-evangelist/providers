---
aid: circlecis
url: https://raw.githubusercontent.com/api-evangelist/circlecis/refs/heads/main/apis.yml
name: CircleCI
tags:
  - CI/CD
  - Continuous Deployment
  - Continuous Integration
  - DevOps
  - Pipelines
  - Workflows
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-23'
position: Consumer
description: CircleCI is a continuous integration and delivery platform that automates software building, testing, and deployment. This repository is an alias of the primary `circleci` index and is preserved so historical references and links continue to resolve. The full set of REST, runner, webhook, and orbs APIs is profiled in the `circleci` repository at https://github.com/api-evangelist/circleci.
apis:
  - aid: circlecis:rest-api-v2
    name: CircleCI REST API V2
    tags:
      - CI/CD
      - Pipelines
      - Workflows
    humanURL: https://circleci.com/docs/api/v2/
    properties:
      - url: https://circleci.com/docs/api/v2/
        type: Documentation
    description: The CircleCI REST API v2 provides programmatic access for managing pipelines, projects, workflows, jobs, contexts, and users.
  - aid: circlecis:runner-api
    name: CircleCI Self-Hosted Runner API
    tags:
      - CI/CD
      - Runners
      - Self-Hosted
    humanURL: https://circleci.com/docs/runner-api/
    properties:
      - url: https://circleci.com/docs/runner-api/
        type: Documentation
    description: The CircleCI Runner API is used for the management and execution of self-hosted runner jobs.
  - aid: circlecis:webhooks
    name: CircleCI Webhooks
    tags:
      - CI/CD
      - Events
      - Webhooks
    humanURL: https://circleci.com/docs/webhooks/
    properties:
      - url: https://circleci.com/docs/webhooks/
        type: Documentation
    description: Real-time event notifications for pipeline, workflow, and job lifecycle events delivered via HTTP callbacks.
common:
  - type: Website
    url: https://circleci.com/
  - type: Portal
    url: https://circleci.com/developer
  - type: Documentation
    url: https://circleci.com/docs/
  - type: Canonical Profile
    url: https://github.com/api-evangelist/circleci
  - type: Privacy Policy
    url: https://circleci.com/privacy/
  - type: Terms of Service
    url: https://circleci.com/terms-of-service/
  - type: Support
    url: https://support.circleci.com/
  - type: Status
    url: https://status.circleci.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
