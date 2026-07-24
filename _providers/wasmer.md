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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Wasmer Agentic Access
  operation_count: 2
  slug: wasmer-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: The wasmer command-line client (wasmer login, publish, deploy, run, ssh) - a first-class consumer of the Registry GraphQL API that wraps publish and Edge deployment workflows.
  name: Wasmer CLI
  slug: wasmer-cli
- description: The GraphQL API from Wasmer — 1 operation(s) for graphql.
  name: Wasmer GraphQL API
  slug: wasmer-graphql-api
artifact_total: 11
collections:
- collection_type: open
  name: Wasmer Registry GraphQL API
  slug: open-wasmer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wasmer-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wasmer-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wasmer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wasmer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wasmerio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wasmer
- group: company
  title: ''
  type: Website
  url: https://wasmer.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wasmer.io
- group: commercial
  title: ''
  type: Plans
  url: plans/wasmer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wasmer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wasmer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.wasmer.io/feed
created: '2026-06-20'
description: Wasmer is a WebAssembly runtime, package registry, and edge platform. The Wasmer Registry stores and distributes WebAssembly packages and namespaces, Wasmer Edge deploys those packages as auto-scaling apps, and the wasmer CLI and wasmer.sh interact with the platform through a single public GraphQL API at registry.wasmer.io/graphql.
finops:
- name: Wasmer Finops
  service_category: Compute and Edge
  slug: wasmer-finops
graphqls:
- description: Representative GraphQL schema for the [Wasmer](https://wasmer.io) Registry and Edge
  name: Wasmer Registry GraphQL API
  slug: wasmer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wasmer.png
layout: provider
modified: '2026-06-20'
name: Wasmer
nav: Providers
network: true
overview: 'Wasmer publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include WebAssembly, Wasm, Registry, Edge, and Runtime.


  Wasmer''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Wasmer Plans Pricing
  plan_count: 3
  slug: wasmer-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Wasmer Rate Limits
  slug: wasmer-rate-limits
score:
  band: thin
  composite: 38.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wasmer/refs/heads/main/screenshots/wasmer-2026-06-20T201241.png
security:
- kind: authentication
  name: Wasmer Authentication
  slug: wasmer-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wasmer Domain Security
  slug: wasmer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wasmer Vulnerability Disclosure
  slug: wasmer-vulnerability-disclosure
  summary_line: disclosure policy published
slug: wasmer
tags:
- WebAssembly
- Wasm
- Registry
- Edge
- Runtime
website: https://wasmer.io
---
