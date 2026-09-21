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
  score: 10.8
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'Anonymous A2A 0.3.0 agent at https://baconhollow.com (JSON-RPC, POST only). Four skills: portfolio-status, weather-forecast-edge, market-scan and oracle-picks. message/send and tasks/get are implement'
  name: Bot Hub (A2A)
  slug: bot-hub-a2a
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/security/baconhollow-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baconhollow-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baconhollow.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/a2a/baconhollow-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/baconhollow-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/well-known/baconhollow-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baconhollow-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/authentication/baconhollow-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/baconhollow-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/conformance/baconhollow-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baconhollow-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/lifecycle/baconhollow-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/baconhollow-com-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/llms/baconhollow-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baconhollow-com-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/plans/baconhollow-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/baconhollow-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/rate-limits/baconhollow-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/baconhollow-com-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/packages/baconhollow-com-packages.yml
  title: ''
  type: Packages
  url: packages/baconhollow-com-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/baconhollow-com/refs/heads/main/regulatory/baconhollow-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/baconhollow-com-regulatory-posture.yml
created: '2026-09-19'
description: 'Bot Hub is an anonymous, read-only A2A agent for Kalshi prediction markets served from baconhollow.com and listed on a2aregistry.org. Its agent card (protocolVersion 0.3.0, JSON-RPC transport, no authentication) declares four skills — portfolio status for a set of trading bots, weather-forecast edge on Kalshi temperature markets computed from GFS forecasts with a calibrated normal CDF model, a market scan, and "Weather Oracle" trading picks with tier-based access and a buyer sign-up — and a live anonymous message/send returned a six-strategy catalog, every strategy marked "testing" with no live track record and one "deprecated". The agent is the entire published surface: the apex answers 405 to GET, there is no www host, no web page, documentation, OpenAPI, MCP server, llms.txt, pricing, terms, privacy policy or operator identity anywhere, and the registry lists the author as Unknown. The domain was registered 2026-02-20.'
layout: provider
modified: '2026-09-19'
name: Bot Hub
nav: Providers
network: true
overview: 'Bot Hub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, A2A, Autonomous Agents, Prediction Markets, and Kalshi.


  Bot Hub''s developer surface includes authentication and 11 more developer resources.'
plans:
- name: Baconhollow Com Plans Pricing
  plan_count: 0
  slug: baconhollow-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Baconhollow Com Rate Limits
  slug: baconhollow-com-rate-limits
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 2.8
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Baconhollow Com Authentication
  slug: baconhollow-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Baconhollow Com Domain Security
  slug: baconhollow-com-domain-security
  summary_line: TLSv1.3
slug: baconhollow-com
tags:
- AI Agents
- A2A
- Autonomous Agents
- Prediction Markets
- Kalshi
- Trading Signals
- Weather
- agent-native
website: https://baconhollow.com/
---
