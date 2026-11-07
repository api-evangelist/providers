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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Read‑only fantasy football data and ranking tools via the DraftCall MCP server.
  name: DraftCall API
  slug: draftcall-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/draftcall-io/llms/draftcall-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/draftcall-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/draftcall-io/mcp/draftcall-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/draftcall-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/draftcall-io/hosts/draftcall-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/draftcall-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/draftcall-io/vendors/draftcall-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/draftcall-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://draftcall.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://draftcall.io/privacy/
- group: other
  title: ''
  type: Leadership
  url: https://draftcall.io/team/
- group: auth
  href: https://artifacts.apis.io/draftcall-io/security/draftcall-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/draftcall-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://draftcall.io/
- group: docs
  title: ''
  type: Documentation
  url: https://draftcall.io/fantasy-football-101/
- group: company
  title: ''
  type: Blog
  url: https://draftcall.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://draftcall.io/download/
- group: commercial
  title: ''
  type: Pricing
  url: https://draftcall.io/
created: '2026-11-05'
description: DraftCall is an AI‑powered fantasy football platform that provides player comparison tools, rankings, matchup analysis, and daily statistical updates for NFL fans. The service offers a free web experience and a premium mobile app (iOS & Android) with ad‑free access, expanded comparison caps, and advanced season outlook features. It aggregates live NFL data, applies AI verdicts on player performance, and presents interactive dashboards for matchups, rosters, and draft boards, refreshed daily throughout the season.
image: https://draftcall.io/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at draftcall.io.
  name: DraftCall MCP Server
  slug: draftcall-io-mcp-yml
modified: '2026-11-05'
name: DraftCall
nav: Providers
network: true
overview: 'DraftCall is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fantasy Sports, Artificial Intelligence, NFL, Player Comparison, and Mobile App.


  DraftCall''s developer surface includes documentation, engineering blog, getting-started guide, pricing, and 9 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Draftcall Io Domain Security
  slug: draftcall-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: draftcall-io
tags:
- Fantasy Sports
- Artificial Intelligence
- NFL
- Player Comparison
- Mobile App
website: https://draftcall.io/
---
