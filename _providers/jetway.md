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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/travelperk/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextravel.com
created: '2026-07-17'
description: Jetway was surfaced as a 500 Global portfolio lead pointing at nextravel.com. Enrichment found that nextravel.com now 301-redirects to TravelPerk (www.travelperk.com), which itself redirects to www.perk.com, an all-in-one business travel and expense-management platform. NexTravel was a US corporate-travel startup acquired by TravelPerk; it no longer operates as an independent brand and publishes no public developer API, API documentation, developer portal, or /.well-known discovery documents at nextravel.com (every probed path soft-404s to the Perk marketing site). This profile is retained as an acquired/redirected lead with no independent developer surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetway.png
layout: provider
modified: '2026-07-19'
name: Jetway
nav: Providers
network: true
overview: Jetway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Corporate Travel, Business Travel, and Expense Management.
random_paper: 9
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/jetway/refs/heads/main/screenshots/jetway-2026-07-25T223138.png
security:
- kind: domain-security
  name: Jetway Domain Security
  slug: jetway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jetway
tags:
- Company
- Travel
- Corporate Travel
- Business Travel
- Expense Management
- Acquired
website: https://nextravel.com
---
