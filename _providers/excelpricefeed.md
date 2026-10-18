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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/excelpricefeed/refs/heads/main/plans/excelpricefeed-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/excelpricefeed-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/excelpricefeed/refs/heads/main/changelog/excelpricefeed-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/excelpricefeed-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/excelpricefeed/refs/heads/main/hosts/excelpricefeed-hosts.yml
  title: ''
  type: Hosts
  url: hosts/excelpricefeed-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.excelpricefeed.com/status
- group: company
  title: ''
  type: Newsroom
  url: https://www.excelpricefeed.com/userguide/excel-formula-yahoo-finance/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.excelpricefeed.com/release-notes
- group: start
  title: ''
  type: GettingStarted
  url: https://www.excelpricefeed.com/userguide/account-setup-ig-index
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/excelpricefeed/refs/heads/main/security/excelpricefeed-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/excelpricefeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.excelpricefeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.excelpricefeed.com/userguide
- group: company
  title: ''
  type: Blog
  url: https://blog.excelpricefeed.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.excelpricefeed.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.excelpricefeed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.excelpricefeed.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.excelpricefeed.com/faq
coverage:
  checked: '2026-10-16'
  detail: The site provides Excel formula templates and pricing but no developer API or documentation.
  evidence:
  - status: 200
    url: https://www.excelpricefeed.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Excel Price Feed provides a real-time financial data add‑in for Microsoft Excel, delivering live stock, index, option, mutual fund, forex, commodity and cryptocurrency prices directly into spreadsheets via over 100 custom Excel formulas. Users can access real‑time NYSE and NASDAQ data, delayed international market data, historical price series, and fundamental company financials sourced from Yahoo Finance and other providers. The platform offers a 10‑day free trial, integrates with Interactive Brokers and IG Markets, and serves private investors, financial advisors, and institutions such as the U.S. SEC. It includes tools for portfolio valuation, stock screening, and technical analysis without any coding required.
layout: provider
modified: '2026-10-16'
name: Excel Price Feed
nav: Providers
network: true
overview: 'Excel Price Feed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Excel, and Real-Time Data.


  Excel Price Feed''s developer surface includes changelog, getting-started guide, documentation, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Excelpricefeed Plans Pricing
  plan_count: 4
  slug: excelpricefeed-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 12.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 37.5
    operational_transparency: 31.6
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Excelpricefeed Domain Security
  slug: excelpricefeed-domain-security
  summary_line: TLSv1.3 · HSTS
slug: excelpricefeed
tags:
- Company
- Finance
- Excel
- Real-Time Data
website: https://www.excelpricefeed.com/
---
