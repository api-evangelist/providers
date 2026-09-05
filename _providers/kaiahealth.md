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
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kaiahealth-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kaiahealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://kaiahealth.com/legal/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/kaiahealth-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kaiahealth-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kaiahealth.com/legal/security/
- group: company
  title: ''
  type: Website
  url: https://www.kaiahealth.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KaiaHealth
- group: company
  title: ''
  type: Blog
  url: https://kaiahealth.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.kaiahealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kaiahealth.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kaiahealth.com/legal/terms-conditions/
created: '2026-07-17'
description: Kaia Health is a digital therapeutics company founded in 2016 (New York and Munich) that delivers evidence-based, digital-first care for musculoskeletal (MSK) pain and respiratory conditions. Its smartphone apps use AI and computer vision (motion tracking) plus in-house physical-therapy doctors to guide members through clinically validated exercise and behavioral programs without appointments or wearable devices. Products include Kaia MSK (joint and muscle care) and Kaia Breathe (respiratory / COPD). The company sells to employers and health plans, claims 2,500+ enterprise clients and 3x ROI, and is HIPAA, GDPR, HITRUST, SOC 2 Type II, ISO 27001, ISO 13485, and CE-certified. Kaia Health was acquired by Sword Health in January 2026. It is backed by Balderton Capital. Kaia Health publishes no public API; this profile captures its identity, security, and compliance posture.
image: https://avatars.githubusercontent.com/u/31281033?v=4
layout: provider
modified: '2026-07-19'
name: kaiahealth
nav: Providers
network: true
overview: 'kaiahealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Therapeutics, Digital Health, Healthcare, and Musculoskeletal.


  kaiahealth''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 20.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    - jurisdiction: US
      standard: hitrust
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Health
    regime_id: health
    score: 37.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kaiahealth/refs/heads/main/screenshots/kaiahealth-2026-07-25T223410.png
security:
- kind: domain-security
  name: Kaiahealth Domain Security
  slug: kaiahealth-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kaiahealth Vulnerability Disclosure
  slug: kaiahealth-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Kaiahealth Trust Center
  slug: kaiahealth-trust-center
  summary_line: SOC 2 Type II, ISO 27001, ISO 13485, HITRUST, HIPAA, GDPR, CCPA, CE Medical Device
slug: kaiahealth
tags:
- Company
- Digital Therapeutics
- Digital Health
- Healthcare
- Musculoskeletal
- MSK
- DTx
- Physical Therapy
website: https://www.kaiahealth.com/
---
