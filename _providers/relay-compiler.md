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
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: The Relay Compiler is Meta's ahead-of-time GraphQL compiler that generates optimized runtime artifacts and type-safe code for Relay applications. It processes GraphQL fragments in JavaScript/TypeScrip
  name: Relay Compiler
  slug: relay-compiler
- description: The Relay Runtime provides the client-side execution environment for Relay applications. It includes the normalized in-memory store, network layer, and React hooks including usePreloadedQuery, useFrag
  name: Relay Runtime
  slug: relay-runtime
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relay-compiler-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://relay.dev
- group: docs
  title: ''
  type: Documentation
  url: https://relay.dev/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/facebook/relay
- group: build
  title: ''
  type: npm Package
  url: https://www.npmjs.com/package/relay-compiler
- group: company
  title: ''
  type: Blog
  url: https://relay.dev/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/facebook/relay/releases
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/json-ld/relay-compiler-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/vocabulary/relay-compiler-vocabulary.yml
created: '2026-03-25'
description: Relay is Meta's open-source JavaScript framework and ahead-of-time GraphQL compiler for building data-driven React applications. The Relay Compiler scans JavaScript code for GraphQL fragments, aggregates and optimizes data requirements for entire apps, pre-computes queries at build time for efficient runtime performance, and generates TypeScript/Flow types for React components. It supports pagination, mutations, subscriptions, and deferred data streaming via GraphQL directives.
finops:
- name: Relay Compiler Finops
  service_category: API
  slug: relay-compiler-finops
graphqls:
- description: The Relay Compiler is Meta's ahead-of-time GraphQL compiler that generates optimized runtime artifacts and type-safe code for Relay applications. It processes GraphQL fragments in JavaScript/TypeScrip
  name: Relay Compiler GraphQL API
  slug: relay-compiler-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relay-compiler.png
jsonld:
- class_count: 0
  name: Relay Compiler Context
  property_count: 20
  slug: relay-compiler-context
layout: provider
modified: '2026-05-02'
name: Relay Compiler
nav: Providers
network: true
overview: 'Relay Compiler publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, GraphQL, React, Meta, and Open Source.


  The Relay Compiler catalog on APIs.io includes 1 JSON-LD context.


  Relay Compiler''s developer surface includes documentation, engineering blog, changelog, and 6 more developer resources.'
plans:
- name: Relay Compiler Plans Pricing
  plan_count: 3
  slug: relay-compiler-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Relay Compiler Rate Limits
  slug: relay-compiler-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 13.2
    operational_transparency: 52.6
  previous_composite: 30.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relay-compiler/refs/heads/main/screenshots/relay-compiler-2026-06-20T192823.png
security:
- kind: domain-security
  name: Relay Compiler Domain Security
  slug: relay-compiler-domain-security
  summary_line: TLSv1.3
slug: relay-compiler
tags:
- Code Generation
- GraphQL
- React
- Meta
- Open Source
- TypeScript
- Build Tools
website: https://relay.dev
---
