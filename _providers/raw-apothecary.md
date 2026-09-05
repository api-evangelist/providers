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
  url: security/raw-apothecary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rawapothecary.mx
created: '2026-07-17'
description: Raw Apothecary is a Mexico-based consumer brand that operated a Shopify storefront at rawapothecary.mx (Spanish-language, powered-by Shopify), surfaced in the API Evangelist network as a 500 Global portfolio company. As of this enrichment pass the storefront returns "Tienda no disponible" (HTTP 402, "Store Unavailable"), and the company publishes no public API, developer portal, documentation, or machine-readable specification surface. This profile is retained as a company record; there is no API to enrich beyond a live domain-security probe of the storefront host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raw-apothecary.png
layout: provider
modified: '2026-07-20'
name: Raw Apothecary
nav: Providers
network: true
overview: Raw Apothecary is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer, and Shopify.
random_paper: 19
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Raw Apothecary Domain Security
  slug: raw-apothecary-domain-security
  summary_line: TLSv1.3 · DMARC
slug: raw-apothecary
tags:
- Company
- E-Commerce
- Retail
- Consumer
- Shopify
- Mexico
website: https://rawapothecary.mx
---
