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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baba-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baba.care/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://baba.care/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://baba.care/privacy
- group: start
  title: ''
  type: Login
  url: https://baba.care/
- group: operate
  title: ''
  type: Support
  url: mailto:help@callbaba.com
created: '2026-07-17'
description: Baba Care, Inc. is a healthcare company that provides patient advocacy and care-navigation services for Medicare beneficiaries in the United States. Operating under the tagline "Healthcare simplified," Baba pairs each member with a dedicated advocate who handles their healthcare headaches — coordinating care, benefits, and administrative tasks — with the service covered by Medicare. The member experience is delivered through a login-gated web application at baba.care; the company publishes no public developer or API surface at this time. This profile was surfaced as a portfolio company of General Catalyst and added to the API Evangelist network for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/baba.png
layout: provider
modified: '2026-07-18'
name: Baba
nav: Providers
network: true
overview: 'Baba is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medicare, Patient Advocacy, and Care Navigation.


  Baba''s developer surface includes support and 5 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baba/refs/heads/main/screenshots/baba-2026-07-25T202149.png
security:
- kind: domain-security
  name: Baba Domain Security
  slug: baba-domain-security
  summary_line: TLSv1.3 · HSTS
slug: baba
tags:
- Company
- Healthcare
- Medicare
- Patient Advocacy
- Care Navigation
- Health Insurance
- Digital Health
website: https://baba.care/
---
