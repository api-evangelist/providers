---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fintool-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fintool.ai
created: '2026-07-17'
description: Fintool is an AI-powered equity research analyst and financial copilot built for institutional investors such as hedge funds, asset managers, and buy-side and sell-side analysts. Its assistant ingests SEC filings (10-K, 10-Q, 8-K), earnings-call transcripts, and financial data to answer research questions with source citations, accelerating fundamental analysis and due diligence. Fintool is a portfolio company of Menlo Ventures. This profile was added to the API Evangelist network from VC-portfolio discovery; Fintool operates as an enterprise SaaS product and, as of this enrichment pass, publishes no public developer API, SDK, or developer portal that could be harvested.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fintool.png
layout: provider
modified: '2026-07-19'
name: Fintool
nav: Providers
network: true
overview: Fintool is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Artificial Intelligence, Equity Research, and Investment Research.
random_paper: 7
score:
  band: minimal
  composite: 1.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fintool/refs/heads/main/screenshots/fintool-2026-08-07T165316.png
security:
- kind: domain-security
  name: Fintool Domain Security
  slug: fintool-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fintool
tags:
- Company
- Financial-Services
- Artificial Intelligence
- Equity Research
- Investment Research
- SEC Filings
- Fintech
- Large Language Models
website: https://fintool.ai
---
