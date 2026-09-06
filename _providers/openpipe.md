---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Openpipe Agentic Access
  operation_count: 23
  slug: openpipe-agentic-access
  summary_line: 23 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Chat API from OpenPipe — 1 operation(s) for chat.
  name: OpenPipe Chat API
  slug: openpipe-chat-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Check Cache API from OpenPipe — 1 operation(s) for check cache.
  name: OpenPipe Check Cache API
  slug: openpipe-check-cache-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Criteria API from OpenPipe — 1 operation(s) for criteria.
  name: OpenPipe Criteria API
  slug: openpipe-criteria-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Datasets API from OpenPipe — 3 operation(s) for datasets.
  name: OpenPipe Datasets API
  slug: openpipe-datasets-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Local Testing Only Get Latest Logged Call API from OpenPipe — 1 operation(s) for local testing only get latest logged call.
  name: OpenPipe Local Testing Only Get Latest Logged Call API
  slug: openpipe-local-testing-only-get-latest-logged-call-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Logs API from OpenPipe — 2 operation(s) for logs.
  name: OpenPipe Logs API
  slug: openpipe-logs-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Models API from OpenPipe — 2 operation(s) for models.
  name: OpenPipe Models API
  slug: openpipe-models-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Report Anthropic API from OpenPipe — 1 operation(s) for report anthropic.
  name: OpenPipe Report Anthropic API
  slug: openpipe-report-anthropic-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Report API from OpenPipe — 1 operation(s) for report.
  name: OpenPipe Report API
  slug: openpipe-report-api
- baseURL: https://api.openpipe.ai/api/v1
  baseurl_source: declared
  description: The Unstable API from OpenPipe — 7 operation(s) for unstable.
  name: OpenPipe Unstable API
  slug: openpipe-unstable-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenPipe Chat API
  slug: open-openpipe-chat-api
- collection_type: open
  name: OpenPipe Chat Check Cache API
  slug: open-openpipe-check-cache-api
- collection_type: open
  name: OpenPipe Chat Criteria API
  slug: open-openpipe-criteria-api
- collection_type: open
  name: OpenPipe Chat Datasets API
  slug: open-openpipe-datasets-api
- collection_type: open
  name: OpenPipe Chat Local Testing Only Get Latest Logged Call API
  slug: open-openpipe-local-testing-only-get-latest-logged-call-api
- collection_type: open
  name: OpenPipe Chat Logs API
  slug: open-openpipe-logs-api
- collection_type: open
  name: OpenPipe Chat Models API
  slug: open-openpipe-models-api
- collection_type: open
  name: OpenPipe Chat Report Anthropic API
  slug: open-openpipe-report-anthropic-api
- collection_type: open
  name: OpenPipe Chat Report API
  slug: open-openpipe-report-api
- collection_type: open
  name: OpenPipe Chat Unstable API
  slug: open-openpipe-unstable-api
- collection_type: open
  name: OpenPipe API
  slug: open-openpipe
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openpipe-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openpipe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openpipe-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenPipe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openpipe
- group: company
  title: ''
  type: Website
  url: https://openpipe.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openpipe.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/openpipe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openpipe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openpipe-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.openpipe.ai/llms.txt
created: '2026-05-08'
description: OpenPipe is a fine-tuning and inference platform for distilling expensive frontier-LLM workloads into smaller, cheaper specialized models. Captures production traces (OpenAI and Anthropic), fine-tunes, evaluates with judges, caches results, and serves the result via OpenAI-compatible API. Also supports proxying to external models.
finops:
- name: Openpipe Finops
  service_category: AI
  slug: openpipe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openpipe.png
layout: provider
modified: '2026-05-19'
name: OpenPipe
nav: Providers
network: true
overview: 'OpenPipe publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Check Cache API, Criteria API, and 7 more. Tagged areas include Artificial Intelligence, LLM, Fine-Tuning, Distillation, and Inference.


  OpenPipe''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Openpipe Plans Pricing
  plan_count: 1
  slug: openpipe-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Openpipe Rate Limits
  slug: openpipe-rate-limits
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 21.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openpipe/refs/heads/main/screenshots/openpipe-2026-06-20T191022.png
security:
- kind: authentication
  name: Openpipe Authentication
  slug: openpipe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openpipe Domain Security
  slug: openpipe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openpipe
tags:
- Artificial Intelligence
- LLM
- Fine-Tuning
- Distillation
- Inference
- OpenAI-Compatible
- Anthropic Compatible
- Caching
website: https://openpipe.ai/
---
