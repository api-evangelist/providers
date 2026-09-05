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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.mindoktor.se/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/min-doktor-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/min-doktor-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://skandia.mindoktor.se/responsible-disclosure-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mindoktor
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mindoktor.se/integritetspolicy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mindoktor.se/anvandarvillkor/
created: '2026-07-17'
description: Min Doktor is a Swedish digital healthcare provider (operated by MD International AB) offering online primary care through its mobile app and web service. Founded in 2013 as one of Sweden's first digital-first care providers, it connects patients with doctors, psychologists and nurses for consultations, prescriptions, referrals and vaccinations, and also runs white-label care services for partners such as Skandia. It was surfaced as a portfolio company of EQT Ventures. Min Doktor operates as a consumer/patient-facing service and does not publish a public developer API or documentation surface; this profile captures its verifiable public security, identity and compliance footprint.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/min-doktor.png
layout: provider
modified: '2026-07-20'
name: Min Doktor
nav: Providers
network: true
overview: Min Doktor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Telemedicine, Digital Health, and Primary Care.
random_paper: 20
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/min-doktor/refs/heads/main/screenshots/min-doktor-2026-08-07T172920.png
security:
- kind: domain-security
  name: Min Doktor Domain Security
  slug: min-doktor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Min Doktor Vulnerability Disclosure
  slug: min-doktor-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: min-doktor
tags:
- Company
- Health Tech
- Telemedicine
- Digital Health
- Primary Care
- Healthcare
- Sweden
website: https://www.mindoktor.se/
---
