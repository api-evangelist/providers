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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ornikar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ornikar.com/
created: '2026-07-17'
description: 'Ornikar is a French online driving school and insurance company that guides consumers from earning their driving permit through to car, home, and pet insurance. Founded in France, it offers highway-code (code de la route) training, driving lessons, accelerated permit programs, point-recovery courses, and corporate road-safety training, alongside auto, home, and pet insurance products and CPF financing. Surfaced as a portfolio company of Partech and added to the API Evangelist network as a stub for enrichment. Sector: Consumer. No public developer API surface was found during the enrichment pass; only domain-security signals were probed.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ornikar.png
layout: provider
modified: '2026-07-20'
name: Ornikar
nav: Providers
network: true
overview: Ornikar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Insurance, Driving School, and Education.
random_paper: 2
score:
  band: minimal
  composite: 2.3
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
  previous_composite: 2.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ornikar/refs/heads/main/screenshots/ornikar-2026-08-07T190947.png
security:
- kind: domain-security
  name: Ornikar Domain Security
  slug: ornikar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ornikar
tags:
- Company
- Consumer
- Insurance
- Driving School
- Education
- Insurtech
- France
website: https://www.ornikar.com/
---
