---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - '{''url'': ''https://nianticlabs.com/'', ''status'': 301, ''note'': ''declared website redirects to https://explore.scopely.com/ — a different registrable domain (nianticlabs.com -> scopely.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: NSDK 4.x is Niantic Spatial's unified, SDK-first developer platform for Unity, Swift, Android, and ROS 2, exposing VPS 2.0 visual positioning (centimeter-level 6DoF localization), semantic understandi
  name: Niantic Spatial Development Kit (NSDK)
  slug: niantic-spatial-development-kit-nsdk
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://nianticlabs.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.nianticspatial.com/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.nianticspatial.com/docs/nsdk/
- group: docs
  title: ''
  type: APIReference
  url: https://www.nianticspatial.com/docs/api/unity/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.nianticspatial.com/docs/nsdk/setup/
- group: operate
  title: ''
  type: Support
  url: https://community.nianticspatial.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nianticspatial.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nianticspatial
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nianticspatial.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nianticspatial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nianticspatial.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/niantic-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/niantic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/niantic-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/niantic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/niantic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/niantic-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/niantic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/niantic-domain-security.yml
created: '2026-07-17'
description: Niantic Spatial, Inc. (spun out of Niantic, Inc. in 2025 after the sale of its games division to Scopely) builds real-world foundation models for physical AI. Its Large Geospatial Model (LGM), trained on 30+ billion posed real-world images, powers a three-part geospatial platform — Reconstruct (3D models via Gaussian splats and meshes), Localize (VPS, centimeter-level 6DoF visual positioning that works indoors, outdoors, and in GPS-denied environments), and Understand (semantic querying of 3D maps). Developers build on the Niantic Spatial Development Kit (NSDK 4.x, formerly the Lightship ARDK) across Unity, Swift, Android, and ROS 2, connecting to Scaniverse and VPS 2.0. Enterprise focus areas include robotics, defense and intelligence, and oil and gas.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/niantic.png
layout: provider
modified: '2026-07-20'
name: Niantic
nav: Providers
network: true
overview: 'Niantic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Geospatial, Augmented Reality, Computer-Vision, and Visual Positioning.


  Niantic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 12 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/niantic/refs/heads/main/screenshots/niantic-2026-08-07T185242.png
security:
- kind: authentication
  name: Niantic Authentication
  slug: niantic-authentication
  summary_line: apiKey/token · 2 schemes
- kind: domain-security
  name: Niantic Domain Security
  slug: niantic-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: niantic
tags:
- Company
- Geospatial
- Augmented Reality
- Computer-Vision
- Visual Positioning
- Spatial Computing
- SDK
- Physical AI
- Robotics
website: https://nianticlabs.com/
---
