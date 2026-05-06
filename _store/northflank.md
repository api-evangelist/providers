---
aid: northflank
name: Northflank
description: Northflank is an internal developer platform providing self-service deployment, scaling, and management of applications, databases, and jobs across cloud providers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Deployment
  - Developer Experience
  - Internal Developer Platform
  - Platform Engineering
url: https://raw.githubusercontent.com/api-evangelist/northflank/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: northflank:northflank-api
    name: Northflank API
    description: The Northflank REST API provides programmatic access to manage projects, services, jobs, addons, workflows, pipelines, volumes, secrets, cloud providers, domains, integrations, load balancers, teams, and organizations on the Northflank platform.
    humanURL: https://northflank.com
    baseURL: https://api.northflank.com/v1
    tags:
      - Cloud Deployment
      - Developer Experience
      - Internal Developer Platform
    properties:
      - type: Documentation
        url: https://northflank.com/docs/v1/api/
      - type: Getting Started
        url: https://northflank.com/docs/getting-started
      - type: Authentication
        url: https://northflank.com/docs/v1/api/getting-started/authentication
common:
  - type: Website
    url: https://northflank.com
  - type: Documentation
    url: https://northflank.com/docs
  - type: API Documentation
    url: https://northflank.com/docs/v1/api/
  - type: GitHub Organization
    url: https://github.com/northflank
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
