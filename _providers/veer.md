---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://veer.tv'', ''status'': 301, ''note'': ''declared website redirects to https://veervr.com/ — a different registrable domain (veer.tv -> veervr.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/veer-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/veer-llms.txt
- group: company
  title: ''
  type: Website
  url: https://veer.tv
created: '2026-07-17'
description: VeeR VR is a virtual reality content community founded in June 2016 that lets creators produce, edit, and share 360-degree videos and photos through its VeeR VR and VeeR Editor mobile apps, and is a Qiming Venture Partners portfolio company. As of July 2026 the company publishes no public API surface, and its primary domain veer.tv redirects to veervr.com, which no longer resolves.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/veer.png
layout: provider
modified: '2026-07-21'
name: VeeR VR
nav: Providers
network: true
overview: VeeR VR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Virtual Reality, 360 Video, Video Sharing, and Content Community.
random_paper: 14
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/veer/refs/heads/main/screenshots/veer-2026-09-02T165601.png
security:
- kind: domain-security
  name: Veer Domain Security
  slug: veer-domain-security
  summary_line: TLSv1.3
slug: veer
tags:
- Company
- Virtual Reality
- 360 Video
- Video Sharing
- Content Community
- Mobile Apps
website: https://veer.tv
---
