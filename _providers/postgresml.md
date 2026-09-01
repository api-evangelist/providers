---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://postgresml.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://postgresml.org/docs
- group: docs
  title: ''
  type: Documentation
  url: https://postgresml.org/docs
- group: company
  title: ''
  type: Blog
  url: https://postgresml.org/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://postgresml.org/pricing
- group: start
  title: ''
  type: SignUp
  url: https://postgresml.org/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postgresml.org/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postgresml.org/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/DmyJP3qJ7U
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postgresml
- group: build
  title: ''
  type: Packages
  url: packages/postgresml-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/postgresml-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postgresml-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/postgresml-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postgresml-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/postgresml-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/postgresml-llms.txt
created: '2026-07-17'
description: PostgresML brings machine learning and AI into PostgreSQL. Using the open-source pgml extension it runs embedding generation, LLM inference, vector search, and classic supervised learning (regression, classification, clustering) directly inside the database, so applications index, filter, and rank vectors and generate fact-based, real-time outputs without operating a separate ML or vector stack. It is consumed as SQL over the Postgres wire protocol and through the first-party Korvus SDK (Python, JavaScript, Rust, and C bindings), which unifies the entire RAG pipeline into a single database query. PostgresML Cloud offers managed serverless and dedicated Postgres databases with the extensions pre-installed, and PgCat provides connection pooling, sharding, and failover. There is no REST/HTTP API; authentication is a standard PostgreSQL connection string. Backed by Amplify Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postgresml.png
layout: provider
modified: '2026-07-20'
name: PostgresML
nav: Providers
network: true
overview: 'PostgresML is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Ml, Machine-Learning, Vector Search, and Embeddings.


  PostgresML''s developer surface includes documentation, engineering blog, pricing, signup flow, support, authentication, and 11 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 24.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Postgresml Authentication
  slug: postgresml-authentication
  summary_line: connection-string · 1 scheme
- kind: domain-security
  name: Postgresml Domain Security
  slug: postgresml-domain-security
  summary_line: TLSv1.3
slug: postgresml
tags:
- Company
- Ai Ml
- Machine-Learning
- Vector Search
- Embeddings
- PostgreSQL
- RAG
- LLM
- Database
website: https://postgresml.org
---
