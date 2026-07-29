---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
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
random_paper: 0
score:
  band: emerging
  composite: 13.7
  delta: -0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 14.6
  provenance:
    conformance: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
