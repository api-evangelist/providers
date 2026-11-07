---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: DocStoX provides data on Indian stocks via its platform; API details are not publicly documented.
  name: DocStoX API
  slug: docstox-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/docstox-com/rate-limits/docstox-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/docstox-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/docstox-com/plans/docstox-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docstox-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/docstox-com/changelog/docstox-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docstox-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/docstox-com/llms/docstox-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docstox-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/docstox-com/mcp/docstox-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/docstox-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/docstox-com/well-known/docstox-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docstox-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/docstox-com/hosts/docstox-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docstox-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/docstox-com/vendors/docstox-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docstox-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://docstox.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://docstox.com/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://docstox.com/docs/help/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docstox.com/docs/getting-started/what-is-docstox
- group: auth
  href: https://artifacts.apis.io/docstox-com/security/docstox-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docstox-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docstox.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docstox.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://docstox.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docstox.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docstox.com/terms
- group: operate
  title: ''
  type: Support
  url: https://docstox.com/contact
coverage:
  checked: '2026-10-30'
  detail: Docs are rendered via JavaScript and no machine‑readable API spec could be extracted.
  evidence:
  - status: 200
    url: https://docstox.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: DocStoX is a financial platform that explains every stock, offering research tools, a screener, watchlist, portfolio tracking, news, and market data. Users can explore over 5,700 stocks, view detailed financial ratios, price charts, and AI‑driven insights. The service provides free and Pro pricing plans, a sign‑up flow, and comprehensive privacy and terms documentation.
image: https://docstox.com/logo/docstox-wordmark-light@2x.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.docstox.com.
  name: docstox-com MCP Server
  slug: docstox-com-mcp-yml
modified: '2026-10-30'
name: docstox-com
nav: Providers
network: true
overview: 'docstox-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Stocks, Research, Data, and Platform.


  docstox-com''s developer surface includes changelog, documentation, getting-started guide, pricing, signup flow, support, and 13 more developer resources.'
plans:
- name: Docstox Com Plans Pricing
  plan_count: 3
  slug: docstox-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Docstox Com Rate Limits
  slug: docstox-com-rate-limits
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 56.0
    catalog_earned_first_party: 24.0
    catalog_gap: 59.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.5
    operational_transparency: 39.5
  previous_composite: 33.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/docstox-com/docstox-com-2026-11-03T130901.png
security:
- kind: authentication
  name: Docstox Com Authentication
  slug: docstox-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Docstox Com Domain Security
  slug: docstox-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: docstox-com
tags:
- Finance
- Stocks
- Research
- Data
- Platform
website: https://docstox.com/
---
