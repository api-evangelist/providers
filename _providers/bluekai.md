---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.bluekai.com/'', ''status'': 301, ''note'': ''declared website redirects to http://www.oracle.com:80/us/corporate/acquisitions/bluekai/index.html — a different registrable domain (bluekai.com -> oracle.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/bluekai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.bluekai.com/
created: '2026-07-17'
description: BlueKai was a data management platform (DMP) and third-party audience data marketplace founded in 2008 that let marketers collect, organize, and activate first- and third-party audience data for programmatic advertising and targeting. Oracle acquired BlueKai in 2014 and folded it into the Oracle Data Cloud; Oracle wound down its advertising business (including the former BlueKai and Data Cloud assets) in 2024. The company operates no independent developer program today — the bluekai.com domain 301-redirects to Oracle's advertising pages and exposes no live public API surface. This profile is retained as a historical/defunct provider record in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bluekai.png
layout: provider
modified: '2026-07-18'
name: BlueKai
nav: Providers
network: true
overview: BlueKai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Management Platform, DMP, Audience Data, and AdTech.
random_paper: 19
score:
  band: minimal
  composite: 5.0
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bluekai/refs/heads/main/screenshots/bluekai-2026-07-25T203457.png
security:
- kind: domain-security
  name: Bluekai Domain Security
  slug: bluekai-domain-security
  summary_line: DMARC
slug: bluekai
tags:
- Company
- Data Management Platform
- DMP
- Audience Data
- AdTech
- Marketing
- Defunct
- Acquired
website: http://www.bluekai.com/
---
