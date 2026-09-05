---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Code Ocean Agentic Access
  operation_count: 26
  slug: code-ocean-agentic-access
  summary_line: 26 operations · 19 acting
api_count: 1
apis:
- baseURL: https://codeocean.com/api/v1
  baseurl_source: declared
  description: Reproducible compute capsules and pipelines
  name: Code Ocean Capsules API
  slug: code-ocean-capsules-api
- baseURL: https://codeocean.com/api/v1
  baseurl_source: declared
  description: Runs of capsules and pipelines
  name: Code Ocean Computations API
  slug: code-ocean-computations-api
- baseURL: https://codeocean.com/api/v1
  baseurl_source: declared
  description: Versioned datasets and result data
  name: Code Ocean Data Assets API
  slug: code-ocean-data-assets-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Code Ocean Capsules API
  slug: open-code-ocean-capsules-api
- collection_type: open
  name: Code Ocean Capsules Computations API
  slug: open-code-ocean-computations-api
- collection_type: open
  name: Code Ocean Capsules Data Assets API
  slug: open-code-ocean-data-assets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/code-ocean-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.codeocean.com/user-guide/code-ocean-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codeocean.com/user-guide/code-ocean-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.codeocean.com/user-guide/code-ocean-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codeocean.com/user-guide/key-concepts
- group: auth
  title: ''
  type: Authentication
  url: authentication/code-ocean-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codeocean
- group: build
  title: ''
  type: Packages
  url: packages/code-ocean-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/code-ocean-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/code-ocean-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/code-ocean-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/code-ocean-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/code-ocean-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/code-ocean-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/code-ocean-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/code-ocean-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/code-ocean-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/code-ocean-domain-security.yml
created: '2026-07-17'
description: Code Ocean is a computational research platform that helps scientists, engineers, and research organizations produce, manage, and reproduce computational science at scale. Its cloud environment centers on three resources — Capsules and Pipelines (self-contained, versioned compute environments that bundle code, data, environment, and results), Computations (tracked runs of those capsules and pipelines), and Data Assets (versioned datasets and captured results). Code Ocean exposes a REST API, an official Python SDK, and an official Model Context Protocol (MCP) server so teams can automate reproducible research, integrate the platform into data pipelines, and drive capsules and data assets from agents. The company was surfaced as a Battery Ventures portfolio company and is widely used across life sciences, biotech, and academic research computing.
image: https://raw.githubusercontent.com/codeocean/branding/main/logo/CO_logo_135x72.png
layout: provider
mcp_servers:
- description: Official Code Ocean MCP server. Provides tools to search and run capsules and pipelines and to manage data assets. Runs locally as a stdio child process; authenticates with a Code Ocean access token v
  name: Code Ocean MCP Server
  slug: code-ocean-mcp-server
modified: '2026-07-18'
name: Code Ocean
nav: Providers
network: true
overview: 'Code Ocean publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capsules API, Computations API, and Data Assets API. Tagged areas include Company, Reproducible Research, Computational Science, Data Science, and Research Computing.


  Code Ocean''s developer surface includes documentation, API reference, getting-started guide, authentication, and 15 more developer resources.'
random_paper: 8
scopes:
- name: Code Ocean Scopes
  scope_count: 4
  slug: code-ocean-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 62.6
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/code-ocean/refs/heads/main/screenshots/code-ocean-2026-07-25T205905.png
security:
- kind: authentication
  name: Code Ocean Authentication
  slug: code-ocean-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Code Ocean Domain Security
  slug: code-ocean-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: code-ocean
tags:
- Company
- Reproducible Research
- Computational Science
- Data Science
- Research Computing
- Life Sciences
- Pipelines
- MLOps
- Cloud Platform
- Developer Tools
website: https://docs.codeocean.com/user-guide/code-ocean-api
---
