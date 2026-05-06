---
aid: encore
name: Encore
description: Encore is an open source development platform for building type-safe, production-ready backend applications and distributed systems. It supports Go and TypeScript, provides built-in infrastructure automation for databases, caches, pub/sub, and cron jobs, and includes a local development dashboard with automatic API documentation, distributed tracing, and OpenAPI client generation.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Backend
  - Cloud Native
  - Frameworks
  - Go
  - Infrastructure Automation
  - Microservices
  - Open Source
  - TypeScript
url: https://raw.githubusercontent.com/api-evangelist/encore/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: encore:encore-application-config
    name: Encore Application Configuration
    description: The encore.app configuration file is the canonical declaration of an Encore application, including its platform application ID, primary language, global CORS rules, and authenticator settings. The JSONSchema captures the supported fields and is used to validate encore.app files in editors and CI pipelines.
    humanURL: https://encore.dev/docs/ts/develop/app-config
    tags:
      - Application Configuration
      - Encore App
      - JSON Schema
    properties:
      - type: Documentation
        url: https://encore.dev/docs/ts/develop/app-config
      - type: JSONSchema
        url: json-schema/encore-app-configuration.json
  - aid: encore:encore-cli
    name: Encore CLI
    description: The Encore CLI provides commands for creating, running, building, testing, deploying, and operating Encore applications. It also generates type-safe API clients in Go, TypeScript, JavaScript, and experimental OpenAPI from any Encore backend, targeting local, staging, and production environments on the Encore Cloud Platform.
    humanURL: https://encore.dev/docs/ts/cli/cli-reference
    tags:
      - CLI
      - Client Generation
      - Developer Tooling
    properties:
      - type: Documentation
        url: https://encore.dev/docs/ts/cli/cli-reference
      - type: Client Generation
        url: https://encore.dev/docs/ts/cli/client-generation
      - type: Install
        url: https://encore.dev/docs/ts/install
      - type: Source Code
        url: https://github.com/encoredev/encore
common:
  - type: Website
    url: https://encore.dev/
  - type: Documentation
    url: https://encore.dev/docs
  - type: Getting Started
    url: https://encore.dev/docs/ts/quick-start
  - type: GitHub Organization
    url: https://github.com/encoredev
  - type: GitHub Repository
    url: https://github.com/encoredev/encore
  - type: Blog
    url: https://encore.dev/blog
  - type: Pricing
    url: https://encore.dev/pricing
  - type: Discord
    url: https://encore.dev/discord
  - type: License
    url: https://github.com/encoredev/encore/blob/main/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
