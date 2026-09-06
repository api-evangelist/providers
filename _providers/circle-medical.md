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
  url: security/circle-medical-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.circlemedical.com
- group: company
  title: ''
  type: Blog
  url: https://www.circlemedical.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.circlemedical.com/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.circlemedical.com/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.circlemedical.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.circlemedical.com/legal/terms-of-use
- group: auth
  title: ''
  type: Compliance
  url: https://www.circlemedical.com/legal/notice-of-hipaa-privacy-practices
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/circlemedical
created: '2026-07-17'
description: Circle Medical is a San Francisco-based online and in-person primary care clinic offering telemedicine and clinic-based visits with same and next-day availability. Founded through Y Combinator, the company operates 20+ physical locations and provides virtual appointments across multiple US states through Circle Medical Care of California, an independent medical practice. Its 400+ board-certified physicians, physician assistants, and nurse practitioners treat primary care, mental health (ADHD, anxiety, depression), hormone and sexual health, urgent care, weight loss (GLP-1s), sleep, and dermatology. Circle Medical is a HIPAA-covered, patient-facing digital health provider; it publishes no public developer API or SDK program, and this profile captures its public web, legal, support, and security surface for the API Evangelist network.
image: https://www.circlemedical.com/_astro/logo.B6HQVoip.webp
layout: provider
modified: '2026-07-18'
name: Circle Medical
nav: Providers
network: true
overview: 'Circle Medical is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Primary Care, and Digital Health.


  Circle Medical''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circle-medical/refs/heads/main/screenshots/circle-medical-2026-07-25T205410.png
security:
- kind: domain-security
  name: Circle Medical Domain Security
  slug: circle-medical-domain-security
  summary_line: TLSv1.3 · DMARC
slug: circle-medical
tags:
- Company
- Healthcare
- Telehealth
- Primary Care
- Digital Health
- Telemedicine
- HIPAA
website: https://www.circlemedical.com
---
