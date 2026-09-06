---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.scalyr.com/'', ''status'': 302, ''note'': ''declared website redirects to https://www.sentinelone.com/dataset/ — a different registrable domain (scalyr.com -> sentinelone.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sentinelone/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scalyr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scalyr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.scalyr.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://app.scalyr.com/help/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dataset.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.dataset.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.scalyr.com/login
created: '2026-07-17'
description: Scalyr was a cloud log management, server monitoring, and observability platform for engineering, DevOps, and security teams, known for an index-free, columnar architecture delivering sub-second queries across hundreds of terabytes of structured and unstructured log data. Founded in 2011, Scalyr was acquired by SentinelOne in 2021 and rebranded as DataSet; the scalyr.com domain now redirects to dataset.com. Its REST API (hosted at app.scalyr.com) covered log ingestion (addEvents), querying, and account/file management via API-key authentication. This profile was surfaced as a portfolio company of bloomberg-beta, gv, and susa-ventures and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalyr.png
layout: provider
modified: '2026-07-21'
name: Scalyr
nav: Providers
network: true
overview: 'Scalyr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Log Management, Observability, Monitoring, and Log Analytics.


  Scalyr''s developer surface includes documentation, API reference, pricing, engineering blog, and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalyr/refs/heads/main/screenshots/scalyr-2026-09-02T154511.png
security:
- kind: domain-security
  name: Scalyr Domain Security
  slug: scalyr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scalyr
tags:
- Company
- Log Management
- Observability
- Monitoring
- Log Analytics
- DevOps
- Security
website: https://www.scalyr.com/
---
