---
aid: bump-sh
name: Bump.sh
description: Bump.sh is an API documentation and changelog platform that automatically generates beautiful, interactive documentation from OpenAPI and AsyncAPI specifications. It provides diff-based changelogs, API hubs, webhooks, and team collaboration features for API-first organizations.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Changelog
  - API Documentation
  - API Hub
  - AsyncAPI
  - CI/CD
  - OpenAPI
url: https://raw.githubusercontent.com/api-evangelist/bump-sh/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-21'
specificationVersion: '0.19'
apis:
  - aid: bump-sh:bump-sh-api
    name: Bump.sh API
    description: The Bump.sh REST API allows programmatic management of API documentation, deployments, and changelogs. Integrates with CI/CD pipelines to automatically publish OpenAPI and AsyncAPI spec changes as versioned documentation with visual diffs.
    humanURL: https://bump.sh
    baseURL: https://bump.sh/api/v1
    tags:
      - API Changelog
      - API Documentation
      - CI/CD
      - Deployments
      - OpenAPI
    properties:
      - type: Documentation
        url: https://docs.bump.sh
      - type: Getting Started
        url: https://docs.bump.sh/help/getting-started/
      - type: GitHub Repository
        url: https://github.com/bump-sh
      - type: OpenAPI
        url: https://developers.bump.sh/openapi.yaml
    x-features:
      - Automated documentation generation from OpenAPI/AsyncAPI specs
      - Diff-based API changelog with visual diffs
      - API hubs for multi-API organizations
      - Webhook notifications on spec changes
      - CI/CD pipeline integration
      - Team collaboration and access controls
      - Custom domains and branding
    x-use-cases:
      - Publish API documentation automatically on every commit
      - Generate API changelogs for consumers
      - Manage API portals for multiple APIs
      - Notify stakeholders of breaking changes
common:
  - type: Website
    url: https://bump.sh
  - type: Documentation
    url: https://docs.bump.sh
  - type: GitHub Organization
    url: https://github.com/bump-sh
  - type: Blog
    url: https://bump.sh/blog
  - type: Pricing
    url: https://bump.sh/pricing
  - type: Changelog
    url: https://bump.sh/changelog
  - type: Sign Up
    url: https://bump.sh/users/sign_up
  - type: Login
    url: https://bump.sh/users/sign_in
  - type: Status
    url: https://bumpsh.statuspage.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
