---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.voucherify.io
  baseurl_source: declared
  description: The Vouchers API from Voucherify — 1 operation(s) for vouchers.
  name: Voucherify Vouchers API
  slug: voucherify-vouchers-api
artifact_total: 10
asyncapis:
- description: ''
  name: Voucherify Webhooks
  slug: voucherify-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/voucherify/plans/voucherify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/voucherify-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/voucherify/rules/voucherify-rules.yml
  title: ''
  type: Spectral
  url: rules/voucherify-rules.yml
- group: design
  href: https://artifacts.apis.io/voucherify/asyncapi/voucherify-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/voucherify-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/voucherify/changelog/voucherify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/voucherify-changelog.yml
- group: auth
  href: https://artifacts.apis.io/voucherify/authentication/voucherify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/voucherify-authentication.yml
- group: design
  href: https://artifacts.apis.io/voucherify/lifecycle/voucherify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/voucherify-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/voucherify/conformance/voucherify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/voucherify-conformance.yml
- group: agent
  href: https://artifacts.apis.io/voucherify/llms/voucherify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/voucherify-llms.txt
- group: other
  href: https://artifacts.apis.io/voucherify/a2a/voucherify-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/voucherify-a2a.yml
- group: agent
  href: https://artifacts.apis.io/voucherify/mcp/voucherify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/voucherify-mcp.yml
- group: auth
  href: https://artifacts.apis.io/voucherify/well-known/voucherify-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voucherify-status-security.txt
- group: agent
  href: https://artifacts.apis.io/voucherify/well-known/voucherify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voucherify-well-known.yml
- group: other
  href: https://artifacts.apis.io/voucherify/hosts/voucherify-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voucherify-hosts.yml
- group: other
  href: https://artifacts.apis.io/voucherify/vendors/voucherify-vendors.yml
  title: ''
  type: Vendors
  url: vendors/voucherify-vendors.yml
- group: build
  href: https://artifacts.apis.io/voucherify/packages/voucherify-packages.yml
  title: ''
  type: SDKs
  url: packages/voucherify-packages.yml
- group: build
  href: https://artifacts.apis.io/voucherify/packages/voucherify-packages.yml
  title: ''
  type: Packages
  url: packages/voucherify-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voucherify.io/legal/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.voucherify.io/newsroom
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.voucherify.io/changelog/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.voucherify.io/guides/api-quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.voucherify.io`
- group: auth
  href: https://artifacts.apis.io/voucherify/scopes/voucherify-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/voucherify-scopes.yml
- group: auth
  href: https://artifacts.apis.io/voucherify/security/voucherify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voucherify-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voucherify.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.voucherify.io/guides/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.voucherify.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.voucherify.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.voucherify.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.voucherify.io/contact-support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.voucherify.io/
coverage:
  checked: '2026-10-14'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable spec was found.
  evidence:
  - status: 200
    url: https://docs.voucherify.io/guides/api-quickstart
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-13'
description: Voucherify provides a cloud‑based incentive optimization platform that enables enterprises to create, manage, and experiment with promotions, loyalty programs, and reward campaigns. Its API lets developers integrate real‑time coupon generation, referral tracking, and reward redemption into web, mobile, and backend services, supporting A/B testing and analytics to maximize conversion and customer engagement.
finops:
- has_sources: true
  method: derived
  name: Voucherify Finops
  primary_unit: seat
  service_category: ''
  slug: voucherify-finops
  template: false
image: https://cdn.prod.website-files.com/60793752293570132aa47da2/691466b7bd965d99f983f82d_5c62fad34c6c2411e7a1d963e5ecd8f7_OpenGraph%20Voucherify.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.voucherify.io.
  name: Voucherify MCP Server
  slug: voucherify-mcp-yml
modified: '2026-10-13'
name: Voucherify
nav: Providers
network: true
overview: 'Voucherify is listed with 1 API on the [APIs.io](https://apis.io/) network: Vouchers API. Tagged areas include Company, Incentives, Promotions, and Loyalty.


  The Voucherify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Voucherify''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 24 more developer resources.'
plans:
- name: Voucherify Plans Pricing
  plan_count: 4
  slug: voucherify-plans-pricing
- name: Voucherify Price Estimates
  plan_count: 0
  slug: voucherify-price-estimates
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Voucherify API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: voucherify-rules
scopes:
- name: Voucherify Scopes
  scope_count: 42
  slug: voucherify-scopes
  summary_line: 42 scopes · clientCredentials
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.5
    catalog_earned_first_party: 12.0
    catalog_gap: 63.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 50.0
    contract_governance: 31.8
    contract_quality: 19.8
    developer_ergonomics: 44.0
    discoverability: 67.5
    operational_transparency: 34.2
  previous_composite: 50.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/voucherify/voucherify-2026-11-03T145928.png
security:
- kind: authentication
  name: Voucherify Authentication
  slug: voucherify-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Voucherify Domain Security
  slug: voucherify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: voucherify
tags:
- Company
- Incentives
- Promotions
- Loyalty
website: https://www.voucherify.io
---
