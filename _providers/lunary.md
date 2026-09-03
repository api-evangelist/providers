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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Lunary Agentic Access
  operation_count: 82
  slug: lunary-agentic-access
  summary_line: 82 operations · 50 acting
api_count: 1
apis:
- description: 'REST API for Lunary covering ingestion (logs/traces), prompts (template management with versions and labels), datasets, evaluations, projects, users, and analytics. Authentication uses Bearer tokens; '
  name: Lunary API
  slug: platform
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Analytics API from Lunary — 1 operation(s) for analytics.
  name: Lunary Analytics API
  slug: lunary-analytics-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The AuditLogs API from Lunary — 1 operation(s) for auditlogs.
  name: Lunary AuditLogs API
  slug: lunary-auditlogs-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Checklists API from Lunary — 2 operation(s) for checklists.
  name: Lunary Checklists API
  slug: lunary-checklists-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Datasets API from Lunary — 3 operation(s) for datasets.
  name: Lunary Datasets API
  slug: lunary-datasets-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The DatasetsV2 API from Lunary — 13 operation(s) for datasetsv2.
  name: Lunary DatasetsV2 API
  slug: lunary-datasetsv2-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Evals API from Lunary — 7 operation(s) for evals.
  name: Lunary Evals API
  slug: lunary-evals-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The ExternalUsers API from Lunary — 2 operation(s) for externalusers.
  name: Lunary ExternalUsers API
  slug: lunary-externalusers-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Models API from Lunary — 2 operation(s) for models.
  name: Lunary Models API
  slug: lunary-models-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Playground API from Lunary — 2 operation(s) for playground.
  name: Lunary Playground API
  slug: lunary-playground-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Runs API from Lunary — 10 operation(s) for runs.
  name: Lunary Runs API
  slug: lunary-runs-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Templates API from Lunary — 5 operation(s) for templates.
  name: Lunary Templates API
  slug: lunary-templates-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The TestEndpoint API from Lunary — 2 operation(s) for testendpoint.
  name: Lunary TestEndpoint API
  slug: lunary-testendpoint-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Views API from Lunary — 2 operation(s) for views.
  name: Lunary Views API
  slug: lunary-views-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Lunary Analytics API
  slug: open-lunary-analytics-api
- collection_type: open
  name: Lunary Analytics AuditLogs API
  slug: open-lunary-auditlogs-api
- collection_type: open
  name: Lunary Analytics Checklists API
  slug: open-lunary-checklists-api
- collection_type: open
  name: Lunary Analytics Datasets API
  slug: open-lunary-datasets-api
- collection_type: open
  name: Lunary Analytics DatasetsV2 API
  slug: open-lunary-datasetsv2-api
- collection_type: open
  name: Lunary Analytics Evals API
  slug: open-lunary-evals-api
- collection_type: open
  name: Lunary Analytics ExternalUsers API
  slug: open-lunary-externalusers-api
- collection_type: open
  name: Lunary Analytics Models API
  slug: open-lunary-models-api
- collection_type: open
  name: Lunary Analytics Playground API
  slug: open-lunary-playground-api
- collection_type: open
  name: Lunary Analytics Runs API
  slug: open-lunary-runs-api
- collection_type: open
  name: Lunary Analytics Templates API
  slug: open-lunary-templates-api
- collection_type: open
  name: Lunary Analytics TestEndpoint API
  slug: open-lunary-testendpoint-api
- collection_type: open
  name: Lunary Analytics Views API
  slug: open-lunary-views-api
- collection_type: open
  name: Lunary API
  slug: open-lunary
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lunary-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lunary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lunary-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lunaryai
- group: company
  title: ''
  type: Website
  url: https://lunary.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lunary.ai/
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/lunary-ai/lunary
- group: commercial
  title: ''
  type: Plans
  url: plans/lunary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lunary-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lunary-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lunary.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://lunary.ai/blog
created: '2026-05-08'
description: 'Lunary is an open-source LLM observability and evaluation platform: tracing, prompt management, datasets, evaluations, and analytics for LLM apps. Available as a hosted SaaS at lunary.ai and as a self-hosted Apache 2.0 deployment. Exposes a REST API authenticated with Bearer tokens.'
finops:
- name: Lunary Finops
  service_category: AI Observability
  slug: lunary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunary.png
layout: provider
modified: '2026-05-08'
name: Lunary
nav: Providers
network: true
overview: 'Lunary publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, AuditLogs API, Checklists API, and 10 more. Tagged areas include AI Evaluation, Observability, Open-Source, LLM, and Tracing.


  Lunary''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Lunary Plans Pricing
  plan_count: 4
  slug: lunary-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Lunary Rate Limits
  slug: lunary-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 11
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 33.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lunary/refs/heads/main/screenshots/lunary-2026-06-20T184802.png
security:
- kind: authentication
  name: Lunary Authentication
  slug: lunary-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lunary Domain Security
  slug: lunary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lunary
tags:
- AI Evaluation
- Observability
- Open-Source
- LLM
- Tracing
- Prompts
website: https://lunary.ai/
---
