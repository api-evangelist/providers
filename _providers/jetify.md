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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nixhub Pkg API
  slug: open-jetify-pkg-api
- collection_type: open
  name: Nixhub Pkg Resolve API
  slug: open-jetify-resolve-api
- collection_type: open
  name: Nixhub Pkg Search API
  slug: open-jetify-search-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/jetify-nixhub-overlay.yaml
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
  name: Jetify MCP Server
  slug: jetify-mcp-server
modified: '2026-07-19'
name: Jetify
nav: Providers
network: true
overview: 'Jetify publishes 3 APIs on the [APIs.io](https://apis.io/) network: Pkg API, Resolve API, and Search API. Tagged areas include Company, Enterprise, Developer Tools, Nix, and Package Management.


  Jetify''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, CLI, authentication, and 20 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 44.7
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 51.7
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 44.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
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
