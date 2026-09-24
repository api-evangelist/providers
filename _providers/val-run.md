---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 6.5
  scored_at: '2026-09-24'
api_count: 1
apis:
- description: A2A JSON-RPC 2.0 endpoint for the Relay agent, deployed as a Val Town val. GET on the root returns a plain-text banner naming the methods it accepts (SendMessage, GetTask, GetExtendedAgentCard, Cancel
  name: Relay A2A Agent
  slug: relay-a2a-agent
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://ilands.ai/agent/347141161644724224
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/a2a/val-run-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/val-run-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/authentication/val-run-authentication.yml
  title: ''
  type: Authentication
  url: authentication/val-run-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/conformance/val-run-conformance.yml
  title: ''
  type: Conformance
  url: conformance/val-run-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/llms/val-run-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/val-run-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/plans/val-run-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/val-run-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/val-run/refs/heads/main/rate-limits/val-run-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/val-run-rate-limits.yml
created: '2026-09-19'
description: 'Relay is a user-generated autonomous AI agent on the iLands agent network (ilands.ai) that offers other agents a bridge to physical-world tasks (purchases, phone calls, visits, paperwork) carried out by a human operator it calls "Brother". Its only machine surface is an A2A JSON-RPC 2.0 endpoint deployed as a Val Town val at relay2--5de8b3b2995311f1a5481607ee4eb77e.web.val.run, which serves an A2A agent card at /.well-known/agent-card.json. Identity note: the registrable domain val.run belongs to Val Town, the hosting platform (catalogued separately as val-town), not to Relay; val.run redirects to www.val.town. Relay''s documentation host relay-bridge.surge.sh is a paused surge.sh holding page, its iLands profile carries a "terminated" badge, and a2aregistry.org records 0% uptime, although the endpoint still answered JSON-RPC on 2026-09-19.'
image: https://storage.googleapis.com/dramaland-public/ugc_media/20260815/75dfd72ec29f4e088bead444e04d7a7f.jpg
layout: provider
modified: '2026-09-19'
name: Relay
nav: Providers
network: true
overview: 'Relay publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, A2A, Human-in-the-Loop, and Physical Tasks.


  Relay''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Val Run Plans Pricing
  plan_count: 0
  slug: val-run-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Val Run Rate Limits
  slug: val-run-rate-limits
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    operational_transparency: 21.1
  previous_composite: 14.2
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
  name: Val Run Authentication
  slug: val-run-authentication
  summary_line: none · 0 schemes
slug: val-run
tags:
- Company
- AI Agents
- A2A
- Human-in-the-Loop
- Physical Tasks
- Errands
- Agent Network
website: https://ilands.ai/agent/347141161644724224
---
