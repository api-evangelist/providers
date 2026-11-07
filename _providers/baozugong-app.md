---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
    dynamic_client_registration: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP API allows AI agents to access Baozugong data such as recommendations, portfolio, etc.
  name: MCP
  slug: mcp
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/baozugong-app/plans/baozugong-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/baozugong-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/baozugong-app/changelog/baozugong-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/baozugong-app-changelog.yml
- group: agent
  href: https://artifacts.apis.io/baozugong-app/llms/baozugong-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baozugong-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/baozugong-app/mcp/baozugong-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/baozugong-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/baozugong-app/well-known/baozugong-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baozugong-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/baozugong-app/hosts/baozugong-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baozugong-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/baozugong-app/vendors/baozugong-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baozugong-app-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://baozugong.app/changelog
- group: auth
  href: https://artifacts.apis.io/baozugong-app/security/baozugong-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baozugong-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baozugong.app/
- group: docs
  title: ''
  type: Documentation
  url: https://baozugong.app/learn
- group: commercial
  title: ''
  type: Pricing
  url: https://baozugong.app/pricing
- group: operate
  title: ''
  type: Support
  url: https://baozugong.app/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://baozugong.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baozugong.app/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genki3ng
created: '2026-11-02'
description: 包租公（Baozugong / YieldLord）是美股投资者的免费 AI 期权收租管家：把你长期看好的股票「租」出去——卖 Covered Call / Cash Secured Put / Wheel，每周收租金，好公司拿得住、拿得久。开仓前用 RENT 14 因子帮你挑合约，开仓后每个交易日帮你盯仓提醒。券商只读、不碰钱、不代下单。 包租公两档：免费档一直免费，完整覆盖挑合约、盯持仓与复盘，每月 30 次计算和生成额度；Gold 创始会员价 ¥100/月（海外 $14.99），券商自动同步、持仓主动提醒、不限次、可接 AI agent。免费领取 14 天 Gold 试用，不绑卡、不自动续费。
examples:
- key_count: 3
  name: Baozugong App Mcp Tools
  slug: baozugong-app-mcp-tools
image: https://baozugong.app/icons/og-1200x630-v5.png
layout: provider
mcp_servers:
- description: Remote MCP server at baozugong.app requiring OAuth.
  name: 包租公 MCP Server
  slug: baozugong-app-mcp-yml
modified: '2026-11-02'
name: 包租公
nav: Providers
network: true
overview: '包租公 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Investing, Artificial Intelligence, Options, and US-Stocks.


  包租公''s developer surface includes changelog, documentation, pricing, support, and 12 more developer resources.'
plans:
- name: Baozugong App Plans Pricing
  plan_count: 2
  slug: baozugong-app-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 23.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baozugong App Domain Security
  slug: baozugong-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: baozugong-app
tags:
- Finance
- Investing
- Artificial Intelligence
- Options
- US-Stocks
website: https://baozugong.app/
---
