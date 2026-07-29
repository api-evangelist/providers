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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Parea Agentic Access
  operation_count: 20
  slug: parea-agentic-access
  summary_line: 20 operations · 16 acting
api_count: 1
apis:
- description: The Parea API from Parea AI — 19 operation(s) for parea.
  name: Parea AI Parea API
  slug: parea-parea-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parea-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parea-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parea-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/parea-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.parea.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parea.ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/parea-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parea-ai/
- group: company
  title: ''
  type: Blog
  url: https://docs.parea.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.parea.ai/#pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/PareaAI
- group: commercial
  title: ''
  type: Plans
  url: plans/parea-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/parea-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/parea-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/parea-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/parea-context.jsonld
created: 2026-06-13
description: Parea AI is an LLM evaluation, testing, and observability platform designed for AI engineering teams building production-ready LLM applications. The platform provides a REST API for managing prompt versions, running automated test suites, collecting human feedback, and tracking quality metrics across model versions. Parea supports experiment tracking with aggregate statistics, trace logging for end-to-end observability, and an LLM proxy gateway that enables unified access to multiple model providers with built-in caching and retries. Native SDKs for Python and TypeScript integrate with popular frameworks including OpenAI, Anthropic, LangChain, Instructor, DSPy, and LiteLLM, making it easy to instrument existing applications.
finops:
- name: Parea Finops
  service_category: ''
  slug: parea-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parea.png
json_schemas:
- name: AddColumnsSchema
  property_count: 2
  slug: AddColumnsSchema
- name: AddExperimentTraceLogsToAnnotationQueuesSchema
  property_count: 2
  slug: AddExperimentTraceLogsToAnnotationQueuesSchema
- name: AddTraceLogsToAnnotationQueuesSchema
  property_count: 2
  slug: AddTraceLogsToAnnotationQueuesSchema
- name: AnalyticsRequestSchema
  property_count: 2
  slug: AnalyticsRequestSchema
- name: AnnotationCriterionSchema
  property_count: 10
  slug: AnnotationCriterionSchema
- name: AnnotationQueueItemSchema
  property_count: 2
  slug: AnnotationQueueItemSchema
- name: AnnotationQueueSchema
  property_count: 5
  slug: AnnotationQueueSchema
- name: BootstrapEvalFullResultSchema
  property_count: 5
  slug: BootstrapEvalFullResultSchema
- name: TestCaseSchema
  property_count: 3
  slug: TestCaseSchema
- name: TraceLogSchema
  property_count: 43
  slug: TraceLogSchema
jsonld:
- class_count: 8
  name: Parea Context
  property_count: 25
  slug: parea-context
layout: provider
modified: 2026-06-13
name: Parea AI
nav: Providers
network: true
overview: 'Parea AI publishes 1 API on the [APIs.io](https://apis.io/) network: Parea API. Tagged areas include LLM, Evaluation, Observability, Testing, and Prompt Management.


  The Parea AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Parea AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Parea Plans Pricing
  plan_count: 4
  slug: parea-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 0
  name: Parea Rate Limits
  slug: parea-rate-limits
rules:
- name: Parea AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: parea-jsonschema-spectral-rules
scopes:
- name: Parea Scopes
  scope_count: 0
  slug: parea-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.7
  delta: -5.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.1
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/parea/refs/heads/main/screenshots/parea-2026-06-20T191406.png
security:
- kind: authentication
  name: Parea Authentication
  slug: parea-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Parea Domain Security
  slug: parea-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: parea
tags:
- LLM
- Evaluation
- Observability
- Testing
- Prompt Management
- AI Engineering
- Machine Learning
- Tracing
- Experimentation
- Human Feedback
website: https://www.parea.ai/
---
