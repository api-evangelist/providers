---
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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nisshi/refs/heads/main/hosts/nisshi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nisshi-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nisshi/refs/heads/main/packages/nisshi-packages.yml
  title: ''
  type: SDKs
  url: packages/nisshi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/nisshi/refs/heads/main/packages/nisshi-packages.yml
  title: ''
  type: Packages
  url: packages/nisshi-packages.yml
- group: company
  title: ''
  type: Website
  url: https://nisshi.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nisshi.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nisshi-io
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/nisshi-io/nisshi
coverage:
  checked: '2026-10-13'
  detail: Tansu is a Kafka-wire-protocol broker with no published HTTP contract, its tansu.io site no longer resolves in DNS, and the repo now redirects to the renamed Nisshi project (github.com/nisshi-io/nisshi).
  evidence:
  - status: 0
    url: https://tansu.io
  - status: 200
    url: https://github.com/tansu-io/tansu
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-13'
description: 'Nisshi (formerly Tansu) is an open-source (Apache-2.0), Rust-built, Apache Kafka compatible message broker that stores data in S3, PostgreSQL, SQLite/libSQL or memory and can write schema-validated topics (JSON Schema, Avro, Protocol Buffers) as Apache Iceberg or Delta Lake tables. Its surface is the Kafka wire protocol rather than an HTTP API, and no OpenAPI, AsyncAPI or GraphQL contract is published. The project has been renamed Nisshi (README: ''Nisshi (nee Tansu)''); github.com/tansu-io/tansu redirects to github.com/nisshi-io/nisshi and tansu.io no longer resolves in DNS.'
layout: provider
modified: '2026-10-14'
name: Nisshi
nav: Providers
network: true
overview: 'Nisshi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Kafka, Message Broker, Streaming, and Open Source.


  Nisshi''s developer surface includes documentation and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: nisshi
tags:
- Company
- Kafka
- Message Broker
- Streaming
- Open Source
- Apache Iceberg
- Delta Lake
- Rust
website: https://nisshi.io
---
