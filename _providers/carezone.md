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
  url: security/carezone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carezone.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carezone.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carezone.com/tos.html
created: '2026-07-17'
description: CareZone is a consumer digital-health company (Care Zone Inc., backed by Obvious Ventures) offering a medication-management and family health-organization platform. Its mobile app lets people scan pill bottles to track medications, set reminders, log health readings such as blood glucose and blood pressure, and organize care information for themselves and loved ones, with a free medication delivery service and Medicare savings consultations. CareFlow, CareZone's pharmacy platform, automates traditional pharmacy workflows behind an ecommerce experience. The app reports over 5 million installs. CareZone operates as a consumer product and does not publish a public developer program, API documentation, or SDKs; this profile captures its public identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carezone.png
layout: provider
modified: '2026-07-18'
name: Carezone
nav: Providers
network: true
overview: Carezone is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Health, Medication Management, Digital Health, and Pharmacy.
random_paper: 15
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carezone/refs/heads/main/screenshots/carezone-2026-07-25T204602.png
security:
- kind: domain-security
  name: Carezone Domain Security
  slug: carezone-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carezone
tags:
- Company
- Human Health
- Medication Management
- Digital Health
- Pharmacy
- Consumer Health
- Care Coordination
website: https://carezone.com
---
