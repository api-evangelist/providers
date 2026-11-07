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
- description: 台灣網站電商情報 API，提供開店平台、技術、廣告投放、流量估算、競品與名單等資訊。
  name: ECPRO 電商博士 API
  slug: ecpro-api
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/ecpro-tw/llms/ecpro-tw-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecpro-tw-llms.txt
- group: build
  href: https://artifacts.apis.io/ecpro-tw/mcp/ecpro-tw-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ecpro-tw-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ecpro-tw/mcp/ecpro-tw-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ecpro-tw-mcp.yml
- group: other
  href: https://artifacts.apis.io/ecpro-tw/hosts/ecpro-tw-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecpro-tw-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecpro-tw/vendors/ecpro-tw-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecpro-tw-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecpro.tw/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://ecpro.tw/status
- group: commercial
  title: ''
  type: Pricing
  url: https://ecpro.tw/toolbox/pricing-markup
- group: company
  title: ''
  type: Newsroom
  url: https://ecpro.tw/industry/media
- group: other
  title: ''
  type: Leadership
  url: https://ecpro.tw/team
- group: company
  title: ''
  type: Blog
  url: https://ecpro.tw/blog
- group: auth
  href: https://artifacts.apis.io/ecpro-tw/security/ecpro-tw-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecpro-tw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecpro.tw/
created: '2026-11-06'
description: ECPRO 電商博士, founded by 林克威, provides Taiwan website real‑price registration and the nation’s first e‑commerce media platform. It aggregates public website data, offering transparent insights into e‑commerce platforms, payment systems, advertising pixels, traffic, and company registration details. Users can query site technology stacks, compare competitors, and access free tools, reports, and AI‑assisted analysis, all aimed at making Taiwan’s e‑commerce landscape openly understandable.
image: https://ecpro.tw/og.svg
layout: provider
mcp_servers:
- description: Remote MCP server at ecpro.tw.
  name: ECPRO MCP Server
  slug: ecpro-tw-mcp-yml
modified: '2026-11-06'
name: ECPRO
nav: Providers
network: true
overview: 'ECPRO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Data, Taiwan, and Media.


  ECPRO''s developer surface includes pricing, engineering blog, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 60.0
    operational_transparency: 15.8
  provenance:
    mcp: first-party
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
  name: Ecpro Tw Domain Security
  slug: ecpro-tw-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ecpro-tw
tags:
- E-Commerce
- Data
- Taiwan
- Media
website: https://ecpro.tw/
---
