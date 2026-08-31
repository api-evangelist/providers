---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.9
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://github.com/pgvector/pgvector
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/pgvector/pgvector
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pgvector
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/pgvector/pgvector#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/pgvector/pgvector#reference
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/pgvector/pgvector#getting-started
- group: operate
  title: ''
  type: Support
  url: https://github.com/pgvector/pgvector/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/pgvector/pgvector/blob/master/CHANGELOG.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/pgvector/pgvector/blob/master/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/pgvector-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pgvector-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pgvector-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pgvector-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pgvector-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pgvector-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pgvector-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pgvector-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pgvector-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pgvector-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-27'
description: 'pgvector is an open-source PostgreSQL extension for vector similarity search, created and maintained by Andrew Kane. It adds vector, halfvec and sparsevec data types, six distance operators (L2, inner product, cosine, L1, Hamming, Jaccard) and two approximate-nearest-neighbour index access methods (HNSW and IVFFlat) to a Postgres server, so embeddings live beside the rest of an application''s data with full ACID semantics, JOINs, point-in-time recovery and existing backup and replication tooling. It is not a service and exposes no HTTP API: the interface is SQL, the contract is the extension''s own installation DDL, and consumers reach it through an ordinary Postgres driver. The project also publishes first-party client libraries for seventeen languages, which handle vector encoding for each language''s Postgres driver.'
image: https://avatars.githubusercontent.com/u/98363230?v=4
layout: provider
modified: '2026-08-27'
name: pgvector
nav: Providers
network: true
overview: 'pgvector is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Vector Databases, Databases, Open-Source, and PostgreSQL.


  pgvector''s developer surface includes documentation, API reference, getting-started guide, support, changelog, and 15 more developer resources.'
plans:
- name: Pgvector Plans Pricing
  plan_count: 0
  slug: pgvector-plans-pricing
random_paper: 13
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 12
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 19.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: pgvector
tags:
- Artificial Intelligence
- Vector Databases
- Databases
- Open-Source
- PostgreSQL
- Search
- Embeddings
- Extensions
- Company
---
