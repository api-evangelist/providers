---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quiver Agentic Access
  operation_count: 6
  slug: quiver-agentic-access
  summary_line: 6 operations
api_count: 2
apis:
- description: The Quiver Quantitative API provides REST access to alternative financial datasets including Congressional and Senate stock trading, insider transactions, lobbying disclosures, government contracts, c
  name: Quiver Quantitative API
  slug: quiver
- description: The Beta API from Quiver Quantitative — 6 operation(s) for beta.
  name: Quiver Quantitative Beta API
  slug: quiver-beta-api
artifact_total: 9
collections:
- collection_type: open
  name: Quiver Quantitative API
  slug: open-quiver
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quiver-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quiver-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quiver-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quiver-quantitative
- group: company
  title: ''
  type: Website
  url: https://www.quiverquant.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.quiverquant.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.quiverquant.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.quiverquant.com/signup/
- group: company
  title: ''
  type: Blog
  url: https://www.quiverquant.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quiverquant.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quiverquant.com/privacy/
created: '2025-02-12'
description: Quiver Quantitative is an alternative-data platform that aggregates non-traditional financial datasets and exposes them through a single API. The platform covers congressional and Senate trading, insider trading, lobbying activity, government contracts, corporate patents, executive compensation, institutional and ETF holdings, off-exchange activity, app ratings, and more, giving developers and quantitative researchers programmatic access to alternative data signals starting at $10 per month.
finops:
- name: Quiver Finops
  service_category: API
  slug: quiver-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiver.png
layout: provider
modified: '2026-04-28'
name: Quiver Quantitative
nav: Providers
network: true
overview: 'Quiver Quantitative publishes 1 API on the [APIs.io](https://apis.io/) network: Beta API. Tagged areas include Alternative Data, Financial Data, Investment Research, Market Data, and Government Data.


  Quiver Quantitative''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
plans:
- name: Quiver Plans Pricing
  plan_count: 3
  slug: quiver-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Quiver Rate Limits
  slug: quiver-rate-limits
score:
  band: developing
  composite: 42.2
  delta: -1.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/screenshots/quiver-2026-06-20T192443.png
security:
- kind: authentication
  name: Quiver Authentication
  slug: quiver-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quiver Domain Security
  slug: quiver-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quiver
tags:
- Alternative Data
- Financial Data
- Investment Research
- Market Data
- Government Data
- Congressional Trading
website: https://www.quiverquant.com/
---
