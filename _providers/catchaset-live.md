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
    agent_card: false
    agent_skills: unknown
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
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/catchaset-live/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/catchaset-live/mcp/catchaset-live-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/catchaset-live-mcp.yml
- group: other
  href: https://artifacts.apis.io/catchaset-live/hosts/catchaset-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/catchaset-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/catchaset-live/vendors/catchaset-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/catchaset-live-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://catchaset.live/auth/login
- group: auth
  href: https://artifacts.apis.io/catchaset-live/security/catchaset-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/catchaset-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://catchaset.live/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://catchaset.live/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://catchaset.live/privacy
coverage:
  checked: '2026-11-04'
  detail: No machine‑readable API specification (OpenAPI/AsyncAPI/GraphQL) was found despite probing known hosts.
  evidence:
  - status: 200
    url: https://catchaset.live/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CatchaSet is a live‑music discovery platform focused on Austin, helping users find concerts that match their musical tastes. The service aggregates event data, provides personalized recommendations, and offers tools for browsing venues, artists, and upcoming shows. It aims to connect music fans with live experiences through an intuitive web interface and curated listings.
image: https://catchaset.live/assets/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at catchaset.live.
  name: CatchaSet MCP Server
  slug: catchaset-live-mcp-yml
modified: '2026-11-04'
name: CatchaSet
nav: Providers
network: true
overview: CatchaSet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Live Events, Discovery, Austin, and Entertainment.
random_paper: 5
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Catchaset Live Domain Security
  slug: catchaset-live-domain-security
  summary_line: TLSv1.3 · DMARC
slug: catchaset-live
tags:
- Music
- Live Events
- Discovery
- Austin
- Entertainment
website: https://catchaset.live/
---
