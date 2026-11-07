---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Faros Agentic Access
  operation_count: 12
  slug: faros-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Account API from Faros AI — 2 operation(s) for account.
  name: Faros AI Account API
  slug: faros-account-api
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Events API from Faros AI — 1 operation(s) for events.
  name: Faros AI Events API
  slug: faros-events-api
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Graphs API from Faros AI — 2 operation(s) for graphs.
  name: Faros AI Graphs API
  slug: faros-graphs-api
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Ingestion API from Faros AI — 2 operation(s) for ingestion.
  name: Faros AI Ingestion API
  slug: faros-ingestion-api
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Webhooks API from Faros AI — 1 operation(s) for webhooks.
  name: Faros AI Webhooks API
  slug: faros-webhooks-api
- baseURL: https://prod.api.faros.ai
  baseurl_source: declared
  description: The Graph QL API from Faros AI — 1 operation(s) for graph ql.
  name: Faros AI Graph QL API
  slug: faros-graph-ql-api
artifact_total: 22
collections:
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
  href: https://artifacts.apis.io/faros/agentic-access/faros-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/faros-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/faros/security/faros-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/faros-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/faros/security/faros-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/faros-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/faros/authentication/faros-authentication.yml
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
  href: https://artifacts.apis.io/faros/plans/faros-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/faros-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/faros/rate-limits/faros-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/faros-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/faros/finops/faros-finops.yml
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
- has_sources: true
  method: generated
  name: Faros Finops
  primary_unit: ''
  service_category: Developer Tools and Engineering Intelligence
  slug: faros-finops
  template: false
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
overview: 'Faros AI publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Events API, Graphs API, and 3 more. Tagged areas include Engineering Operations, Software Engineering Intelligence, SEI, DORA Metrics, and Developer Productivity.


  The Faros AI catalog on APIs.io includes 1 Spectral governance ruleset.


  Faros AI''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Faros Plans Pricing
  plan_count: 4
  slug: faros-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Faros Rate Limits
  slug: faros-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Faros AI API Rules
  rule_count: 54
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 1
  slug: faros-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 9.0
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 22.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/faros/faros-2026-07-25T214235.png
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
