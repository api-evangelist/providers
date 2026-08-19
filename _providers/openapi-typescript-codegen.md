---
access_model:
  confidence: high
  label: Free / Open Source (MIT)
  onboarding: unknown
  pricing: free
  public: true
  source:
  - plans
  - https://github.com/ferdikoomen/openapi-typescript-codegen/blob/main/LICENSE
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The openapi CLI and Node.js library. Consumes an OpenAPI 2.0 or 3.0 specification and writes a typed TypeScript client (models, services, and core runtime) for fetch, node-fetch, XHR, Axios, or Angula
  name: OpenAPI TypeScript Codegen
  slug: openapi-typescript-codegen
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/ferdikoomen/openapi-typescript-codegen
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/ferdikoomen/openapi-typescript-codegen/wiki
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ferdikoomen/openapi-typescript-codegen/wiki/Basic-usage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ferdikoomen
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/ferdikoomen/openapi-typescript-codegen
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ferdikoomen/openapi-typescript-codegen
- group: operate
  title: ''
  type: Support
  url: https://github.com/ferdikoomen/openapi-typescript-codegen/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/ferdikoomen/openapi-typescript-codegen/blob/main/LICENSE
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openapi-typescript-codegen-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/ferdikoomen/openapi-typescript-codegen#important-announcement
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openapi-typescript-codegen-lifecycle.yml
- group: build
  title: ''
  type: CLI
  url: cli/openapi-typescript-codegen-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/openapi-typescript-codegen-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openapi-typescript-codegen-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openapi-typescript-codegen-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/openapi-typescript-codegen-plans-pricing.yml
coverage:
  checked: '2026-08-06'
  detail: OpenAPI TypeScript Codegen is a build-time npm CLI that generates clients from someone else's OpenAPI — it ships no API, no baseURL, and no domain of its own, so there is no host to probe for a spec, /.well-known, MCP, or an agent card; the artifacts here describe the tool (npm package, CLI flags, changelog, deprecation notice) rather than a service.
  evidence:
  - status: 404
    url: https://raw.githubusercontent.com/ferdikoomen/openapi-typescript-codegen/main/llms.txt
  - status: 404
    url: https://raw.githubusercontent.com/ferdikoomen/openapi-typescript-codegen/main/SECURITY.md
  - status: 200
    url: https://registry.npmjs.org/openapi-typescript-codegen
  - status: 200
    url: https://api.github.com/repos/ferdikoomen/openapi-typescript-codegen
  reason: no-developer-program
  state: none
created: '2026-03-27'
description: 'OpenAPI TypeScript Codegen is an MIT-licensed Node.js library and CLI by Ferdi Koomen that reads an OpenAPI 2.0 or 3.0 specification — JSON or YAML, from a path, URL, or string — and generates a lightweight, fully typed TypeScript client. It emits models, services, and core runtime files for one of five HTTP clients (fetch, node-fetch, XHR, Axios, or Angular), and supports cancelable promises, union types instead of enums, runtime schemas, custom request files, and external $ref resolution. It is a build-time developer tool, not a hosted service: there is no API to call, no key to issue, and no pricing. The maintainer has publicly declared the project unmaintained and asks users to migrate to @hey-api/openapi-ts, yet maintenance releases still shipped in December 2025 and June 2026 and the package records roughly 2.46 million npm downloads a month.'
finops:
- name: Openapi Typescript Codegen Finops
  service_category: Developer Tools
  slug: openapi-typescript-codegen-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openapi-typescript-codegen.png
layout: provider
modified: '2026-08-06'
name: OpenAPI TypeScript Codegen
nav: Providers
network: true
overview: 'OpenAPI TypeScript Codegen publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Generation, OpenAPI, Swagger, SDKs, and TypeScript.


  OpenAPI TypeScript Codegen''s developer surface includes documentation, getting-started guide, support, changelog, CLI, and 11 more developer resources.'
plans:
- name: Openapi Typescript Codegen Plans Pricing
  plan_count: 1
  slug: openapi-typescript-codegen-plans-pricing
random_paper: 141
rate_limits:
- limit_count: 0
  name: Openapi Typescript Codegen Rate Limits
  slug: openapi-typescript-codegen-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: 0.9
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 23.8
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openapi-typescript-codegen/refs/heads/main/screenshots/openapi-typescript-codegen-2026-06-20T190912.png
slug: openapi-typescript-codegen
tags:
- Code Generation
- OpenAPI
- Swagger
- SDKs
- TypeScript
- Developer Tools
- CLI
- Open Source
---
