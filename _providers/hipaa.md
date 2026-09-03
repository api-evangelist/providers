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
  url: security/hipaa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hhs.gov/hipaa/index.html
- group: docs
  title: ''
  type: Reference
  url: https://www.hhs.gov/hipaa/for-professionals/index.html
created: '2025'
description: HIPAA (Health Insurance Portability and Accountability Act) is U.S. legislation providing data privacy and security provisions for safeguarding medical information. HIPAA compliance is required for healthcare providers, health plans, and their business associates handling protected health information (PHI).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hipaa.png
layout: provider
modified: '2026-04-28'
name: HIPAA
nav: Providers
network: true
overview: HIPAA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Compliance, Healthcare, Privacy, and Security.
random_paper: 11
score:
  band: minimal
  composite: 3.8
  coverage:
    artifact_dirs: 2
    catalog_gap: 93.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hipaa/refs/heads/main/screenshots/hipaa-2026-06-20T182743.png
security:
- kind: domain-security
  name: Hipaa Domain Security
  slug: hipaa-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: hipaa
tags:
- Compliance
- Healthcare
- Privacy
- Security
website: https://www.hhs.gov/hipaa/index.html
---
