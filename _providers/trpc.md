---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trpc Agentic Access
  operation_count: 4
  slug: trpc-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- description: tRPC procedures exposed as REST endpoints
  name: tRPC Procedures API
  slug: trpc-procedures-api
artifact_total: 16
collections:
- collection_type: open
  name: tRPC OpenAPI Example
  slug: open-trpc
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trpc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trpc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trpc-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://trpc.io/
- group: docs
  title: ''
  type: Documentation
  url: https://trpc.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trpc
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/trpc/trpc
- group: build
  title: ''
  type: NPM
  url: https://www.npmjs.com/package/@trpc/server
- group: operate
  title: ''
  type: Discord
  url: https://trpc.io/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/alexdotjs
- group: agent
  title: ''
  type: LlmsText
  url: https://trpc.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://trpc.io/blog/rss.xml
created: '2026-03-27'
description: tRPC is a TypeScript framework for building end-to-end typesafe APIs without code generation or schemas. It leverages TypeScript's type inference to provide full static typesafety and autocompletion between client and server, with zero runtime dependencies. tRPC v11 supports queries, mutations, and subscriptions via HTTP GET/POST and WebSocket adapters for Express, Fastify, Next.js, AWS Lambda, and edge runtimes.
examples:
- key_count: 3
  name: Trpc Mutation Procedure Example
  slug: trpc-mutation-procedure-example
- key_count: 3
  name: Trpc Query Procedure Example
  slug: trpc-query-procedure-example
finops:
- name: Trpc Finops
  service_category: API
  slug: trpc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trpc.png
json_schemas:
- name: tRPC Error
  property_count: 1
  slug: trpc-error
- name: tRPC Procedure
  property_count: 3
  slug: trpc-procedure
json_structures:
- name: Trpc Router Structure
  property_count: 0
  slug: trpc-router-structure
jsonld:
- class_count: 19
  name: Trpc Context
  property_count: 0
  slug: trpc-context
layout: provider
modified: '2026-05-19'
name: tRPC
nav: Providers
network: true
overview: 'tRPC publishes 1 API on the [APIs.io](https://apis.io/) network: Procedures API. Tagged areas include API Composition, API Framework, BFF, End-to-End Type Safety, and RPC.


  The tRPC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  tRPC''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Trpc Plans Pricing
  plan_count: 3
  slug: trpc-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 5
  name: Trpc Rate Limits
  slug: trpc-rate-limits
rules:
- name: tRPC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: trpc-jsonschema-spectral-rules
- name: tRPC API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 3
    info: 0
    warn: 2
  slug: trpc-rules
score:
  band: developing
  composite: 48.9
  delta: -5.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/trpc/refs/heads/main/screenshots/trpc-2026-06-20T195747.png
security:
- kind: authentication
  name: Trpc Authentication
  slug: trpc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Trpc Domain Security
  slug: trpc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: trpc
tags:
- API Composition
- API Framework
- BFF
- End-to-End Type Safety
- RPC
- TypeScript
website: https://trpc.io/
---
