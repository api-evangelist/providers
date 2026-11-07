---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.6
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'Hosted Model Context Protocol endpoint at https://api.rosentic.com/mcp (Streamable HTTP, POST), live since 2026-07-23, exposing three read tools over stored scan snapshots — run_status (every lane in '
  name: Rosentic Remote MCP Server
  slug: rosentic-remote-mcp-server
- description: 'Agent2Agent protocol surface: an agent card served from https://api.rosentic.com/.well-known/agent-card.json (protocolVersion 0.3.0, version 1.0.0, streaming true, stateTransitionHistory true; also by'
  name: Rosentic A2A Agent
  slug: rosentic-a2a-agent
- description: 'The Bearer-key REST surface documented on the orchestrator-integration page for wiring Conductor, Claude Squad, LangGraph and other agent orchestrators to a Rosentic workspace: GET /v1/feed/rules retu'
  name: Rosentic Dashboard Feed API
  slug: rosentic-dashboard-feed-api
artifact_total: 11
common:
- group: auth
  href: https://artifacts.apis.io/rosentic-com/security/rosentic-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rosentic-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rosentic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rosentic.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://rosentic.com/docs/integrations/
- group: start
  title: ''
  type: GettingStarted
  url: https://rosentic.com/install/
- group: commercial
  title: ''
  type: Pricing
  url: https://rosentic.com/pricing/
- group: commercial
  href: https://artifacts.apis.io/rosentic-com/plans/rosentic-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rosentic-com-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://rosentic.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://rosentic.com/changelog/
- group: operate
  href: https://artifacts.apis.io/rosentic-com/changelog/rosentic-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rosentic-com-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Rosentic
- group: operate
  title: ''
  type: Support
  url: https://github.com/Rosentic/rosentic-action/issues
- group: start
  title: ''
  type: SignUp
  url: https://api.rosentic.com/onboard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rosentic/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/RosenticHQ
- group: agent
  href: https://artifacts.apis.io/rosentic-com/llms/rosentic-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rosentic-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://rosentic.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/rosentic-com/well-known/rosentic-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rosentic-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/rosentic-com/a2a/rosentic-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rosentic-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/rosentic-com/mcp/rosentic-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rosentic-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/rosentic-com/scopes/rosentic-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/rosentic-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/rosentic-com/authentication/rosentic-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rosentic-com-authentication.yml
- group: build
  href: https://artifacts.apis.io/rosentic-com/packages/rosentic-com-packages.yml
  title: ''
  type: Packages
  url: packages/rosentic-com-packages.yml
- group: build
  href: https://artifacts.apis.io/rosentic-com/cli/rosentic-com-cli.yml
  title: ''
  type: CLI
  url: cli/rosentic-com-cli.yml
- group: agent
  href: https://artifacts.apis.io/rosentic-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/rosentic-com/sandbox/rosentic-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rosentic-com-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/rosentic-com/rate-limits/rosentic-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rosentic-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/rosentic-com/errors/rosentic-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rosentic-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rosentic-com/lifecycle/rosentic-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rosentic-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/rosentic-com/conventions/rosentic-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rosentic-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/rosentic-com/conformance/rosentic-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rosentic-com-conformance.yml
created: '2026-09-19'
description: 'Rosentic is a developer-tools company whose product checks the open branches in a git repository against each other before merge, catching the function-signature mismatches, HTTP route contract breaks, GraphQL/typed-schema conflicts and Protobuf/gRPC changes that pass CI on every branch individually and break main when parallel AI coding agents land together. The engine is deterministic tree-sitter AST analysis across 13 languages with no LLM in the scan path, shipped as a GitHub Action that runs on the consumer''s own runner and as rosentic-mcp on PyPI, a local MCP server and CLI with nine tools. Hosted surfaces on api.rosentic.com: Rosentic Remote, an MCP endpoint behind OAuth 2.1 with PKCE and dynamic client registration; an A2A 0.3.0 agent card with five skills and a live JSON-RPC endpoint; and a Bearer-key REST feed. Detection is free at every tier; paid plans buy stored history and quotas. No OpenAPI is published.'
finops:
- has_sources: true
  method: derived
  name: Rosentic Com Finops
  primary_unit: subscription
  service_category: ''
  slug: rosentic-com-finops
  template: false
image: https://raw.githubusercontent.com/Rosentic/cursor-plugin/main/assets/logo.png
layout: provider
mcp_servers:
- description: Rosentic ships MCP two ways and they are different products. (1) Rosentic Remote — a hosted Streamable-HTTP endpoint at https://api.rosentic.com/mcp, live since 2026-07-23 per the provider's changelog
  name: Rosentic MCP Server
  slug: rosentic-com-mcp-yml
modified: '2026-09-19'
name: Rosentic
nav: Providers
network: true
overview: 'Rosentic is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, CI/CD, Version Control, Static Analysis, and Merge Safety.


  Rosentic''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, changelog, support, and 24 more developer resources.'
plans:
- name: Rosentic Com Plans Pricing
  plan_count: 4
  slug: rosentic-com-plans-pricing
- name: Rosentic Com Price Estimates
  plan_count: 0
  slug: rosentic-com-price-estimates
random_paper: 11
rate_limits:
- limit_count: 1
  name: Rosentic Com Rate Limits
  slug: rosentic-com-rate-limits
scopes:
- name: Rosentic Com Scopes
  scope_count: 1
  slug: rosentic-com-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.3
  facets:
    access_clarity: 51.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 51.2
    discoverability: 80.0
    operational_transparency: 31.6
  previous_composite: 43.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rosentic-com/rosentic-com-2026-10-11T125419.png
security:
- kind: authentication
  name: Rosentic Com Authentication
  slug: rosentic-com-authentication
  summary_line: oauth2/http-bearer/none · 4 schemes
- kind: domain-security
  name: Rosentic Com Domain Security
  slug: rosentic-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rosentic-com
tags:
- Developer Tools
- CI/CD
- Version Control
- Static Analysis
- Merge Safety
- AI Coding Agents
- MCP
- A2A
- GitHub Actions
- Agent-Native
website: https://rosentic.com/
---
