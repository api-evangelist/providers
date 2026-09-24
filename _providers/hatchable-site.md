---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://intentguard.hatchable.site
  baseurl_source: declared
  description: 'x402-paid AI model routing and prompt optimization from IntentGuard - 3 operations: a free routing preview (previewModelRoute), the paid router that selects the best model, cheapest acceptable alterna'
  name: IntentGuard Router API
  slug: intentguard-router-api
artifact_total: 6
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/llms/hatchable-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hatchable-site-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/a2a/hatchable-site-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hatchable-site-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/mcp/hatchable-site-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hatchable-site-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/mcp/hatchable-site-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hatchable-site-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/well-known/hatchable-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hatchable-site-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/overlays/hatchable-site-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hatchable-site-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/conventions/hatchable-site-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hatchable-site-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/errors/hatchable-site-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hatchable-site-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/lifecycle/hatchable-site-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hatchable-site-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/conformance/hatchable-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hatchable-site-conformance.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/plans/hatchable-site-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hatchable-site-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/rate-limits/hatchable-site-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hatchable-site-rate-limits.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/authentication/hatchable-site-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hatchable-site-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hatchable-site/refs/heads/main/security/hatchable-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hatchable-site-domain-security.yml
created: '2026-09-19'
description: IntentGuard operates IntentGuard Router, a machine-payable AI model-routing service for agents, hosted as a tenant app at intentguard.hatchable.site on the Hatchable AI-app platform. Before executing a task an agent posts it to the router, which returns the best model for quality, cost and speed, the cheapest acceptable alternative, a model to avoid, an optimized execution prompt, a fallback trigger and a savings estimate. A free preview endpoint returns task complexity, routing risk and a savings range; the paid route and a legacy image-intent preflight cost 0.0009 USDC per call, settled on Base mainnet through the x402 v2 protocol with no account or API key. The same two tools are exposed over a hosted Streamable HTTP MCP endpoint and described by a conformant A2A 1.0 agent card, an OpenAPI 3.1 document, an llms.txt, an OpenAI plugin manifest, an x402 service manifest and a provider-authored Agent Skill.
layout: provider
mcp_servers:
- description: ''
  name: IntentGuard Router
  slug: intentguard-router
modified: '2026-09-19'
name: IntentGuard
nav: Providers
network: true
overview: 'IntentGuard publishes 1 API on the [APIs.io](https://apis.io/) network: Router API. Tagged areas include Company, Artificial Intelligence, Agents, Model Routing, and Cost Optimization.


  IntentGuard''s developer surface includes documentation, pricing, authentication, and 15 more developer resources.'
plans:
- name: Hatchable Site Plans Pricing
  plan_count: 1
  slug: hatchable-site-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Hatchable Site Rate Limits
  slug: hatchable-site-rate-limits
score:
  band: thin
  composite: 31.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.0
    catalog_earned_first_party: 16.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 19.0
    discoverability: 72.2
    operational_transparency: 21.1
  previous_composite: 31.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hatchable Site Authentication
  slug: hatchable-site-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hatchable Site Domain Security
  slug: hatchable-site-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
- pay-per-call
- Prompt Optimization
- Agentic Payments
website: https://intentguard.hatchable.site/
---
