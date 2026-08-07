---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 43
  human_in_the_loop: 2
  name: Phoenix Agentic Access
  operation_count: 84
  slug: phoenix-agentic-access
  summary_line: 84 operations · 43 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: The annotation_configs API from Arize Phoenix — 3 operation(s) for annotation_configs.
  name: Arize Phoenix annotation_configs API
  slug: phoenix-annotation-configs-api
- description: The annotations API from Arize Phoenix — 3 operation(s) for annotations.
  name: Arize Phoenix annotations API
  slug: phoenix-annotations-api
- description: The Arize Phoenix Version API from Arize Phoenix — 1 operation(s) for arize phoenix version.
  name: Arize Phoenix Arize Phoenix Version API
  slug: phoenix-arize-phoenix-version-api
- description: The Auth API from Arize Phoenix — 6 operation(s) for auth.
  name: Arize Phoenix Auth API
  slug: phoenix-auth-api
- description: The chat API from Arize Phoenix — 2 operation(s) for chat.
  name: Arize Phoenix chat API
  slug: phoenix-chat-api
- description: The datasets API from Arize Phoenix — 9 operation(s) for datasets.
  name: Arize Phoenix datasets API
  slug: phoenix-datasets-api
- description: The experiments API from Arize Phoenix — 8 operation(s) for experiments.
  name: Arize Phoenix experiments API
  slug: phoenix-experiments-api
- description: The Healthz API from Arize Phoenix — 1 operation(s) for healthz.
  name: Arize Phoenix Healthz API
  slug: phoenix-healthz-api
- description: The Oauth2 API from Arize Phoenix — 2 operation(s) for oauth2.
  name: Arize Phoenix Oauth2 API
  slug: phoenix-oauth2-api
- description: The projects API from Arize Phoenix — 2 operation(s) for projects.
  name: Arize Phoenix projects API
  slug: phoenix-projects-api
- description: The prompts API from Arize Phoenix — 8 operation(s) for prompts.
  name: Arize Phoenix prompts API
  slug: phoenix-prompts-api
- description: The Readyz API from Arize Phoenix — 1 operation(s) for readyz.
  name: Arize Phoenix Readyz API
  slug: phoenix-readyz-api
- description: The secrets API from Arize Phoenix — 1 operation(s) for secrets.
  name: Arize Phoenix secrets API
  slug: phoenix-secrets-api
- description: The sessions API from Arize Phoenix — 5 operation(s) for sessions.
  name: Arize Phoenix sessions API
  slug: phoenix-sessions-api
- description: The spans API from Arize Phoenix — 6 operation(s) for spans.
  name: Arize Phoenix spans API
  slug: phoenix-spans-api
- description: The traces API from Arize Phoenix — 4 operation(s) for traces.
  name: Arize Phoenix traces API
  slug: phoenix-traces-api
- description: The users API from Arize Phoenix — 3 operation(s) for users.
  name: Arize Phoenix users API
  slug: phoenix-users-api
artifact_total: 38
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/phoenix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phoenix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arize.com/phoenix/
- group: docs
  title: ''
  type: Documentation
  url: https://arize.com/docs/phoenix
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Arize-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arizeai
- group: company
  title: ''
  type: Blog
  url: https://arize.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://arize.com/pricing/
- group: other
  title: ''
  type: X
  url: https://twitter.com/arizeai
- group: commercial
  title: ''
  type: Plans
  url: plans/phoenix-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/phoenix-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/phoenix-finops.yml
created: '2026-06-13'
description: Arize Phoenix is an open-source AI observability and evaluation platform built on OpenTelemetry, enabling developers to trace, evaluate, and debug LLM applications in production or locally. Phoenix exposes a REST API for programmatically ingesting spans and traces, managing datasets, running experiments, submitting annotations, and querying evaluation results. The platform supports a wide range of LLM frameworks including LangChain, LlamaIndex, OpenAI, Anthropic, and CrewAI through auto-instrumentation. Phoenix can be self-hosted in a single command or used as a managed cloud service (Arize AX), with authentication via API keys and OAuth2/OIDC for enterprise deployments.
examples:
- key_count: 1
  name: Phoenix Annotate Spans Example
  slug: phoenix-annotate-spans-example
- key_count: 0
  name: Phoenix Create Experiment Example
  slug: phoenix-create-experiment-example
- key_count: 1
  name: Phoenix Create Project Example
  slug: phoenix-create-project-example
- key_count: 1
  name: Phoenix Create Span Example
  slug: phoenix-create-span-example
finops:
- name: Phoenix Finops
  service_category: ''
  slug: phoenix-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/phoenix.png
json_schemas:
- name: AnnotateSpansRequestBody
  property_count: 1
  slug: phoenix-annotatespansrequestbody
- name: AnnotateSpansResponseBody
  property_count: 1
  slug: phoenix-annotatespansresponsebody
- name: AnnotationResult
  property_count: 3
  slug: phoenix-annotationresult
- name: Dataset
  property_count: 7
  slug: phoenix-dataset
- name: DatasetVersion
  property_count: 4
  slug: phoenix-datasetversion
- name: Experiment
  property_count: 14
  slug: phoenix-experiment
- name: ExperimentRun
  property_count: 9
  slug: phoenix-experimentrun
- name: Project
  property_count: 3
  slug: phoenix-project
- name: Span
  property_count: 11
  slug: phoenix-span
- name: SpanAnnotation
  property_count: 11
  slug: phoenix-spanannotation
jsonld:
- class_count: 17
  name: Phoenix Context
  property_count: 37
  slug: phoenix-context
layout: provider
modified: '2026-06-13'
name: Arize Phoenix
nav: Providers
network: true
overview: 'Arize Phoenix publishes 17 APIs on the [APIs.io](https://apis.io/) network, including annotation_configs API, annotations API, Arize Phoenix Version API, and 14 more. Tagged areas include LLM Observability, AI Evaluation, OpenTelemetry, Tracing, and LLMOps.


  The Arize Phoenix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arize Phoenix''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Phoenix Plans Pricing
  plan_count: 5
  slug: phoenix-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 4
  name: Phoenix Rate Limits
  slug: phoenix-rate-limits
rules:
- name: Arize Phoenix API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: phoenix-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.4
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phoenix/refs/heads/main/screenshots/phoenix-2026-06-20T191644.png
security:
- kind: domain-security
  name: Phoenix Domain Security
  slug: phoenix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: phoenix
tags:
- LLM Observability
- AI Evaluation
- OpenTelemetry
- Tracing
- LLMOps
- AI Monitoring
- Open Source
- Prompt Engineering
- Datasets
- Experiments
website: https://arize.com/phoenix/
---
