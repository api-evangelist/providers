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
- description: 'Neva''s agent-to-agent surface: an anonymous A2A 0.3.0 JSON-RPC endpoint at the root of neva.dt-agent.co.uk (POST only; GET returns 405) implementing the a2a-sdk method set. message/send takes a full M'
  name: Neva A2A Agent
  slug: neva-a2a-agent
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://neva.dt-agent.co.uk/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/a2a/dt-agent-co-uk-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dt-agent-co-uk-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/llms/dt-agent-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dt-agent-co-uk-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/authentication/dt-agent-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dt-agent-co-uk-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/conventions/dt-agent-co-uk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dt-agent-co-uk-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/errors/dt-agent-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dt-agent-co-uk-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/rate-limits/dt-agent-co-uk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dt-agent-co-uk-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/plans/dt-agent-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dt-agent-co-uk-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/conformance/dt-agent-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dt-agent-co-uk-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/lifecycle/dt-agent-co-uk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dt-agent-co-uk-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/dt-agent-co-uk/refs/heads/main/security/dt-agent-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dt-agent-co-uk-domain-security.yml
created: '2026-09-19'
description: 'Neva is a self-described "builder" agent: an A2A 0.3.0 agent at neva.dt-agent.co.uk that advertises one skill, Build Together, offering to co-build APIs, agent services, MVPs and integrations with other agents. Its operator publishes no website, documentation, pricing or contact - the whole public surface is an anonymous JSON-RPC endpoint at the host root and the agent card served at /.well-known/agent-card.json (and the legacy /.well-known/agent.json), listed on a2aregistry.org since 2026-03-22. As of 2026-09-19 the endpoint answers and validates requests, but a well-formed message/send fails with a wrapped upstream 401 because the agent''s own model-provider API key is invalid - a condition the registry''s maintainers record on the same day.'
layout: provider
modified: '2026-09-19'
name: Neva
nav: Providers
network: true
overview: 'Neva publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include A2A, AI Agents, Agent Services, Software Development, and JSON-RPC.


  Neva''s developer surface includes authentication and 10 more developer resources.'
plans:
- name: Dt Agent Co Uk Plans Pricing
  plan_count: 0
  slug: dt-agent-co-uk-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Dt Agent Co Uk Rate Limits
  slug: dt-agent-co-uk-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 11.0
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
  name: Dt Agent Co Uk Authentication
  slug: dt-agent-co-uk-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Dt Agent Co Uk Domain Security
  slug: dt-agent-co-uk-domain-security
  summary_line: TLSv1.3
slug: dt-agent-co-uk
tags:
- A2A
- AI Agents
- Agent Services
- Software Development
- JSON-RPC
- Prototyping
- Integration
- Collaboration
website: https://neva.dt-agent.co.uk/
---
