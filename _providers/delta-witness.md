---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The browser verification API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for browser verification.
  name: DELTA Witness — Trust Layer for Autonomous Actions browser verification API
  slug: delta-witness-browser-verification-api
- baseURL: https://delta-witness-partner-gateway.ruphussten.workers.dev
  baseurl_source: declared
  description: The Capture API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for capture.
  name: DELTA Witness — Trust Layer for Autonomous Actions Capture API
  slug: delta-witness-capture-api
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The Demo API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for demo.
  name: DELTA Witness — Trust Layer for Autonomous Actions Demo API
  slug: delta-witness-demo-api
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The guarded-action-pilot API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for guarded-action-pilot.
  name: DELTA Witness — Trust Layer for Autonomous Actions Guarded Action Pilot API
  slug: delta-witness-guarded-action-pilot-api
- baseURL: https://delta-witness-partner-gateway.ruphussten.workers.dev
  baseurl_source: declared
  description: The Health API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for health.
  name: DELTA Witness — Trust Layer for Autonomous Actions Health API
  slug: delta-witness-health-api
- baseURL: https://delta-witness-partner-gateway.ruphussten.workers.dev
  baseurl_source: declared
  description: The Preflight API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for preflight.
  name: DELTA Witness — Trust Layer for Autonomous Actions Preflight API
  slug: delta-witness-preflight-api
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The preflight autonomous action API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for preflight autonomous action.
  name: DELTA Witness — Trust Layer for Autonomous Actions preflight autonomous action API
  slug: delta-witness-preflight-autonomous-action-api
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The Proofs API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for proofs.
  name: DELTA Witness — Trust Layer for Autonomous Actions Proofs API
  slug: delta-witness-proofs-api
- baseURL: https://delta-witness-api.ruphussten.workers.dev
  baseurl_source: spec
  description: The Quote API from DELTA Witness — Trust Layer for Autonomous Actions — 1 operation(s) for quote.
  name: DELTA Witness — Trust Layer for Autonomous Actions Quote API
  slug: delta-witness-quote-api
- baseURL: https://delta-witness-partner-gateway.ruphussten.workers.dev
  baseurl_source: declared
  description: The Watch API from DELTA Witness — Trust Layer for Autonomous Actions — 2 operation(s) for watch.
  name: DELTA Witness — Trust Layer for Autonomous Actions Watch API
  slug: delta-witness-watch-api
artifact_total: 19
common:
- group: agent
  title: ''
  type: AgentSkill
  url: https://delta-witness-api.ruphussten.workers.dev/SKILL.md
- group: company
  title: ''
  type: Website
  url: https://delta-witness-api.ruphussten.workers.dev
- group: auth
  href: https://artifacts.apis.io/delta-witness/security/delta-witness-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/delta-witness-domain-security.yml
- group: build
  href: https://artifacts.apis.io/delta-witness/packages/delta-witness-packages.yml
  title: ''
  type: SDKs
  url: packages/delta-witness-packages.yml
- group: build
  href: https://artifacts.apis.io/delta-witness/packages/delta-witness-packages.yml
  title: ''
  type: Packages
  url: packages/delta-witness-packages.yml
- group: agent
  href: https://artifacts.apis.io/delta-witness/mcp/delta-witness-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/delta-witness-mcp.yml
- group: build
  href: https://artifacts.apis.io/delta-witness/mcp/delta-witness-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/delta-witness-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/delta-witness/a2a/delta-witness-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/delta-witness-a2a.yml
- group: agent
  href: https://artifacts.apis.io/delta-witness/well-known/delta-witness-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/delta-witness-well-known.yml
- group: other
  href: https://artifacts.apis.io/delta-witness/overlays/delta-witness-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/delta-witness-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/delta-witness/conformance/delta-witness-conformance.yml
  title: ''
  type: Conformance
  url: conformance/delta-witness-conformance.yml
- group: design
  href: https://artifacts.apis.io/delta-witness/errors/delta-witness-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/delta-witness-problem-types.yml
- group: design
  href: https://artifacts.apis.io/delta-witness/lifecycle/delta-witness-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/delta-witness-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/delta-witness/authentication/delta-witness-authentication.yml
  title: ''
  type: Authentication
  url: authentication/delta-witness-authentication.yml
- group: design
  href: https://artifacts.apis.io/delta-witness/conventions/delta-witness-conventions.yml
  title: ''
  type: Conventions
  url: conventions/delta-witness-conventions.yml
- group: design
  href: https://artifacts.apis.io/delta-witness/conventions/delta-witness-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/delta-witness-conventions.yml
- group: commercial
  href: https://artifacts.apis.io/delta-witness/plans/delta-witness-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/delta-witness-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/delta-witness/rate-limits/delta-witness-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/delta-witness-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/delta-witness/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/15998194110/delta-witness
created: '2026-09-11'
description: Machine-verifiable capture and preflight verification of public web sources. Returns timestamped content hashes plus a public verifier, keeping raw capture artifacts private. Access is payment-gated via the x402 v2 protocol using USDC on Base mainnet. Proves observation and change, not truth.
layout: provider
mcp_servers:
- description: First-party MCP server exposing the paid DELTA Witness Capture and Guard (preflight) tools for public-source observation before autonomous actions.
  name: DELTA Witness MCP
  slug: delta-witness-mcp
modified: '2026-09-11'
name: DELTA Witness — Trust Layer for Autonomous Actions
nav: Providers
network: true
overview: 'DELTA Witness — Trust Layer for Autonomous Actions publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including browser verification API, Capture API, Demo API, and 7 more. Tagged areas include web-verification, proof-of-observation, page-state-monitoring, content-hashing, and agent-guardrails.


  The DELTA Witness — Trust Layer for Autonomous Actions catalog on APIs.io includes 1 Spectral governance ruleset.


  DELTA Witness — Trust Layer for Autonomous Actions'' developer surface includes authentication and 19 more developer resources.'
plans:
- name: Delta Witness Plans Pricing
  plan_count: 3
  slug: delta-witness-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Delta Witness Rate Limits
  slug: delta-witness-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: DELTA Witness — Trust Layer for Autonomous Actions API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: delta-witness-rules
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 31.6
    contract_governance: 13.6
    contract_quality: 48.1
    developer_ergonomics: 39.8
    discoverability: 60.0
    operational_transparency: 2.6
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 70.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/delta-witness/delta-witness-2026-10-11T103646.png
security:
- kind: authentication
  name: Delta Witness Authentication
  slug: delta-witness-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Delta Witness Domain Security
  slug: delta-witness-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: delta-witness-guarded-action-pilot
  slug: delta-witness-guarded-action-pilot
- name: delta-witness-preflight-guard
  slug: delta-witness-preflight-guard
- name: delta-witness
  slug: delta-witness-skill
slug: delta-witness
tags:
- web-verification
- proof-of-observation
- page-state-monitoring
- content-hashing
- agent-guardrails
- preflight-checks
- x402 Payments
- Pay-Per-Use
- base-usdc
- Autonomous Agents
- MCP
- A2A
- Agent Skills
- Trust and Safety
website: https://delta-witness-api.ruphussten.workers.dev
---
