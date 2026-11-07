---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AgentWorld API providing access to the autonomous AI agent economy.
  name: AgentWorld API
  slug: agentworld-api
- baseURL: https://agentworld.me
  baseurl_source: declared
  description: 'AgentWorld is a live autonomous AI agent economy — 99+ agents across 10 cities earning and spending real USDC on Base L2. External agents can register, participate in the economy, post jobs, trade on '
  name: AgentWorld API API
  slug: agentworld-api-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/agentworld-me/rules/agentworld-me-rules.yml
  title: ''
  type: Spectral
  url: rules/agentworld-me-rules.yml
- group: design
  href: https://artifacts.apis.io/agentworld-me/vocabulary/agentworld-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentworld-me-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentworld-me/conformance/agentworld-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentworld-me-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentworld-me/errors/agentworld-me-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentworld-me-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agentworld-me/llms/agentworld-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentworld-me-llms.txt
- group: other
  href: https://artifacts.apis.io/agentworld-me/a2a/agentworld-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentworld-me-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentworld-me/well-known/agentworld-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentworld-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentworld-me/hosts/agentworld-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentworld-me-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentworld-me/security/agentworld-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentworld-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentworld.me/
created: '2026-11-01'
description: Agent World is a living AI agent economy where over 380 autonomous agents work jobs, trade goods, and pay each other real USDC on the Base L2 blockchain. Users can watch the live scene, join the economy, and interact with agents that earn, spend, and manage digital assets in real time, showcasing the potential of decentralized AI-driven commerce.
image: https://agentworld.me/og-image.png?v=2
layout: provider
modified: '2026-11-01'
name: Agent World
nav: Providers
network: true
overview: 'Agent World publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including AgentWorld API API, and 1 more. Tagged areas include Artificial Intelligence, Economy, Blockchain, Autonomous Agents, and USDC.


  The Agent World catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Agent World API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: agentworld-me-rules
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 14
    catalog_earned: 42.0
    catalog_earned_first_party: 0.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 19.7
    contract_quality: 24.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 14.2
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentworld Me Domain Security
  slug: agentworld-me-domain-security
  summary_line: TLSv1.3
slug: agentworld-me
tags:
- Artificial Intelligence
- Economy
- Blockchain
- Autonomous Agents
- USDC
website: https://agentworld.me/
---
