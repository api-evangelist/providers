---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Faros Agentic Access
  operation_count: 12
  slug: faros-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 6
apis:
- description: The Account API from Faros AI — 2 operation(s) for account.
  name: Faros AI Account API
  slug: faros-account-api
- description: The Events API from Faros AI — 1 operation(s) for events.
  name: Faros AI Events API
  slug: faros-events-api
- description: The GraphQL API from Faros AI — 1 operation(s) for graphql.
  name: Faros AI GraphQL API
  slug: faros-graphql-api
- description: The Graphs API from Faros AI — 2 operation(s) for graphs.
  name: Faros AI Graphs API
  slug: faros-graphs-api
- description: The Ingestion API from Faros AI — 2 operation(s) for ingestion.
  name: Faros AI Ingestion API
  slug: faros-ingestion-api
- description: The Webhooks API from Faros AI — 1 operation(s) for webhooks.
  name: Faros AI Webhooks API
  slug: faros-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Faros AI Account API
  slug: open-faros-account-api
- collection_type: open
  name: Faros AI Account Events API
  slug: open-faros-events-api
- collection_type: open
  name: Faros AI Account GraphQL API
  slug: open-faros-graphql-api
- collection_type: open
  name: Faros AI Account Graphs API
  slug: open-faros-graphs-api
- collection_type: open
  name: Faros AI Account Ingestion API
  slug: open-faros-ingestion-api
- collection_type: open
  name: Faros AI Account Webhooks API
  slug: open-faros-webhooks-api
- collection_type: open
  name: Faros AI API
  slug: open-faros
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/faros-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/faros-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/faros-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/faros-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/faros-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/faros-ai
- group: company
  title: ''
  type: Website
  url: https://www.faros.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.faros.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/faros-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/faros-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/faros-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.faros.ai/blog
created: '2026-06-21'
description: Faros AI is an engineering-operations intelligence platform (software engineering intelligence / SEI) that ingests data from across the SDLC toolchain into a connected canonical model and exposes it for querying. The platform offers a REST API for events and data ingestion at https://prod.api.faros.ai plus a GraphQL query API over the canonical model, with an open-source Faros Community Edition.
finops:
- name: Faros Finops
  service_category: Developer Tools and Engineering Intelligence
  slug: faros-finops
graphqls:
- description: 'Faros AI exposes a native, Hasura-powered GraphQL API over its connected canonical model for the whole software development lifecycle (50+ entities, from tasks to deployments). Any GraphQL client can '
  name: Faros AI GraphQL API
  slug: faros-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/faros.png
layout: provider
modified: '2026-06-21'
name: Faros AI
nav: Providers
network: true
overview: 'Faros AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Account API, Events API, GraphQL API, and 3 more. Tagged areas include Engineering Operations, Software Engineering Intelligence, SEI, DORA Metrics, and Developer Productivity.


  Faros AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Faros Plans Pricing
  plan_count: 4
  slug: faros-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Faros Rate Limits
  slug: faros-rate-limits
score:
  band: thin
  composite: 39.1
  delta: -1.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 56.0
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/faros/refs/heads/main/screenshots/faros-2026-07-25T214235.png
security:
- kind: authentication
  name: Faros Authentication
  slug: faros-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Faros Domain Security
  slug: faros-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Faros Trust Center
  slug: faros-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: faros
tags:
- Engineering Operations
- Software Engineering Intelligence
- SEI
- DORA Metrics
- Developer Productivity
- Data Ingestion
website: https://www.faros.ai
---
