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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/solomon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solomontax.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solomontax.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solomontax.ai/privacy
created: '2026-07-17'
description: Solomon (Solomon AI, solomontax.ai) is an agentic AI platform for tax preparation aimed at accounting firms, automating the preparation of review-ready individual 1040 returns for high-net-worth and ultra-high-net-worth clients. The system interprets K-1/K-3 footnotes, applies multi-state SALT rules to K-1s, reconciles rental and real estate investments, analyzes brokerage statements for foreign income, and produces workpapers and audit trails, positioning itself to replace legacy tools such as SurePrep and K1x. Backed by Bessemer Venture Partners. This profile was surfaced as a portfolio-company lead and enriched by the API Evangelist pipeline; the company publishes no public developer/API surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/solomon.png
layout: provider
modified: '2026-07-21'
name: Solomon
nav: Providers
network: true
overview: Solomon is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Tax, Accounting, and Artificial Intelligence.
random_paper: 19
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/solomon/refs/heads/main/screenshots/solomon-2026-09-02T160125.png
security:
- kind: domain-security
  name: Solomon Domain Security
  slug: solomon-domain-security
  summary_line: TLSv1.3 · DMARC
slug: solomon
tags:
- Company
- Ai Ml
- Tax
- Accounting
- Artificial Intelligence
- Fintech
- Automation
website: https://solomontax.ai/
---
