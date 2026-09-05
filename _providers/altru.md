---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://altrulabs.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.icims.com/ — a different registrable domain (altrulabs.com -> icims.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/altru-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altrulabs.com/
- group: start
  title: ''
  type: Login
  url: https://app.altrulabs.com/
created: '2026-07-17'
description: Altru (Altru Labs, Inc.) was a mobile-first, employee-generated video storytelling platform for recruitment marketing and talent acquisition, enabling organizations to capture, edit, brand, approve, and distribute authentic employee video content across career sites, social media, and email/text campaigns, with video transcription in 14+ languages. Founded in 2017 and based in Brooklyn, New York, and backed by Techstars, Altru served brands including Target, PwC, Intuit, L'Oreal, and Box before being acquired by iCIMS on December 14, 2020 and folded into the iCIMS Talent Cloud. Altru no longer operates as an independent provider — altrulabs.com now redirects to icims.com and there is no public developer or API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/altru.png
layout: provider
modified: '2026-07-17'
name: Altru
nav: Providers
network: true
overview: Altru is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Talent Acquisition, Recruitment Marketing, HR Tech, and Video.
random_paper: 6
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altru/refs/heads/main/screenshots/altru-2026-07-25T195842.png
security:
- kind: domain-security
  name: Altru Domain Security
  slug: altru-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: altru
tags:
- Company
- Talent Acquisition
- Recruitment Marketing
- HR Tech
- Video
- Employee Generated Content
- Employer Branding
- Acquired
website: https://altrulabs.com/
---
