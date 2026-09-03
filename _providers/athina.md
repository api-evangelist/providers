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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Athina Agentic Access
  operation_count: 18
  slug: athina-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.athina.ai/api/v1
  baseurl_source: declared
  description: Create and manage datasets used for evals and experiments.
  name: Athina AI Datasets API
  slug: athina-datasets-api
- baseURL: https://api.athina.ai/api/v1
  baseurl_source: declared
  description: Run evaluations against datasets and logged inferences.
  name: Athina AI Evaluations API
  slug: athina-evaluations-api
- baseURL: https://api.athina.ai/api/v1
  baseurl_source: declared
  description: Log LLM inferences and prompt runs.
  name: Athina AI Logging API
  slug: athina-logging-api
- baseURL: https://api.athina.ai/api/v1
  baseurl_source: declared
  description: Create, version, fetch, and run prompt templates.
  name: Athina AI Prompts API
  slug: athina-prompts-api
- baseURL: https://api.athina.ai/api/v1
  baseurl_source: declared
  description: Create and manage traces and spans.
  name: Athina AI Tracing API
  slug: athina-tracing-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Athina AI Datasets API
  slug: open-athina-datasets-api
- collection_type: open
  name: Athina AI Datasets Evaluations API
  slug: open-athina-evaluations-api
- collection_type: open
  name: Athina AI Datasets Logging API
  slug: open-athina-logging-api
- collection_type: open
  name: Athina AI Datasets Prompts API
  slug: open-athina-prompts-api
- collection_type: open
  name: Athina AI Datasets Tracing API
  slug: open-athina-tracing-api
- collection_type: open
  name: Athina AI API
  slug: open-athina
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/athina-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athina-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/athina-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/athina-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/athina-ai
- group: company
  title: ''
  type: Website
  url: https://www.athina.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.athina.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/athina-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/athina-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/athina-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.athina.ai/rss.xml
created: '2026-06-20'
description: Athina AI is an LLM monitoring, evaluation, and experimentation platform for building production-grade AI applications. Its REST API lets teams log inferences and traces, manage datasets, run 50+ preset and custom evaluations, version and run prompt templates, and collaborate on experiments across the full LLM development lifecycle.
finops:
- name: Athina Finops
  service_category: AI and Machine Learning
  slug: athina-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/athina.png
layout: provider
modified: '2026-06-20'
name: Athina AI
nav: Providers
network: true
overview: 'Athina AI publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Evaluations API, Logging API, and 2 more. Tagged areas include Artificial Intelligence, LLM, Observability, Evaluation, and Monitoring.


  Athina AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Athina Plans Pricing
  plan_count: 3
  slug: athina-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Athina Rate Limits
  slug: athina-rate-limits
score:
  band: developing
  composite: 40.8
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
    contract_quality: 57.8
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/athina/refs/heads/main/screenshots/athina-2026-06-20T172520.png
security:
- kind: authentication
  name: Athina Authentication
  slug: athina-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Athina Domain Security
  slug: athina-domain-security
  summary_line: TLSv1.3 · HSTS
slug: athina
tags:
- Artificial Intelligence
- LLM
- Observability
- Evaluation
- Monitoring
website: https://www.athina.ai
---
