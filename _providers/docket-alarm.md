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
api_count: 1
apis:
- description: Provides programmatic access to Docket Alarm case data, pricing plans, and documentation.
  name: Developer API
  slug: developer-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/plans/docket-alarm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/docket-alarm-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/well-known/docket-alarm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docket-alarm-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/hosts/docket-alarm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docket-alarm-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/packages/docket-alarm-packages.yml
  title: ''
  type: SDKs
  url: packages/docket-alarm-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/packages/docket-alarm-packages.yml
  title: ''
  type: Packages
  url: packages/docket-alarm-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docketalarm.com/TermsOfService
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docketalarm.com/Privacy
- group: company
  title: ''
  type: Newsroom
  url: https://sandbox.docketalarm.com/news
- group: start
  title: ''
  type: Login
  url: https://www.docketalarm.com/login/google
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocketAlarm
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docket-alarm/refs/heads/main/security/docket-alarm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docket-alarm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.docketalarm.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.docketalarm.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.docketalarm.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.docketalarm.com/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docketalarm.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.docketalarm.com/blog
created: '2026-10-14'
description: Docket Alarm provides a cloud‑based platform that aggregates and delivers federal, state, and intellectual‑property court filings. Attorneys and paralegals can search, receive alerts, and run analytics on litigation outcomes. The service offers a public Developer API for programmatic access to case data, pricing plans, and documentation, supporting legal research and workflow automation.
image: https://www.docketalarm.com/site_media/img/logo75px.png
layout: provider
modified: '2026-10-14'
name: Docket Alarm
nav: Providers
network: true
overview: 'Docket Alarm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Litigation, and Data.


  Docket Alarm''s developer surface includes documentation, API reference, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Docket Alarm Plans Pricing
  plan_count: 4
  slug: docket-alarm-plans-pricing
random_paper: 16
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Docket Alarm Domain Security
  slug: docket-alarm-domain-security
  summary_line: TLSv1.3 · DMARC
slug: docket-alarm
tags:
- Company
- Legal Tech
- Litigation
- Data
website: https://www.docketalarm.com
---
