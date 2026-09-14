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
api_count: 1
apis:
- description: 'Artillery Cloud is the hosted platform behind the open source Artillery CLI: it runs distributed load and Playwright E2E tests at scale across AWS Lambda, AWS Fargate and Azure ACI, stores and retains'
  name: Artillery Cloud API
  slug: artillery-cloud-api
artifact_total: 22
common:
- group: company
  title: ''
  type: Website
  url: https://www.artillery.io/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/artilleryio/artillery/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/artilleryio/artillery/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/artilleryio/artillery/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/artilleryio/artillery/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/artilleryio/artillery/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/artilleryio/artillery/blob/main/LICENSE.txt
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
  type: ChangeLog
  url: https://www.artillery.io/changelog
- group: commercial
  title: Pricing
  type: Pricing
  url: https://www.artillery.io/pricing
- group: docs
  title: Artillery CLI Reference
  type: APIReference
  url: https://www.artillery.io/docs/reference/cli
- group: start
  title: Run Your First Artillery Test
  type: GettingStarted
  url: https://www.artillery.io/docs/get-started/first-test
- group: operate
  title: GitHub Discussions
  type: Support
  url: https://github.com/artilleryio/artillery/discussions
- group: start
  title: Sign in to Artillery Cloud
  type: SignUp
  url: https://app.artillery.io/login
- group: commercial
  title: Terms of Service
  type: TermsOfService
  url: https://www.artillery.io/terms/tos
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://www.artillery.io/terms/privacy
- group: auth
  title: Security Policy
  type: Security
  url: https://www.artillery.io/terms/security
- group: operate
  title: Artillery Status
  type: StatusPage
  url: https://artilleryio.statuspage.datadoghq.com/
- group: operate
  title: Supported Versions Policy
  type: Deprecation
  url: https://github.com/artilleryio/artillery/blob/main/SECURITY.md
- group: build
  title: First-party packages
  type: Packages
  url: packages/artillery-packages.yml
- group: build
  title: Artillery client libraries
  type: SDKs
  url: packages/artillery-packages.yml
- group: build
  title: Artillery CLI surface
  type: CLI
  url: cli/artillery-cli.yml
- group: agent
  title: llms.txt
  type: LLMsTxt
  url: llms/artillery-llms.txt
- group: agent
  title: Artillery official agent skills
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: Authentication profile
  type: Authentication
  url: authentication/artillery-authentication.yml
- group: design
  title: API conventions and reversibility
  type: Conventions
  url: conventions/artillery-conventions.yml
- group: design
  title: Lifecycle, versioning and support policy
  type: Lifecycle
  url: lifecycle/artillery-lifecycle.yml
- group: operate
  title: Structured changelog
  type: ChangeLog
  url: changelog/artillery-changelog.yml
- group: design
  title: Standards conformance
  type: Conformance
  url: conformance/artillery-conformance.yml
- group: auth
  title: Vulnerability disclosure
  type: VulnerabilityDisclosure
  url: security/artillery-vulnerability-disclosure.yml
- group: auth
  title: Security posture
  type: TrustCenter
  url: security/artillery-trust-center.yml
- group: commercial
  title: Plans and pricing
  type: Plans
  url: plans/artillery-plans-pricing.yml
- group: operate
  title: Published usage limits
  type: RateLimits
  url: rate-limits/artillery-rate-limits.yml
- group: commercial
  title: FinOps profile
  type: FinOps
  url: finops/artillery-finops.yml
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
modified: '2026-09-07'
name: Artillery
nav: Providers
network: true
overview: 'Artillery publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Load Testing, Performance Testing, Open-Source, Testing, and DevOps.


  Artillery''s developer surface includes engineering blog, developer portal, documentation, changelog, pricing, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Artillery Plans Pricing
  plan_count: 4
  slug: artillery-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 12
  name: Artillery Rate Limits
  slug: artillery-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/artillery/refs/heads/main/screenshots/artillery-2026-06-20T172444.png
security:
- kind: authentication
  name: Artillery Authentication
  slug: artillery-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Artillery Domain Security
  slug: artillery-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Artillery Vulnerability Disclosure
  slug: artillery-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Artillery Trust Center
  slug: artillery-trust-center
  summary_line: trust center published
slug: artillery
tags:
- Load Testing
- Performance Testing
- Open-Source
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
