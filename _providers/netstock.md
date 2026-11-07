---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Netstock provides inventory management and planning tools, but no machine‑readable API contract was found.
  name: Netstock API
  slug: netstock-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/netstock/plans/netstock-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/netstock-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/netstock/conformance/netstock-conformance.yml
  title: ''
  type: Conformance
  url: conformance/netstock-conformance.yml
- group: agent
  href: https://artifacts.apis.io/netstock/llms/netstock-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/netstock-llms.txt
- group: auth
  href: https://artifacts.apis.io/netstock/well-known/netstock-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/netstock-help-security.txt
- group: agent
  href: https://artifacts.apis.io/netstock/well-known/netstock-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/netstock-well-known.yml
- group: other
  href: https://artifacts.apis.io/netstock/hosts/netstock-hosts.yml
  title: ''
  type: Hosts
  url: hosts/netstock-hosts.yml
- group: other
  href: https://artifacts.apis.io/netstock/vendors/netstock-vendors.yml
  title: ''
  type: Vendors
  url: vendors/netstock-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.netstock.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netstock.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netstock.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.netstock.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.netstock.com/en/articles/13435031-getting-started-with-learning-in-netstock
- group: docs
  title: ''
  type: Documentation
  url: https://help.netstock.com/
- group: auth
  href: https://artifacts.apis.io/netstock/security/netstock-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/netstock-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://netstock.com/
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are HTML only and no OpenAPI/AsyncAPI/GraphQL spec could be located.
  evidence:
  - status: 200
    url: https://help.netstock.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: 'Netstock is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://www.netstock.com/wp-content/uploads/2022/04/og.png
layout: provider
modified: '2026-10-27'
name: Netstock
nav: Providers
network: true
overview: 'Netstock is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain Planning, Inventory, Demand Planning, Artificial Intelligence, and ERP Integration.


  Netstock''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 10 more developer resources.'
plans:
- name: Netstock Plans Pricing
  plan_count: 1
  slug: netstock-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Netstock Rate Limits
  slug: netstock-rate-limits
scopes:
- name: Netstock Scopes
  scope_count: 0
  slug: netstock-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/netstock/netstock-2026-11-03T140139.png
security:
- kind: authentication
  name: Netstock Authentication
  slug: netstock-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Netstock Domain Security
  slug: netstock-domain-security
  summary_line: TLSv1.3 · DMARC
slug: netstock
tags:
- Supply Chain Planning
- Inventory
- Demand Planning
- Artificial Intelligence
- ERP Integration
- Manufacturing
- Retail
- Wholesale
website: https://netstock.com/
---
