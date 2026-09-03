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
  url: security/verse-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.versemedical.com/
created: '2026-07-17'
description: Verse Medical is a software-driven durable medical equipment (DME) supplier delivering hospital-quality healthcare at home across the United States. Founded in 2018 (Y Combinator S18) and based in New York City, the company builds software that replaces fax-based ordering so doctors and clinics can prescribe, order, and manage medical supplies such as catheters, wound dressings, and diabetes supplies for patients at home. Backed by General Catalyst, SignalFire, Sapphire Ventures, Abstract Ventures, and Y Combinator. No public developer API, docs portal, or specification surface was found during enrichment; this profile carries company identity plus a probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/verse-medical.png
layout: provider
modified: '2026-07-21'
name: Verse Medical
nav: Providers
network: true
overview: Verse Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Durable Medical Equipment, Home Healthcare, and Medical Supplies.
random_paper: 11
score:
  band: minimal
  composite: 3.3
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/verse-medical/refs/heads/main/screenshots/verse-medical-2026-09-02T165749.png
security:
- kind: domain-security
  name: Verse Medical Domain Security
  slug: verse-medical-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: verse-medical
tags:
- Company
- Health Tech
- Durable Medical Equipment
- Home Healthcare
- Medical Supplies
- Health Technology
- DME
website: https://www.versemedical.com/
---
