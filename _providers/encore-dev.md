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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Encore Dev Agentic Access
  operation_count: 10
  slug: encore-dev-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 6
apis:
- description: Encore's Infrastructure from Code API lets developers declare cloud infrastructure resources — PostgreSQL databases, Pub/Sub topics and subscriptions, object storage buckets, cron jobs, caches, and se
  name: Encore Infrastructure API
  slug: encore-infrastructure-api
- description: Encore captures distributed traces, structured logs, and runtime metrics automatically from every api(), database query, Pub/Sub publish, cron tick, and outbound HTTP call. The local Development Dashb
  name: Encore Observability API
  slug: encore-observability-api
- description: Encore ships a built-in Model Context Protocol server (`encore mcp start` for SSE, `encore mcp run` for stdio) that exposes the live Encore application — services, middleware, auth handlers, databases
  name: Encore MCP Server
  slug: encore-mcp-server
- description: The Apps API from Encore — 5 operation(s) for apps.
  name: Encore Apps API
  slug: encore-dev-apps-api
- description: The Encore API from Encore — 2 operation(s) for encore.
  name: Encore Encore API
  slug: encore-dev-encore-api
- description: The Encore Framework API API from Encore — 1 operation(s) for encore framework api.
  name: Encore Encore Framework API API
  slug: encore-dev-encore-framework-api-api
artifact_total: 48
collections:
- collection_type: postman
  name: Encore Framework Apps API
  slug: postman-encore-dev-apps-api
- collection_type: postman
  name: Framework Apps Encore API
  slug: postman-encore-dev-encore-api
- collection_type: postman
  name: Encore Framework Apps Encore Framework API API
  slug: postman-encore-dev-encore-framework-api-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Encore Framework Apps API
  slug: open-encore-dev-apps-api
- collection_type: open
  name: Framework Apps Encore API
  slug: open-encore-dev-encore-api
- collection_type: open
  name: Encore Framework Apps Encore Framework API API
  slug: open-encore-dev-encore-framework-api-api
- collection_type: open
  name: Encore Framework API
  slug: open-encore-framework
- collection_type: open
  name: Encore Cloud Platform API
  slug: open-encore-platform
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/encore/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/encore-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/encore-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/encore-dev-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/encoredev
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/encoredev/encore
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/encoredev/examples
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/encoredev/encore.dev
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/go
- group: start
  title: ''
  type: GettingStarted
  url: https://encore.dev/docs/ts/quick-start
- group: start
  title: ''
  type: GettingStarted
  url: https://encore.dev/docs/go/quick-start
- group: start
  title: ''
  type: Portal
  url: https://encore.cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://encore.cloud/pricing
- group: company
  title: ''
  type: Blog
  url: https://encore.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://encore.dev/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.encore.cloud
- group: operate
  title: ''
  type: Community
  url: https://encore.dev/discord
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/cli/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/ai-integration
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/observability/tracing
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/observability/dev-dash
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/primitives/databases
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/primitives/pubsub
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/primitives/cron-jobs
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/primitives/object-storage
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/primitives/secrets
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/develop/auth
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/develop/middleware
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/develop/streaming-apis
- group: build
  title: ''
  type: SDKs
  url: https://encore.dev/docs/ts/cli/cli-reference
- group: build
  title: ''
  type: SDKs
  url: https://encore.dev/docs/ts/develop/client-generation
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/docs/ts/develop/api-docs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/encoredev/homebrew-tap
- group: docs
  title: ''
  type: Documentation
  url: https://encore.dev/use-cases
- group: commercial
  title: ''
  type: Plans
  url: plans/encore-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/encore-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/encore-dev-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/encore-dev-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/encore-dev-rules.yml
