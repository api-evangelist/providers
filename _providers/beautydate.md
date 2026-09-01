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
- group: company
  title: ''
  type: Website
  url: https://beautydate.com.br
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beautydate-domain-security.yml
created: '2026-07-17'
description: BeautyDate (beautydate.com.br) is a Brazilian beauty and wellness marketplace that connects consumers with salons and independent beauty professionals for discovering and booking appointments online. It was surfaced as a 500 Global venture-portfolio company and added to the API Evangelist network for enrichment. At the time of this enrichment pass the public website and application endpoints were unreachable (HTTP 530 behind Cloudflare, with api.beautydate.com.br redirecting to a down app.beautydate.com.br origin), so no developer portal, API documentation, or machine-readable specification could be captured.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beautydate.png
layout: provider
modified: '2026-07-18'
name: BeautyDate
nav: Providers
network: true
overview: BeautyDate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Beauty, Booking, Scheduling, and Appointments.
random_paper: 14
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
  name: Beautydate Domain Security
  slug: beautydate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beautydate
tags:
- Company
- Beauty
- Booking
- Scheduling
- Appointments
- Marketplace
- Brazil
- Wellness
website: https://beautydate.com.br
---
