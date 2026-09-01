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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
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
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/facebook/relay/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/facebook/relay/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/facebook/relay/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/facebook/relay/blob/main/LICENSE
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
overview: 'Relay Compiler publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, GraphQL, React, Meta, and Open-Source.


  The Relay Compiler catalog on APIs.io includes 1 JSON-LD context.


  Relay Compiler''s developer surface includes documentation, engineering blog, changelog, and 10 more developer resources.'
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
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 9
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 15.2
    contract_quality: 10.7
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 15.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 25.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Open-Source
- TypeScript
- Build Tools
website: https://relay.dev
---
