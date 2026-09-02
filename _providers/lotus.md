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
  url: security/lotus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lotus.ai/
- group: operate
  title: ''
  type: Support
  url: https://help.lotus.ai/en/
created: '2026-07-17'
description: 'Lotus (Lotus Health AI) is a consumer healthcare company delivering AI-driven medical care backed by real physicians through an iOS app. The service offers an AI Doctor that analyzes a member''s health, prescriptions sent to any U.S. pharmacy, lab orders across 6,000+ test sites, centralized medical-record storage, and 24/7 care. Founded by KJ Dhaliwal (CEO) and Zekka Nelson (CTO) with clinicians from UCLA Health, UCSF, and Johns Hopkins, and backed by CRV among others. As of this enrichment pass Lotus publishes no public developer/API surface: no developer portal, API documentation, OpenAPI, well-known discovery, or security.txt were found. Only an end-user Intercom help center and a careers page are public.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lotus.png
layout: provider
modified: '2026-07-20'
name: Lotus
nav: Providers
network: true
overview: 'Lotus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health, Artificial Intelligence, and Telehealth.


  Lotus'' developer surface includes support and 2 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 4.3
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lotus/refs/heads/main/screenshots/lotus-2026-07-25T225558.png
security:
- kind: domain-security
  name: Lotus Domain Security
  slug: lotus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lotus
tags:
- Company
- Healthcare
- Health
- Artificial Intelligence
- Telehealth
- Digital Health
- Consumer App
website: https://lotus.ai/
---
