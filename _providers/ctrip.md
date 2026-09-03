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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ctrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ctrip.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openapi.ctrip.com/
- group: docs
  title: ''
  type: Documentation
  url: https://connect.trip.com/doc/trip
created: '2026-07-17'
description: 'Ctrip (Ctrip.com International / Trip.com Group, NASDAQ: TCOM) is one of the world''s largest online travel agencies, founded in 1999 and headquartered in Shanghai, China. Its consumer platform sells hotels, flights, train tickets, car rentals, tours, cruises, and travel packages across China and internationally, and the broader Trip.com Group also operates the Trip.com, Qunar, and Skyscanner brands. Ctrip exposes partner and B2B travel-distribution capabilities through the Ctrip Open Platform (openapi.ctrip.com), the Trip.com Group open platform (connect.trip.com), and a corporate-travel developer platform (ctripbiz). These developer surfaces are partner-gated and largely account-restricted; no public OpenAPI or first-party SDK has been discovered for this profile.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ctrip.png
layout: provider
modified: '2026-07-18'
name: Ctrip
nav: Providers
network: true
overview: 'Ctrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Technology, Travel, Online Travel Agency, and Hotels.


  Ctrip''s developer surface includes documentation and 3 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.8
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
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ctrip/refs/heads/main/screenshots/ctrip-2026-07-25T210858.png
security:
- kind: domain-security
  name: Ctrip Domain Security
  slug: ctrip-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ctrip
tags:
- Company
- Consumer Technology
- Travel
- Online Travel Agency
- Hotels
- Flights
- Trip.com Group
- China
website: https://ctrip.com/
---
