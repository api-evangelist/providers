---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 5
apis:
- description: REST API for retrieving end-user accounts, transactions, and balances across 3,400+ European banks via PSD2 AISP.
  name: Tink Account Aggregation API
  slug: account-aggregation-api
- description: Verify account ownership and IBAN details for an end user.
  name: Tink Account Check API
  slug: account-check-api
- description: Categorized income data derived from aggregated transaction history.
  name: Tink Income Check API
  slug: income-check-api
- description: Risk indicators and affordability signals derived from aggregated bank data.
  name: Tink Risk Insights API
  slug: risk-insights-api
- description: Initiate single, recurring, and bulk SEPA / domestic-rail payments via PSD2 PISP.
  name: Tink Payments API
  slug: payments-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tink-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fintecsystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tink-ab
- group: start
  title: ''
  type: Portal
  url: https://tink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tink.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tink.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/tink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tink-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tink.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://tink.com/blog/
created: '2026-05-08'
description: Tink (a Visa company) is a European open-banking platform offering account aggregation, payment initiation, identity, and KYC products across 3,400+ banks. The Tink API exposes Account Check, Account Aggregation, Income Check, Risk Insights, Money Manager, and Payments products under a single OAuth-protected REST surface at api.tink.com.
finops:
- name: Tink Finops
  service_category: Open Banking
  slug: tink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tink.png
layout: provider
modified: '2026-05-08'
name: Tink
nav: Providers
network: true
overview: 'Tink publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Open Banking, PSD2, Europe, and Visa.


  Tink''s developer surface includes developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Tink Plans Pricing
  plan_count: 2
  slug: tink-plans-pricing
random_paper: 99
rate_limits:
- limit_count: 3
  name: Tink Rate Limits
  slug: tink-rate-limits
score:
  band: emerging
  composite: 22.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tink/refs/heads/main/screenshots/tink-2026-06-20T195408.png
security:
- kind: domain-security
  name: Tink Domain Security
  slug: tink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tink Vulnerability Disclosure
  slug: tink-vulnerability-disclosure
  summary_line: security.txt
slug: tink
tags:
- Fintech
- Open Banking
- PSD2
- Europe
- Visa
- Account Aggregation
- Payments
- KYC
website: https://tink.com/
---
