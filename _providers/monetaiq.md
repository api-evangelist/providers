---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Financial data API providing access to company financials, balance sheets, income statements, and cash flow data.
  name: MonetaIQ API
  slug: monetaiq-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/monetaiq/plans/monetaiq-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monetaiq-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/monetaiq/llms/monetaiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monetaiq-llms.txt
- group: agent
  href: https://artifacts.apis.io/monetaiq/well-known/monetaiq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monetaiq-well-known.yml
- group: other
  href: https://artifacts.apis.io/monetaiq/hosts/monetaiq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monetaiq-hosts.yml
- group: other
  href: https://artifacts.apis.io/monetaiq/vendors/monetaiq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monetaiq-vendors.yml
- group: auth
  href: https://artifacts.apis.io/monetaiq/security/monetaiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monetaiq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monetaiq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://monetaiq.com/api/
- group: docs
  title: ''
  type: APIReference
  url: https://monetaiq.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://monetaiq.com/price/
- group: operate
  title: ''
  type: Support
  url: https://monetaiq.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://monetaiq.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monetaiq.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monetaiq.com/privacy-notice-website/
created: '2026-10-18'
description: MonetaIQ provides global financial data covering over 400 million private and public companies, offering balance sheets, income statements, cash flow, and P&L information sourced directly from official registries and stock exchanges. Their platform includes a Managed Coverage Platform (MCP), extensive data dictionaries, and API access for seamless integration into financial analysis workflows.
layout: provider
modified: '2026-10-18'
name: MonetaIQ
nav: Providers
network: true
overview: 'MonetaIQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Data, Data Platform, and Analytics.


  MonetaIQ''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
plans:
- name: Monetaiq Plans Pricing
  plan_count: 4
  slug: monetaiq-plans-pricing
random_paper: 22
score:
  band: emerging
  composite: 16.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 51.8
    operational_transparency: 0.0
  previous_composite: 22.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/monetaiq/monetaiq-2026-11-03T135829.png
security:
- kind: domain-security
  name: Monetaiq Domain Security
  slug: monetaiq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: monetaiq
tags:
- Company
- Financial Data
- Data Platform
- Analytics
website: https://monetaiq.com/
---
