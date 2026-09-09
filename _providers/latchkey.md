---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-09-08'
api_count: 1
apis:
- description: REST API for creating, submitting, monitoring, and cancelling ephemeral runner jobs. Each job runs one command on a fresh Ubuntu 24.04 x86_64 machine that is destroyed afterwards. Uses HTTP Bearer aut
  name: Latchkey Jobs API
  slug: latchkey-jobs-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://latchkey.dev/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/latchkey-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/latchkey-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/latchkey-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://latchkey.dev/documentation/security-architecture
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/latchkey-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/latchkey-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/latchkey-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/latchkey-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/latchkey-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/latchkey-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/latchkey-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/latchkey-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/latchkey-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/latchkey-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/latchkey-jobs-api-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/latchkey-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/latchkey-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://latchkey.dev/documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://latchkey.dev/documentation/quickstart
- group: operate
  title: ''
  type: Support
  url: https://latchkey.dev/support
- group: company
  title: ''
  type: Blog
  url: https://latchkey.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://latchkey.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://latchkey.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://latchkey.dev/privacy
- group: start
  title: ''
  type: Login
  url: https://latchkey.dev/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/latchkey-dev
created: '2026-09-06'
description: Managed ephemeral GitHub Actions runners that repair failing builds mid-run. The Jobs API gives coding agents and CI systems direct access to a fresh Ubuntu 24.04 x86_64 runner that runs one command and is then destroyed, with a hosted MCP server, CLI, and llms.txt for agent-native access.
image: https://latchkey.dev/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Latchkey Jobs API MCP Server
  slug: latchkey-jobs-api-mcp-server
- description: ''
  name: Latchkey Jobs API MCP Server
  slug: latchkey-jobs-api-mcp-server-2
modified: '2026-09-07'
name: Latchkey Jobs API
nav: Providers
network: true
overview: 'Latchkey Jobs API publishes 1 API on the [APIs.io](https://apis.io/) network: Latchkey Jobs API. Tagged areas include CI/CD, DevOps, GitHub Actions, Ephemeral Compute, and Build & Test Infrastructure.


  Latchkey Jobs API''s developer surface includes authentication, CLI, documentation, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Latchkey Plans Pricing
  plan_count: 4
  slug: latchkey-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Latchkey Rate Limits
  slug: latchkey-rate-limits
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 33.3
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 45.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Latchkey Authentication
  slug: latchkey-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Latchkey Domain Security
  slug: latchkey-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Latchkey Vulnerability Disclosure
  slug: latchkey-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: latchkey
tags:
- CI/CD
- DevOps
- GitHub Actions
- Ephemeral Compute
- Build & Test Infrastructure
- Agent-Native
- AI Coding Agents
website: https://latchkey.dev/
---
