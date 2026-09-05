---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://tantanapp.com/en'', ''status'': 302, ''note'': ''declared website redirects to https://thetantanapp.com/ — a different registrable domain (tantanapp.com -> thetantanapp.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/tantan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tantanapp.com/en
created: '2026-07-17'
description: Tantan (探探) is a Chinese location-based social discovery and online dating application, launched in 2014 and widely described as "China's Tinder" for its swipe-based matching mechanic. The app pairs nearby users who mutually express interest and layers on messaging, moments, live streaming, and interest-based social features. An early DCM Ventures portfolio company, Tantan was acquired by Momo Inc. (now Hello Group) in 2018 and operates as a consumer mobile product across China and several international markets. Tantan is a mobile-first consumer app and publishes no public developer API, SDK, or developer portal; this profile captures its public web identity and probed domain-security posture.
image: https://tantanapp.com/intl2/static/media/logo.ico
layout: provider
modified: '2026-07-21'
name: Tantan
nav: Providers
network: true
overview: Tantan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Dating, Social, and Mobile.
random_paper: 16
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tantan/refs/heads/main/screenshots/tantan-2026-09-02T162525.png
security:
- kind: domain-security
  name: Tantan Domain Security
  slug: tantan-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tantan
tags:
- Company
- Consumer
- Dating
- Social
- Mobile
- Social Networking
- Online Dating
website: https://tantanapp.com/en
---
