---
aid: nango
name: Nango
description: Nango.dev is a developer infrastructure platform that simplifies building product integrations with external APIs. It provides the infrastructure to build reliable, scalable integrations fast, including API authentication, a syncing framework, webhook handling, and observability, supporting over 400 APIs with 600+ pre-built integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/nango/refs/heads/main/apis.yml
created: '2026-01-02'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - AI Agents
  - Integrations
  - OAuth
  - Syncing
  - Unified API
  - Webhooks
apis:
  - aid: nango:nango
    name: Nango
    tags:
      - Integrations
      - OAuth
      - Unified API
    humanURL: https://www.nango.dev/
    properties:
      - url: https://www.nango.dev/
        type: Documentation
      - url: https://nango.dev/docs/reference/api
        type: Reference
      - url: https://nango.dev/docs/getting-started/quickstart
        type: Getting Started
      - url: https://nango.dev/docs/guides/primitives/auth
        type: Authentication
      - url: https://nango.dev/docs/llms.txt
        type: LLMs.txt
    description: Nango provides a unified API platform for building product integrations with 600+ external APIs. It offers managed API authentication (OAuth and other auth methods), a syncing framework, proxy for API requests with automatic credential injection, webhook handling, and observability.
common:
  - url: https://nango.dev/docs
    type: Documentation
  - url: https://nango.dev/docs/getting-started/quickstart
    type: Getting Started
  - url: https://nango.dev/pricing
    type: Pricing
  - url: https://nango.dev/blog
    type: Blog
  - url: https://nango.dev/docs/updates
    type: Change Log
  - url: https://status.nango.dev/
    type: Status
  - url: https://app.nango.dev
    type: Portal
  - url: https://nango.dev/terms
    type: Terms of Service
  - url: https://nango.dev/privacy-policy
    type: Privacy Policy
  - url: https://github.com/NangoHQ/nango
    type: GitHub Repository
  - type: Features
    data:
      - 'Free: 10 connections, 100k proxy/runs/logs/storage/webhooks, 2 envs'
      - 'Starter from $50/mo: 20 connections, 200k usage, 3 envs'
      - 'Growth from $500/mo: 100 connections, 1M usage, 10 envs, priority support'
      - 'Enterprise custom: unlimited, SOC 2, RBAC, SAML SSO, HIPAA option'
      - Self-hosting available on Enterprise
      - 400+ pre-built API integrations
      - 'Auth: OAuth 2.0/1.0a, API Key, Basic, JWT, custom'
      - Proxy API for authenticated calls without token management
      - Sync engine for incremental data syncs
      - Actions for one-shot operations
      - Webhooks bridging external -> your app
      - Functions (TypeScript) for custom logic
      - Connect UI for embedded auth flows
      - Admin dashboard for connection health
      - Logs and metrics for each integration
      - Open-source core (MIT license)
    sources:
      - https://www.nango.dev/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
