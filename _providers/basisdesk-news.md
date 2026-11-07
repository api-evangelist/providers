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
    agent_skills: derived
    agentic_access: derived
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
  score: 6.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Basisdesk News Agentic Access
  operation_count: 9
  slug: basisdesk-news-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Read‑only crypto market data and MCP server for news search. Provides ticker, snapshot, movers, sparklines, whale transfers and research datasets.
  name: Basis Desk API
  slug: basis-desk-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/basisdesk-news/agentic-access/basisdesk-news-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/basisdesk-news-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/basisdesk-news/rules/basisdesk-news-rules.yml
  title: ''
  type: Spectral
  url: rules/basisdesk-news-rules.yml
- group: agent
  href: https://artifacts.apis.io/basisdesk-news/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/basisdesk-news/conformance/basisdesk-news-conformance.yml
  title: ''
  type: Conformance
  url: conformance/basisdesk-news-conformance.yml
- group: agent
  href: https://artifacts.apis.io/basisdesk-news/llms/basisdesk-news-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/basisdesk-news-llms.txt
- group: agent
  href: https://artifacts.apis.io/basisdesk-news/mcp/basisdesk-news-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/basisdesk-news-mcp.yml
- group: other
  href: https://artifacts.apis.io/basisdesk-news/hosts/basisdesk-news-hosts.yml
  title: ''
  type: Hosts
  url: hosts/basisdesk-news-hosts.yml
- group: other
  href: https://artifacts.apis.io/basisdesk-news/vendors/basisdesk-news-vendors.yml
  title: ''
  type: Vendors
  url: vendors/basisdesk-news-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basisdesk.news/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://basisdesk.news/security/today
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basisdesk.news/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://basisdesk.news/news
- group: docs
  title: ''
  type: APIReference
  url: https://basisdesk.news/developers
- group: auth
  href: https://artifacts.apis.io/basisdesk-news/security/basisdesk-news-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/basisdesk-news-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://basisdesk.news/
created: '2026-11-02'
description: Basis Desk is an AI‑native crypto newsroom that delivers source‑verified news, live market data, and daily briefs without hype. It aggregates information from regulators, protocol teams, exchanges, and client releases, offering readers quick, sober insights into the cryptocurrency market.
image: https://basisdesk.news/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at basisdesk.news.
  name: Basis Desk MCP Server
  slug: basisdesk-news-mcp-yml
modified: '2026-11-02'
name: Basis Desk
nav: Providers
network: true
overview: 'Basis Desk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, News, Artificial Intelligence, Media, and Data.


  The Basis Desk catalog on APIs.io includes 1 Spectral governance ruleset.


  Basis Desk''s developer surface includes API reference and 14 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Basis Desk API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: basisdesk-news-rules
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 5.4
    discoverability: 65.8
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Basisdesk News Domain Security
  slug: basisdesk-news-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-market-snapshot
  slug: basisdesk-news-get-market-snapshot
slug: basisdesk-news
tags:
- Cryptocurrency
- News
- Artificial Intelligence
- Media
- Data
- Finance
website: https://basisdesk.news/
---
