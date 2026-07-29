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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moneyview-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moneyview-llms.txt
- group: company
  title: ''
  type: Website
  url: https://moneyview.in
created: '2026-07-17'
description: 'Moneyview is an India-based digital financial services platform and consumer fintech app offering instant personal loans (up to 10 lakh), home loans, loan against property, credit cards, credit score checks, insurance, digital gold investment, UPI payments, EMI calculators, and personal-finance tools. It operates an RBI-guideline-compliant, paperless lending experience via web and mobile apps for Indian consumers. As of this enrichment pass the company publishes no public developer API surface, SDKs, developer portal, or OpenAPI: no developer/docs/api subdomain resolves and /.well-known/ discovery paths are blocked. It does publish a site-level llms.txt describing its consumer products. Backed by Ribbit Capital; surfaced to the API Evangelist network as a portfolio lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moneyview.png
layout: provider
modified: '2026-07-20'
name: Moneyview
nav: Providers
network: true
overview: Moneyview is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Personal Loans, and Credit Cards.
random_paper: 35
score:
  band: minimal
  composite: 6.2
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Moneyview Domain Security
  slug: moneyview-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: moneyview
tags:
- Company
- Fintech
- Lending
- Personal Loans
- Credit Cards
- Credit Score
- UPI
- Insurance
- India
- Digital Lending
website: https://moneyview.in
---
