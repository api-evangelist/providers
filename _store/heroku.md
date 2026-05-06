---
aid: heroku
name: Heroku
description: Heroku is a cloud platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud. The Heroku Platform API enables programmatic access to Heroku's features for app deployment, scaling, and management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Deployment
  - Cloud Platform
  - DevOps
  - PaaS
url: https://raw.githubusercontent.com/api-evangelist/heroku/refs/heads/main/apis.yml
created: '2025-02-08'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: heroku:heroku-platform-api
    name: Heroku Platform API
    description: The Heroku Platform API enables programmatic access to Heroku's deployment platform, including apps, dynos, add-ons, pipelines, and other platform resources.
    humanURL: https://devcenter.heroku.com/articles/platform-api-reference
    baseURL: https://api.heroku.com
    tags:
      - Deployment
      - PaaS
      - REST
    properties:
      - type: Documentation
        url: https://devcenter.heroku.com/articles/platform-api-reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/heroku/refs/heads/main/openapi/heroku-platform-api.yml
      - type: Getting Started
        url: https://devcenter.heroku.com/articles/platform-api-quickstart
      - type: Authentication
        url: https://devcenter.heroku.com/articles/platform-api-reference#authentication
common:
  - type: Portal
    url: https://devcenter.heroku.com/
  - type: Website
    url: https://www.heroku.com/
  - type: Getting Started
    url: https://devcenter.heroku.com/start
  - type: Documentation
    url: https://devcenter.heroku.com/
  - type: Sign Up
    url: https://signup.heroku.com/
  - type: Login
    url: https://id.heroku.com/login
  - type: Status
    url: https://status.heroku.com/
  - type: Blog
    url: https://blog.heroku.com/
  - type: Support
    url: https://help.heroku.com/
  - type: Pricing
    url: https://www.heroku.com/pricing
  - type: GitHub Organization
    url: https://github.com/heroku
  - type: Terms of Service
    url: https://www.heroku.com/policy/tos
  - type: Privacy Policy
    url: https://www.heroku.com/policy/privacy
  - type: Features
    data:
      - 'Eco Dynos: $5/mo for 1,000 dyno-hours pool (sleeps when idle)'
      - 'Basic Dyno: $7/mo, never sleeps, 512 MB RAM'
      - 'Standard-1X: $25/mo, 512 MB RAM, horizontal scaling'
      - 'Standard-2X: $50/mo, 1 GB RAM'
      - 'Performance-M/L/XL/2XL: $250-$1,500/mo, dedicated infra'
      - 'Heroku Postgres Essential: $5-$9/mo (hobby)'
      - 'Heroku Postgres Standard: $50-$200/mo (production)'
      - 'Heroku Postgres Premium: $200-$350/mo (HA)'
      - 'Heroku Key-Value Store (Redis-compatible): $3-$120/mo'
      - 'Platform API: 4,500 req/hr/token rate limit'
      - Buildpacks for languages (Node, Ruby, Python, Java, Go, etc.)
      - Heroku Connect for Salesforce sync (separate)
      - Heroku Add-ons marketplace
      - Pipelines for staging→production promotion
      - Review apps for PR previews
      - Salesforce-owned with Salesforce integration
    sources:
      - https://www.heroku.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
