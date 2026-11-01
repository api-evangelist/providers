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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/profit/conformance/profit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/profit-conformance.yml
- group: other
  href: https://artifacts.apis.io/profit/hosts/profit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/profit-hosts.yml
- group: other
  href: https://artifacts.apis.io/profit/vendors/profit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/profit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://profit.com/resources/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://profit.com/resources/help-center
- group: start
  title: ''
  type: Sandbox
  url: https://profit.com/console/home
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://profit.com/resources/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://profit.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://profit.com/news/home
- group: operate
  title: ''
  type: ChangeLog
  url: https://profit.com/learning/release-notes
- group: company
  title: ''
  type: Blog
  url: https://profit.com/learning/blog
- group: auth
  href: https://artifacts.apis.io/profit/security/profit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/profit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://profit.com/
created: '2026-10-21'
description: Profit.com is a cloud‑based financial analytics platform that offers a suite of APIs enabling businesses to integrate real‑time profit‑and‑loss reporting, revenue forecasting, expense tracking, and KPI dashboards into their own applications. The service provides programmable access to transactional data, customizable reporting templates, and secure multi‑tenant architecture, helping companies automate financial insights and drive data‑driven decision making. Profit.com’s APIs are RESTful, support JSON payloads, and include comprehensive documentation for developers.
image: https://cdn.profit.com/static/profit/open-graph/og-image-home.jpg
layout: provider
modified: '2026-10-21'
name: Profit.com
nav: Providers
network: true
overview: 'Profit.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Analytics, API, and SaaS.


  Profit.com''s developer surface includes support, sandbox, pricing, changelog, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Profit Domain Security
  slug: profit-domain-security
  summary_line: TLSv1.2 · DMARC
slug: profit
tags:
- Company
- Finance
- Analytics
- API
- SaaS
website: https://profit.com/
---
