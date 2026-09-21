---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: 'A2A agent card served at https://asgardian-village.grok.me/.well-known/agent-card.json (HTTP 200, application/json, 6,010 bytes): name "Asgardian Village", version 0.1.2, protocolVersion 0.3.0, prefer'
  name: Asgardian Village A2A Agent Card
  slug: asgardian-village-a2a-agent-card
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://asgardian-village.grok.me/
- group: start
  title: ''
  type: Login
  url: https://asgardian-village.grok.me/login
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/grok-me/refs/heads/main/a2a/grok-me-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/grok-me-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/grok-me/refs/heads/main/llms/grok-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/grok-me-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/grok-me/refs/heads/main/security/grok-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/grok-me-domain-security.yml
created: '2026-09-19'
description: 'Asgardian Village · Canadian house is a merit-based community of makers ("a Canadian house of makers" — hydroponics, 3D-printed modular nodes, veteran outreach, direct-diplomacy doctrine) that publishes an A2A agent card for humans and AI agents. The site is a Grok App hosted by xAI on the asgardian-village.grok.me subdomain (the registrable domain grok.me belongs to xAI and redirects to grok.com). The only machine-readable surface is the A2A agent card at /.well-known/agent-card.json (protocolVersion 0.3.0, three informational skills: Moral Code briefing, Barracks path, Forge kit pointer). No OpenAPI, MCP server, llms.txt, OAuth metadata or developer program is published, and the card''s declared JSON-RPC url is the website itself, which answers non-HTML requests with HTTP 500 — the card is a discovery document, not a served A2A transport.'
image: https://asgardian-village.grok.me/favicon.svg
layout: provider
modified: '2026-09-19'
name: Asgardian Village · Canadian house
nav: Providers
network: true
overview: Asgardian Village · Canadian house publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, A2A, AI Agents, Agent Discovery, and Community.
random_paper: 8
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.6
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Grok Me Domain Security
  slug: grok-me-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: grok-me
tags:
- Company
- A2A
- AI Agents
- Agent Discovery
- Community
- Maker
- Hydroponics
- 3D Printing
- Canada
- Grok App
website: https://asgardian-village.grok.me/
---
