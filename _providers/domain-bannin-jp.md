---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides domain management services including email authentication, SSL certificates, and DNS operations.
  name: Domain Bannin API
  slug: domain-bannin-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/domain-bannin-jp/plans/domain-bannin-jp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/domain-bannin-jp-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/domain-bannin-jp/llms/domain-bannin-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/domain-bannin-jp-llms.txt
- group: agent
  href: https://artifacts.apis.io/domain-bannin-jp/mcp/domain-bannin-jp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/domain-bannin-jp-mcp.yml
- group: agent
  href: https://artifacts.apis.io/domain-bannin-jp/well-known/domain-bannin-jp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/domain-bannin-jp-well-known.yml
- group: other
  href: https://artifacts.apis.io/domain-bannin-jp/hosts/domain-bannin-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/domain-bannin-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/domain-bannin-jp/vendors/domain-bannin-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/domain-bannin-jp-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://domain-bannin.jp/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://domain-bannin.jp/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://domain-bannin.jp/pricing
- group: company
  title: ''
  type: Blog
  url: https://domain-bannin.jp/blog
- group: auth
  href: https://artifacts.apis.io/domain-bannin-jp/security/domain-bannin-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/domain-bannin-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://domain-bannin.jp/
coverage:
  detail: The provider's API reference page https://domain-bannin.jp/api returns a 404 HTML page with no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract.
  evidence:
  - status: 404
    url: https://domain-bannin.jp/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: ドメイン番人は、メール認証（SPF / DKIM / DMARC）から SSL 証明書、DNS の安定運用まで、20 年のインフラ運用経験を持つ代表が中小企業のドメイン全体を守るサービスです。顧客のメールが届かない、ドメインが期限切れになる、SSL が未設定といったリスクを一つの窓口で診断・対策し、PDF レポートで結果を提供します。自動チェックツールで設定状況を測定し、専門家が目視で確認することで、ビジネスへの影響を最小化します。
image: https://domain-bannin.jp/opengraph-image?4d33698a42fb5cec
layout: provider
mcp_servers:
- description: Remote MCP server at domain-bannin.jp.
  name: ドメイン番人 MCP Server
  slug: domain-bannin-jp-mcp-yml
modified: '2026-11-05'
name: ドメイン番人
nav: Providers
network: true
overview: 'ドメイン番人 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domain, Security, DNS, Email, and SSL.


  ドメイン番人''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Domain Bannin Jp Plans Pricing
  plan_count: 9
  slug: domain-bannin-jp-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Domain Bannin Jp Domain Security
  slug: domain-bannin-jp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: domain-bannin-jp
tags:
- Domain
- Security
- DNS
- Email
- SSL
website: https://domain-bannin.jp/
---
