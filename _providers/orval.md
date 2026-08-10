---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://github.com/orval-labs/orval/blob/master/LICENSE
  - https://www.npmjs.com/package/orval
  - https://orval.dev/playground
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Orval generates TypeScript API clients, TanStack Query/SWR hooks, Angular services, SolidStart primitives, Hono server handlers, Zod and Effect schemas, MSW mocks, and MCP servers from OpenAPI v3 or S
  name: Orval
  slug: orval
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orval-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orval.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orval.dev
- group: docs
  title: ''
  type: Documentation
  url: https://orval.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://orval.dev/docs/reference/cli
- group: start
  title: ''
  type: GettingStarted
  url: https://orval.dev/docs/quick-start
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orval-labs/orval
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/6fC2sjDU7w
- group: operate
  title: ''
  type: Support
  url: https://github.com/orval-labs/orval/discussions
- group: build
  title: ''
  type: Samples
  url: https://orval.dev/docs/guides/react-query
- group: agent
  title: ''
  type: LlmsText
  url: https://orval.dev/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orval-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/orval-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/orval-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orval-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/orval-labs/orval/releases
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/orval-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/orval-labs/orval/blob/master/SECURITY.md#supported-versions
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/orval-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/orval-labs/orval/blob/master/SECURITY.md
- group: design
  title: ''
  type: Conformance
  url: conformance/orval-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/orval-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://orval.dev/playground
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/orval-robots.txt
- group: commercial
  title: ''
  type: License
  url: https://github.com/orval-labs/orval/blob/master/LICENSE
created: '2026-03-25'
description: Orval is an MIT-licensed open source code generator that turns any valid OpenAPI v3 or Swagger v2 specification into type-safe TypeScript. From one spec it emits HTTP request functions (Fetch by default, Axios optional), TanStack Query hooks for React, Vue, Svelte, Solid and Angular, SWR hooks, Angular HttpClient services, SolidStart primitives, Hono server templates, Zod and Effect validation schemas, MSW handlers with Faker mock data, and Model Context Protocol servers for agent integration. It ships as a CLI plus a programmatic API, is configured through an orval.config.ts file with per-project targets, transformers, hooks and output modes, and is distributed on npm as `orval` alongside thirteen first-party `@orval/*` generator packages and an official ghcr.io container image. Orval itself exposes no hosted HTTP API — the specification is the input, and generated client code is the product.
finops:
- name: Orval Finops
  service_category: API
  slug: orval-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/orval.png
layout: provider
modified: '2026-08-06'
name: Orval
nav: Providers
network: true
overview: 'Orval publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, OpenAPI, Swagger, SDKs, and TypeScript.


  Orval''s developer surface includes documentation, API reference, getting-started guide, support, CLI, changelog, sandbox, and 19 more developer resources.'
plans:
- name: Orval Plans Pricing
  plan_count: 3
  slug: orval-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 5
  name: Orval Rate Limits
  slug: orval-rate-limits
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 77.8
    governance: 12.5
    operational_transparency: 71.1
  previous_composite: 38.2
  provenance:
    conformance: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/orval/refs/heads/main/screenshots/orval-2026-06-20T191211.png
security:
- kind: domain-security
  name: Orval Domain Security
  slug: orval-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Orval Vulnerability Disclosure
  slug: orval-vulnerability-disclosure
  summary_line: security.txt
slug: orval
tags:
- Code Generation
- OpenAPI
- Swagger
- SDKs
- TypeScript
- Developer Tools
- CLI
- Open Source
- Mocking
- Schema Validation
website: https://orval.dev
---
