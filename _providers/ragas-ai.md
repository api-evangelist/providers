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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Ragas Python library is the primary surface of the project, installed via `pip install ragas` and imported as `ragas`. It exposes evaluation entry points (`ragas.evaluate`), metric classes (Faithf
  name: Ragas Python Library
  slug: ragas
artifact_total: 27
common:
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/vibrantlabsai/ragas/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/vibrantlabsai/ragas/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/vibrantlabsai/ragas/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ragas-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ragas.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ragas.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ragas.io/en/stable/getstarted/
- group: other
  title: ''
  type: Concepts
  url: https://docs.ragas.io/en/stable/concepts/
- group: other
  title: ''
  type: Metrics
  url: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
- group: docs
  title: ''
  type: HowToGuides
  url: https://docs.ragas.io/en/stable/howtos/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/explodinggradients/ragas
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/explodinggradients
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/ragas/
- group: commercial
  title: ''
  type: License
  url: https://github.com/explodinggradients/ragas/blob/main/LICENSE
- group: operate
  title: ''
  type: Issues
  url: https://github.com/explodinggradients/ragas/issues
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/explodinggradients/ragas/releases
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/5djav8GGNZ
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ragas_io
- group: other
  title: ''
  type: Company
  url: https://www.vibrantlabs.ai/
- group: operate
  title: ''
  type: Contact
  url: mailto:founders@vibrantlabs.com
created: '2026-05-25'
description: Ragas is an open-source evaluation toolkit for Large Language Model applications, with particular depth on Retrieval Augmented Generation (RAG) and agentic systems. Originally created under the Exploding Gradients organization on GitHub and now maintained by Vibrant Labs AI, Ragas is a Python library distributed on PyPI under the Apache 2.0 license. It moves teams from informal "vibe checks" to systematic evaluation loops by providing objective LLM-based and traditional metrics, automated test dataset generation, experiment tracking, and integrations with the broader LLM ecosystem including LangChain, LlamaIndex, OpenAI, Anthropic, and popular observability platforms. Ragas exposes a metrics library covering faithfulness, response relevancy, context precision and recall, factual correctness, semantic similarity, agent tool-use accuracy, SQL equivalence, Nvidia-defined RAG metrics, and general-purpose rubric scoring. The project ships a CLI (`ragas`) with quickstart templates
  such as `rag_eval`, and is consumed primarily as a `pip install ragas` library rather than as a hosted API service. Ragas is widely cited as a default evaluation harness for RAG applications and has grown a substantial community on GitHub and Discord.
features:
- description: Faithfulness, Response Relevancy, Context Precision, Context Recall, Context Entities Recall, and Noise Sensitivity for retrieval augmented generation pipelines.
  name: RAG Evaluation Metrics
- description: Topic Adherence, Tool Call Accuracy, Tool Call F1, and Agent Goal Accuracy for evaluating multi-step agentic systems.
  name: Agent and Tool-Use Metrics
- description: Factual Correctness, Semantic Similarity, BLEU, ROUGE, CHRF, Exact Match, and String Presence metrics for output comparison.
  name: Natural Language Comparison
- description: Execution-based Datacompy Score and SQL Query Equivalence metrics for text-to-SQL applications.
  name: SQL Evaluation
- description: Aspect Critic, Simple Criteria Scoring, Rubrics-based scoring, and instance-specific rubrics for custom evaluation criteria.
  name: General Purpose Scoring
- description: Answer Accuracy, Context Relevance, and Response Groundedness metrics contributed by Nvidia for RAG quality.
  name: Nvidia Metrics
- description: Automated synthesis of diverse test datasets covering single-hop, multi-hop, and abstract query types over user knowledge bases.
  name: Test Data Generation
- description: Experiment-first workflow comparing prompts, models, and configurations across datasets with iterative result tracking.
  name: Experiments
- description: DiscreteMetric and decorator-based APIs for defining LLM-judge and rule-based custom evaluation metrics.
  name: Custom Metrics
- description: The `ragas quickstart` command scaffolds evaluation projects including the `rag_eval` template for RAG systems.
  name: CLI Quickstart Templates
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ragas-ai.png
integrations:
- description: Native integration for evaluating LangChain chains, retrievers, and agents using Ragas metrics.
  name: LangChain
- description: Integration for evaluating LlamaIndex RAG pipelines and query engines.
  name: LlamaIndex
- description: Default LLM judge backend uses OpenAI models such as GPT-4 class judges.
  name: OpenAI
- description: Anthropic Claude models supported as LLM judges via the LangChain LLM abstraction.
  name: Anthropic
- description: Support for Hugging Face embeddings and models as judges, plus dataset interop via the `datasets` library.
  name: Hugging Face
- description: Result tracking and trace inspection via LangSmith observability.
  name: LangSmith
- description: Observability integration for tracing Ragas evaluations alongside production LLM traffic.
  name: Arize Phoenix
- description: LLM cost and trace observability for Ragas-driven evaluations.
  name: Helicone
- description: Datasets and evaluation results are exposed as pandas DataFrames for analysis.
  name: Pandas
layout: provider
modified: '2026-05-25'
name: Ragas
nav: Providers
network: true
overview: 'Ragas publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include LLM Evaluation, RAG Evaluation, Retrieval Augmented Generation, AI Evaluation, and Open-Source.


  Ragas'' developer surface includes documentation, getting-started guide, release notes, and 17 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 100.0
  previous_composite: 24.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ragas-ai/refs/heads/main/screenshots/ragas-ai-2026-06-20T192527.png
security:
- kind: domain-security
  name: Ragas Ai Domain Security
  slug: ragas-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ragas-ai
tags:
- LLM Evaluation
- RAG Evaluation
- Retrieval Augmented Generation
- AI Evaluation
- Open-Source
- Python
- Metrics
- Test Data Generation
- Agent Evaluation
- LLM Tooling
use_cases:
- description: Scoring retrieval and generation quality in RAG applications across faithfulness, relevance, and context fidelity.
  name: RAG Pipeline Evaluation
- description: Measuring tool-call correctness, goal completion, and topic adherence in multi-step LLM agents.
  name: Agent Evaluation
- description: Running Ragas metrics in CI pipelines to detect quality regressions across prompt, model, and configuration changes.
  name: Regression Testing in CI
- description: Comparing candidate models and prompt variants on a fixed dataset using Ragas experiments.
  name: Model and Prompt Selection
- description: Generating diverse evaluation datasets from a knowledge base for systematic LLM testing.
  name: Synthetic Test Set Generation
- description: Validating generated SQL against reference queries using execution and structural equivalence metrics.
  name: Text-to-SQL Evaluation
website: https://www.ragas.io/
---
