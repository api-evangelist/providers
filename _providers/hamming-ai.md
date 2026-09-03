---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 11
  human_in_the_loop: 0
  name: Hamming Ai Agentic Access
  operation_count: 16
  slug: hamming-ai-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 1
apis:
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: Manage datasets of test cases and scenarios.
  name: Hamming AI Datasets API
  slug: hamming-ai-datasets-api
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: Create and run experiments and experiment items.
  name: Hamming AI Experiments API
  slug: hamming-ai-experiments-api
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: Ingest traces, logs, and production call logs.
  name: Hamming AI Monitoring API
  slug: hamming-ai-monitoring-api
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: List and fetch versioned prompts from the registry.
  name: Hamming AI Prompts API
  slug: hamming-ai-prompts-api
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: Register custom scoring functions.
  name: Hamming AI Scoring API
  slug: hamming-ai-scoring-api
- baseURL: https://app.hamming.ai/api/rest
  baseurl_source: declared
  description: Run voice agents against datasets and retrieve experiment calls.
  name: Hamming AI Voice Testing API
  slug: hamming-ai-voice-testing-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hamming AI REST Datasets API
  slug: open-hamming-ai-datasets-api
- collection_type: open
  name: Hamming AI REST Datasets Experiments API
  slug: open-hamming-ai-experiments-api
- collection_type: open
  name: Hamming AI REST Datasets Monitoring API
  slug: open-hamming-ai-monitoring-api
- collection_type: open
  name: Hamming AI REST Datasets Prompts API
  slug: open-hamming-ai-prompts-api
- collection_type: open
  name: Hamming AI REST Datasets Scoring API
  slug: open-hamming-ai-scoring-api
- collection_type: open
  name: Hamming AI REST Datasets Voice Testing API
  slug: open-hamming-ai-voice-testing-api
- collection_type: open
  name: Hamming AI REST API
  slug: open-hamming-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hamming-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hamming-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hamming-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HammingHQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hammingai
- group: company
  title: ''
  type: Website
  url: https://hamming.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hamming.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/hamming-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hamming-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hamming-ai-finops.yml
created: '2026-06-21'
description: Hamming AI is a testing, evaluation, and observability platform for voice and LLM AI agents. Its REST API runs experiments and voice/call test runs against your agents, manages datasets, registers custom scorers and evaluations, and ingests traces, logs, and production call logs for monitoring. A prompt optimizer and registry round out the platform.
finops:
- name: Hamming Ai Finops
  service_category: AI and Machine Learning
  slug: hamming-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hamming-ai.png
layout: provider
modified: '2026-06-21'
name: Hamming AI
nav: Providers
network: true
overview: 'Hamming AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Datasets API, Experiments API, Monitoring API, and 3 more. Tagged areas include Artificial Intelligence, Voice Agents, LLM, Testing, and Evaluation.


  Hamming AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Hamming Ai Plans Pricing
  plan_count: 2
  slug: hamming-ai-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Hamming Ai Rate Limits
  slug: hamming-ai-rate-limits
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 34.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hamming-ai/refs/heads/main/screenshots/hamming-ai-2026-07-25T220600.png
security:
- kind: authentication
  name: Hamming Ai Authentication
  slug: hamming-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hamming Ai Domain Security
  slug: hamming-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hamming-ai
tags:
- Artificial Intelligence
- Voice Agents
- LLM
- Testing
- Evaluation
- Observability
website: https://hamming.ai/
---
