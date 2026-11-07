---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Model Context Protocol server providing AI strategy frameworks via JSON-RPC over HTTP.
  name: Boardroom Bob MCP
  slug: boardroom-bob-mcp
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/boardroombob-com/plans/boardroombob-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boardroombob-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/boardroombob-com/llms/boardroombob-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boardroombob-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/boardroombob-com/mcp/boardroombob-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boardroombob-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/boardroombob-com/hosts/boardroombob-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boardroombob-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boardroombob-com/vendors/boardroombob-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boardroombob-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/boardroombob-com/security/boardroombob-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boardroombob-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boardroombob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://boardroombob.com/guides
- group: commercial
  title: ''
  type: Pricing
  url: https://boardroombob.com/pricing
- group: agent
  title: ''
  type: MCP
  url: https://boardroombob.com/mcp
- group: other
  title: ''
  type: CaseStudies
  url: https://boardroombob.com/case-studies
created: '2026-11-02'
description: Boardroom Bob is an AI‑powered strategy consulting service for solo founders and small teams. It offers a library of 19 proven business frameworks – such as SWOT, Porter’s Five Forces, BCG Matrix and decision‑making tools – that users can apply via an interactive web form. The platform generates structured analyses, diagrams and actionable recommendations, with a strict truthfulness policy that flags unknown information instead of fabricating data. Free users get limited monthly analyses, while paid plans unlock unlimited use and premium support. Boardroom Bob also provides an MCP server for AI agents like Claude and Cursor to run the frameworks directly.
image: https://boardroombob.com/__l5e/assets-v1/20deb611-36ee-4b9a-a94d-8ae72c10810a/boardroombob-social.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.boardroombob.com.
  name: Boardroom Bob MCP Server
  slug: boardroombob-com-mcp-yml
modified: '2026-11-02'
name: Boardroom Bob
nav: Providers
network: true
overview: 'Boardroom Bob is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Strategy, Consulting, Startups, and Founder Tools.


  Boardroom Bob''s developer surface includes documentation, pricing, and 9 more developer resources.'
plans:
- name: Boardroombob Com Plans Pricing
  plan_count: 3
  slug: boardroombob-com-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 13.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boardroombob Com Domain Security
  slug: boardroombob-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: boardroombob-com
tags:
- Artificial Intelligence
- Strategy
- Consulting
- Startups
- Founder Tools
- Company
website: https://boardroombob.com/
---
