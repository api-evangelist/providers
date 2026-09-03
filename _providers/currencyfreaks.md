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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Provides current and historical currency exchange rates with free plan 1K requests/month
  name: CurrencyFreaks
  slug: currencyfreaks
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currencyfreaks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://currencyfreaks.com/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://currencyfreaks.com/blog
created: '2026-05-28'
description: Provides current and historical currency exchange rates with free plan 1K requests/month
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/currencyfreaks.png
layout: provider
modified: '2026-05-28'
name: CurrencyFreaks
nav: Providers
network: true
overview: 'CurrencyFreaks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Currency Exchange and Public APIs.


  CurrencyFreaks'' developer surface includes engineering blog and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/currencyfreaks/refs/heads/main/screenshots/currencyfreaks-2026-06-20T175337.png
security:
- kind: domain-security
  name: Currencyfreaks Domain Security
  slug: currencyfreaks-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: currencyfreaks
tags:
- Currency Exchange
- Public APIs
website: https://currencyfreaks.com/
---
