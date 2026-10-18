---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Quiver Agentic Access
  operation_count: 6
  slug: quiver-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- description: The Quiver Quantitative API provides REST access to alternative financial datasets including Congressional and Senate stock trading, insider transactions, lobbying disclosures, government contracts, c
  name: Quiver Quantitative API
  slug: quiver
- baseURL: https://api.quiverquant.com
  baseurl_source: declared
  description: The Beta API from Quiver Quantitative — 6 operation(s) for beta.
  name: Quiver Quantitative Beta API
  slug: quiver-beta-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Quiver Quantitative Beta API
  slug: open-quiver-beta-api
- collection_type: open
  name: Quiver Quantitative API
  slug: open-quiver
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/plans/quiver-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quiver-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/rate-limits/quiver-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quiver-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/finops/quiver-finops.yml
  title: ''
  type: FinOps
  url: finops/quiver-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/agentic-access/quiver-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quiver-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/security/quiver-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quiver-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quiver/refs/heads/main/authentication/quiver-authentication.yml
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
- has_sources: false
  method: generated
  name: Quiver Finops
  primary_unit: ''
  service_category: API
  slug: quiver-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quiver.png
layout: provider
modified: '2026-04-28'
name: Quiver Quantitative
nav: Providers
network: true
overview: 'Quiver Quantitative publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Beta API, and 1 more. Tagged areas include Alternative Data, Financial Data, Investment Research, Market Data, and Government Data.


  Quiver Quantitative''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
plans:
- name: Quiver Plans Pricing
  plan_count: 3
  slug: quiver-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Quiver Rate Limits
  slug: quiver-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 43.0
    catalog_earned_first_party: 0.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 30.4
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
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
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
