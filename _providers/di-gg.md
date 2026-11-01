---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/di-gg/llms/di-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/di-gg-llms.txt
- group: agent
  href: https://artifacts.apis.io/di-gg/mcp/di-gg-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/di-gg-mcp.yml
- group: other
  href: https://artifacts.apis.io/di-gg/hosts/di-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/di-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/di-gg/vendors/di-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/di-gg-vendors.yml
- group: auth
  href: https://artifacts.apis.io/di-gg/security/di-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/di-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://digg.com
created: '2026-10-24'
description: Digg is a digital media company that curates and publishes news, technology, entertainment, and AI content. It operates the Digg.com website, offering articles, videos, and a platform for user engagement. The company focuses on delivering timely, high-quality journalism and insights across a wide range of topics, including technology, science, business, and culture.
image: https://digg.com/ai/opengraph-image
layout: provider
mcp_servers:
- description: Remote MCP server at digg.com.
  name: Digg MCP Server
  slug: di-gg-mcp-yml
modified: '2026-10-24'
name: Digg
nav: Providers
network: true
overview: Digg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, News, Media, Technology, and AI.
random_paper: 0
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Di Gg Domain Security
  slug: di-gg-domain-security
  summary_line: TLSv1.3 · HSTS
slug: di-gg
tags:
- Company
- News
- Media
- Technology
- AI
website: https://digg.com
---
