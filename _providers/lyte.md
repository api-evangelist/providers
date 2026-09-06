---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/lyte-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lyte.ai/
- group: operate
  title: ''
  type: Support
  url: https://lyte.ai/Support
- group: company
  title: ''
  type: Blog
  url: https://lyte.ai/News
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lyte.ai/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lyte.ai/Privacy
- group: company
  title: ''
  type: Careers
  url: https://lyte.ai/Careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lyte-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Lyte ships an embedded robotics perception system (LyteVision hardware plus an on-device stack that streams into NVIDIA Holoscan/Isaac), not a developer platform — its own llms.txt and sitemap enumerate all sixteen pages on lyte.ai and none of them is a developer portal, API reference or docs page, and api./docs./developer./developers./ sdk./portal./status.lyte.ai all fail to resolve (NXDOMAIN).
  evidence:
  - status: 200
    url: https://lyte.ai/llms.txt
  - status: 200
    url: https://lyte.ai/sitemap.xml
  - status: 404
    url: https://lyte.ai/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: Lyte is a Mountain View, California perception company building an end-to-end integrated vision system for robotics and Physical AI. Founded in 2021 by Alexander Shpunt, Arman Hajati and Yuval Gerson — architects of Apple's depth-sensing and Face ID perception stack, and, in Shpunt's case, co-founder and CTO of PrimeSense — the company emerged from stealth in January 2026 with $107M in aggregate funding from Fidelity Management & Research, Atreides Management, Exor Ventures, Key1 Capital, Avigdor Willenz's group and Venture Tech Alliance. Its flagship product, LyteVision, combines 4D sensing (distance plus velocity), RGB imaging and inertial motion awareness with custom silicon and software into a single plug-and-play perception platform for robots, mobility and next-generation automation; it won a CES 2026 Best of Innovation award in Robotics and was named an honoree in Vehicle Tech and Advanced Mobility. Lyte is collaborating with NVIDIA to stream perception into GPUs over
  Holoscan Sensor Bridge (zero-copy, Jetson Thor, CUDA, NITROS) and into Omniverse and Isaac Sim for real-time digital twins. Lyte ships hardware and an embedded perception stack rather than a developer platform, and publishes no public API, SDK, developer portal or machine-readable contract as of this profile.
image: https://qtrypzzcjebvfcihiynt.supabase.co/storage/v1/object/public/base44-prod/public/691d45a813e743f6146d0261/5b76f1f0f_Lyte_logo.png
layout: provider
modified: '2026-08-25'
name: Lyte
nav: Providers
network: true
overview: 'Lyte is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Computer-Vision, Perception, Sensors, and Physical AI.


  Lyte''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lyte/refs/heads/main/screenshots/lyte-2026-09-02T150411.png
security:
- kind: domain-security
  name: Lyte Domain Security
  slug: lyte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lyte
tags:
- Robotics
- Computer-Vision
- Perception
- Sensors
- Physical AI
- Semiconductors
- Artificial Intelligence
- Advanced Mobility
- Hardware
website: https://lyte.ai/
---
