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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Galileo Ai Agentic Access
  operation_count: 37
  slug: galileo-ai-agentic-access
  summary_line: 37 operations · 20 acting
api_count: 8
apis:
- description: The Annotations API from Galileo — 2 operation(s) for annotations.
  name: Galileo Annotations API
  slug: galileo-ai-annotations-api
- description: The ApiKeys API from Galileo — 3 operation(s) for apikeys.
  name: Galileo ApiKeys API
  slug: galileo-ai-apikeys-api
- description: The Auth API from Galileo — 4 operation(s) for auth.
  name: Galileo Auth API
  slug: galileo-ai-auth-api
- description: The Datasets API from Galileo — 5 operation(s) for datasets.
  name: Galileo Datasets API
  slug: galileo-ai-datasets-api
- description: The Experiments API from Galileo — 3 operation(s) for experiments.
  name: Galileo Experiments API
  slug: galileo-ai-experiments-api
- description: The Groups API from Galileo — 4 operation(s) for groups.
  name: Galileo Groups API
  slug: galileo-ai-groups-api
- description: The Health API from Galileo — 1 operation(s) for health.
  name: Galileo Health API
  slug: galileo-ai-health-api
- description: The Integrations API from Galileo — 3 operation(s) for integrations.
  name: Galileo Integrations API
  slug: galileo-ai-integrations-api
artifact_total: 28
collections:
- collection_type: open
  name: Galileo Public API
  slug: open-galileo-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/galileo-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/galileo-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/galileo-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://galileo.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.galileo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.galileo.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.galileo.ai/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://galileo.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://galileo.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rungalileo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/galileo-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/galileo-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/galileo-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/galileo-ai-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/galileo-ai-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/galileo-ai-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/galileo-ai-rules.yml
created: '2026-05-08'
description: Galileo (galileo.ai, formerly rungalileo.io) is the GenAI evaluation, observability, and production guardrail platform for LLM and agentic applications. Galileo provides pre-built and custom evaluators, agentic trace and span logging, dataset and experiment management, prompt management, runtime protect (guardrails), and integrations with major LLM providers and agent frameworks. The platform exposes a public REST API plus official Python and TypeScript SDKs and integrates with LangChain, CrewAI, OpenAI Agents, and OpenTelemetry/OpenInference. Galileo is deployable as SaaS, VPC, or on-prem.
examples:
- key_count: 2
  name: Galileo Ai Create Experiment Example
  slug: galileo-ai-create-experiment-example
- key_count: 2
  name: Galileo Ai Create Project Example
  slug: galileo-ai-create-project-example
- key_count: 2
  name: Galileo Ai List Datasets Example
  slug: galileo-ai-list-datasets-example
- key_count: 2
  name: Galileo Ai Query Dataset Example
  slug: galileo-ai-query-dataset-example
finops:
- name: Galileo Ai Finops
  service_category: AI Observability
  slug: galileo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/galileo-ai.png
json_schemas:
- name: Galileo Dataset
  property_count: 7
  slug: galileo-ai-dataset
- name: Galileo Experiment
  property_count: 9
  slug: galileo-ai-experiment
- name: Galileo Metric
  property_count: 5
  slug: galileo-ai-metric
- name: Galileo Project
  property_count: 6
  slug: galileo-ai-project
- name: Galileo Trace
  property_count: 10
  slug: galileo-ai-trace
json_structures:
- name: Galileo Ai Core Structure
  property_count: 0
  slug: galileo-ai-core-structure
jsonld:
- class_count: 0
  name: Galileo Ai Context
  property_count: 14
  slug: galileo-ai-context
layout: provider
modified: '2026-05-25'
name: Galileo
nav: Providers
network: true
overview: 'Galileo publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, ApiKeys API, Auth API, and 5 more. Tagged areas include AI Evaluation, AI Observability, GenAI, Guardrails, and Agentic AI.


  The Galileo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Galileo''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Galileo Ai Plans Pricing
  plan_count: 3
  slug: galileo-ai-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Galileo Ai Rate Limits
  slug: galileo-ai-rate-limits
rules:
- name: Galileo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: galileo-ai-jsonschema-spectral-rules
- name: Galileo API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: galileo-ai-rules
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.9
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 51.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/galileo-ai/refs/heads/main/screenshots/galileo-ai-2026-06-20T181635.png
security:
- kind: authentication
  name: Galileo Ai Authentication
  slug: galileo-ai-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Galileo Ai Domain Security
  slug: galileo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: galileo-ai
tags:
- AI Evaluation
- AI Observability
- GenAI
- Guardrails
- Agentic AI
- LLM
- Tracing
- Experiments
- Prompts
- Datasets
website: https://galileo.ai/
---
