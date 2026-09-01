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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/casaone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.casaone.com
created: '2026-07-17'
description: CasaOne is a US-based home-furnishing and furniture-rental company backed by Accel, offering month-to-month rental of furniture, decor, and appliances for homes, offices, and real-estate staging, with an option to buy rented pieces. It operated a direct-to-consumer e-commerce storefront serving multiple US metros. As of this profiling its public storefront at www.casaone.com returns an HTTP 402 "Store unavailable" response (a frozen/unpaid storefront state), and no public developer portal, API documentation, or machine-readable API surface (OpenAPI/AsyncAPI/GraphQL) could be located. This API Evangelist profile records the company identity and its probed domain-security posture; no API artifacts are available to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/casaone.png
layout: provider
modified: '2026-07-18'
name: CasaOne
nav: Providers
network: true
overview: CasaOne is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Furniture, Rentals, and Homes.
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Casaone Domain Security
  slug: casaone-domain-security
  summary_line: TLSv1.3
slug: casaone
tags:
- Company
- Consumer
- Furniture
- Rentals
- Homes
- E-Commerce
- Staging
- Interior Design
website: http://www.casaone.com
---
