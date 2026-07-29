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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: High-performance GraphQL runtime for composing multiple upstream REST, gRPC, and GraphQL APIs into a unified GraphQL schema. Configuration-driven via declarative .graphql files with @server, @http, @u
  name: Tailcall GraphQL Runtime
  slug: tailcall-graphql-runtime
- description: ForgeCode is the commercial CLI coding harness product from Tailcall Inc, positioned as an AI-enabled programming assistant supporting 300+ models (Claude, GPT, Grok, Gemini, Deepseek, and more). Prov
  name: ForgeCode API (Tailcall Inc)
  slug: forgecode-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tailcall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tailcall.run
- group: docs
  title: ''
  type: Documentation
  url: https://tailcall.run/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tailcallhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tailcall
- group: company
  title: ''
  type: Blog
  url: https://forgecode.dev/blog/
- group: other
  title: ''
  type: X
  url: https://x.com/tailcallhq
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/kRZBPpkgwq
- group: commercial
  title: ''
  type: Plans
  url: plans/tailcall-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tailcall-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tailcall-finops.yml
created: '2026-06-13'
description: Tailcall is a high-performance GraphQL API gateway and runtime that lets developers compose multiple upstream REST, gRPC, and GraphQL APIs into a unified GraphQL schema. Built in Rust, it offers declarative configuration via .graphql files with directives for HTTP, caching, batching, and security controls. The open-source runtime (Apache 2.0) supports deployment on AWS Lambda, Cloudflare Workers, Docker, and bare metal. Tailcall Inc has subsequently shipped ForgeCode, a CLI coding harness built on the same performance-first ethos.
finops:
- name: Tailcall Finops
  service_category: ''
  slug: tailcall-finops
graphqls:
- description: Tailcall is a high-performance GraphQL gateway and runtime built in Rust. It does not expose a fixed hosted GraphQL API endpoint — instead, it is a self-hosted runtime that developers configure and de
  name: Tailcall GraphQL API
  slug: tailcall-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tailcall.png
jsonld:
- class_count: 32
  name: Tailcall Context
  property_count: 11
  slug: tailcall-context
layout: provider
modified: '2026-06-13'
name: Tailcall
nav: Providers
network: true
overview: 'Tailcall publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, API Gateway, GraphQL Runtime, REST, and gRPC.


  The Tailcall catalog on APIs.io includes 1 JSON-LD context.


  Tailcall''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Tailcall Plans Pricing
  plan_count: 4
  slug: tailcall-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 0
  name: Tailcall Rate Limits
  slug: tailcall-rate-limits
score:
  band: thin
  composite: 31.5
  delta: 6.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.6
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/tailcall/refs/heads/main/screenshots/tailcall-2026-06-20T194904.png
security:
- kind: domain-security
  name: Tailcall Domain Security
  slug: tailcall-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tailcall
tags:
- GraphQL
- API Gateway
- GraphQL Runtime
- REST
- gRPC
- Rust
- Open Source
- API Composition
- Caching
- Batching
website: https://tailcall.run
---