created: '2026-05-24T00:00:00.000Z'
description: Encore is a backend application framework and developer cloud that lets engineering teams build type-safe distributed systems in TypeScript (Encore.ts) and Go (Encore.go) using declarative Infrastructure from Code. Developers describe APIs, databases, Pub/Sub, object storage, caches, cron jobs, and secrets as typed code primitives; the framework provisions matching infrastructure locally with no Docker Compose, and Encore Cloud provisions equivalent managed resources in the customer's own AWS or GCP account. The platform ships built-in distributed tracing, a local development dashboard, auto-generated API docs and client SDKs, a Model Context Protocol server for AI agents, preview environments per pull request, and CI/CD — positioning Encore as an opinionated alternative to PaaS and a productivity layer on top of hyperscaler infrastructure.
features:
- Encore.ts — TypeScript backend framework with zero npm dependencies, claimed 9x faster than Express.js and 3x faster than ElysiaJS and Hono via a Rust runtime
- Encore.go — Go backend framework with type-safe APIs declared via //encore:api annotations
- Infrastructure from Code (IfC) — declare PostgreSQL, Pub/Sub, object storage, caches, cron jobs, and secrets as typed code primitives
- Automatic local development environment with Docker-free database, Pub/Sub, and bucket provisioning
- Local Development Dashboard with distributed tracing, API explorer, service catalog, database explorer, and architecture flow diagrams
- Type-safe service-to-service calls with automatic service discovery and network plumbing
- Auto-generated client SDKs in TypeScript, Go, and JavaScript from the backend source
- Auto-generated API documentation and service catalog kept in sync with source
- Raw endpoints (api.raw) for webhooks and low-level HTTP, plus streaming endpoints for WebSockets
- Built-in authentication primitives and pluggable auth handlers (Clerk, Auth0, Firebase, Ory)
- Built-in middleware, request validation, and response shaping derived from TypeScript interfaces / Go structs
- Encore MCP Server exposing services, traces, metrics, source, and docs to AI agents
- '`encore run`, `encore build docker`, and `git push encore` for local, container, and managed deployments'
- Write-once / deploy-anywhere — same code runs locally, on AWS, on GCP, or self-hosted via Docker export
- Encore Cloud preview environments per pull request, automatic infra provisioning, and CI/CD
- Multi-cloud production deployments on AWS (RDS, SQS, SNS, S3) and GCP (Cloud SQL, Pub/Sub, GCS)
- Distributed tracing with 1M events/month free, 20M/month on Pro, forwarding to Datadog, Grafana, and Sentry
- SOC 2 compliance assistance and custom RBAC on Enterprise
- Open-source MPL-2.0 framework with ~12,000 GitHub stars and active v1.57.x release cadence
- Python support on the roadmap
finops:
- name: Encore Dev Finops
  service_category: ''
  slug: encore-dev-finops
image: https://encore.dev/assets/branding/icon.svg
json_schemas:
- name: Encore API Endpoint
  property_count: 11
  slug: encore-api-endpoint
- name: Encore Infrastructure Resource
  property_count: 5
  slug: encore-infrastructure-resource
- name: Encore Service
  property_count: 8
  slug: encore-service
- name: Encore Trace Event
  property_count: 11
  slug: encore-trace-event
jsonld:
- class_count: 31
  name: Encore Dev Context
  property_count: 5
  slug: encore-dev-context
layout: provider
modified: '2026-05-24'
name: Encore
nav: Providers
network: true
overview: 'Encore publishes 3 APIs on the [APIs.io](https://apis.io/) network: Apps API, Encore API, and Encore Framework API API. Tagged areas include Backend, Framework, Cloud, TypeScript, and Go.


  The Encore catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Encore''s developer surface includes documentation, getting-started guide, developer portal, pricing, engineering blog, changelog, and 35 more developer resources.'
plans:
- name: Encore Dev Plans Pricing
  plan_count: 3
  slug: encore-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 9
  name: Encore Dev Rate Limits
  slug: encore-dev-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Encore API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: encore-dev-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Encore API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: encore-dev-rules
score:
  band: strong
  composite: 55.7
  delta: -5.1
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 61.8
    developer_ergonomics: 59.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 68.4
  previous_composite: 60.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/encore-dev/refs/heads/main/screenshots/encore-dev-2026-06-20T180721.png
security:
- kind: domain-security
  name: Encore Dev Domain Security
  slug: encore-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Encore Dev Vulnerability Disclosure
  slug: encore-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: encore-dev
tags:
- Backend
- Framework
- Cloud
- TypeScript
- Go
- DeveloperTools
- InfrastructureFromCode
- Microservices
- Observability
- Multicloud
website: https://encore.cloud
---
