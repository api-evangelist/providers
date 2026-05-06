---
aid: render
name: Render
description: Render is a cloud platform for building and running applications and websites with automatic Git-based deployments. It provides managed infrastructure for web services, static sites, background workers, cron jobs, private services, PostgreSQL databases, Redis/Key-Value stores, and persistent disks. The Render API enables programmatic control of all platform resources including service deployments, scaling, environment configuration, custom domains, blueprints, logging, metrics, and workflow automation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud
  - Platform
  - Deployment
  - Infrastructure
  - DevOps
  - Web Services
  - Databases
  - Hosting
url: https://raw.githubusercontent.com/api-evangelist/render/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: render:render-api
    name: Render API
    description: The Render Public API enables full programmatic management of Render services, databases, and infrastructure. It supports deploying web services, static sites, background workers, cron jobs, and private services; managing PostgreSQL and Key-Value databases; configuring environment variables, secret files, custom domains, and blueprints; scaling and autoscaling services; streaming logs and metrics; and orchestrating multi-service workflows. Authentication uses a Bearer API key from the Render Dashboard.
    humanURL: https://render.com/docs/api
    baseURL: https://api.render.com/v1
    tags:
      - Cloud
      - Platform
      - Deployment
      - Infrastructure
      - DevOps
    properties:
      - type: Documentation
        url: https://render.com/docs/api
      - type: OpenAPI
        url: openapi/render-openapi.json
      - type: OpenAPISpec
        url: https://api-docs.render.com/v1.0/openapi/render-public-api-1.json
      - type: ReferenceDocumentation
        url: https://api-docs.render.com
      - type: Rules
        url: rules/render-rules.yml
      - type: Capabilities
        url: capabilities/service-deployment.yaml
      - type: JSONSchema
        url: json-schema/render-service-schema.json
      - type: JSONSchema
        url: json-schema/render-deploy-schema.json
      - type: JSONStructure
        url: json-structure/render-service-structure.json
      - type: JSONLD
        url: json-ld/render-context.jsonld
      - type: Example
        url: examples/render-create-service-example.json
      - type: Example
        url: examples/render-trigger-deploy-example.json
      - type: Vocabulary
        url: vocabulary/render-vocabulary.yml
common:
  - url: https://render.com
    name: Render
    type: Website
    description: Render cloud platform homepage
  - url: https://render.com/docs
    name: Render Documentation
    type: Documentation
    description: Full documentation for Render services and platform features
  - url: https://render.com/docs/api
    name: Render API Documentation
    type: Documentation
    description: REST API reference for managing Render services programmatically
  - url: https://dashboard.render.com
    name: Render Dashboard
    type: Portal
    description: Web dashboard for managing Render services and API keys
  - url: https://community.render.com
    name: Render Community
    type: Forum
    description: Community forum for Render users and developers
  - url: https://render.com/pricing
    name: Render Pricing
    type: Pricing
    description: Pricing plans for Render services
  - url: https://status.render.com
    name: Render Status
    type: Status
    description: Real-time status page for Render services
  - url: https://github.com/renderinc
    name: Render GitHub
    type: GitHubOrganization
    description: Render open-source projects and tools
  - url: https://render.com/blog
    name: Render Blog
    type: Blog
    description: Engineering blog and product announcements
  - type: Features
    data:
      - 'Free instance: 512 MB RAM, 0.1 vCPU, auto-sleep'
      - 'Starter $7/mo: 512 MB, 0.5 vCPU, always-on'
      - 'Standard $25/mo: 2 GB, 1 vCPU'
      - 'Pro $85/mo: 4 GB, 2 vCPU'
      - 'Pro Plus $175/mo: 8 GB, 4 vCPU'
      - 'Pro Max $225/mo: 16 GB, 4 vCPU'
      - 'Pro Ultra $450/mo: 32 GB, 8 vCPU'
      - 'Professional Workspace: $19/user/mo for team collaboration'
      - Per-second billing prorated
      - Web Services, Background Workers, Cron Jobs, Static Sites
      - Managed Postgres and Redis Key Value Store
      - Private Services for internal-only
      - REST API at api.render.com
      - Default 400 req/min rate limit
      - Bearer token auth (per-user API tokens)
      - GitHub/GitLab/Bitbucket auto-deploy
    sources:
      - https://render.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
