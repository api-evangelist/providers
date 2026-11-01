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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: SEC EDGAR Financial Data API — Health scores, sentiment, financial statements, insider trades, and more.
  name: slacking.biz API
  slug: slacking-biz-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/slacking-biz/conformance/slacking-biz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/slacking-biz-conformance.yml
- group: other
  href: https://artifacts.apis.io/slacking-biz/hosts/slacking-biz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/slacking-biz-hosts.yml
- group: auth
  href: https://artifacts.apis.io/slacking-biz/security/slacking-biz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slacking-biz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://slacking.biz/
- group: docs
  title: ''
  type: APIReference
  url: https://slacking.biz/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://slacking.biz/signup
- group: company
  title: ''
  type: Blog
  url: https://slacking.biz/alerts
- group: start
  title: ''
  type: SignUp
  url: https://slacking.biz/signup
- group: start
  title: ''
  type: Login
  url: https://slacking.biz/login
- group: operate
  title: ''
  type: StatusPage
  url: https://slacking.biz/status
created: '2026-10-31'
description: Slacking Biz provides a financial data API that aggregates market, company, and economic indicators. The platform offers real-time and historical data streams, customizable dashboards, and integration tools for developers building fintech applications, investment analytics, and business intelligence solutions. It emphasizes secure access, comprehensive documentation, and flexible pricing plans for startups to enterprises.
layout: provider
modified: '2026-10-31'
name: slacking-biz
nav: Providers
network: true
overview: 'slacking-biz is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Data API, SEC Filings, Company Health Scores, Insider Trading, and Sentiment Analysis.


  slacking-biz''s developer surface includes API reference, getting-started guide, engineering blog, signup flow, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 8.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Slacking Biz Domain Security
  slug: slacking-biz-domain-security
  summary_line: TLSv1.3
slug: slacking-biz
tags:
- Financial Data API
- SEC Filings
- Company Health Scores
- Insider Trading
- Sentiment Analysis
- Financial Statements
- Stock Screener
- Industry Comparison
website: https://slacking.biz/
---
