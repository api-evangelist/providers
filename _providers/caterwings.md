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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://caterwings.de/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caterwings-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caterwings-well-known.yml
created: '2026-07-17'
description: 'Caterwings was a European online catering marketplace connecting businesses with local caterers for office and event food ordering, surfaced in the API Evangelist network as a portfolio company of HV Capital. As of the July 2026 enrichment probe the brand appears to be retired: caterwings.com no longer serves a site (AWS S3 responds 403 AllAccessDisabled) and caterwings.de redirects to www.eatfirst.com, the corporate-catering platform operated by B2B Food Group of Berlin, which also runs the EatFirst and Feedr brands. No developer portal, API documentation, OpenAPI definition, SDK package, or GitHub organization could be found for Caterwings; this repo is retained as a historical network record with no live API surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/caterwings.png
layout: provider
modified: '2026-07-20'
name: Caterwings
nav: Providers
network: true
overview: Caterwings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Catering, and Food Delivery.
random_paper: 8
score:
  band: minimal
  composite: 5.0
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caterwings/refs/heads/main/screenshots/caterwings-2026-07-25T204807.png
security:
- kind: domain-security
  name: Caterwings Domain Security
  slug: caterwings-domain-security
  summary_line: TLSv1.3 · HSTS
slug: caterwings
tags:
- Company
- Consumer
- Marketplace
- Catering
- Food Delivery
- Food and Beverage
- Europe
- Defunct
website: https://caterwings.de/
---
