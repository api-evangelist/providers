---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
api_count: 1
apis:
- description: Free, read-only, aggregate counts of acquirers on the Ayebot buyer register by sector and Southeast Asian market.
  name: Ayebot Buyer Index API
  slug: ayebot-buyer-index-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/ayebot-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ayebot-com/conformance/ayebot-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ayebot-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/ayebot-com/mcp/ayebot-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ayebot-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ayebot-com/mcp/ayebot-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ayebot-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ayebot-com/well-known/ayebot-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ayebot-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ayebot-com/hosts/ayebot-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ayebot-com-hosts.yml
- group: docs
  title: ''
  type: APIReference
  url: https://ayebot.com/developers
- group: auth
  href: https://artifacts.apis.io/ayebot-com/security/ayebot-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ayebot-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ayebot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ayebot.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://ayebot.com/start/
created: '2026-11-02'
description: Ayebot is an AI-powered business broker and deal engine for sell-side M&A in Singapore and Southeast Asia. It maps the buyer market, runs the process at machine speed, and keeps every number traceable. The judgement stays with the adviser. The platform is built by Aye Bot Pte. Ltd., offering AI-driven valuation, buyer matching, and advisory services to founders seeking exits.
image: https://ayebot.com/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at ayebot.com.
  name: Ayebot MCP Server
  slug: ayebot-com-mcp-yml
modified: '2026-11-02'
name: Ayebot
nav: Providers
network: true
overview: 'Ayebot is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI-powered business broker, M&A, Singapore, Southeast Asia, and Business Valuation.


  Ayebot''s developer surface includes API reference, documentation, getting-started guide, and 8 more developer resources.'
random_paper: 0
scopes:
- name: Ayebot Com Scopes
  scope_count: 0
  slug: ayebot-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.9
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 14.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ayebot Com Authentication
  slug: ayebot-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ayebot Com Domain Security
  slug: ayebot-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: buyer-index
  slug: ayebot-com-buyer-index
slug: ayebot-com
tags:
- AI-powered business broker
- M&A
- Singapore
- Southeast Asia
- Business Valuation
- Exit Readiness
website: https://ayebot.com/
---
