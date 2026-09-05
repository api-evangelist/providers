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
  url: security/daybreak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.daybreakhealth.com
- group: company
  title: ''
  type: Blog
  url: https://www.daybreakhealth.com/resources
- group: operate
  title: ''
  type: Support
  url: https://www.daybreakhealth.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.daybreakhealth.com/daybreak-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.daybreakhealth.com/daybreak-privacy-policy
created: '2026-07-17'
description: Daybreak Health is a B2B mental health company that delivers teletherapy and mental health programs for K-12 students (ages 5-19) in partnership with school districts and health plans. Its services include one-on-one teletherapy, in-person and hybrid onsite programs, universal mental health screeners, and mental health classes, with programs tailored for BIPOC, LGBTQIA+, and low-income student populations. Daybreak is a care-delivery organization sold to schools and payers rather than a developer platform; as of this enrichment pass it publishes no public developer or API surface. This APIs.json profile captures the company's public web properties and domain-security posture.
image: https://cdn.prod.website-files.com/64bac3de8f242d758b850cba/64de0d9ac07ba4c4237977bd_og.png
layout: provider
modified: '2026-07-18'
name: Daybreak
nav: Providers
network: true
overview: 'Daybreak is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mental Health, Healthcare, Teletherapy, and Behavioral Health.


  Daybreak''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 10.5
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/daybreak/refs/heads/main/screenshots/daybreak-2026-07-25T211437.png
security:
- kind: domain-security
  name: Daybreak Domain Security
  slug: daybreak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: daybreak
tags:
- Company
- Mental Health
- Healthcare
- Teletherapy
- Behavioral Health
- Education
- K-12
- Digital Health
website: https://www.daybreakhealth.com
---
