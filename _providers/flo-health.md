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
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flo-health-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flo-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flo.health/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.flo.health/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://flo.health/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://flo.health/careers
- group: company
  title: ''
  type: Press
  url: https://flo.health/press-center
- group: other
  title: ''
  type: MedicalAffairs
  url: https://flo.health/medical-affairs-and-research
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flo-health-inc-
created: '2026-05-23'
description: Flo Health operates the Flo app, a leading consumer period, ovulation, pregnancy, and reproductive health tracker with hundreds of millions of downloads worldwide. The product surface includes cycle tracking, ovulation and pregnancy predictions, an AI-assisted symptom checker, Secret Chats, Flo for Partners (partner-shared mode), Anonymous Mode, and a Premium subscription tier. Flo's Medical Affairs team partners with clinicians and researchers on women's health science. Flo is a consumer mobile product; no public developer API or partner API portal has been identified at this time. This entry catalogs the company surface for the API Evangelist index.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flo-health.png
layout: provider
modified: '2026-05-23'
name: Flo Health
nav: Providers
network: true
overview: Flo Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Femtech, Women's Health, Reproductive Health, Period Tracker, and Cycle Tracking.
random_paper: 9
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 91.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flo-health/refs/heads/main/screenshots/flo-health-2026-06-20T181317.png
security:
- kind: domain-security
  name: Flo Health Domain Security
  slug: flo-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Flo Health Vulnerability Disclosure
  slug: flo-health-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flo-health
tags:
- Femtech
- Women's Health
- Reproductive Health
- Period Tracker
- Cycle Tracking
- Fertility
- Pregnancy
- Consumer App
- Mobile Health
website: https://flo.health/
---
