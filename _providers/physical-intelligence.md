---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.physicalintelligence.company'', ''status'': 308, ''note'': ''declared website redirects to https://www.pi.website/ — a different registrable domain (physicalintelligence.company -> pi.website), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/physical-intelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.physicalintelligence.company
- group: company
  title: ''
  type: AlternateWebsite
  url: https://www.pi.website
- group: company
  title: ''
  type: Blog
  url: https://www.pi.website/blog
- group: other
  title: ''
  type: Research
  url: https://www.pi.website/research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Physical-Intelligence
- group: other
  title: ''
  type: OpenPi
  url: https://github.com/Physical-Intelligence/openpi
- group: company
  title: ''
  type: Careers
  url: https://www.pi.website/careers
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/physical_int
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/physical-intelligence
created: '2026-05-23'
description: 'Physical Intelligence (often styled "Pi" or "π") is a San Francisco-based research company building general-purpose foundation models for robotics with the stated goal of producing learning algorithms that can control any robot to do any task. The company has published a continuing line of Vision-Language-Action (VLA) models: π0 (October 2024, first generalist multi-task multi-robot policy), π0-FAST (autoregressive variant via Real-time Action Chunking / FAST tokenization), π0.5 (April 2025, open-world generalization), π*0.6 (November 2025, reinforcement-learning from experience), and π0.7 (April 2026, steerable model with emergent capabilities). Physical Intelligence releases significant work as open source: the openpi repository (~12K stars) is the canonical home for π0 weights and code, with companion repos including real-time-chunking-kinetix, pi-data-sharing, aloha, augmax, and rlds_dataset_builder. The company does not yet offer a hosted commercial API; access to the
  platform is via open-weight models and research collaborations.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/physical-intelligence.png
layout: provider
modified: '2026-05-23'
name: Physical Intelligence
nav: Providers
network: true
overview: 'Physical Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Foundation Models, Vision Language Action, Embodied AI, and Reinforcement Learning.


  Physical Intelligence''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 3.1
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 3.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/physical-intelligence/refs/heads/main/screenshots/physical-intelligence-2026-06-20T191657.png
security:
- kind: domain-security
  name: Physical Intelligence Domain Security
  slug: physical-intelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: physical-intelligence
tags:
- Robotics
- Foundation Models
- Vision Language Action
- Embodied AI
- Reinforcement Learning
- Imitation Learning
- Open-Source
- Open Weights
- pi0
- openpi
- Manipulation
- Generalist Policy
website: https://www.physicalintelligence.company
---
