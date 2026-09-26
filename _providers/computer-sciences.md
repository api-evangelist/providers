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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/computer-sciences-corporation-csc
- group: company
  title: ''
  type: Successor Website
  url: https://www.dxc.com
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Computer_Sciences_Corporation
- group: other
  title: ''
  type: DXC Wikipedia
  url: https://en.wikipedia.org/wiki/DXC_Technology
coverage:
  checked: '2026-09-05'
  detail: The Computer Sciences Corporation brand was retired on 2017-04-01 when CSC merged into DXC Technology; csc.com and www.csc.com now answer every path — including /openapi.json, /llms.txt and all seven /.well-known/ documents — with a blanket 301 to dxc.com/<path>?merger=true, and developer/api/apis/developers.csc.com have no DNS record at all.
  evidence:
  - status: 301
    url: https://csc.com/
  - status: 301
    url: https://csc.com/.well-known/api-catalog
  - status: 301
    url: https://csc.com/openapi.json
  - status: 200
    url: https://github.com/csc
  reason: defunct
  state: none
created: '2025-03-23'
description: Computer Sciences Corporation (CSC) was a multinational information technology services and professional services company. On April 1, 2017, CSC merged with the Enterprise Services line of business of Hewlett Packard Enterprise to form DXC Technology, retiring the standalone CSC brand. This profile is preserved as a historical record; CSC did not publish any public developer APIs and the entity is no longer actively operated under this name.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/computer-sciences.png
layout: provider
modified: '2026-09-05'
name: Computer Sciences Corporation
nav: Providers
network: true
overview: Computer Sciences Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Consulting, Defunct, Enterprise Services, Information Technology, and Outsourcing.
press:
- date: ''
  title: Emerging Artificial Intelligence Applications in Computer ...
  url: https://www.iospress.com/node15242/books/emerging-artificial-intelligence-applications-in-computer-engineering
- date: ''
  title: The Role of Artificial Intelligence in Computer Science ...
  url: https://www.mdpi.com/2076-3417/15/7/3960
- date: ''
  title: UMass Lowell is advancing the future of artificial ...
  url: https://www.instagram.com/p/DXrfx6QGgXJ/
- date: ''
  title: Artificial Intelligence - Khoury College of Computer Sciences
  url: https://www.khoury.northeastern.edu/research_areas/artificial-intelligence/
- date: ''
  title: UW Board of Regents approves UW–Madison proposal to ...
  url: https://news.wisc.edu/uw-board-of-regents-approves-uw-madison-proposal-to-create-college-of-computing-and-artificial-intelligence/
random_paper: 9
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/computer-sciences/refs/heads/main/screenshots/computer-sciences-2026-06-20T174837.png
slug: computer-sciences
tags:
- Consulting
- Defunct
- Enterprise Services
- Information Technology
- Outsourcing
- Fortune 500
---
