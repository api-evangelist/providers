---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://lumoshelmet.co/'', ''status'': 301, ''note'': ''declared website redirects to https://ridelumos.com/ — a different registrable domain (lumoshelmet.co -> ridelumos.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/lumos-helmet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lumoshelmet.co/
- group: operate
  title: ''
  type: Support
  url: https://lumoshelmetsupport.zendesk.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridelumos.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridelumos.com/policies/terms-of-service
created: '2026-07-17'
description: Lumos (Lumos Helmet) is a consumer hardware company that designs and manufactures smart bike helmets and connected bike lights with integrated safety features such as turn signals, brake lights, and high-visibility LED lighting. Its product line spans commuter, e-bike, and kids' helmets plus standalone smart bike lights, controlled through companion iOS and Android mobile apps. Backed by Techstars, Lumos sells direct-to-consumer through an online store; it does not currently publish a public API, developer platform, or SDK. This profile was enriched by the API Evangelist pipeline, which confirmed no programmatic API surface and captured the company's identity and domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lumos-helmet.png
layout: provider
modified: '2026-07-20'
name: Lumos Helmet
nav: Providers
network: true
overview: 'Lumos Helmet is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Hardware, Wearables, Cycling, and Bike Safety.


  Lumos Helmet''s developer surface includes support and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.2
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lumos-helmet/refs/heads/main/screenshots/lumos-helmet-2026-08-07T171846.png
security:
- kind: domain-security
  name: Lumos Helmet Domain Security
  slug: lumos-helmet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lumos-helmet
tags:
- Company
- Consumer Hardware
- Wearables
- Cycling
- Bike Safety
- Smart Helmets
- IoT
- Mobile Apps
website: https://lumoshelmet.co/
---
