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
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Single-contract API providing access to consumer and business credit reports across major bureaus (Equifax, Experian, TransUnion). Supports soft and hard credit pulls, FICO and Vantage scoring models,
  name: CRS Credit Data API
  slug: credit-data-api
- description: API powering the eCredit Monitoring service for continuous consumer credit monitoring including alerts on credit profile changes.
  name: CRS Credit Monitoring API
  slug: credit-monitoring-api
- description: API for furnishing data to credit bureaus. Currently announced as coming soon on the CRS developer portal.
  name: CRS Data Furnishing API
  slug: data-furnishing-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crs-credit-api-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crscreditapi
- group: company
  title: ''
  type: Website
  url: https://crscreditapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://crscreditapi.redoc.ly/
- group: docs
  title: ''
  type: Reference
  url: https://crscreditapi.redoc.ly/
- group: company
  title: ''
  type: Blog
  url: https://crscreditapi.com/blog/
created: '2024-11-14'
description: CRS Credit API delivers credit data-as-a-service for fast, compliant financial decisioning. The platform aggregates consumer and business credit, identity, fraud, and public records data from major bureaus (Equifax, Experian, TransUnion, LexisNexis, CIC, PitchPoint) through a single contract and developer interface.
finops:
- name: Crs Credit Api Finops
  service_category: API
  slug: crs-credit-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crs-credit-api.png
layout: provider
modified: '2026-04-28'
name: CRS Credit API
nav: Providers
network: true
overview: 'CRS Credit API publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Credit, Consumer Credit, Business Credit, Identity, and Fraud.


  CRS Credit API''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Crs Credit Api Plans Pricing
  plan_count: 3
  slug: crs-credit-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Crs Credit Api Rate Limits
  slug: crs-credit-api-rate-limits
score:
  band: emerging
  composite: 14.5
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crs-credit-api/refs/heads/main/screenshots/crs-credit-api-2026-06-20T175259.png
security:
- kind: domain-security
  name: Crs Credit Api Domain Security
  slug: crs-credit-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crs-credit-api
tags:
- Credit
- Consumer Credit
- Business Credit
- Identity
- Fraud
- Data
website: https://crscreditapi.com/
---
