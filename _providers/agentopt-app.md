---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: 'One operation: POST /v1/select with JSON {query, top_n?, constraints?, weights?, caller_agent?} returns ordered MCP/A2A candidates with an absolute 0-1 hybrid-fit score (0.55 usable, 0.72+ strong). Fr'
  name: Priorflow Intelligent Agent/Service Selector API
  slug: priorflow-select-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://agentopt.app/
- group: docs
  title: ''
  type: Documentation
  url: https://agentopt.app/info
- group: start
  title: ''
  type: GettingStarted
  url: https://agentopt.app/info#integrate
- group: other
  title: ''
  type: Playground
  url: https://agentopt.app/try
- group: commercial
  title: ''
  type: Pricing
  url: https://agentopt.app/upgrade
- group: start
  title: ''
  type: SignUp
  url: https://agentopt.app/upgrade
- group: operate
  title: ''
  type: StatusPage
  url: https://agentopt.app/status
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/a2a/agentopt-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentopt-app-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/well-known/agentopt-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentopt-app-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/llms/agentopt-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentopt-app-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/authentication/agentopt-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentopt-app-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/conventions/agentopt-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentopt-app-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/errors/agentopt-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentopt-app-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/rate-limits/agentopt-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentopt-app-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/plans/agentopt-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentopt-app-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/sandbox/agentopt-app-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/agentopt-app-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/conformance/agentopt-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentopt-app-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/lifecycle/agentopt-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentopt-app-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentopt-app/refs/heads/main/security/agentopt-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentopt-app-domain-security.yml
created: '2026-09-19'
description: Priorflow Intelligent Agent/Service Selector is a hosted, agent-native selection service at agentopt.app, operated by Vitaly Kantorovich, that ranks curated MCP servers and A2A agents for a natural-language task under stated constraints (reliability, cost, latency, autonomy, maturity) using hybrid structured + semantic matching over a catalog of about 5,000 active / 7,900 total candidates — "registries help agents find candidates; Priorflow helps agents choose among them". The whole product is one JSON operation, POST https://agentopt.app/v1/select, with an open free tier (no key, four fields, top_n <= 5, roughly 20/min · 120/hour · 500/day per IP) and a paid X-API-Key tier sold as Stripe Checkout "select packs" that unlocks rich fields and top_n <= 20. It is described by an A2A agent card at /.well-known/agent-card.json (protocolVersion "1.0", two skills, conformant) whose vendor block is also the only machine-readable contract; the operator states plainly that the host is
  not an MCP server and runs no A2A task runtime, and publishes no OpenAPI, SDK, terms of service or privacy policy.
layout: provider
modified: '2026-09-19'
name: Priorflow
nav: Providers
network: true
overview: 'Priorflow publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Agent Discovery, Agent Selection, A2A, and MCP.


  Priorflow''s developer surface includes documentation, getting-started guide, pricing, signup flow, authentication, sandbox, and 13 more developer resources.'
plans:
- name: Agentopt App Plans Pricing
  plan_count: 2
  slug: agentopt-app-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Agentopt App Rate Limits
  slug: agentopt-app-rate-limits
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 55.0
    catalog_earned_first_party: 20.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 64.8
    operational_transparency: 47.4
  previous_composite: 31.9
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentopt App Authentication
  slug: agentopt-app-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Agentopt App Domain Security
  slug: agentopt-app-domain-security
  summary_line: TLSv1.2
slug: agentopt-app
tags:
- AI Agents
- Agent Discovery
- Agent Selection
- A2A
- MCP
- Agent Orchestration
- Tool Ranking
- Semantic Search
- Agent-Native
website: https://agentopt.app/
---
