---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Arize Ai Agentic Access
  operation_count: 1
  slug: arize-ai-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 5
apis:
- description: Arize AX is the commercial AI engineering platform covering tracing, evaluation, experiments, prompt management, annotations, and dashboards for LLM applications and agents. Built on OpenInference and
  name: Arize AX
  slug: arize-ax
- description: Phoenix is Arize's open-source LLM observability platform offering local tracing, evaluation, experiments, and prompt iteration. Distributed as a Python package with a local UI, deployable in notebook
  name: Phoenix
  slug: phoenix
- description: OpenInference is Arize's open-source set of OpenTelemetry conventions and instrumentation libraries for LLM applications, agents, RAG pipelines, and frameworks. Provides Python and TypeScript instrume
  name: OpenInference
  slug: openinference
- description: Alyx is Arize's AI engineering agent that helps developers debug traces, create evaluators, build dashboards, and compare experiments inside the Arize AX platform.
  name: Alyx
  slug: alyx
- description: OTLP trace ingestion
  name: Arize AI Traces API
  slug: arize-ai-traces-api
artifact_total: 36
collections:
- collection_type: open
  name: Arize AX OTLP Ingestion API
  slug: open-arize-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arize-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arize-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arize-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://arize.com/
- group: docs
  title: ''
  type: Documentation
  url: https://arize.com/docs/ax
- group: docs
  title: ''
  type: PhoenixDocumentation
  url: https://docs.arize.com/phoenix
- group: company
  title: ''
  type: Blog
  url: https://arize.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://arize.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.arize.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Arize-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Arize-ai/phoenix
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Arize-ai/openinference
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arizeai/
- group: operate
  title: ''
  type: Community
  url: https://arize-ai.slack.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://arize.com/llms.txt
created: '2026-05-23'
description: Arize AI is an AI engineering and observability platform for LLM applications, agents, and traditional ML systems. The commercial Arize AX platform (with Generative and ML & CV variants) provides tracing, evaluation, experiments, prompt management, and the Alyx AI engineering agent, built on the OpenInference OpenTelemetry conventions. Phoenix is the open-source counterpart used by tens of thousands of developers for local tracing, evaluation, and prompt iteration. Arize is vendor- and framework-agnostic with 30+ instrumentation providers and an OTLP-native ingestion path.
features:
- description: Capture spans for LLM calls, retrieval steps, tool invocations, and agent loops via OpenInference OTel.
  name: LLM Tracing
- description: Run built-in and custom evaluators on production traces, experiments, and datasets.
  name: LLM Evaluation
- description: Compare prompt and model variants over curated datasets with structured logging.
  name: Experiments
- description: Playground, hub, builder, and versioning for prompts used across applications.
  name: Prompt Management
- description: Capture human feedback on traces and outputs for evaluator development and dataset curation.
  name: Annotations
- description: AI assistant for debugging, evaluator authoring, dashboarding, and experiment comparison.
  name: Alyx AI Engineer
- description: Drift, data quality, and performance monitoring for traditional ML and computer vision models.
  name: ML Monitoring
- description: Open-source local tracing and evaluation tool runnable in notebooks or self-hosted.
  name: Phoenix OSS
finops:
- name: Arize Ai Finops
  service_category: API
  slug: arize-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arize-ai.png
integrations:
- description: OpenInference instrumentation for OpenAI Chat Completions, Assistants, and Responses APIs.
  name: OpenAI
- description: Instrumentation for Anthropic Claude models.
  name: Anthropic
- description: Instrumentation and evaluators for LangChain chains and agents.
  name: LangChain
- description: Trace and evaluate LangGraph stateful agents.
  name: LangGraph
- description: Instrumentation for LlamaIndex RAG pipelines.
  name: LlamaIndex
- description: Trace CrewAI multi-agent crews.
  name: CrewAI
- description: Trace and evaluate DSPy programs.
  name: DSPy
- description: Instrumentation for Vercel AI SDK applications.
  name: Vercel AI SDK
- description: OTLP-native ingestion compatible with any OTel collector or backend.
  name: OpenTelemetry
- description: Instrumentation for AWS Bedrock model invocations.
  name: Bedrock
- description: Instrumentation for Google Vertex AI and Gemini.
  name: Vertex AI
layout: provider
modified: '2026-05-23'
name: Arize AI
nav: Providers
network: true
overview: 'Arize AI publishes 1 API on the [APIs.io](https://apis.io/) network: Traces API. Tagged areas include LLM Observability, ML Monitoring, Open Source, OpenTelemetry, and Phoenix.


  Arize AI''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Arize Ai Plans Pricing
  plan_count: 1
  slug: arize-ai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Arize Ai Rate Limits
  slug: arize-ai-rate-limits
score:
  band: thin
  composite: 41.1
  delta: -1.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arize-ai/refs/heads/main/screenshots/arize-ai-2026-06-20T172430.png
security:
- kind: authentication
  name: Arize Ai Authentication
  slug: arize-ai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Arize Ai Domain Security
  slug: arize-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: arize-ai
tags:
- LLM Observability
- ML Monitoring
- Open Source
- OpenTelemetry
- Phoenix
- Tracing
- Evaluation
use_cases:
- description: Monitor production LLM applications with traces, evaluators, and alerting.
  name: LLM Application Observability
- description: Inspect multi-step agent runs across tool calls and intermediate reasoning.
  name: Agent Debugging
- description: Evaluate retrieval and generation quality over time in RAG systems.
  name: RAG Quality Monitoring
- description: Detect drift and degradation in classical ML and CV models.
  name: ML Monitoring
- description: Iterate on prompts and evals locally with Phoenix before shipping to Arize AX.
  name: Local Development
website: https://arize.com/
---
