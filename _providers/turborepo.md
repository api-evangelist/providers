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
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Turborepo Agentic Access
  operation_count: 6
  slug: turborepo-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 2
apis:
- description: Operations for recording cache usage analytics
  name: Turborepo analytics API
  slug: turborepo-analytics-api
- description: Operations for managing cache artifacts
  name: Turborepo artifacts API
  slug: turborepo-artifacts-api
artifact_total: 28
collections:
- collection_type: open
  name: Turborepo Remote Cache API
  slug: open-turborepo-remote-cache-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turborepo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turborepo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turborepo-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://turborepo.dev
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://turborepo.dev/docs/getting-started/installation
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs/reference/configuration
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs/reference
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs/core-concepts/remote-caching
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs/crafting-your-repository
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/docs/telemetry
- group: company
  title: ''
  type: Blog
  url: https://turborepo.dev/blog
- group: docs
  title: ''
  type: Documentation
  url: https://turborepo.dev/showcase
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vercel/turborepo
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/vercel/turborepo
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/vercel/turborepo/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/vercel/turborepo/blob/main/LICENSE
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/vercel/turborepo/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/vercel/turborepo/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/vercel/turborepo/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/turbo
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/create-turbo
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/eslint-config-turbo
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/eslint-plugin-turbo
- group: build
  title: ''
  type: Package
  url: https://www.npmjs.com/package/turbo-ignore
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/vercel/turborepo/tree/main/examples
- group: docs
  title: ''
  type: Documentation
  url: https://vercel.com/docs/monorepos/turborepo
- group: docs
  title: ''
  type: Documentation
  url: https://vercel.com/docs/monorepos/remote-caching
- group: commercial
  title: ''
  type: Pricing
  url: https://vercel.com/pricing
- group: auth
  title: ''
  type: Authentication
  url: https://vercel.com/account/tokens
- group: operate
  title: ''
  type: Forums
  url: https://github.com/vercel/turborepo/discussions
- group: other
  title: ''
  type: X
  url: https://x.com/turborepo
- group: company
  title: ''
  type: BlueSky
  url: https://bsky.app/profile/turborepo.com
created: '2026-05-25T00:00:00.000Z'
description: Turborepo is a high-performance build system for JavaScript and TypeScript codebases, built by Vercel and written in Rust. It accelerates monorepo development by orchestrating task pipelines with explicit dependency graphs, hashing task inputs to skip redundant work, and caching task outputs locally and remotely so the same build/lint/test never runs twice across developers and CI. The project ships the turbo CLI (turbo run, prune, watch, boundaries, ls, query, generate, login, link, telemetry) plus an open Remote Cache HTTP API specification that any server can implement — Vercel's Remote Cache is the reference, and community implementations enable fully self-hosted caching. Turborepo is MIT-licensed open source at github.com/vercel/turborepo.
features:
- High-performance build system for JavaScript and TypeScript monorepos, written in Rust
- Task pipeline orchestration with dependsOn graphs (turbo run build, lint, test)
- Content-addressable local caching of task outputs
- Remote Caching with shared artifact store across teammates and CI
- Open Remote Cache API specification — any HTTP server can implement it
- Vercel Remote Cache as the reference implementation (api.vercel.com)
- Self-hosted remote cache compatible (ducktors/turborepo-remote-cache, brunojppb/turbo-cache-server)
- Package manager support — npm, pnpm, Yarn, Bun
- turbo prune for shipping minimal monorepo subsets to Docker/production
- turbo watch for single-process dependency-aware task watching
- turbo boundaries for enforcing architectural rules between packages
- turbo query — GraphQL queries over monorepo structure
- turbo ls for listing packages and dependencies
- turbo gen scaffolding for new apps and packages
- turbo-ignore helper for CI skip-build decisions based on affected packages
- Codemods via turbo-codemod for upgrading between major versions
- VS Code extension (turbo-vsc) and ESLint plugin/config
- Telemetry CLI (turbo telemetry enable/disable/status) with anonymous opt-out
- Login flow (turbo login, turbo link, turbo unlink) for Remote Cache provider auth
- turbo bin and turbo docs helper commands
- MIT licensed, open source on GitHub (vercel/turborepo)
graphqls:
- description: ''
  name: Turborepo GraphQL API
  slug: turborepo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turborepo.png
layout: provider
modified: '2026-05-25'
name: Turborepo
nav: Providers
network: true
overview: 'Turborepo publishes 2 APIs on the [APIs.io](https://apis.io/) network: analytics API and artifacts API. Tagged areas include Build System, Monorepo, JavaScript, TypeScript, and Caching.


  Turborepo''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, code examples, and 26 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 63.6
    developer_ergonomics: 41.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turborepo/refs/heads/main/screenshots/turborepo-2026-06-20T195834.png
security:
- kind: authentication
  name: Turborepo Authentication
  slug: turborepo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Turborepo Domain Security
  slug: turborepo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: turborepo
tags:
- Build System
- Monorepo
- JavaScript
- TypeScript
- Caching
- Open Source
- Rust
- Vercel
- Developer Tools
- CI/CD
website: https://turborepo.dev
---
