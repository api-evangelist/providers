---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: Open-source Python framework (superduper-framework) for declaring AI models, embeddings, vector indexes, RAG pipelines, and listeners directly on top of an existing database. Apache 2.0 licensed.
  name: Superduper Framework
  slug: framework
- description: Database backend plugin (superduper-mongodb) that turns a MongoDB cluster into a Superduper-managed AI datastore with vector search and model listeners.
  name: Superduper MongoDB Plugin
  slug: mongodb-plugin
- description: Database backend plugin (superduper-sql) for SQL databases - PostgreSQL, MySQL, SQLite, DuckDB, and other SQLAlchemy-supported engines.
  name: Superduper SQL Plugin
  slug: sql-plugin
- description: Database backend plugin (superduper-snowflake) that runs Superduper against a Snowflake account, including the Snowflake Marketplace distribution path for Superduper Agents.
  name: Superduper Snowflake Plugin
  slug: snowflake-plugin
- description: Database backend plugin (superduper-redis) for Redis-backed Superduper deployments.
  name: Superduper Redis Plugin
  slug: redis-plugin
- description: Commercial enterprise AI agent orchestration product for BI and data operations. Connects to 40+ databases, data warehouses, and business tools - PostgreSQL, MongoDB, Snowflake, Salesforce, Slack, Hub
  name: Superduper Agents
  slug: agents
artifact_total: 10
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/superduper-io/superduper/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superduperdb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superduper.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.superduper.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/superduper-io
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/superduper-public/shared_invite/zt-1yodhtx8y-KxzECued5QBtT6JFnsSNrQ
created: '2026-05-23'
description: Superduper (formerly SuperDuperDB) is an open-source Python framework for building database-integrated AI agents and applications directly on top of existing databases - MongoDB, SQL databases, Snowflake, and Redis - without separate vector stores or ETL. It supports semantic / vector search, RAG, transformer and PyTorch model integration, LLM serving, and distributed ML workflows. The commercial side, Superduper Agents, is an enterprise AI agent orchestration platform for BI and data operations, distributed via the Snowflake Marketplace and self-hosted enterprise installs.
finops:
- name: Superduperdb Finops
  service_category: API
  slug: superduperdb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/superduperdb.png
layout: provider
modified: '2026-05-23'
name: Superduper
nav: Providers
network: true
overview: 'Superduper publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Framework, Vector Search, RAG, LLMs, and MLOps.


  Superduper''s developer surface includes documentation, GitHub presence, and 4 more developer resources.'
plans:
- name: Superduperdb Plans Pricing
  plan_count: 1
  slug: superduperdb-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 2
  name: Superduperdb Rate Limits
  slug: superduperdb-rate-limits
score:
  band: emerging
  composite: 19.2
  delta: 0.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/superduperdb/refs/heads/main/screenshots/superduperdb-2026-06-20T194712.png
security:
- kind: domain-security
  name: Superduperdb Domain Security
  slug: superduperdb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superduperdb
tags:
- AI Framework
- Vector Search
- RAG
- LLMs
- MLOps
- Open Source
- AI Agents
website: https://superduper.io/
---
