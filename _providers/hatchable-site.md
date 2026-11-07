---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
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
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://intentguard.hatchable.site
  baseurl_source: spec
  description: The Intent Check API from IntentGuard — 1 operation(s) for intent check.
  name: IntentGuard Intent Check API
  slug: hatchable-site-intent-check-api
- baseURL: https://intentguard.hatchable.site
  baseurl_source: spec
  description: The Route API from IntentGuard — 1 operation(s) for route.
  name: IntentGuard Route API
  slug: hatchable-site-route-api
- baseURL: https://intentguard.hatchable.site
  baseurl_source: spec
  description: The Router Preview API from IntentGuard — 1 operation(s) for router preview.
  name: IntentGuard Router Preview API
  slug: hatchable-site-router-preview-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Blog
  url: https://intentguard.hatchable.site/blog/
- group: company
  title: ''
  type: Website
  url: https://intentguard.hatchable.site/
- group: docs
  title: ''
  type: Documentation
  url: https://intentguard.hatchable.site/
- group: commercial
  title: ''
  type: Pricing
  url: https://intentguard.hatchable.site/.well-known/x402-service.json
- group: agent
  href: https://artifacts.apis.io/hatchable-site/llms/hatchable-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hatchable-site-llms.txt
- group: other
  href: https://artifacts.apis.io/hatchable-site/a2a/hatchable-site-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hatchable-site-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hatchable-site/mcp/hatchable-site-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hatchable-site-mcp.yml
- group: build
  href: https://artifacts.apis.io/hatchable-site/mcp/hatchable-site-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hatchable-site-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hatchable-site/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/hatchable-site/well-known/hatchable-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hatchable-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/hatchable-site/overlays/hatchable-site-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hatchable-site-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/hatchable-site/conventions/hatchable-site-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hatchable-site-conventions.yml
- group: design
  href: https://artifacts.apis.io/hatchable-site/errors/hatchable-site-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hatchable-site-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hatchable-site/lifecycle/hatchable-site-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hatchable-site-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hatchable-site/conformance/hatchable-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hatchable-site-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/hatchable-site/plans/hatchable-site-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hatchable-site-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hatchable-site/rate-limits/hatchable-site-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hatchable-site-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/hatchable-site/authentication/hatchable-site-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hatchable-site-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hatchable-site/security/hatchable-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hatchable-site-domain-security.yml
created: '2026-09-19'
description: IntentGuard operates IntentGuard Router, a machine-payable AI model-routing service for agents, hosted as a tenant app at intentguard.hatchable.site on the Hatchable AI-app platform. Before executing a task an agent posts it to the router, which returns the best model for quality, cost and speed, the cheapest acceptable alternative, a model to avoid, an optimized execution prompt, a fallback trigger and a savings estimate. A free preview endpoint returns task complexity, routing risk and a savings range; the paid route and a legacy image-intent preflight cost 0.0009 USDC per call, settled on Base mainnet through the x402 v2 protocol with no account or API key. The same two tools are exposed over a hosted Streamable HTTP MCP endpoint and described by a conformant A2A 1.0 agent card, an OpenAPI 3.1 document, an llms.txt, an OpenAI plugin manifest, an x402 service manifest and a provider-authored Agent Skill.
layout: provider
mcp_servers:
- description: Remote MCP server at intentguard.hatchable.site over streamable HTTP; 2 tools listed.
  name: IntentGuard Router
  slug: intentguard-router
modified: '2026-10-06'
name: IntentGuard
nav: Providers
network: true
overview: 'IntentGuard publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Intent Check API, Route API, and Router Preview API. Tagged areas include Company, Artificial Intelligence, Agents, Model Routing, and Cost Optimization.


  The IntentGuard catalog on APIs.io includes 1 Spectral governance ruleset.


  IntentGuard''s developer surface includes engineering blog, documentation, pricing, authentication, and 15 more developer resources.'
plans:
- name: Hatchable Site Plans Pricing
  plan_count: 1
  slug: hatchable-site-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Hatchable Site Rate Limits
  slug: hatchable-site-rate-limits
rules:
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: IntentGuard API Rules
  rule_count: 27
  severity_counts:
    error: 25
    hint: 0
    info: 1
    warn: 1
  slug: hatchable-site-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 50.5
    catalog_earned_first_party: 16.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 31.6
    contract_governance: 31.8
    contract_quality: 48.3
    developer_ergonomics: 21.4
    discoverability: 63.3
    operational_transparency: 21.1
  previous_composite: 32.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/hatchable-site/hatchable-site-2026-10-11T105134.png
security:
- kind: authentication
  name: Hatchable Site Authentication
  slug: hatchable-site-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hatchable Site Domain Security
  slug: hatchable-site-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: intentguard-router
  slug: hatchable-site-router
slug: hatchable-site
tags:
- Company
- Artificial Intelligence
- Agents
- Model Routing
- Cost Optimization
- x402
- MCP
- A2A
- Pay-per-call
- Prompt Optimization
- Agentic Payments
website: https://intentguard.hatchable.site/
---
