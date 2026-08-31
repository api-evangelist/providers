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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pharos.health
created: '2026-07-17'
description: Pharos is a healthcare technology company whose stated mission is to improve hospital quality and patient safety. Backed by Felicis, it operates a gated product application (app.pharos.health) and access-restricted documentation (docs.pharos.health requires an access code), indicating an enterprise offering sold to hospitals and health systems rather than a public, self-serve developer platform. As of this enrichment pass Pharos publishes a marketing site but no public API, OpenAPI specification, SDKs, developer portal, or other machine-readable developer surface. Surfaced as a portfolio company of Felicis and added to the API Evangelist network as a lead, this profile is retained for monitoring should a public API program emerge.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pharos.png
layout: provider
modified: '2026-07-20'
name: Pharos
nav: Providers
network: true
overview: Pharos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Safety, Hospitals, and Quality Improvement.
random_paper: 2
score:
  band: minimal
  composite: 3.3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Pharos Domain Security
  slug: pharos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pharos
tags:
- Company
- Healthcare
- Patient Safety
- Hospitals
- Quality Improvement
- Health Technology
- Clinical
website: https://pharos.health
---
