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
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 18.3
  scored_at: '2026-07-27'
api_count: 2
apis:
- description: The encore.app configuration file is the canonical declaration of an Encore application, including its platform application ID, primary language, global CORS rules, and authenticator settings. The JSO
  name: Encore Application Configuration
  slug: encore-application-config
- description: The Encore CLI provides commands for creating, running, building, testing, deploying, and operating Encore applications. It also generates type-safe API clients in Go, TypeScript, JavaScript, and expe
  name: Encore CLI
  slug: encore-cli
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/encore-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encore-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/encore
- group: company
  title: ''
  type: Website
  url: https://encore.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://encore.dev/docs/ts/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/encoredev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/encoredev/encore
- group: company
  title: ''
  type: Blog
  url: https://encore.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://encore.dev/pricing
- group: operate
  title: ''
  type: Discord
  url: https://encore.dev/discord
- group: commercial
  title: ''
  type: License
  url: https://github.com/encoredev/encore/blob/main/LICENSE
- group: agent
  title: ''
  type: MCPServer
  url: https://encore.dev/blog/mcp-server
- group: agent
  title: ''
  type: LlmsText
  url: https://encore.dev/llms.txt
created: '2026-03-26'
description: Encore is an open source development platform for building type-safe, production-ready backend applications and distributed systems. It supports Go and TypeScript, provides built-in infrastructure automation for databases, caches, pub/sub, and cron jobs, and includes a local development dashboard with automatic API documentation, distributed tracing, and OpenAPI client generation.
finops:
- name: Encore Finops
  service_category: API
  slug: encore-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/encore.png
json_schemas:
- name: Encore App Configuration
  property_count: 6
  slug: encore-app-configuration
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Encore
nav: Providers
network: true
overview: 'Encore publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Backend, Cloud Native, Frameworks, Go, and Infrastructure Automation.


  The Encore catalog on APIs.io includes 1 Spectral governance ruleset.


  Encore''s developer surface includes documentation, getting-started guide, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Encore Plans Pricing
  plan_count: 3
  slug: encore-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Encore Rate Limits
  slug: encore-rate-limits
rules:
- name: Encore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: encore-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 11.3
    developer_ergonomics: 30.4
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 40.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/encore/refs/heads/main/screenshots/encore-2026-06-20T180722.png
security:
- kind: domain-security
  name: Encore Domain Security
  slug: encore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encore Vulnerability Disclosure
  slug: encore-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: encore
tags:
- Backend
- Cloud Native
- Frameworks
- Go
- Infrastructure Automation
- Microservices
- Open Source
- TypeScript
website: https://encore.dev/
---
