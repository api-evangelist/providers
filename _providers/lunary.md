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
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
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
  description: The Evals API from Lunary — 7 operation(s) for evals.
  name: Lunary Evals API
  slug: lunary-evals-api
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
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Audit Logs API from Lunary — 1 operation(s) for audit logs.
  name: Lunary Audit Logs API
  slug: lunary-audit-logs-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The Datasets V2 API from Lunary — 13 operation(s) for datasets v2.
  name: Lunary Datasets V2 API
  slug: lunary-datasets-v2-api
- baseURL: https://api.lunary.ai/v1
  baseurl_source: declared
  description: The External Users API from Lunary — 2 operation(s) for external users.
  name: Lunary External Users API
  slug: lunary-external-users-api
artifact_total: 36
collections:
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
- group: other
  href: https://artifacts.apis.io/lunary/capabilities/lunary-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lunary-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/lunary/agentic-access/lunary-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lunary-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lunary/security/lunary-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lunary-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lunary/authentication/lunary-authentication.yml
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
  href: https://artifacts.apis.io/lunary/plans/lunary-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lunary-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lunary/rate-limits/lunary-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lunary-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lunary/finops/lunary-finops.yml
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
- has_sources: true
  method: generated
  name: Lunary Finops
  primary_unit: ''
  service_category: AI Observability
  slug: lunary-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lunary.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.lunary.ai over HTTP; 3 tools listed.
  name: Lunary MCP Server
  slug: lunary
modified: '2026-05-08'
name: Lunary
nav: Providers
network: true
overview: 'Lunary publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Checklists API, Datasets API, and 11 more. Tagged areas include AI Evaluation, Observability, Open Source, LLM, and Tracing.


  The Lunary catalog on APIs.io includes 1 Spectral governance ruleset.


  Lunary''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Lunary Plans Pricing
  plan_count: 4
  slug: lunary-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Lunary Rate Limits
  slug: lunary-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Lunary API Rules
  rule_count: 55
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 3
  slug: lunary-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 46.5
    catalog_earned_first_party: 0.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 33.3
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/lunary/lunary-2026-06-20T184802.png
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
- Open Source
- LLM
- Tracing
- Prompts
website: https://lunary.ai/
---
