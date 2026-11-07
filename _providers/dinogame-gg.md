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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dinogame-gg/llms/dinogame-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dinogame-gg-llms.txt
- group: agent
  href: https://artifacts.apis.io/dinogame-gg/mcp/dinogame-gg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dinogame-gg-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dinogame-gg/well-known/dinogame-gg-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dinogame-gg-well-known.yml
- group: other
  href: https://artifacts.apis.io/dinogame-gg/hosts/dinogame-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dinogame-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/dinogame-gg/vendors/dinogame-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dinogame-gg-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dinogame-gg/security/dinogame-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dinogame-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dinogame.gg/
- group: company
  title: ''
  type: About
  url: https://dinogame.gg/about/
- group: operate
  title: ''
  type: Contact
  url: https://dinogame.gg/contact/
- group: commercial
  title: ''
  type: Privacy
  url: https://dinogame.gg/privacy/
- group: company
  title: ''
  type: Blog
  url: https://dinogame.gg/blog/
coverage:
  checked: '2026-11-05'
  detail: Only an MCP JSON endpoint is available, no OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://api.dinogame.gg/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dinogame.gg is a curated library of free browser games, offering over 80 titles across arcade, puzzle, strategy, card, word, casino, and memory categories. The site started as a tribute to Google Chrome’s offline T‑Rex Easter egg and now provides instant, no‑login, no‑tracking gameplay directly in the browser. It emphasizes privacy, no in‑app purchases, and a clean experience for players of all ages.
layout: provider
mcp_servers:
- description: Remote MCP server at dinogame.gg.
  name: dinogame-gg MCP Server
  slug: dinogame-gg-mcp-yml
modified: '2026-11-05'
name: dinogame-gg
nav: Providers
network: true
overview: 'dinogame-gg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Games, Free, Browser, and No-Tracking.


  dinogame-gg''s developer surface includes privacy policy, engineering blog, and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 45.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dinogame Gg Domain Security
  slug: dinogame-gg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dinogame-gg
tags:
- Company
- Games
- Free
- Browser
- No-Tracking
website: https://dinogame.gg/
---
