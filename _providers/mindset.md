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
  url: security/mindset-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmindset.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://api.getmindset.com/pages/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://mindsetdive.zendesk.com/hc/en-us/requests/new
- group: start
  title: ''
  type: Login
  url: https://api.getmindset.com/login
created: '2026-07-17'
description: Mindset is a mobile self-care and wellness application by DIVE Studios that pairs audio content from celebrity artists and musicians with expert-led mental health resources. Features include Celebrity Mindsets audio collections, a five-minute Daily Check-In routine, Daily Reflections community sharing, licensed-professional advice, and daily quotes, delivered on iOS and Android with a 50,000+ member Discord community. Mindset operates a private, login-gated mobile backend at api.getmindset.com behind Google OAuth; no public developer API, documentation, SDKs, or well-known discovery surface is published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindset.png
layout: provider
modified: '2026-07-20'
name: Mindset
nav: Providers
network: true
overview: 'Mindset is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellness, Mental Health, Self-Care, and Audio.


  Mindset''s developer surface includes support and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindset/refs/heads/main/screenshots/mindset-2026-08-07T172937.png
security:
- kind: domain-security
  name: Mindset Domain Security
  slug: mindset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindset
tags:
- Company
- Wellness
- Mental Health
- Self-Care
- Audio
- Consumer
- Mobile App
website: https://www.getmindset.com
---
