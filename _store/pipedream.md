---
aid: pipedream
name: Pipedream
segments:
  - ProCode_API_Composition
  - Workflows
description: Pipedream is a developer-centric integration platform allowing custom code and API connections embedded directly into production workflows. Trusted by over one million developers, Pipedream provides 3,000+ integrations, pre-built actions, and support for Node.js, Python, Golang, and Bash, enabling teams to connect APIs, AI, databases, and more.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - ProCode_API_Composition
  - Workflows
created: '2026-03-03'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/pipedream/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: pipedream:rest-api
    name: Pipedream REST API
    description: The Pipedream REST API allows developers to programmatically create and manage workflows, event sources, subscriptions, and user resources. The API supports Bearer token authentication via OAuth access tokens or user API keys, pagination with cursors, and filtering with include and exclude parameters.
    humanURL: https://pipedream.com/docs/rest-api/
    baseURL: https://api.pipedream.com/v1
    tags:
      - Automation
      - Event Sources
      - Subscriptions
      - Workflows
    properties:
      - type: Documentation
        url: https://pipedream.com/docs/rest-api/
      - type: Authentication
        url: https://pipedream.com/docs/rest-api/auth
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pipedream/refs/heads/master/openapi/pipedream-openapi.yml
  - aid: pipedream:connect-api
    name: Pipedream Connect API
    description: The Pipedream Connect API is the end-to-end developer toolkit for adding customer-facing integrations to applications and AI agents. It provides managed authentication for 3,000+ APIs, pre-built components and triggers, a Connect proxy for custom API requests, and usage tracking. Resources are scoped to projects and the API supports production and development environments.
    humanURL: https://pipedream.com/docs/connect
    baseURL: https://api.pipedream.com/v1/connect
    tags:
      - AI Agents
      - Connect
      - Integrations
      - Managed Auth
    properties:
      - type: Documentation
        url: https://pipedream.com/docs/connect/api-ref
      - type: GettingStarted
        url: https://pipedream.com/docs/connect/quickstart
      - type: SDKs
        url: https://pipedream.com/docs/connect/api-reference/sdks
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/pipedream/refs/heads/master/openapi/pipedream-openapi.yml
common:
  - type: Portal
    url: https://pipedream.com/
    name: Pipedream Platform
    description: 'null'
  - type: Documentation
    url: https://pipedream.com/docs
    name: Pipedream Documentation
    description: 'null'
  - type: GettingStarted
    url: https://pipedream.com/docs/quickstart/
    name: Workflow Development Quickstart
    description: 'null'
  - type: Authentication
    url: https://pipedream.com/docs/rest-api/auth
    name: API Authentication
    description: 'null'
  - type: Blog
    url: https://pipedream.com/blog/
    name: Pipedream Blog
    description: 'null'
  - type: Changelog
    url: https://pipedream.com/docs/changelog
    name: Product Changelog
    description: 'null'
  - type: Status
    url: https://status.pipedream.com/
    name: Pipedream Status
    description: 'null'
  - type: Support
    url: https://pipedream.com/support
    name: Pipedream Support
    description: 'null'
  - type: Forum
    url: https://pipedream.com/community/
    name: Pipedream Community Forum
    description: 'null'
  - type: Pricing
    url: https://pipedream.com/pricing/
    name: Pipedream Pricing
    description: 'null'
  - type: SignUp
    url: https://pipedream.com/auth/signup
    name: Sign Up
    description: 'null'
  - type: Login
    url: https://pipedream.com/auth/login
    name: Log In
    description: 'null'
  - type: TermsOfService
    url: https://pipedream.com/terms
    name: Terms of Service
    description: 'null'
  - type: PrivacyPolicy
    url: https://pipedream.com/privacy
    name: Privacy Statement
    description: 'null'
  - type: Security
    url: https://pipedream.com/docs/privacy-and-security
    name: Privacy and Security
    description: 'null'
  - type: GitHubOrg
    url: https://github.com/PipedreamHQ/pipedream
    name: Pipedream GitHub Repository
    description: 'null'
  - type: Features
    data:
      - 'Free: 100 credits/day (1 credit = 30 sec compute @ 256 MB)'
      - 'Basic $29/mo: 2,000 credits/day, 30-day event history'
      - 'Advanced $79/mo: 10,000 credits/day, 1-year history, custom domains'
      - 'Business custom: unlimited credits, SSO/SAML, audit logs'
      - 2,500+ pre-built integrations
      - Code-level workflow editor (Node.js, Python, Go)
      - HTTP source endpoints (5 MB event size)
      - Schedule (cron) sources
      - Webhook destinations
      - 'Connect: embeddable user-auth flow'
      - OAuth 2.0 for 200+ services pre-handled
      - 'REST API: 60 req/min/user'
      - 'HTTP source: 100 req/sec/endpoint'
      - Workflow concurrency varies by plan
      - Step caching for memoization
      - Open-source workflow components
    sources:
      - https://pipedream.com/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
