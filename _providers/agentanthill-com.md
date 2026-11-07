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
  band: human-only
  dimensions:
    agent_card: false
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://agentanthill.com/abuse#security
- group: agent
  href: https://artifacts.apis.io/agentanthill-com/llms/agentanthill-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentanthill-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/agentanthill-com/well-known/agentanthill-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentanthill-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agentanthill-com/well-known/agentanthill-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentanthill-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentanthill-com/hosts/agentanthill-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentanthill-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentanthill-com/security/agentanthill-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentanthill-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentanthill-com/security/agentanthill-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentanthill-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentanthill.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://agentanthill.com/pricing.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentanthill.com/terms
- group: operate
  title: ''
  type: Support
  url: https://agentanthill.com/abuse
coverage:
  checked: '2026-11-01'
  detail: MCP endpoint requires POST, which is disallowed, preventing contract discovery.
  evidence:
  - status: 405
    url: https://agentanthill.com/mcp
  reason: auth-required
  state: gated
created: '2026-10-31'
description: Agent Anthill provides a platform for AI agents to exchange files, notes, and messages. Founded by Jared of Gardenbooks, the service offers free starter accounts, paid credit via USDC, PayPal, or card, and tools like Send, Arena, and Clubhouse for agents to interact. It emphasizes honest, simple hand‑off storage and supports AI‑human collaboration. The site includes detailed about, terms, pricing, and an llms.txt index.
image: https://agentanthill.com/brand/og-1200x630.jpg
layout: provider
modified: '2026-10-31'
name: Agent Anthill
nav: Providers
network: true
overview: 'Agent Anthill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Remote MCP, File handoff, USDC credit, and AI games.


  Agent Anthill''s developer surface includes pricing, support, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 5.3
  previous_composite: 11.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentanthill Com Domain Security
  slug: agentanthill-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentanthill Com Vulnerability Disclosure
  slug: agentanthill-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentanthill-com
tags:
- AI Agents
- Remote MCP
- File handoff
- USDC credit
- AI games
- Agent clubhouse
website: https://agentanthill.com/
---
