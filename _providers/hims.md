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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hims-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://forhims.com/vulnerability-disclosure-terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hims-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hims-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hims-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://forhims.com
created: '2026-07-17'
description: 'Hims is the men''s brand of Hims & Hers Health, Inc. (NYSE: HIMS), a U.S.-based direct-to-consumer telehealth platform. Through forhims.com it connects patients with licensed medical providers and affiliated pharmacies to offer treatment for sexual health, hair loss, dermatology and skincare, mental health, and weight loss, including provider consultations, personalized prescriptions, and recurring subscription fulfillment shipped to the customer. Hims & Hers operates the sibling Hers brand for women and runs its own pharmacy and fulfillment operations. This API Evangelist profile tracks the company''s public developer, security, and trust surface; Hims does not currently publish a public developer API, so this record is identity- and security-focused rather than spec-bearing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hims.png
layout: provider
modified: '2026-07-19'
name: Hims
nav: Providers
network: true
overview: Hims is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Wellness.
random_paper: 13
score:
  band: minimal
  composite: 5.8
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
    operational_transparency: 10.5
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Hims Domain Security
  slug: hims-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hims Vulnerability Disclosure
  slug: hims-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hims
tags:
- Company
- Health
- Healthcare
- Telehealth
- Wellness
- Pharmacy
- Consumer
- E-Commerce
website: https://forhims.com
---
