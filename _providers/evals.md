---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 20
apis:
- description: OpenAI Evals is the open-source framework released by OpenAI for evaluating large language models and LLM-based systems. The README states "Evals provide a framework for evaluating large language mode
  name: OpenAI Evals
  slug: openai-evals
- description: Inspect AI is an open-source framework for large language model evaluations developed and maintained by the UK AI Security Institute (UK AISI) and Meridian Labs. It supports text comparisons, model-ba
  name: Inspect AI
  slug: inspect-ai
- description: Braintrust is a commercial evaluation platform that captures eval runs as immutable, comparable experiment snapshots. The product supports code-based scorers, built-in autoevals, and LLM-as-a-judge ev
  name: Braintrust
  slug: braintrust
- description: 'LangSmith Evaluation is LangChain''s evaluation framework for measuring application quality across the lifecycle. The docs describe evals as "a way to breakdown what ''good'' looks like and measure it." '
  name: LangSmith Evaluation
  slug: langsmith-evaluation
- description: Promptfoo is an open-source CLI and library for evaluating and red-teaming LLM applications. The docs describe it as enabling "test-driven LLM development rather than trial-and-error" and producing "m
  name: Promptfoo
  slug: promptfoo
- description: Helicone is an open-source observability and monitoring platform for LLM applications. The homepage states "The world's fastest-growing AI companies rely on Helicone to route, debug, and analyze their
  name: Helicone
  slug: helicone
