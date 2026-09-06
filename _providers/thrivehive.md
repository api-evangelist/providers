---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://thrivehive.com/'', ''status'': 301, ''note'': ''declared website redirects to https://localiq.com/ — a different registrable domain (thrivehive.com -> localiq.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/thrivehive-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thrivehive-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/thrivehive-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrivehive-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thrivehive
- group: company
  title: ''
  type: Website
  url: https://thrivehive.com/
created: '2026-07-17'
description: ThriveHive was a Boston-based guided marketing platform for small businesses (10 or fewer employees), founded in 2011 by Max Faingezicht and Adam Blake and part of the Techstars Boston 2015 class. It was acquired by Propel Marketing (GateHouse Media) in 2016 for $11.8M and the brand was folded into Gannett's LocaliQ after the 2019 GateHouse-Gannett merger. The company published no public API or developer portal; thrivehive.com now serves LocaliQ content behind an expired TLS certificate.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thrivehive.png
layout: provider
modified: '2026-07-21'
name: ThriveHive
nav: Providers
network: true
overview: ThriveHive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Small Business, Advertising, and Software-as-a-Service.
random_paper: 15
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 5
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thrivehive/refs/heads/main/screenshots/thrivehive-2026-09-02T163643.png
security:
- kind: domain-security
  name: Thrivehive Domain Security
  slug: thrivehive-domain-security
  summary_line: DMARC
slug: thrivehive
tags:
- Company
- Marketing
- Small Business
- Advertising
- Software-as-a-Service
- Acquired
website: https://thrivehive.com/
---
