---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'REST API providing partner access to OnDeck''s small business lending platform, supporting credit pre-qualifications, loan application submission, business health score retrieval via the OnDeck Score, '
  name: OnDeck Lending API
  slug: ondeck-lending-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ondeck-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ondeck-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ondeck.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ondeck.com/partner
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ondeck/
- group: other
  title: ''
  type: X
  url: https://twitter.com/OnDeckCapital/
- group: company
  title: ''
  type: Blog
  url: https://www.ondeck.com/resources
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ondeck.com/partner
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/plans/ondeck-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/rate-limits/ondeck-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/finops/ondeck-finops.yml
created: '2026-06-13'
description: OnDeck is a small business lending platform that provides partner APIs for submitting loan applications, checking business health scores via the OnDeck Score, managing loan products including term loans and lines of credit, and processing repayments. The API enables banks, brokers, and online service providers to embed OnDeck lending capabilities directly into their own platforms through credit pre-qualification, pre-approval, and full loan application submission workflows. OnDeck is an Enova International brand serving 185,000+ small businesses with $25 billion+ in capital delivered.
finops:
- name: Ondeck Finops
  service_category: ''
  slug: ondeck-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ondeck.png
layout: provider
modified: '2026-06-13'
name: OnDeck
nav: Providers
network: true
overview: 'OnDeck publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Small Business Lending, Fintech, Loans, Credit Scoring, and Business Health.


  OnDeck''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Ondeck Plans Pricing
  plan_count: 1
  slug: ondeck-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Ondeck Rate Limits
  slug: ondeck-rate-limits
score:
  band: emerging
  composite: 19.3
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ondeck/refs/heads/main/screenshots/ondeck-2026-06-20T190706.png
security:
- kind: domain-security
  name: Ondeck Domain Security
  slug: ondeck-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ondeck Vulnerability Disclosure
  slug: ondeck-vulnerability-disclosure
  summary_line: Hackerone
slug: ondeck
tags:
- Small Business Lending
- Fintech
- Loans
- Credit Scoring
- Business Health
- Term Loans
- Line of Credit
- Loan Origination
website: https://www.ondeck.com/
---
