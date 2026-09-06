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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Promptlayer Agentic Access
  operation_count: 16
  slug: promptlayer-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.promptlayer.com
  baseurl_source: declared
  description: Create, run, and score evaluation reports against datasets.
  name: PromptLayer Evaluations & Datasets API
  slug: promptlayer-evaluations-datasets-api
- baseURL: https://api.promptlayer.com
  baseurl_source: declared
  description: Log and track LLM requests, scores, and metadata.
  name: PromptLayer Logging & Tracking API
  slug: promptlayer-logging-tracking-api
- baseURL: https://api.promptlayer.com
  baseurl_source: declared
  description: Retrieve and publish versioned prompt templates.
  name: PromptLayer Prompt Registry API
  slug: promptlayer-prompt-registry-api
- baseURL: https://api.promptlayer.com
  baseurl_source: declared
  description: Ingest spans and manage traces for LLM observability.
  name: PromptLayer Spans & Traces API
  slug: promptlayer-spans-traces-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PromptLayer Evaluations & Datasets API
  slug: open-promptlayer-evaluations-datasets-api
- collection_type: open
  name: PromptLayer Evaluations & Datasets Logging & Tracking API
  slug: open-promptlayer-logging-tracking-api
- collection_type: open
  name: PromptLayer Evaluations & Datasets Prompt Registry API
  slug: open-promptlayer-prompt-registry-api
- collection_type: open
  name: PromptLayer Evaluations & Datasets Spans & Traces API
  slug: open-promptlayer-spans-traces-api
- collection_type: open
  name: PromptLayer API
  slug: open-promptlayer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/promptlayer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/promptlayer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/promptlayer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MagnivOrg
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/promptlayer
- group: company
  title: ''
  type: Website
  url: https://www.promptlayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.promptlayer.com
- group: commercial
  title: ''
  type: Plans
  url: plans/promptlayer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/promptlayer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/promptlayer-finops.yml
created: '2026-06-20'
description: PromptLayer is a prompt engineering, prompt management, and LLM observability platform. Its REST API logs and tracks LLM requests, manages a versioned prompt registry with release labels, ingests OpenTelemetry-style spans and traces, and runs evaluations and datasets so teams can monitor, debug, and improve their LLM applications.
finops:
- name: Promptlayer Finops
  service_category: AI and Machine Learning
  slug: promptlayer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/promptlayer.png
layout: provider
modified: '2026-06-20'
name: PromptLayer
nav: Providers
network: true
overview: 'PromptLayer publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Evaluations & Datasets API, Logging & Tracking API, Prompt Registry API, and 1 more. Tagged areas include Artificial Intelligence, LLM, Prompt Engineering, Prompt Management, and Observability.


  PromptLayer''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Promptlayer Plans Pricing
  plan_count: 4
  slug: promptlayer-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Promptlayer Rate Limits
  slug: promptlayer-rate-limits
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
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 29.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/promptlayer/refs/heads/main/screenshots/promptlayer-2026-06-20T192157.png
security:
- kind: authentication
  name: Promptlayer Authentication
  slug: promptlayer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Promptlayer Domain Security
  slug: promptlayer-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: promptlayer
tags:
- Artificial Intelligence
- LLM
- Prompt Engineering
- Prompt Management
- Observability
- Evaluation
website: https://www.promptlayer.com
---
