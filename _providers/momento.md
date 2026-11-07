---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Region-scoped HTTP API for reading, writing, and deleting cache items in a Momento cache without a gRPC client. Supports GET, PUT (set with TTL), and DELETE against a named cache, authenticated with a
  name: Momento Cache HTTP API
  slug: momento-cache-http-api
artifact_total: 10
asyncapis:
- description: ''
  name: Momento Webhooks
  slug: momento-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/momento/plans/momento-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/momento-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gomomento.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.gomomento.com/feed
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
  href: https://artifacts.apis.io/momento/packages/momento-packages.yml
  title: ''
  type: SDKs
  url: packages/momento-packages.yml
- group: build
  href: https://artifacts.apis.io/momento/packages/momento-packages.yml
  title: ''
  type: Packages
  url: packages/momento-packages.yml
- group: build
  href: https://artifacts.apis.io/momento/cli/momento-cli.yml
  title: ''
  type: CLI
  url: cli/momento-cli.yml
- group: other
  href: https://artifacts.apis.io/momento/grpc/momento-grpc.yml
  title: ''
  type: Protobuf
  url: grpc/momento-grpc.yml
- group: auth
  href: https://artifacts.apis.io/momento/authentication/momento-authentication.yml
  title: ''
  type: Authentication
  url: authentication/momento-authentication.yml
- group: design
  href: https://artifacts.apis.io/momento/conventions/momento-conventions.yml
  title: ''
  type: Conventions
  url: conventions/momento-conventions.yml
- group: design
  href: https://artifacts.apis.io/momento/errors/momento-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/momento-error-codes.yml
- group: design
  href: https://artifacts.apis.io/momento/data-model/momento-data-model.yml
  title: ''
  type: DataModel
  url: data-model/momento-data-model.yml
- group: design
  href: https://artifacts.apis.io/momento/asyncapi/momento-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/momento-webhooks.yml
- group: design
  href: https://artifacts.apis.io/momento/lifecycle/momento-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/momento-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/momento/conformance/momento-conformance.yml
  title: ''
  type: Conformance
  url: conformance/momento-conformance.yml
- group: agent
  href: https://artifacts.apis.io/momento/mcp/momento-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/momento-mcp.yml
- group: agent
  href: https://artifacts.apis.io/momento/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/momento/llms/momento-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/momento-llms.txt
- group: auth
  href: https://artifacts.apis.io/momento/security/momento-domain-security.yml
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
finops:
- has_sources: true
  method: derived
  name: Momento Finops
  primary_unit: gb-month
  service_category: ''
  slug: momento-finops
  template: false
image: https://github.com/momentohq.png
layout: provider
modified: '2026-10-06'
name: Momento
nav: Providers
network: true
overview: 'Momento is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Infrastructure, Caching, Serverless, and Cache.


  The Momento catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Momento''s developer surface includes engineering blog, documentation, API reference, getting-started guide, CLI, authentication, pricing, and 23 more developer resources.'
plans:
- name: Momento Plans Pricing
  plan_count: 15
  slug: momento-plans-pricing
- name: Momento Price Estimates
  plan_count: 0
  slug: momento-price-estimates
random_paper: 23
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 70.8
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 48.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/momento/momento-2026-08-07T184119.png
security:
- kind: authentication
  name: Momento Authentication
  slug: momento-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Momento Domain Security
  slug: momento-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Cache a value and read it back
  slug: momento-cache-set-and-get
- name: Maintain a leaderboard and read ranks
  slug: momento-leaderboard-upsert-and-rank
- name: Publish and subscribe on a Topic
  slug: momento-topics-pub-sub
slug: momento
tags:
- Company
- AI Infrastructure
- Caching
- Serverless
- Cache
- Pub/Sub
- Messaging
- Event Bus
- Leaderboards
- Real-Time
- gRPC
- Developer Tools
website: https://www.gomomento.com/
---
