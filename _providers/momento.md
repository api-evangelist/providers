---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Region-scoped HTTP API for reading, writing, and deleting cache items in a Momento cache without a gRPC client. Supports GET, PUT (set with TTL), and DELETE against a named cache, authenticated with a
  name: Momento Cache HTTP API
  slug: momento-cache-http-api
artifact_total: 5
asyncapis:
- description: ''
  name: Momento Webhooks
  slug: momento-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.gomomento.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.momentohq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.momentohq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.momentohq.com/cache/develop/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.momentohq.com/getting-started
- group: build
  title: ''
  type: SDKs
  url: packages/momento-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/momento-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/momento-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/momento-grpc.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/momento-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/momento-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/momento-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/momento-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/momento-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/momento-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/momento-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/momento-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/momento-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/momento-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/momentohq
- group: company
  title: ''
  type: Blog
  url: https://www.gomomento.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gomomento.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.gomomento.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gomomento.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gomomento.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/gomomento
created: '2026-07-17'
description: Momento is a serverless data platform that provides low-latency, pay-as-you-go infrastructure without servers to provision, tune, or scale. Its core services are Momento Cache (an ephemeral serverless cache and drop-in Redis replacement), Momento Topics (a serverless publish/subscribe event bus), and Momento Leaderboards (massive, durable sorted sets). The platform is accessed over gRPC and a region-scoped HTTP API, with official SDKs for 15+ languages spanning browsers, mobile (iOS/Android/Flutter/Unity/Unreal), and 10+ server-side runtimes, plus a CLI and a Terraform provider. Authentication uses Momento API keys and short-lived disposable tokens with fine-grained permissions. Momento is backed by Bain Capital Ventures.
image: https://github.com/momentohq.png
layout: provider
mcp_servers:
- description: ''
  name: momento-mcp.yml
  slug: momento-mcpyml
modified: '2026-07-20'
name: Momento
nav: Providers
network: true
overview: 'Momento publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Infrastructure, Caching, Serverless, and Cache.


  The Momento catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Momento''s developer surface includes documentation, API reference, getting-started guide, CLI, authentication, engineering blog, pricing, and 20 more developer resources.'
random_paper: 71
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 44.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/momento/refs/heads/main/screenshots/momento-2026-08-07T184119.png
security:
- kind: authentication
  name: Momento Authentication
  slug: momento-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Momento Domain Security
  slug: momento-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: momento
tags:
- Company
- Ai Infrastructure
- Caching
- Serverless
- Cache
- Pub/Sub
- Messaging
- Event Bus
- Leaderboards
- Real Time
- gRPC
- Developer Tools
website: https://www.gomomento.com/
---
