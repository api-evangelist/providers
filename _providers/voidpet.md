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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://voidpet.com
  baseurl_source: spec
  description: The Discovery API from Voidpet — 1 operation(s) for discovery.
  name: Voidpet Discovery API
  slug: voidpet-discovery-api
- baseURL: https://voidpet.com
  baseurl_source: spec
  description: The Health API from Voidpet — 1 operation(s) for health.
  name: Voidpet Health API
  slug: voidpet-health-api
artifact_total: 9
collections:
- collection_type: open
  name: Voidpet Public Discovery API
  slug: open-voidpet-discovery-api
- collection_type: open
  name: Voidpet Public Discovery Health API
  slug: open-voidpet-health-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.voidpet.com/
- group: other
  href: https://artifacts.apis.io/voidpet/overlays/voidpet-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/voidpet-discovery-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/voidpet/security/voidpet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voidpet-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/voidpet/authentication/voidpet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voidpet-authentication.yml
- group: agent
  href: https://artifacts.apis.io/voidpet/mcp/voidpet-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/voidpet-mcp.yml
- group: agent
  href: https://artifacts.apis.io/voidpet/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/voidpet/well-known/voidpet-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voidpet-well-known.yml
- group: agent
  href: https://artifacts.apis.io/voidpet/llms/voidpet-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voidpet-llms.txt
- group: design
  href: https://artifacts.apis.io/voidpet/conformance/voidpet-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voidpet-conformance.yml
- group: design
  href: https://artifacts.apis.io/voidpet/lifecycle/voidpet-lifecycle.yml
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
- description: Read-only, public MCP server exposing Voidpet's public products, pages, and legal-document discovery metadata. No authentication; no account or game-state access.
  name: Voidpet MCP Server
  slug: voidpet-public-site
modified: '2026-07-21'
name: Voidpet
nav: Providers
network: true
overview: 'Voidpet publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Discovery API and Health API. Tagged areas include Company, Games, Gaming, Mental Health, and Wellness.


  Voidpet''s developer surface includes authentication, documentation, API reference, engineering blog, and 11 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.5
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 38.6
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 29.3
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
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/voidpet/voidpet-2026-09-02T170212.png
security:
- kind: authentication
  name: Voidpet Authentication
  slug: voidpet-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Voidpet Domain Security
  slug: voidpet-domain-security
  summary_line: TLSv1.3 · DNSSEC
skill_count: 2
skills:
- name: voidpet-discovery-api
  slug: voidpet-discovery-api
- name: voidpet-site-guide
  slug: voidpet-site-guide
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
website: https://www.voidpet.com/
---
