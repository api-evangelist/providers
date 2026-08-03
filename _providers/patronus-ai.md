---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-03'
api_count: 7
apis:
- description: The Patronus Evaluation API scores LLM outputs against built-in and custom evaluators covering hallucination, answer relevance, context utilization, safety, and PII. Evaluators can be invoked synchron
  name: Patronus Evaluation API
  slug: patronus-evaluation-api
- description: The Patronus Python SDK provides decorators and clients for instrumenting LLM applications, running evaluators inline, recording traces, and pushing experiments to the Patronus platform.
  name: Patronus Python SDK
  slug: patronus-python-sdk
- description: The Patronus TypeScript SDK brings the same evaluation, tracing, and experiment workflows to Node.js and browser environments used by JavaScript-first AI applications.
  name: Patronus TypeScript SDK
  slug: patronus-typescript-sdk
- description: 'Lynx is Patronus''s open-weights hallucination detection model published on Hugging Face. It is positioned as state-of-the-art on hallucination benchmarks and is available both as downloadable weights '
  name: Lynx
  slug: lynx
- description: Glider is Patronus's small judge model for evaluating reasoning chains and rubric-based scoring with low latency and cost relative to large frontier judges.
  name: Glider
  slug: glider
- description: Percival is Patronus's agent debugging product that ingests agent traces and surfaces failure modes, tool misuse, and reasoning errors across multi-step runs.
  name: Percival
  slug: percival
- description: FinanceBench is an open benchmark of 10,000 financial question-answer pairs grounded in public filings, used to evaluate LLM performance on financial document understanding.
  name: FinanceBench
  slug: financebench
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/patronus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.patronus.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.patronus.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.patronus.ai/reference
- group: company
  title: ''
  type: Blog
  url: https://www.patronus.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.patronus.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.patronus.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/patronus-ai
- group: other
  title: ''
  type: Research
  url: https://www.patronus.ai/research
- group: operate
  title: ''
  type: Contact
  url: mailto:contact@patronus.ai
- group: auth
  title: ''
  type: Security
  url: mailto:security@patronus.ai
created: '2026-05-23'
description: Patronus AI is an evaluation and guardrails platform for production LLM applications and AI agents. It combines an API-first evaluation service with Python and TypeScript SDKs, in-house judge models (Lynx for hallucination detection, Glider for reasoning evaluation, Percival for agent debugging), and a portfolio of open benchmarks and datasets including FinanceBench, BLUR, and RL environments. Customers use Patronus for experimentation, production monitoring, RAG and agent evaluation, dataset generation, and human-in-the-loop annotation.
features:
- description: Hosted API for running built-in and custom evaluators on LLM inputs and outputs.
  name: Evaluation API
- description: State-of-the-art open-weights hallucination judge available as a hosted evaluator.
  name: Lynx Hallucination Detection
- description: Small reasoning-focused judge for rubric-based evaluation at production latency.
  name: Glider Judge
- description: Agent trace analysis surfacing failure modes, tool misuse, and reasoning errors.
  name: Percival Agent Debugger
- description: Compare prompts, models, and configurations across datasets with side-by-side outputs.
  name: Experimentation
- description: Real-time alerts, tracing, and dashboards for live LLM applications.
  name: Production Monitoring
- description: Synthetic dataset creation including red-teaming sets for RAG and agent systems.
  name: Dataset Generation
- description: Workflows for human-in-the-loop labeling and reviewer agreement tracking.
  name: Human Annotation
finops:
- name: Patronus Ai Finops
  service_category: API
  slug: patronus-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/patronus-ai.png
integrations:
- description: Score outputs from OpenAI models inside Patronus experiments and monitoring.
  name: OpenAI
- description: Evaluate Anthropic Claude outputs using Patronus judges.
  name: Anthropic
- description: SDK integrations for LangChain chains and agents.
  name: LangChain
- description: Evaluate LlamaIndex RAG pipelines with Patronus evaluators.
  name: LlamaIndex
- description: Ingest OTel-compatible LLM traces for evaluation and monitoring.
  name: OpenTelemetry
- description: Lynx and Glider weights are distributed via Hugging Face for self-hosting.
  name: Hugging Face
layout: provider
modified: '2026-05-23'
name: Patronus AI
nav: Providers
network: true
overview: 'Patronus AI publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include LLM Evaluation, Guardrails, Judges, Hallucination Detection, and AI Research.


  Patronus AI''s developer surface includes documentation, API reference, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Patronus Ai Plans Pricing
  plan_count: 1
  slug: patronus-ai-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 2
  name: Patronus Ai Rate Limits
  slug: patronus-ai-rate-limits
score:
  band: emerging
  composite: 25.3
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/patronus-ai/refs/heads/main/screenshots/patronus-ai-2026-06-20T191445.png
security:
- kind: domain-security
  name: Patronus Ai Domain Security
  slug: patronus-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: patronus-ai
tags:
- LLM Evaluation
- Guardrails
- Judges
- Hallucination Detection
- AI Research
- Benchmarks
- API
use_cases:
- description: Score retrieval and generation quality in RAG applications across faithfulness, relevance, and context.
  name: RAG Evaluation
- description: Trace and diagnose failures in multi-step agentic systems using Percival.
  name: Agent Debugging
- description: Benchmark candidate models against domain-specific datasets such as FinanceBench.
  name: Model Benchmarking
- description: Apply Patronus judges as runtime guardrails on LLM responses.
  name: Guardrails
- description: Detect quality regressions across prompt, model, and configuration changes.
  name: Regression Testing
website: https://www.patronus.ai/
---
