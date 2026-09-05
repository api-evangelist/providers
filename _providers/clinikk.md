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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clinikk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clinikk.com
- group: company
  title: ''
  type: Blog
  url: https://clinikk.com/blog-home/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clinikk.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clinikk.com/terms-and-conditions/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clinikk-llms.txt
created: '2026-07-17'
description: Clinikk (Clinikk Health Hub) is a Bangalore, India-based primary healthcare provider offering membership-based access to unlimited doctor consultations, free prescribed medicines and lab tests, 24/7 teleconsultation, and optional group health insurance in partnership with IndusInd General Insurance. Clinikk operates in-person Health Hubs across Bangalore alongside a consumer mobile app, and was surfaced as a 500 Global portfolio company. No public developer API surface was found during enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clinikk.png
layout: provider
modified: '2026-07-18'
name: Clinikk
nav: Providers
network: true
overview: 'Clinikk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Primary Care, Health Insurance, and Telemedicine.


  Clinikk''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clinikk/refs/heads/main/screenshots/clinikk-2026-07-25T205627.png
security:
- kind: domain-security
  name: Clinikk Domain Security
  slug: clinikk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clinikk
tags:
- Company
- Healthcare
- Primary Care
- Health Insurance
- Telemedicine
- Membership
- India
website: https://clinikk.com
---
