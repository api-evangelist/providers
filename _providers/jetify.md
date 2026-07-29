---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Pkg API from Jetify — 1 operation(s) for pkg.
  name: Jetify Pkg API
  slug: jetify-pkg-api
- description: The Resolve API from Jetify — 1 operation(s) for resolve.
  name: Jetify Resolve API
  slug: jetify-resolve-api
- description: The Search API from Jetify — 1 operation(s) for search.
  name: Jetify Search API
  slug: jetify-search-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.jetify.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.jetify.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetify.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.jetify.com/docs/nixhub/
- group: company
  title: ''
  type: Blog
  url: https://www.jetify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jetify-com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.jetify.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.jetify.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.jetify.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.jetify.com/legal/privacy
- group: build
  title: ''
  type: SDKs
  url: packages/jetify-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/jetify-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/jetify-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jetify-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jetify-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jetify-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jetify-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/jetify-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jetify-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/jetify-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/jetify-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jetify-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jetify-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jetify-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Jetify builds developer tooling for reproducible environments and package management, backed by the Nix ecosystem. Its open-source Devbox CLI creates instant, isolated, predictable development shells; Jetify Cloud adds team secrets management, a private Nix package cache, and deployments; Nixhub indexes over one million package versions across 100,000+ Nix packages and exposes a free, public REST API for searching and resolving them; and Testpilot is an AI agent for autonomous end-to-end testing. Jetify is backed by GV and Homebrew. This profile was enriched by the API Evangelist pipeline from Jetify's public docs, npm/Go registries, and live API probes.
image: https://avatars.githubusercontent.com/u/65328393?v=4
layout: provider
mcp_servers:
- description: ''
  name: jetify-mcp.yml
  slug: jetify-mcpyml
modified: '2026-07-19'
name: Jetify
nav: Providers
network: true
overview: 'Jetify publishes 3 APIs on the [APIs.io](https://apis.io/) network: Pkg API, Resolve API, and Search API. Tagged areas include Company, Enterprise, Developer Tools, Nix, and Package Management.


  Jetify''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, CLI, authentication, and 19 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 45.6
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.2
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 46.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jetify/refs/heads/main/screenshots/jetify-2026-07-25T223137.png
security:
- kind: authentication
  name: Jetify Authentication
  slug: jetify-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Jetify Domain Security
  slug: jetify-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: jetify
tags:
- Company
- Enterprise
- Developer Tools
- Nix
- Package Management
- Developer Environments
- Reproducible Builds
- CLI
- Search
website: https://www.jetify.com
---
