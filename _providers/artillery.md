---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'Artillery Cloud provides a hosted platform for running distributed load tests at scale, storing test results, team collaboration, and integrating with CI/CD pipelines. The Artillery Cloud API enables '
  name: Artillery Cloud API
  slug: artillery-cloud-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artillery-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.artillery.io/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/artillery-io
- group: start
  title: Artillery Website
  type: Portal
  url: https://www.artillery.io/
- group: docs
  title: Documentation
  type: Documentation
  url: https://www.artillery.io/docs
- group: build
  title: Artillery GitHub Organization
  type: GitHubOrganization
  url: https://github.com/artilleryio
- group: build
  title: Artillery Source Repository
  type: GitHubRepository
  url: https://github.com/artilleryio/artillery
- group: operate
  title: Changelog
  type: ReleaseNotes
  url: https://github.com/artilleryio/artillery/blob/main/CHANGELOG.md
- group: commercial
  title: Pricing
  type: Pricing
  url: https://www.artillery.io/pricing
created: '2026-03-25'
description: Artillery is an open source load testing and performance testing platform for APIs, microservices, and web applications. Built with Node.js and available as an npm package, Artillery supports HTTP/1, HTTP/2, WebSocket, Socket.IO, gRPC, and custom protocols through plugins. It includes a YAML-based test scenario definition language, a plugin ecosystem for extending functionality, and Artillery Cloud for distributed load testing, CI/CD integration, and centralized reporting. Artillery is used by developers, QA engineers, and SREs to run load tests, performance benchmarks, Playwright-based synthetic monitoring, and end-to-end tests at scale. The project is licensed under MPL-2.0 and maintained by Artilleryio.
features:
- description: Load test HTTP/1 and HTTP/2 REST APIs, GraphQL endpoints, and web applications with configurable virtual users, arrival rates, and scenario definitions.
  name: HTTP Load Testing
- description: Test real-time applications with WebSocket and Socket.IO protocol support, enabling load testing of chat, notifications, and streaming applications.
  name: WebSocket and Socket.IO Testing
- description: Run Playwright browser-based end-to-end scenarios under load, enabling realistic user simulation and synthetic monitoring from the same test framework.
  name: Playwright Integration
- description: Extensible plugin system with official plugins for gRPC, Kafka, AWS Lambda, Kinesis, and community plugins for many other protocols.
  name: Plugin Ecosystem
- description: Hosted cloud platform for running distributed load tests at massive scale across multiple cloud regions, with centralized results and team collaboration features.
  name: Artillery Cloud
- description: Human-readable YAML test scenario definitions supporting think time, loops, conditional logic, data CSV files, and custom JavaScript functions.
  name: YAML Test Scenarios
finops:
- name: Artillery Finops
  service_category: API
  slug: artillery-finops
graphqls:
- description: ''
  name: Artillery GraphQL API
  slug: artillery-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/artillery.png
integrations:
- description: Official Artillery GitHub Action for running load tests in CI/CD pipelines with automatic reporting and performance gate enforcement.
  name: GitHub Actions
- description: Artillery publishes metrics to Datadog for real-time monitoring and alerting during load test runs.
  name: Datadog
- description: Artillery can run distributed load tests using AWS Lambda as the execution backend, enabling serverless-scale testing.
  name: AWS Lambda
- description: Native Playwright integration for browser-based load testing and synthetic monitoring scenarios.
  name: Playwright
layout: provider
modified: '2026-04-19'
name: Artillery
nav: Providers
network: true
overview: 'Artillery publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Load Testing, Performance Testing, Open Source, Testing, and DevOps.


  Artillery''s developer surface includes engineering blog, developer portal, documentation, release notes, pricing, and 4 more developer resources.'
plans:
- name: Artillery Plans Pricing
  plan_count: 3
  slug: artillery-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Artillery Rate Limits
  slug: artillery-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artillery/refs/heads/main/screenshots/artillery-2026-06-20T172444.png
security:
- kind: domain-security
  name: Artillery Domain Security
  slug: artillery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: artillery
tags:
- Load Testing
- Performance Testing
- Open Source
- Testing
- DevOps
- Node.js
use_cases:
- description: Backend developers and QA engineers run load tests against REST and GraphQL APIs to identify performance bottlenecks and ensure stability under expected traffic volumes.
  name: API Load Testing
- description: Engineering teams integrate Artillery into CI/CD pipelines to run performance tests on every pull request, failing builds that exceed latency or error rate thresholds.
  name: CI/CD Performance Gates
- description: SREs use Artillery with Playwright to run synthetic monitors that continuously validate critical user journeys from multiple cloud regions.
  name: Synthetic Monitoring
- description: Product teams run stress tests before major launches or sales events to identify the maximum capacity of their infrastructure.
  name: Pre-Launch Stress Testing
website: https://www.artillery.io/
---
