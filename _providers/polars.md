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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polars-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pola.rs/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pola.rs/user-guide/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pola.rs/api/python/stable/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pola.rs/user-guide/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://pola.rs/posts/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pola-rs
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/4UfP5cfBE7
- group: build
  title: ''
  type: Packages
  url: packages/polars-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/polars-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/polars-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polars-llms.txt
created: '2026-07-17'
description: Polars is a blazingly fast, open-source DataFrame library and query engine written in Rust, with first-party bindings for Python, Rust, Node.js, and R. It provides lazy and eager execution, streaming for larger-than-memory datasets, automatic query optimization, multi-threading, and the Apache Arrow columnar memory format. Polars Cloud extends the same DataFrame API to managed and on-premise distributed compute with zero code changes. The project is developed by pola-rs and backed by Accel and Bain Capital Ventures.
image: https://raw.githubusercontent.com/api-evangelist/polars/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-20'
name: Polars
nav: Providers
network: true
overview: 'Polars is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DataFrames, Data Processing, Query Engine, and Rust.


  Polars'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, and 6 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 6
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
    developer_ergonomics: 42.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 16.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polars/refs/heads/main/screenshots/polars-2026-09-02T151644.png
security:
- kind: domain-security
  name: Polars Domain Security
  slug: polars-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: polars
tags:
- Company
- DataFrames
- Data Processing
- Query Engine
- Rust
- Python
- Analytics
- Open-Source
website: https://pola.rs/
---
