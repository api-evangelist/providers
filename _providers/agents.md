---
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering AI agents, agent frameworks, and agent runtimes that enable autonomous reasoning, tool use, and multi-step task execution. This profile catalogs the platforms and open-source projects that let developers build, orchestrate, and deploy LLM-powered agents, including foundational frameworks like LangChain, LangGraph, CrewAI, AutoGen, and AutoGPT, hosted agent platforms like Lindy, Relevance AI, and Composio, and provider-native agent runtimes from OpenAI, Anthropic, Google, and Microsoft. Distinct from foundation models and from Agent Skills (capability packages), the Agents topic focuses on the orchestration layer where planning, memory, tool calling, and execution come together.
examples:
- key_count: 10
  name: Agents Agent Definition Example
  slug: agents-agent-definition-example
- key_count: 11
  name: Agents Agent Run Example
  slug: agents-agent-run-example
features:
- description: Agent frameworks like LangGraph, AutoGen, and CrewAI provide structured loops for planning, reflection, and multi-step reasoning over user goals, breaking complex tasks into ordered sub-tasks.
  name: Planning and Reasoning Loops
- description: Agents invoke external functions, APIs, and aggregated tool catalogs through provider-native tool calling, expanding their reach beyond text generation into real-world action.
  name: Tool Calling and Function Use
- description: Frameworks like Letta and LangGraph provide persistent memory, conversation state, and long-running execution context so agents can resume work, remember users, and accumulate knowledge over time.
  name: Memory and State Management
- description: CrewAI, AutoGen, and LangGraph enable multiple specialized agents to collaborate, delegate sub-tasks, and reach consensus, modeling teams of role-based workers around a shared goal.
  name: Multi-Agent Orchestration
- description: OpenAI Assistants, Anthropic Claude tool use, Google ADK, Amazon Bedrock Agents, and Microsoft Azure AI Foundry expose first-party agent runtimes that handle planning, tool invocation, and state on the model provider side.
  name: Provider-Native Agent Runtimes
- description: Agents like AgentQL and browser-driving frameworks let LLMs navigate real web pages, fill forms, and extract structured data, extending agent reach to systems that lack APIs.
  name: Browser and Web Agents
- description: Platforms like Portkey, TrueFoundry, and Bifrost provide tracing, evaluation, cost tracking, and gateway routing across agent runs to make agent behavior observable and debuggable.
  name: Observability and Evaluation
- description: The Linux Foundation Agentic AI Foundation and projects like kagent and AgentGateway are establishing open standards for agent-to-agent communication, identity, and runtime portability.
  name: Open Governance and Interoperability
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: The most widely used open-source framework for building LLM applications, including chains, agents, retrieval, memory, and tool calling across dozens of providers.
  name: LangChain
- description: A graph-based runtime from LangChain for stateful, multi-actor, long-running agent workflows with checkpointing and human-in-the-loop.
  name: LangGraph
- description: Multi-agent framework for orchestrating role-based agent crews that collaborate on complex tasks.
  name: CrewAI
- description: Microsoft's open-source framework for building multi-agent conversations with planner, executor, and critic roles.
  name: AutoGen
- description: Agent execution platform exposing 1000+ apps as governed tools for any agent framework or model.
  name: Composio
- description: Stateful agent platform (formerly MemGPT) focused on long-term memory and persistent agent identity.
  name: Letta
- description: OpenAI's hosted agent runtime with built-in tool use, retrieval, code interpreter, and threads.
  name: OpenAI Assistants
- description: AWS's managed agent runtime over foundation models with action groups, knowledge bases, and guardrails.
  name: Amazon Bedrock Agents
json_schemas:
- name: AgentDefinition
  property_count: 10
  slug: agents-agent-definition
- name: AgentRun
  property_count: 11
  slug: agents-agent-run
json_structures:
- name: Agents Agent Definition Structure
  property_count: 10
  slug: agents-agent-definition-structure
- name: Agents Agent Run Structure
  property_count: 11
  slug: agents-agent-run-structure
jsonld:
- class_count: 8
  name: Agents Context
  property_count: 20
  slug: agents-context
layout: provider
modified: '2026-05-19'
name: Agents
nav: Providers
network: true
overview: 'Agents is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Agent Frameworks, Agent Orchestration, Agent Runtimes, and LLM Orchestration.


  The Agents catalog on APIs.io includes 1 JSON-LD context.


  Agents'' developer surface includes developer portal and 1 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: agents
tags:
- AI Agents
- Agent Frameworks
- Agent Orchestration
- Agent Runtimes
- LLM Orchestration
use_cases:
- description: Hosted agent platforms like Lindy, Relevance AI, and Microsoft Power Virtual Agents handle inbound support tickets, route conversations, and resolve common requests end-to-end.
  name: Customer Support Automation
- description: LangChain and LlamaIndex agents combine retrieval over enterprise documents with reasoning to answer complex questions and synthesize multi-source briefings.
  name: Research and Knowledge Work
- description: Agents built on Lindy, Relevance AI, and Composio prospect leads, draft outreach, log CRM activity, and orchestrate multi-step sales sequences.
  name: Sales and Outbound Workflows
- description: AutoGPT, AutoGen, and CrewAI-based engineering agents read repositories, draft pull requests, run tests, and iterate on code under human review.
  name: Software Engineering Agents
- description: LiveKit and similar runtimes power real-time voice agents that handle phone calls, meetings, and live conversations using streaming LLMs and tool calling.
  name: Voice and Telephony Agents
- description: Agentic platforms like Restack, Trigger.dev, and Stackmint orchestrate long-running internal workflows across SaaS, databases, and identity systems.
  name: Internal Operations and IT Automation
- description: CrewAI and AutoGen model role-based teams (researcher, writer, reviewer) collaborating on a single deliverable, producing higher-quality output than a single agent.
  name: Multi-Agent Team Simulations
website: https://apievangelist.com
---
