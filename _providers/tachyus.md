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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: Daily/monthly production records for a well.
  name: Tachyus Production Data API
  slug: tachyus-production-data-api
- description: Projects map to a specific geographic or operational asset.
  name: Tachyus Projects API
  slug: tachyus-projects-api
- description: Wells belong to projects.
  name: Tachyus Wells API
  slug: tachyus-wells-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://tachyus.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tachyus.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tachyus.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tachyus.com/api/introduction.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tachyus.com/guide/getting-started.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tachyus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tachyus.com/_files/ugd/3ab73f_d653d64a6d4640b3a35762afb01ac3ef.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tachyus-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tachyus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tachyus-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tachyus-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tachyus-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tachyus-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tachyus-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tachyus-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tachyus-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tachyus-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tachyus-tachapps-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/tachyus-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tachyus-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tachyus-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tachyus provides AI-powered operational optimization and greenhouse-gas emissions management software for the energy and industrial sectors, combining data, reservoir physics, and machine learning. Its Tachapps platform spans Strateon (production and injection allocation), Aqueon (conventional reservoir management and optimization), and Aurion (GHG emissions accounting, monitoring, forecasting, and regulatory reporting). The Tachapps REST API (v1) is organized around Projects, Wells, and Production Data, using Bearer API-token authentication with scopes, JSON over HTTPS, cursor-based pagination, and per-plan rate limits.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tachyus.png
layout: provider
mcp_servers:
- description: ''
  name: tachyus-mcp.yml
  slug: tachyus-mcpyml
modified: '2026-07-21'
name: Tachyus
nav: Providers
network: true
overview: 'Tachyus publishes 3 APIs on the [APIs.io](https://apis.io/) network: Production Data API, Projects API, and Wells API. Tagged areas include Company, Energy, Oil and Gas, Reservoir Management, and Production Optimization.


  Tachyus'' developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 17 more developer resources.'
random_paper: 73
rate_limits:
- limit_count: 3
  name: Tachyus Rate Limits
  slug: tachyus-rate-limits
scopes:
- name: Tachyus Scopes
  scope_count: 6
  slug: tachyus-scopes
  summary_line: 6 scopes
score:
  band: developing
  composite: 45.1
  delta: -0.5
  facets:
    commercial_clarity: 10.5
    contract_quality: 58.2
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 60.5
  previous_composite: 45.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Tachyus Authentication
  slug: tachyus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tachyus Domain Security
  slug: tachyus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tachyus
tags:
- Company
- Energy
- Oil and Gas
- Reservoir Management
- Production Optimization
- Emissions Management
- Machine Learning
- Analytics
website: https://tachyus.com
---
