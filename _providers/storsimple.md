---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''http://www.storsimple.com/'', ''status'': 301, ''note'': ''declared website redirects to https://learn.microsoft.com/en-us/previous-versions/azure/storage/files/storage-files-migration-storsimple-8000 — a different registrable domain (storsimple.com -> microsoft.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Azure Resource Manager REST API for managing StorSimple device managers, devices, volumes, backup policies, and jobs under the Microsoft.StorSimple resource provider. Retired (end-of-life December 202
  name: Azure StorSimple Management REST API
  slug: azure-storsimple-management-rest-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storsimple-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/storsimple-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/storsimple-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storsimple-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/storsimple-lifecycle.yml
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/storsimple/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/storsimple/
- group: company
  title: ''
  type: Website
  url: http://www.storsimple.com/
created: '2026-07-17'
description: StorSimple was a Santa Clara, California hybrid cloud storage company founded in 2009 by Ursheet Parikh and Guru Pangal. Its appliances combined primary storage, tiered cloud archiving, deduplication, compression, and encryption behind iSCSI/SMB interfaces, backed by $31.5M from Index Ventures, Redpoint Ventures, Ignition Partners, and Mayfield Fund. Microsoft acquired StorSimple in November 2012 and folded it into Azure as Azure StorSimple (8000 series physical and virtual arrays, plus the StorSimple Data Manager). The product is managed through Azure Resource Manager under the Microsoft.StorSimple resource provider and its REST API. Azure StorSimple reached end-of-life in December 2022 and is out of support; Microsoft directs customers to Azure File Sync and Azure Files.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/storsimple.png
layout: provider
modified: '2026-07-21'
name: StorSimple
nav: Providers
network: true
overview: 'StorSimple publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Storage, Cloud Storage, Hybrid Cloud, and Data Management.


  StorSimple''s developer surface includes documentation, API reference, and 6 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 15.8
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storsimple/refs/heads/main/screenshots/storsimple-2026-09-02T160936.png
security:
- kind: authentication
  name: Storsimple Authentication
  slug: storsimple-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Storsimple Domain Security
  slug: storsimple-domain-security
  summary_line: DMARC
slug: storsimple
tags:
- Company
- Storage
- Cloud Storage
- Hybrid Cloud
- Data Management
- Enterprise Storage
- Azure
- Acquired
website: http://www.storsimple.com/
---
