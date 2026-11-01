---
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/crosser/vendors/crosser-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crosser-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crosser/well-known/crosser-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crosser-support-security.txt
- group: auth
  href: https://artifacts.apis.io/crosser/well-known/crosser-portal-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crosser-portal-security.txt
- group: agent
  href: https://artifacts.apis.io/crosser/well-known/crosser-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crosser-well-known.yml
- group: other
  href: https://artifacts.apis.io/crosser/hosts/crosser-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crosser-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.crosser.io/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://crosser.io/media/eksb4fe3/crosser-solution-overview.svg
- group: start
  title: ''
  type: GettingStarted
  url: https://crosser.io/company/contact/get-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.support.crosser.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crosser.io/
- group: auth
  href: https://artifacts.apis.io/crosser/security/crosser-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crosser-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crosser.io/
- group: company
  title: ''
  type: Blog
  url: https://crosser.io/blog
- group: start
  title: ''
  type: Login
  url: https://cloud.crosser.io/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://crosser.io/
  reason: no-developer-program
  state: none
created: '2026-10-20'
description: Crosser provides an IoT edge streaming analytics platform that enables real-time data processing and insights at the device level. By integrating edge computing with powerful analytics, Crosser helps manufacturers, logistics providers, and other industrial operators to monitor, analyze, and act on sensor data instantly, reducing latency and bandwidth costs while improving operational efficiency and decision-making.
image: https://crosser.io/media/wwtih4vi/crosser-stream-analytics-and-intelligent-integrations.png
layout: provider
modified: '2026-10-20'
name: Crosser - IoT Edge Streaming Analytics
nav: Providers
network: true
overview: 'Crosser - IoT Edge Streaming Analytics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Edge-Computing, Streaming-Analytics, and Industrial.


  Crosser - IoT Edge Streaming Analytics'' developer surface includes getting-started guide, documentation, engineering blog, and 11 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 17.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 50.0
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crosser Domain Security
  slug: crosser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crosser
tags:
- Company
- IoT
- Edge-Computing
- Streaming-Analytics
- Industrial
website: https://crosser.io/
---
