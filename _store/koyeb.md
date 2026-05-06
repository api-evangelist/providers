---
aid: koyeb
name: Koyeb
description: Koyeb is a developer-friendly serverless platform for deploying apps globally. The Koyeb API allows you to interact with the Koyeb platform in a simple, programmatic way using conventional HTTP requests for managing apps, services, deployments, and secrets.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Platform
  - Deployment
  - PaaS
  - Serverless
created: '2025-01-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/koyeb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: koyeb:koyeb-api
    name: Koyeb API
    description: The Koyeb API provides programmatic access to manage apps, services, deployments, secrets, domains, regions, organizations and billing on the Koyeb serverless platform.
    humanURL: https://www.koyeb.com/docs/api
    baseURL: https://app.koyeb.com
    tags:
      - Deployment
      - Serverless
    properties:
      - type: Documentation
        url: https://www.koyeb.com/docs/api
      - type: Reference
        url: https://www.koyeb.com/docs/reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/koyeb/refs/heads/main/openapi/koyeb-openapi.json
common:
  - type: Website
    url: https://www.koyeb.com
  - type: Documentation
    url: https://www.koyeb.com/docs
  - type: Getting Started
    url: https://www.koyeb.com/docs/deploy
  - type: Sign Up
    url: https://app.koyeb.com/auth/signup
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
