---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://opsani.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.splunk.com/en_us/appdynamics-joins-splunk.html?301=appdynamics — a different registrable domain (opsani.com -> splunk.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
artifact_total: 0
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/opsani/servox/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/opsani/servox/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/opsani/servox/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://opsani.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opsani
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/opsani/servox
- group: build
  title: ''
  type: Packages
  url: packages/opsani-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/opsani-packages.yml
created: '2026-07-17'
description: Opsani was an enterprise software company based in Redwood City, California that delivered an ML-driven cloud platform for Continuous Optimization as a Service (COaaS), automatically and continuously tuning cloud-native (Kubernetes) application configurations for the best balance of performance, availability, and cost. Opsani was acquired by Cisco in January 2022 and folded into the Cisco AppDynamics full-stack observability portfolio (subsequently part of Splunk). The company no longer operates an independent API surface — opsani.com now redirects to Splunk and docs.opsani.com no longer resolves. The one surviving public first-party artifact is the open-source Servo (servox) optimization agent, still published on PyPI and hosted at github.com/opsani.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opsani.png
layout: provider
modified: '2026-07-20'
name: Opsani
nav: Providers
network: true
overview: Opsani is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Optimization, Kubernetes, Cloud-Native, and Machine-Learning.
random_paper: 20
score:
  band: minimal
  composite: 10.4
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  open_source:
    applies: true
    score: 25.0
  previous_composite: 10.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opsani/refs/heads/main/screenshots/opsani-2026-08-07T190744.png
slug: opsani
tags:
- Company
- Optimization
- Kubernetes
- Cloud-Native
- Machine-Learning
- Observability
- Acquired
website: https://opsani.com/
---