- description: Patronus AI is a frontier lab building evaluation infrastructure and Digital World Models for human-aligned AGI. Its evaluator models include Lynx (a hallucination-detection model reported to outperfo
  name: Patronus AI
  slug: patronus-ai
- description: DeepEval is an open-source LLM evaluation package, paired with Confident AI as the hosted observability/evals/monitoring tier. The docs call DeepEval "an open-source LLM eval package" and Confident AI
  name: DeepEval (Confident AI)
  slug: deepeval-confident-ai
- description: Arize AI provides an AI observability and evaluation platform centered on Arize AX (the commercial product) and Phoenix (open-source LLM tracing and evaluation). Phoenix runs LLM-as-a-judge evaluators
  name: Arize AI (Phoenix)
  slug: arize-ai-phoenix
- description: 'Galileo is an enterprise AI observability and evaluation engineering platform. The product line emphasizes "20+ built-in evaluators" spanning RAG, agents, safety, and security, plus custom evaluators '
  name: Galileo
  slug: galileo
- description: Humanloop was a development platform for LLM applications, describing itself as having been "the first development platform for LLM applications" and having "shaped industry standards for how to manag
  name: Humanloop
  slug: humanloop
- description: TruLens is an open-source evaluation and tracing platform for AI agents that helps developers "move from vibes to metrics." Its feedback-function library covers the RAG triad — groundedness (responses
  name: TruLens
  slug: trulens
- description: W&B Weave is a platform for evaluating, monitoring, and iterating on AI agents and applications, started with "one line of code." Weave Evaluations enable visual comparison of runs, automatic versioni
  name: Weights and Biases Weave
  slug: weights-and-biases-weave
- description: 'Ragas is an open-source evaluation library focused on retrieval-augmented generation, described in its own docs as "a library that helps you move from ''vibe checks'' to systematic evaluation loops for '
  name: Ragas
  slug: ragas
- description: MLflow LLM evaluate extends MLflow's experiment tracking with mlflow.evaluate() support for LLM tasks. The API runs reference-based and reference-free metrics (toxicity, perplexity, BLEU, ROUGE, exact
  name: MLflow LLM Evaluate
  slug: mlflow-llm-evaluate
- description: MMLU (Measuring Massive Multitask Language Understanding) is a multiple-choice benchmark spanning 57 subjects from STEM and international law to nutrition and religion. It contains 15,908 multiple-cho
  name: MMLU Benchmark
  slug: mmlu-benchmark
- description: HumanEval is OpenAI's evaluation harness for code-generation models, described in its README as "an evaluation harness for the HumanEval problem solving dataset described in the paper 'Evaluating Larg
  name: HumanEval Benchmark
  slug: humaneval-benchmark
- description: GAIA is "a benchmark for General AI Assistants," published in 2023 (arXiv 2311.12983). It tests general-purpose AI agent capability across reasoning, tool use, multi-modality, and web browsing, with a
  name: GAIA Benchmark
  slug: gaia-benchmark
- description: AgentBench is the first benchmark designed to evaluate LLM-as-Agent across a diverse spectrum of environments. It bundles 8 environments — 5 newly created (Operating System, Database, Knowledge Graph,
  name: AgentBench
  slug: agentbench
- description: The Beyond the Imitation Game Benchmark (BIG-Bench) is "a collaborative benchmark intended to probe large language models and extrapolate their future capabilities." It contains more than 200 tasks ac
  name: BIG-Bench
  slug: big-bench
artifact_total: 68
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evals-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: docs
  title: Eval Run Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-eval-run-schema.json
- group: docs
  title: Eval Suite Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-eval-suite-schema.json
- group: docs
  title: Eval Case Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-eval-case-schema.json
- group: docs
  title: Scorer Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-scorer-schema.json
- group: docs
  title: Judge Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-judge-schema.json
- group: docs
  title: Dataset Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-schema/evals-dataset-schema.json
- group: design
  title: Eval Run Structure
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-structure/evals-eval-run-structure.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/json-ld/evals-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/vocabulary/evals-vocabulary.yml
created: '2026-05-22'
description: A landscape catalog of the platforms, frameworks, libraries, and benchmark suites used to evaluate large language models, LLM-based applications, and AI agents. The topic spans human-rated, LLM-as-a-judge, reference-based, reference-free, and benchmark-aligned approaches to measuring AI system quality. Tracked alongside the eval platforms are the canonical multi-task and code/agent benchmark suites (MMLU, HumanEval, GAIA, AgentBench, BIG-Bench) that establish public points of comparison.
examples:
- key_count: 12
  name: Evals Dataset Example
  slug: evals-dataset-example
- key_count: 6
  name: Evals Eval Case Example
  slug: evals-eval-case-example
- key_count: 14
  name: Evals Eval Run Humaneval Example
  slug: evals-eval-run-humaneval-example
- key_count: 15
  name: Evals Eval Run Mmlu Example
  slug: evals-eval-run-mmlu-example
- key_count: 14
  name: Evals Eval Run Pairwise Example
  slug: evals-eval-run-pairwise-example
- key_count: 15
  name: Evals Eval Run Rag Faithfulness Example
  slug: evals-eval-run-rag-faithfulness-example
- key_count: 10
  name: Evals Eval Suite Example
  slug: evals-eval-suite-example
- key_count: 10
  name: Evals Judge Example
  slug: evals-judge-example
- key_count: 11
  name: Evals Scorer Example
  slug: evals-scorer-example
features:
- description: A second LLM evaluates the output of the system-under-test, producing a numeric or categorical score and (optionally) a written rationale. The dominant scoring mode for free-form text outputs across Braintrust, LangSmith, DeepEval, Weave, TruLens, Phoenix, and Patronus.
  name: LLM-as-a-Judge Scoring
- description: Compares model output against a ground-truth expected answer using exact match, BLEU, ROUGE, embedding similarity, or task-specific equality (e.g. unit-test pass/fail). The native mode for benchmarks like MMLU, HumanEval, and GAIA.
  name: Reference-Based Scoring
- description: Assesses output quality without ground truth — toxicity, coherence, faithfulness against retrieved context, criterion adherence. Enables online (production-traffic) evaluation where labels do not exist.
  name: Reference-Free Scoring
- description: A judge ranks two candidate outputs A vs B (or a tie). Useful when absolute scoring is hard but relative preference is reliable. Surfaced explicitly by LangSmith and used widely in chatbot arenas.
  name: Pairwise Comparison
- description: Runs the system-under-test against a standardized public dataset (MMLU, HumanEval, GAIA, AgentBench, BIG-Bench) to produce comparable, headline scores. The basis of model leaderboards.
  name: Benchmark-Aligned Evaluation
- description: Domain experts or end users provide thumbs-up/down, Likert ratings, or written critiques. Used as ground truth, as a judge-calibration signal, and as a final acceptance gate before production.
  name: Human-Rated Scoring
- description: Three feedback functions — groundedness, context relevance, answer relevance — codified by TruLens and widely adopted across Ragas, Phoenix, DeepEval, and LangSmith for evaluating retrieval-augmented generation pipelines.
  name: RAG Triad
- description: Evaluating multi-step agent trajectories — did the agent pick the right tool, did the tool call succeed, did the final answer satisfy the goal. Supported by Inspect AI, Galileo, Weave, LangSmith, Braintrust, and benchmarks like AgentBench and GAIA.
  name: Agent and Tool-Use Evaluation
- description: Eval scorers (typically reference-free LLM judges and Luna-style distilled evaluators) attach to live traffic via tracing/observability layers (Phoenix, Arize, Helicone, Galileo, Weave) to flag regressions in real time.
  name: Online Production Monitoring
- description: Adversarial test suites probe jailbreaks, prompt injection, PII leakage, harmful content, and policy violations. First-class in Promptfoo, Patronus, Galileo, and Inspect AI's safety evals.
  name: Red-Team / Safety Evaluation
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/evals.png
integrations:
- description: Phoenix, TruLens, Weave, and most modern eval platforms ingest LLM traces via OpenTelemetry, making eval a layer on top of standard observability.
  name: OpenTelemetry
- description: LangSmith is the native eval tier for LangChain/LangGraph apps; most other platforms also integrate.
  name: LangChain / LangGraph
- description: Ragas, DeepEval, and Phoenix integrate directly with LlamaIndex for RAG evaluation.
  name: LlamaIndex
- description: MMLU, HumanEval, and GAIA are distributed as Hugging Face datasets and consumed by every eval framework.
  name: Hugging Face Datasets
- description: Braintrust, Promptfoo, LangSmith, and DeepEval ship CI integrations to fail builds on regression.
  name: CI/CD (GitHub Actions, etc.)
- description: OpenAI Evals can log eval results to Snowflake; TruLens (Truera) is now part of Snowflake.
  name: Snowflake
json_schemas:
- name: EvalDataset
  property_count: 12
  slug: evals-dataset
- name: EvalCase
  property_count: 8
  slug: evals-eval-case
- name: EvalRun
  property_count: 17
  slug: evals-eval-run
- name: EvalSuite
  property_count: 10
  slug: evals-eval-suite
- name: Judge
  property_count: 10
  slug: evals-judge
- name: Scorer
  property_count: 11
  slug: evals-scorer
json_structures:
- name: Evals Dataset Structure
  property_count: 12
  slug: evals-dataset-structure
- name: Evals Eval Case Structure
  property_count: 8
  slug: evals-eval-case-structure
- name: Evals Eval Run Structure
  property_count: 17
  slug: evals-eval-run-structure
- name: Evals Eval Suite Structure
  property_count: 10
  slug: evals-eval-suite-structure
- name: Evals Judge Structure
  property_count: 10
  slug: evals-judge-structure
- name: Evals Scorer Structure
  property_count: 11
  slug: evals-scorer-structure
jsonld:
- class_count: 12
  name: Evals Context
  property_count: 52
  slug: evals-context
layout: provider
modified: '2026-05-22'
name: Evals
nav: Providers
network: true
overview: 'Evals publishes 20 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Evals, LLM Evaluation, AI Quality, Benchmarks, and LLM as a Judge.


  The Evals catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 53
rules:
- name: Evals API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: evals-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.8
  delta: -5.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 17.7
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/evals/refs/heads/main/screenshots/evals-2026-06-20T180857.png
security:
- kind: domain-security
  name: Evals Domain Security
  slug: evals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: evals
tags:
- Evals
- LLM Evaluation
- AI Quality
- Benchmarks
- LLM as a Judge
- Observability
- Agent Evaluation
- RAG Evaluation
- Test-Driven AI
use_cases:
- description: Run candidate models (GPT-5, Claude 4.7, Gemini 3, open-weight) against a shared eval suite to choose the best fit for a specific application by quality, cost, and latency.
  name: Model Selection
- description: Compare prompt variants in a matrix-style eval (Promptfoo, LangSmith experiments, Braintrust experiments) to pick the best prompt before shipping.
  name: Prompt Engineering Iteration
- description: Wire an eval suite into CI so a pull request that drops a key scorer below a threshold fails the build, preventing quality regressions from reaching production.
  name: Regression Detection in CI/CD
- description: Use RAG-triad scores (groundedness / context relevance / answer relevance) and faithfulness to tune chunking, embedding, reranking, and prompt choices.
  name: RAG Pipeline Tuning
- description: Score multi-step agent runs on tool-selection correctness, step efficiency, and final-answer faithfulness — the core measurement for production agentic apps.
  name: Agent Trajectory Quality
- description: Deploy dedicated judge models (Lynx, GLIDER, Luna) to flag hallucinations, toxic content, PII leakage, and policy violations in real time.
  name: Hallucination and Safety Guardrails
- description: Independent labs (UK AISI, US AISI) run capability and safety evaluations on frontier models before release, using frameworks like Inspect AI.
  name: Frontier Capability and Safety Assessment
- description: Submit a model's scores against MMLU, HumanEval, GAIA, AgentBench, and BIG-Bench to position it on community leaderboards and back marketing claims with reproducible numbers.
  name: Public Leaderboard Reporting
---
