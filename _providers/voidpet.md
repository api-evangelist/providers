---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Discovery API from Voidpet — 1 operation(s) for discovery.
  name: Voidpet Discovery API
  slug: voidpet-discovery-api
- description: The Health API from Voidpet — 1 operation(s) for health.
  name: Voidpet Health API
  slug: voidpet-health-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Voidpet Public Discovery API
  slug: open-voidpet-discovery-api
- collection_type: open
  name: Voidpet Public Discovery Health API
  slug: open-voidpet-health-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/voidpet-discovery-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voidpet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/voidpet-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/voidpet-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/voidpet-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/voidpet-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/voidpet-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/voidpet-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://voidpet.com/.well-known/api-docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://voidpet.com/.well-known/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://voidpet.com/o/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://voidpet.com/o/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://voidpet.com/o/privacy
created: '2026-07-17'
description: Voidpet is a creative games studio behind emotion-inspired games, stories, characters, and community — including Voidpet Dungeon, a turn-based roguelite RPG about befriending and battling emotion-inspired creatures, and Voidpet Garden, a mental-health companion game for collecting emotions and practicing self care. Beyond the games, Voidpet publishes a small, public, read-only Discovery API (OpenAPI 3.1) plus a hosted Model Context Protocol server and a packaged Agent Skill so agents can discover its public products, pages, and legal documents. The discovery surface exposes no accounts, game state, or authenticated actions — it is agent-facing metadata only.
image: https://voidpet.com/ogimage.png
layout: provider
mcp_servers:
- description: ''
  name: voidpet-mcp.yml
  slug: voidpet-mcpyml
modified: '2026-07-21'
name: Voidpet
nav: Providers
network: true
overview: 'Voidpet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Discovery API and Health API. Tagged areas include Company, Games, Gaming, Mental Health, and Wellness.


  Voidpet''s developer surface includes authentication, documentation, API reference, engineering blog, and 10 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 41.5
  delta: 8.2
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 16.7
    contract_quality: 44.1
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 33.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
security:
- kind: authentication
  name: Voidpet Authentication
  slug: voidpet-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Voidpet Domain Security
  slug: voidpet-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: voidpet
tags:
- Company
- Games
- Gaming
- Mental Health
- Wellness
- Discovery
- Agents
- MCP
- Read Only
---
