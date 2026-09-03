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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Literalai Agentic Access
  operation_count: 1
  slug: literalai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://cloud.getliteral.ai/api/graphql
  baseurl_source: declared
  description: The GraphQL API from Literal AI — 1 operation(s) for graphql.
  name: Literal AI GraphQL API
  slug: literalai-graphql-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Literal AI GraphQL API
  slug: open-literalai-graphql-api
- collection_type: open
  name: Literal AI API
  slug: open-literalai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/literalai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/literalai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/literalai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Chainlit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chainlit
- group: company
  title: ''
  type: Website
  url: https://www.literalai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.literalai.com
- group: commercial
  title: ''
  type: Plans
  url: plans/literalai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/literalai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/literalai-finops.yml
created: '2026-06-20'
description: Literal AI is the collaborative observability, evaluation, and analytics platform for building production-grade LLM applications, from the Chainlit team. Its API is GraphQL (POST /api/graphql) consumed through Python and TypeScript SDKs, capturing threads, steps, generations, datasets, experiments, prompts, and scores, with an additional OpenTelemetry (OTLP) ingestion path for traces.
finops:
- name: Literalai Finops
  service_category: AI and Machine Learning
  slug: literalai-finops
graphqls:
- description: Representative GraphQL schema for the [Literal AI](https://www.literalai.com/) LLM
  name: Literal AI GraphQL API
  slug: literalai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/literalai.png
layout: provider
modified: '2026-06-20'
name: Literal AI
nav: Providers
network: true
overview: 'Literal AI publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Artificial Intelligence, LLM, Observability, Evaluation, and Monitoring.


  Literal AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Literalai Plans Pricing
  plan_count: 3
  slug: literalai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Literalai Rate Limits
  slug: literalai-rate-limits
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 60.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/literalai/refs/heads/main/screenshots/literalai-2026-06-20T184606.png
security:
- kind: authentication
  name: Literalai Authentication
  slug: literalai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Literalai Domain Security
  slug: literalai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: literalai
tags:
- Artificial Intelligence
- LLM
- Observability
- Evaluation
- Monitoring
website: https://www.literalai.com
---
