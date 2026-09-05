---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://transform.co/'', ''status'': 308, ''note'': ''declared website redirects to https://www.getdbt.com/ — a different registrable domain (transform.co -> getdbt.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/transform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transform.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transform-data
- group: build
  title: ''
  type: Packages
  url: packages/transform-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/transform-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transform-llms.txt
created: '2026-07-17'
description: Transform (Transform Data) was a metrics-store and semantic-layer company backed by Redpoint Ventures that offered a metrics framework, a metrics catalog, and the MQL (Metrics Query Language) API, and open-sourced the MetricFlow metrics framework. Transform was acquired by dbt Labs (announced February 2023), and its technology lives on as MetricFlow and the dbt Semantic Layer. transform.co now returns a 308 Permanent Redirect to getdbt.com on every path, and the company no longer operates an independent API or developer surface — see the dbt provider profile in this network for the successor APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transform.png
layout: provider
modified: '2026-07-21'
name: Transform
nav: Providers
network: true
overview: Transform is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Metrics, Semantic Layer, Analytics, and Data.
random_paper: 1
score:
  band: minimal
  composite: 7.5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transform/refs/heads/main/screenshots/transform-2026-09-02T164126.png
security:
- kind: domain-security
  name: Transform Domain Security
  slug: transform-domain-security
  summary_line: TLSv1.3 · HSTS
slug: transform
tags:
- Company
- Metrics
- Semantic Layer
- Analytics
- Data
- Business Intelligence
- Acquired
website: https://transform.co/
---
