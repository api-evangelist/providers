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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The AgentOps Python SDK is the primary entry point, installable via pip install agentops and initialized with two lines of code. It auto-instruments supported agent frameworks and LLM providers, suppo
  name: AgentOps Python SDK
  slug: agentops-python-sdk
- description: AgentOps' TypeScript SDK provides instrumentation for the OpenAI Agents SDK in Node.js applications, surfacing the same traces and metrics as the Python SDK inside the AgentOps dashboard.
  name: AgentOps TypeScript SDK
  slug: agentops-typescript-sdk
- description: The hosted dashboard at app.agentops.ai visualizes agent sessions with waterfall views, time-travel replay, LLM cost tracking, and multi-agent interaction graphs. Supports session export and team coll
  name: AgentOps Dashboard
  slug: agentops-dashboard
artifact_total: 35
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/AgentOps-AI/agentops/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/AgentOps-AI/agentops/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/AgentOps-AI/agentops/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/AgentOps-AI/agentops/blob/main/.github/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentops-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentops.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentops.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.agentops.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agentops.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.agentops.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgentOps-AI
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AgentOps-AI/agentops
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentops-ai/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/FagdcwwXRR
- group: learn
  title: ''
  type: Courses
  url: https://agentops.ai/courses
- group: commercial
  title: ''
  type: License
  url: https://github.com/AgentOps-AI/agentops/blob/main/LICENSE
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.agentops.ai/llms.txt
created: '2026-05-23'
description: AgentOps is an observability, evaluation, and debugging platform for AI agents. Its open-source Python SDK (with TypeScript support for OpenAI Agents) instruments agent runs in two lines of code, capturing LLM calls, tool invocations, costs, latencies, and multi-agent interactions. Sessions are visualized in a hosted dashboard at app.agentops.ai with time-travel debugging, waterfall views, and replay. AgentOps offers native integrations with 400+ LLMs and frameworks including CrewAI, AutoGen / AG2, LangChain, LangGraph, LlamaIndex, OpenAI Agents, Haystack, and Camel AI.
features:
- description: Initialize observability with agentops.init() and automatic framework instrumentation.
  name: Two-Line Instrumentation
- description: Time-travel debugging with full session and event replay in the dashboard.
  name: Session Replay
- description: Token counting and cost tracking across foundation model providers and agents.
  name: LLM Cost Tracking
- description: Visualize interactions between agents in CrewAI, AutoGen, LangGraph, and custom systems.
  name: Multi-Agent Visualization
- description: Time-based waterfall views of all events in a session.
  name: Waterfall Traces
- description: Use the @trace decorator and OTel-aligned spans to instrument custom code paths.
  name: Custom Traces
- description: Self-hosted deployment available on Enterprise plans.
  name: Self-Hosting
- description: Enterprise compliance with SOC 2 and HIPAA available on the Enterprise tier.
  name: SOC 2 / HIPAA
finops:
- name: Agentops Finops
  service_category: API
  slug: agentops-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentops.png
integrations:
- description: Native instrumentation for OpenAI Chat Completions and Responses APIs.
  name: OpenAI
- description: First-class support for OpenAI Agents in Python and TypeScript.
  name: OpenAI Agents SDK
- description: Instrumentation for Anthropic Claude models.
  name: Anthropic
- description: Native CrewAI integration with multi-agent visualization.
  name: CrewAI
- description: Native integration with AG2, formerly AutoGen.
  name: AG2 (AutoGen)
- description: Instrumentation for LangChain chains and agents.
  name: LangChain
- description: Trace and visualize LangGraph stateful agents.
  name: LangGraph
- description: Trace LlamaIndex RAG and agent applications.
  name: LlamaIndex
- description: Instrumentation for Haystack pipelines.
  name: Haystack
- description: Native integration with Camel AI multi-agent system.
  name: Camel AI
- description: Instrumentation for Cohere model calls.
  name: Cohere
- description: Capture calls routed through LiteLLM across providers.
  name: LiteLLM
- description: Instrumentation for Mistral models.
  name: Mistral
- description: Instrumentation for Gemini and Vertex AI.
  name: Google Generative AI
- description: Instrumentation for xAI Grok models.
  name: xAI
layout: provider
modified: '2026-05-23'
name: AgentOps
nav: Providers
network: true
overview: 'AgentOps publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Observability, Evaluation, Tracing, and Python SDK.


  AgentOps'' developer surface includes documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Agentops Plans Pricing
  plan_count: 1
  slug: agentops-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Agentops Rate Limits
  slug: agentops-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 1.4
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 22.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentops/refs/heads/main/screenshots/agentops-2026-06-20T170038.png
security:
- kind: domain-security
  name: Agentops Domain Security
  slug: agentops-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentops
tags:
- AI Agents
- Observability
- Evaluation
- Tracing
- Python SDK
- Open-Source
- Agent Frameworks
use_cases:
- description: Inspect multi-step agent runs, tool calls, and intermediate reasoning to find failures.
  name: Agent Debugging
- description: Track token usage and cost per agent, framework, and provider.
  name: Cost Monitoring
- description: Evaluate agent performance across sessions and compare versions.
  name: Agent Evaluation
- description: Monitor production agents with dashboards, alerts, and exports.
  name: Production Observability
- description: Visualize and debug coordination between agents in multi-agent frameworks.
  name: Multi-Agent Systems
website: https://www.agentops.ai/
---
