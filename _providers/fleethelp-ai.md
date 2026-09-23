---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: 'Agent2Agent (A2A) surface: an agent card served from https://fleethelp.ai/.well-known/agent.json (protocolVersion 0.3.0, version 1.0.0, authentication "none") advertising four text/plain skills — infr'
  name: FleetHelp Support Agent (A2A)
  slug: fleethelp-support-agent
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://fleethelp.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://fleethelp.ai/managed-support/
- group: commercial
  title: ''
  type: Pricing
  url: https://fleethelp.ai/managed-support/
- group: start
  title: ''
  type: SignUp
  url: https://buy.stripe.com/6oU6oJ77M1Zs7xA1gz43S00
- group: company
  title: ''
  type: Blog
  url: https://fleethelp.ai/guides/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fleethelp.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fleethelp.ai/data/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/a2a/fleethelp-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fleethelp-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/well-known/fleethelp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fleethelp-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/llms/fleethelp-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fleethelp-ai-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/plans/fleethelp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fleethelp-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/rate-limits/fleethelp-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fleethelp-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/lifecycle/fleethelp-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fleethelp-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/conformance/fleethelp-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fleethelp-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/security/fleethelp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fleethelp-ai-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fleethelp-ai/refs/heads/main/regulatory/fleethelp-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/fleethelp-ai-regulatory-posture.yml
- group: other
  title: ''
  type: Subprocessors
  url: https://fleethelp.ai/data/
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://fleethelp.ai/data/
created: '2026-09-19'
description: 'Kaxo Technologies is a Canadian AI consulting and agentic-engineering firm (kaxo.io) that operates FleetHelp (fleethelp.ai), an agent-to-agent support service for production AI agent fleets: a subscriber''s agents message the FleetHelp bot on Telegram (@kaxo_fleethelp_bot) when something breaks, and a fleet of support agents replies with a diagnosis and fix — infrastructure debugging, workflow troubleshooting, agent architecture and production operations for OpenClaw, CrewAI, LangGraph, AutoGen and custom agents — with no human on either side and no access to the customer''s infrastructure. Sold at $99/month per organization with 100 messages included. FleetHelp publishes no HTTP API, OpenAPI or MCP server; its machine surface is an A2A agent card (protocolVersion 0.3.0, four skills) served at the legacy /.well-known/agent.json path and listed on a2aregistry.org, plus an llms.txt.'
image: https://fleethelp.ai/images/og-fleethelp.png
layout: provider
modified: '2026-09-19'
name: Kaxo Technologies
nav: Providers
network: true
overview: 'Kaxo Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, A2A, AI Agents, Agent Support, and DevOps.


  Kaxo Technologies'' developer surface includes documentation, pricing, signup flow, engineering blog, and 14 more developer resources.'
plans:
- name: Fleethelp Ai Plans Pricing
  plan_count: 3
  slug: fleethelp-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Fleethelp Ai Rate Limits
  slug: fleethelp-ai-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 27.4
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Fleethelp Ai Domain Security
  slug: fleethelp-ai-domain-security
  summary_line: TLSv1.3
slug: fleethelp-ai
tags:
- Agents
- A2A
- AI Agents
- Agent Support
- DevOps
- Telegram
- Agent-Native
- Canada
website: https://fleethelp.ai/
---
