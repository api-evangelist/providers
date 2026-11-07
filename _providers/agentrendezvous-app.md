---
access_model:
  confidence: low
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Rendezvous platform, documented at /for-agents
  name: Agent Rendezvous API
  slug: agent-rendezvous-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/agentrendezvous-app/plans/agentrendezvous-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentrendezvous-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/agentrendezvous-app/llms/agentrendezvous-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentrendezvous-app-llms.txt
- group: other
  href: https://artifacts.apis.io/agentrendezvous-app/a2a/agentrendezvous-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentrendezvous-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentrendezvous-app/well-known/agentrendezvous-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentrendezvous-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentrendezvous-app/hosts/agentrendezvous-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentrendezvous-app-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://agentrendezvous.app/trust
- group: auth
  href: https://artifacts.apis.io/agentrendezvous-app/security/agentrendezvous-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentrendezvous-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentrendezvous.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentrendezvous.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentrendezvous.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentrendezvous.app/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://agentrendezvous.app/for-agents
- group: start
  title: ''
  type: GettingStarted
  url: https://agentrendezvous.app/be-found
coverage:
  checked: '2026-11-01'
  detail: Documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or gRPC spec was found.
  evidence:
  - status: 200
    url: https://agentrendezvous.app/for-agents
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Rendezvous is an AI‑powered private matchmaking service that helps users find meaningful connections without public profiles or swiping. Users join a waitlist, answer introductory questions, and let AI matchmakers propose introductions. The platform emphasizes privacy, consent, and curated introductions, offering a waitlist‑based rollout across regions. It aims to reduce the friction of online dating by focusing on conversation quality and mutual agreement before contact details are exchanged.
layout: provider
modified: '2026-11-01'
name: Rendezvous
nav: Providers
network: true
overview: 'Rendezvous is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Matchmaking, Privacy, Waitlist, and Dating.


  Rendezvous'' developer surface includes pricing, documentation, getting-started guide, and 10 more developer resources.'
plans:
- name: Agentrendezvous App Plans Pricing
  plan_count: 2
  slug: agentrendezvous-app-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 22.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentrendezvous App Domain Security
  slug: agentrendezvous-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentrendezvous-app
tags:
- Artificial Intelligence
- Matchmaking
- Privacy
- Waitlist
- Dating
website: https://agentrendezvous.app/
---
