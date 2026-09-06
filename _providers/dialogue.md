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
  url: security/dialogue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dialogue.co/en
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dialogue.co/en/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.dialogue.co/en/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dialogue.co/en/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dialogue.co/en/terms
- group: operate
  title: ''
  type: Support
  url: https://help.dialogue.co/hc/en-ca
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dialogue.co/
- group: start
  title: ''
  type: Login
  url: https://app.dialogue.co/?lng=en
created: '2026-07-17'
description: Dialogue is a leading Canadian virtual healthcare and employee wellness provider operating an Integrated Health Platform that delivers primary care, mental health support, Employee Assistance Programs (EAP), and wellness programming to members through a single mobile and web application available 24/7/365. The company serves more than 52,000 Canadian organizations — including Sun Life, National Bank of Canada, Via Rail, Lightspeed, and Samsung — connecting employees and their families with multidisciplinary care teams of nurses, physicians, and mental health specialists. Dialogue is a consumer-facing digital health application; it does not currently publish a public developer API or OpenAPI surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dialogue.png
layout: provider
modified: '2026-07-18'
name: Dialogue
nav: Providers
network: true
overview: 'Dialogue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telemedicine, Virtual Care, and Mental Health.


  Dialogue''s developer surface includes pricing, engineering blog, support, and 6 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 15.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dialogue/refs/heads/main/screenshots/dialogue-2026-07-25T211910.png
security:
- kind: domain-security
  name: Dialogue Domain Security
  slug: dialogue-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dialogue
tags:
- Company
- Healthcare
- Telemedicine
- Virtual Care
- Mental Health
- Employee Assistance Program
- Wellness
- Consumer
- Canada
website: https://www.dialogue.co/en
---
