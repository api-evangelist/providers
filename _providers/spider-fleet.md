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
  url: security/spider-fleet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spider.com.mx
created: '2026-07-17'
description: Spiderfleet (Spider Fleet) is a Mexico-based intelligent fleet-management platform that helps businesses run and maintain their vehicle fleets. Its public site (spider.com.mx, in Spanish) markets fleet onboarding ("Flotillas"), preventive maintenance scheduling ("mantenimientos"), and quote requests ("cotizacion") for fleet operators, and is backed by 500 Global. As of this enrichment pass the company publishes only a static marketing website with no public API, developer portal, documentation, SDKs, or machine-readable specification; two navigation links (contact and login) return 404 and the site's TLS certificate is expired.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spider-fleet.png
layout: provider
modified: '2026-07-21'
name: Spider Fleet
nav: Providers
network: true
overview: Spider Fleet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fleet Management, Mobility, Telematics, and Vehicle Maintenance.
random_paper: 2
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: domain-security
  name: Spider Fleet Domain Security
  slug: spider-fleet-domain-security
  summary_line: DMARC
slug: spider-fleet
tags:
- Company
- Fleet Management
- Mobility
- Telematics
- Vehicle Maintenance
- Mexico
- Software-as-a-Service
website: https://spider.com.mx
---
