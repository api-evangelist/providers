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
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: The Anthropic Tool Use API allows AI agents built on Claude to call client-defined functions or Anthropic-provided server tools such as web search, code execution, and web fetch. Tools are declared in
  name: Anthropic Tool Use API
  slug: anthropic-tool-use-api
- description: 'Google''s Agent Development Kit (ADK) is a flexible framework for building AI agents and multi-agent systems. It supports LLM agents, workflow agents, and custom agents with capabilities including MCP '
  name: Google Agent Development Kit (ADK)
  slug: google-agent-development-kit-adk
- description: The Model Context Protocol (MCP) is an open-source standard for connecting AI applications to external systems. MCP defines a standardized way for AI agents to access data sources, tools, and workflow
  name: Model Context Protocol (MCP)
  slug: model-context-protocol-mcp
artifact_total: 40
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/google/adk-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/google/adk-python/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/google/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/google/adk-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/google/adk-python/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agent-skills-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
- group: docs
  title: Tool Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-schema.json
- group: docs
  title: Tool Call Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-call-schema.json
- group: docs
  title: Tool Result Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-result-schema.json
- group: docs
  title: MCP Server Schema
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-mcp-server-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-ld/agent-skills-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/vocabulary/agent-skills-vocabulary.yaml
created: '2025-01-01'
description: A collection of resources, APIs, and standards related to AI agent skills and capabilities. Agent skills represent the tools, functions, and capabilities that AI agents can invoke to accomplish tasks — spanning web search, code execution, file management, memory, and external API integrations. This topic covers the major platforms and frameworks that define how agent skills are declared, discovered, and invoked.
examples:
- key_count: 6
  name: Agent Skills Mcp Server Example
  slug: agent-skills-mcp-server-example
- key_count: 4
  name: Agent Skills Tool Call Example
  slug: agent-skills-tool-call-example
- key_count: 5
  name: Agent Skills Tool Example
  slug: agent-skills-tool-example
- key_count: 4
  name: Agent Skills Tool Result Example
  slug: agent-skills-tool-result-example
features:
- description: AI agents can invoke user-defined or platform-provided functions based on natural language instructions, with structured input/output schemas.
  name: Function Calling
- description: Platforms like Anthropic and OpenAI run certain agent skills (web search, code execution) on their own infrastructure, removing the need for client-side execution.
  name: Server-Side Tool Execution
- description: The Model Context Protocol provides a universal adapter layer enabling agents to discover and call any MCP-compatible server as a skill.
  name: MCP Integration
- description: Frameworks like Google ADK support coordinating multiple specialized agents, with skills delegated across agent boundaries via protocols like A2A.
  name: Multi-Agent Orchestration
- description: Agent skill definitions can enforce strict JSON Schema compliance to ensure agents produce well-formed tool calls matching the declared parameter schema.
  name: Strict Schema Enforcement
- description: Anthropic's tool_search server tool enables agents to discover available tools at runtime without statically declaring all tool schemas upfront.
  name: Tool Discovery
finops:
- name: Agent Skills Finops
  service_category: API
  slug: agent-skills-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agent-skills.png
integrations:
- description: Native support for tool use and MCP via the Anthropic Messages API.
  name: Claude (Anthropic)
- description: Function calling and MCP tool integration via the OpenAI Responses API.
  name: ChatGPT (OpenAI)
- description: Tool use and ADK integration for Gemini-based agents.
  name: Gemini (Google)
- description: GitHub Copilot supports MCP servers as agent skill providers within the VS Code development environment.
  name: VS Code Copilot
- description: Cursor IDE supports MCP tool integration for AI-assisted coding agents.
  name: Cursor
- description: Open-source framework for composing agent skills into chains and graphs across multiple LLM providers.
  name: LangChain
- description: Data framework enabling agents to index and retrieve from external data sources as structured skills.
  name: LlamaIndex
json_schemas:
- name: MCPServer
  property_count: 6
  slug: agent-skills-mcp-server
- name: ToolCall
  property_count: 4
  slug: agent-skills-tool-call
- name: ToolResult
  property_count: 4
  slug: agent-skills-tool-result
- name: Tool
  property_count: 5
  slug: agent-skills-tool
json_structures:
- name: Agent Skills Mcp Server Structure
  property_count: 6
  slug: agent-skills-mcp-server-structure
- name: Agent Skills Tool Call Structure
  property_count: 4
  slug: agent-skills-tool-call-structure
- name: Agent Skills Tool Result Structure
  property_count: 4
  slug: agent-skills-tool-result-structure
- name: Agent Skills Tool Structure
  property_count: 5
  slug: agent-skills-tool-structure
jsonld:
- class_count: 7
  name: Agent Skills Context
  property_count: 16
  slug: agent-skills-context
layout: provider
modified: '2026-04-19'
name: Agent Skills
nav: Providers
network: true
overview: 'Agent Skills publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agent Skills, AI Agents, Tool Use, Function Calling, and MCP.


  The Agent Skills catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Agent Skills Plans Pricing
  plan_count: 3
  slug: agent-skills-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Agent Skills Rate Limits
  slug: agent-skills-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agent Skills API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: agent-skills-jsonschema-spectral-rules
score:
  band: thin
  composite: 30.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 68.3
    catalog_earned_first_party: 0.0
    catalog_gap: 46.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 14.7
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 30.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/screenshots/agent-skills-2026-06-20T165939.png
security:
- kind: domain-security
  name: Agent Skills Domain Security
  slug: agent-skills-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agent-skills
tags:
- Agent Skills
- AI Agents
- Tool Use
- Function Calling
- MCP
- Agentic AI
- Automation
use_cases:
- description: Agents use web search and fetch skills to retrieve, synthesize, and summarize information from the internet in response to user queries.
  name: Automated Research
- description: Agents invoke code execution skills to write, run, and debug code within sandboxed environments, returning results to the user.
  name: Code Generation and Execution
- description: Agents use OpenAPI-backed skills to read and write data across enterprise systems — CRMs, ERPs, databases — through standardized API calls.
  name: Data Integration
- description: Agents invoke file system skills to read, write, and organize documents, images, and structured data on behalf of users.
  name: File and Document Management
- description: Agents chain multiple skills in sequence — searching, retrieving, transforming, and storing data — to complete complex multi-step tasks autonomously.
  name: Multi-Step Workflow Automation
- description: Customer service agents use CRM lookup, ticketing, and knowledge base skills to resolve customer issues without human escalation.
  name: AI-Assisted Customer Support
---
