---
access_model:
  confidence: medium
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/autrady-com/plans/autrady-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autrady-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/autrady-com/llms/autrady-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autrady-com-llms.txt
- group: build
  href: https://artifacts.apis.io/autrady-com/mcp/autrady-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/autrady-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/autrady-com/mcp/autrady-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/autrady-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/autrady-com/hosts/autrady-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autrady-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/autrady-com/vendors/autrady-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autrady-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/autrady-com/security/autrady-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autrady-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autrady.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://autrady.com/#how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://autrady.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://autrady.com/#faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autrady.com/Home/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autrady.com/Home/Privacy
- group: start
  title: ''
  type: SignUp
  url: https://autrady.com/Identity/Account/Login?returnUrl=%2FDatasets
coverage:
  checked: '2026-11-02'
  detail: Provider's website offers no machine‑readable API specification despite public HTML pages.
  evidence:
  - status: 404
    url: https://autrady.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Autrady audits trading strategies. Upload the signals behind a bot, a paid newsletter or your own backtest, and Autrady tests whether they beat the market after trading costs and allowing for luck. 14 days free with no card, then €19 a month including VAT.
image: https://autrady.com/images/og-cover.png
layout: provider
mcp_servers:
- description: Remote MCP server at autrady.com.
  name: Autrady MCP Server
  slug: autrady-com-mcp-yml
modified: '2026-11-02'
name: Autrady
nav: Providers
network: true
overview: 'Autrady is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Trading, Analytics, Research, and Software.


  Autrady''s developer surface includes getting-started guide, pricing, support, signup flow, and 10 more developer resources.'
plans:
- name: Autrady Com Plans Pricing
  plan_count: 1
  slug: autrady-com-plans-pricing
random_paper: 22
scopes:
- name: Autrady Com Scopes
  scope_count: 0
  slug: autrady-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.3
    operational_transparency: 0.0
  previous_composite: 22.4
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Autrady Com Authentication
  slug: autrady-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Autrady Com Domain Security
  slug: autrady-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autrady-com
tags:
- Finance
- Trading
- Analytics
- Research
- Software
website: https://autrady.com/
---
