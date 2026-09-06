---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://oculus.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.meta.com/quest/ — a different registrable domain (oculus.com -> meta.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/oculus-vr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://oculus.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.meta.com/horizon/
created: '2026-07-17'
description: Oculus VR is the pioneering virtual reality company founded in 2012 and acquired by Facebook (now Meta) in 2014. Its Rift, Go, and Quest headsets defined consumer VR, and the Oculus brand has since been folded into Meta Quest and Meta Horizon OS. The former developer.oculus.com and oculus.com properties now redirect to Meta's developer platform. There is no distinct public REST/OpenAPI surface; developers build against SDK-based tooling (Unity, Unreal Engine, native OpenXR, and the Meta Spatial SDK) rather than a hosted web API. Backed originally by a16z; consumer VR/AR hardware and platform.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oculus-vr.png
layout: provider
modified: '2026-07-20'
name: Oculus VR
nav: Providers
network: true
overview: 'Oculus VR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Virtual Reality, Augmented Reality, and Gaming.


  Oculus VR''s developer surface includes documentation and 2 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 6.9
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
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oculus-vr/refs/heads/main/screenshots/oculus-vr-2026-08-07T185948.png
security:
- kind: domain-security
  name: Oculus Vr Domain Security
  slug: oculus-vr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oculus-vr
tags:
- Company
- Consumer
- Virtual Reality
- Augmented Reality
- Gaming
- Hardware
- Headsets
- Metaverse
website: https://oculus.com
---
