---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.okera.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.databricks.com/ — a different registrable domain (okera.com -> databricks.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/okera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.okera.com/
created: '2026-07-17'
description: 'Okera was a data access governance and data security platform providing fine-grained, attribute-based access control, data discovery and classification, dynamic masking, and audit for analytics and machine-learning workloads across data lakes and warehouses. Founded around 2016, Okera was acquired by Databricks in May 2023 and folded into the Databricks governance stack (Unity Catalog). Okera no longer operates as an independent product: the okera.com domain now 301-redirects to databricks.com, and there is no standalone Okera developer portal, documentation, or public API surface remaining. This profile is retained in the API Evangelist network as an acquired-company record.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/okera.png
layout: provider
modified: '2026-07-20'
name: Okera
nav: Providers
network: true
overview: Okera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developers, Data Governance, Data Security, and Access Control.
random_paper: 5
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
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/okera/refs/heads/main/screenshots/okera-2026-08-07T190047.png
security:
- kind: domain-security
  name: Okera Domain Security
  slug: okera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: okera
tags:
- Company
- Developers
- Data Governance
- Data Security
- Access Control
- Data Access
- Acquired
- Databricks
website: https://www.okera.com/
---
