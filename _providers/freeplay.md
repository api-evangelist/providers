---
access_model:
  confidence: medium
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Freeplay Agentic Access
  operation_count: 29
  slug: freeplay-agentic-access
  summary_line: 29 operations · 18 acting
api_count: 1
apis:
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: List agents within a project.
  name: Freeplay Agents API
  slug: freeplay-agents-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Record completions and aggregate completion statistics.
  name: Freeplay Completions API
  slug: freeplay-completions-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Curate datasets and their test cases.
  name: Freeplay Datasets API
  slug: freeplay-datasets-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Record completion-level and trace-level feedback.
  name: Freeplay Feedback API
  slug: freeplay-feedback-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: List workspace projects.
  name: Freeplay Projects API
  slug: freeplay-projects-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Create, version, retrieve, and deploy prompt templates.
  name: Freeplay Prompt Templates API
  slug: freeplay-prompt-templates-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: API-only search over sessions, traces, and completions.
  name: Freeplay Search API
  slug: freeplay-search-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: List, search, and delete sessions.
  name: Freeplay Sessions API
  slug: freeplay-sessions-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Create, list, and retrieve batch test runs.
  name: Freeplay Test Runs API
  slug: freeplay-test-runs-api
- baseURL: https://app.freeplay.ai/api/v2
  baseurl_source: declared
  description: Record traces that group related completions.
  name: Freeplay Traces API
  slug: freeplay-traces-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Freeplay HTTP Agents API
  slug: open-freeplay-agents-api
- collection_type: open
  name: Freeplay HTTP Agents Completions API
  slug: open-freeplay-completions-api
- collection_type: open
  name: Freeplay HTTP Agents Datasets API
  slug: open-freeplay-datasets-api
- collection_type: open
  name: Freeplay HTTP Agents Feedback API
  slug: open-freeplay-feedback-api
- collection_type: open
  name: Freeplay HTTP Agents Projects API
  slug: open-freeplay-projects-api
- collection_type: open
  name: Freeplay HTTP Agents Prompt Templates API
  slug: open-freeplay-prompt-templates-api
- collection_type: open
  name: Freeplay HTTP Agents Search API
  slug: open-freeplay-search-api
- collection_type: open
  name: Freeplay HTTP Agents Sessions API
  slug: open-freeplay-sessions-api
- collection_type: open
  name: Freeplay HTTP Agents Test Runs API
  slug: open-freeplay-test-runs-api
- collection_type: open
  name: Freeplay HTTP Agents Traces API
  slug: open-freeplay-traces-api
- collection_type: open
  name: Freeplay HTTP API
  slug: open-freeplay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freeplay-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freeplay-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freeplay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freeplay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freeplayai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freeplay-ai
- group: company
  title: ''
  type: Website
  url: https://freeplay.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freeplay.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/freeplay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freeplay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/freeplay-finops.yml
created: '2026-06-20'
description: Freeplay is an LLM product experimentation, evaluation, and observability platform for cross-functional teams. Its HTTP API and SDKs make Freeplay the source of truth for prompt templates, record completions and sessions/traces from production, curate test datasets, run batch test runs and LLM-judge evaluations, and capture human and customer feedback.
finops:
- name: Freeplay Finops
  service_category: AI and Machine Learning
  slug: freeplay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freeplay.png
layout: provider
modified: '2026-06-20'
name: Freeplay
nav: Providers
network: true
overview: 'Freeplay publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Completions API, Datasets API, and 7 more. Tagged areas include Artificial Intelligence, LLM, Evaluation, Observability, and Prompt Management.


  Freeplay''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Freeplay Plans Pricing
  plan_count: 3
  slug: freeplay-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 3
  name: Freeplay Rate Limits
  slug: freeplay-rate-limits
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 49.6
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freeplay/refs/heads/main/screenshots/freeplay-2026-06-20T181534.png
security:
- kind: authentication
  name: Freeplay Authentication
  slug: freeplay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Freeplay Domain Security
  slug: freeplay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Freeplay Trust Center
  slug: freeplay-trust-center
  summary_line: SOC 2, ISO 27001
slug: freeplay
tags:
- Artificial Intelligence
- LLM
- Evaluation
- Observability
- Prompt Management
- Experimentation
website: https://freeplay.ai/
---
