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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fern Api Agentic Access
  operation_count: 3
  slug: fern-api-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 5
apis:
- description: Capability area (CLI/platform, not a hosted REST API) that generates idiomatic, type-safe client SDKs in TypeScript, Python, Go, Java, C#, PHP, Ruby, Swift, and Rust from OpenAPI, AsyncAPI, gRPC, or F
  name: Fern SDK Generation
  slug: fern-api-sdk-generation
- description: Capability area (CLI/platform) that builds a hosted documentation website with a generated API reference, interactive API playground, changelogs, versioning, keyword search, and docs-as-code (Markdown
  name: Fern API Documentation
  slug: fern-api-documentation
- description: Capability area covering Fern's open-source (Apache-2.0) command-line interface and the proprietary Fern Definition API-description format. Core commands include `fern init`, `fern check`, `fern gener
  name: Fern Definition and CLI
  slug: fern-api-definition-cli
- description: Query indexed documentation for AI-generated, grounded answers.
  name: Fern Ask API
  slug: fern-api-ask-api
- description: Index documentation websites and check indexing job status.
  name: Fern Website Sources API
  slug: fern-api-website-sources-api
artifact_total: 11
collections:
- collection_type: open
  name: Fern Ask Fern API
  slug: open-fern-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fern-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fern-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fern-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildwithfern
- group: company
  title: ''
  type: Website
  url: https://buildwithfern.com
- group: docs
  title: ''
  type: Documentation
  url: https://buildwithfern.com/learn/home
- group: commercial
  title: ''
  type: Plans
  url: plans/fern-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fern-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fern-api-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://buildwithfern.com/blog
created: '2026-07-11'
description: 'Fern is a developer-tools platform that turns a single API specification into idiomatic client SDKs, beautiful API documentation, and MCP servers. Given OpenAPI, AsyncAPI, gRPC/Protobuf, or Fern''s own Fern Definition as input, Fern generates type-safe SDKs in TypeScript, Python, Go, Java, C#, PHP, Ruby, Swift, and Rust, publishes them to registries like npm, PyPI, and Maven, and builds a hosted docs site with an interactive API reference, API playground, and an AI-powered "Ask Fern" search. The primary interface is the open-source `fern` CLI (Apache-2.0, github.com/fern-api/fern) driving a hosted platform - the fern-api catalog documents Fern''s SDK-generation, documentation-generation, and Fern Definition capability surfaces as capability areas, plus the one hosted public REST API Fern exposes to customers, the Ask Fern API. Fern is open-core: the CLI and generators are open source, and Docs and SDKs are sold on Hobby (free), Team, and Enterprise plans.'
finops:
- name: Fern Api Finops
  service_category: Developer Tools
  slug: fern-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fern-api.png
layout: provider
modified: '2026-07-11'
name: Fern
nav: Providers
network: true
overview: 'Fern publishes 2 APIs on the [APIs.io](https://apis.io/) network: Ask API and Website Sources API. Tagged areas include API Lifecycle, SDK Generation, Client Library, API Documentation, and Developer Tools.


  Fern''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Fern Api Plans Pricing
  plan_count: 4
  slug: fern-api-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 4
  name: Fern Api Rate Limits
  slug: fern-api-rate-limits
score:
  band: thin
  composite: 38.8
  delta: -0.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fern-api/refs/heads/main/screenshots/fern-api-2026-07-25T214344.png
security:
- kind: authentication
  name: Fern Api Authentication
  slug: fern-api-authentication
  summary_line: http · 1 scheme
slug: fern-api
tags:
- API Lifecycle
- SDK Generation
- Client Library
- API Documentation
- Developer Tools
- OpenAPI
- CLI
- Open Source
- Developer Experience
website: https://buildwithfern.com
---
