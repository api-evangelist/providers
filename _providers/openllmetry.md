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
  scored_at: '2026-09-04'
api_count: 6
apis:
- description: The Traceloop SDK is the developer-facing entry point for OpenLLMetry. A single Traceloop.init() call configures OpenTelemetry, registers all available LLM/vector-DB/framework instrumentations, and st
  name: OpenLLMetry Traceloop SDK
  slug: openllmetry-traceloop-sdk
- description: A vocabulary of span attribute names for GenAI workloads — gen_ai.system, gen_ai.request.model, gen_ai.response.model, gen_ai.usage.input_tokens, gen_ai.usage.output_tokens, llm.prompts, llm.completio
  name: OpenLLMetry Semantic Conventions for AI
  slug: openllmetry-semantic-conventions-ai
- description: Drop-in OpenTelemetry instrumentations for the major LLM providers including OpenAI, Anthropic, AWS Bedrock, Google Generative AI / Vertex AI, Cohere, Mistral AI, Ollama, Groq, Together AI, Replicate,
  name: OpenLLMetry LLM Provider Instrumentations
  slug: openllmetry-llm-instrumentations
- description: 'Instrumentations for vector databases used in retrieval-augmented generation pipelines — Chroma, Pinecone, Qdrant, Weaviate, LanceDB, Milvus, and Marqo. Captures query, upsert, and similarity- search '
  name: OpenLLMetry Vector Database Instrumentations
  slug: openllmetry-vector-db-instrumentations
- description: 'Instrumentations for higher-level LLM frameworks and agent runtimes — LangChain, LlamaIndex, Haystack, CrewAI, Agno, OpenAI Agents, and Model Context Protocol (MCP). Captures chain, retriever, agent, '
  name: OpenLLMetry Framework and Agent Instrumentations
  slug: openllmetry-framework-instrumentations
- description: OpenLLMetry emits standard OpenTelemetry traces and metrics over OTLP (gRPC or HTTP), so any OpenTelemetry-compatible backend can receive its telemetry. Supported destinations include Datadog, Grafana
  name: OpenLLMetry OTLP Exporters
  slug: openllmetry-otlp-exporters
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/traceloop/openllmetry/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/traceloop/openllmetry/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/traceloop/openllmetry/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/traceloop/openllmetry/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/traceloop/openllmetry/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openllmetry-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.traceloop.com/openllmetry
- group: docs
  title: ''
  type: Documentation
  url: https://www.traceloop.com/docs/openllmetry/introduction
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/traceloop/openllmetry
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/traceloop/openllmetry-js
- group: commercial
  title: ''
  type: License
  url: https://github.com/traceloop/openllmetry/blob/main/LICENSE
- group: other
  title: ''
  type: Maintainer
  url: https://www.traceloop.com/
- group: operate
  title: ''
  type: Discord
  url: https://traceloop.com/slack
- group: company
  title: ''
  type: Blog
  url: https://www.traceloop.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.traceloop.com/docs/openllmetry/quick-start/python
- group: design
  title: ''
  type: SemanticConventions
  url: https://opentelemetry.io/docs/specs/semconv/gen-ai/
created: '2026-05-25'
description: OpenLLMetry is an open-source observability framework for LLM and generative AI applications, built on top of OpenTelemetry. Maintained by Traceloop under the Apache 2.0 license, it provides drop-in instrumentation for 30+ LLM providers, vector databases, and agent frameworks, and emits standardized GenAI traces over OTLP to any observability backend (Datadog, Grafana, Honeycomb, New Relic, Splunk, Langfuse, LangSmith, Braintrust, and the Traceloop platform). Its semantic conventions for LLMs have been upstreamed into the OpenTelemetry GenAI semantic conventions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openllmetry.png
layout: provider
modified: '2026-05-25'
name: OpenLLMetry
nav: Providers
network: true
overview: 'OpenLLMetry publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, Observability, Open-Source, and OpenTelemetry.


  OpenLLMetry''s developer surface includes documentation, engineering blog, getting-started guide, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openllmetry/refs/heads/main/screenshots/openllmetry-2026-06-20T191014.png
security:
- kind: domain-security
  name: Openllmetry Domain Security
  slug: openllmetry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: openllmetry
tags:
- Artificial Intelligence
- LLM
- Observability
- Open-Source
- OpenTelemetry
- Tracing
- GenAI
website: https://www.traceloop.com/openllmetry
---
