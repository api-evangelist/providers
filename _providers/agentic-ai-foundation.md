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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Model Context Protocol (MCP) is an open-source standard for connecting AI applications to external systems including data sources, tools, and workflows. Originally developed by Anthropic and donat
  name: Model Context Protocol (MCP)
  slug: model-context-protocol
- description: Goose is a general-purpose, open-source AI agent that runs locally on your machine. Originally from Block and now under AAIF governance, goose supports 15+ LLM providers, 70+ MCP extensions, and provi
  name: Goose AI Agent
  slug: goose
artifact_total: 29
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/modelcontextprotocol/specification/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/modelcontextprotocol/specification/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentic-ai-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agentic-ai-foundation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentic-ai-foundation
- group: start
  title: ''
  type: Portal
  url: https://lfaidata.foundation/
- group: docs
  title: ''
  type: Documentation
  url: https://modelcontextprotocol.io/introduction
created: '2026-03-16'
description: The Agentic AI Foundation (AAIF) is a Linux Foundation project formed in December 2025 that brings together critical open standards and projects for AI agents under neutral governance. It hosts Anthropic's Model Context Protocol (MCP), Block's goose AI agent, and OpenAI's AGENTS.md to enable interoperable, open AI agent ecosystems. The foundation drives standardization of agent communication protocols, tool interfaces, and cross-platform agent portability.
examples:
- key_count: 5
  name: Agentic Ai Foundation Mcp Resource Example
  slug: agentic-ai-foundation-mcp-resource-example
- key_count: 4
  name: Agentic Ai Foundation Mcp Tool Example
  slug: agentic-ai-foundation-mcp-tool-example
features:
- description: All AAIF projects operate under Linux Foundation neutral governance, ensuring no single vendor controls the direction of AI agent standards.
  name: Neutral Open Governance
- description: MCP is a universal adapter standard enabling AI agents to connect to any external tool, data source, or workflow through a consistent protocol.
  name: Model Context Protocol (MCP)
- description: AAIF standards enable AI agents to run consistently across different platforms, environments, and LLM providers without vendor lock-in.
  name: Cross-Platform Agent Portability
- description: The MCP standard enables a rich ecosystem of 70+ tools and extensions that any compliant agent can discover and invoke.
  name: Tool and Extension Ecosystem
- description: AAIF projects support 15+ LLM providers including Anthropic, OpenAI, Google, Azure, and Ollama through standardized provider interfaces.
  name: Multi-LLM Provider Support
- description: The Agent Communication Protocol (ACP) enables agents to authenticate and communicate with each other and LLM providers through open standards.
  name: Open Agent Communication
finops:
- name: Agentic Ai Foundation Finops
  service_category: API
  slug: agentic-ai-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/agentic-ai-foundation.png
integrations:
- description: Native MCP support via the Anthropic Messages API, the originating implementation of the MCP standard.
  name: Claude (Anthropic)
- description: MCP tool integration via the OpenAI Responses API, enabling ChatGPT to invoke MCP-compatible tools.
  name: ChatGPT (OpenAI)
- description: GitHub Copilot in VS Code supports MCP servers for AI-assisted development through the AAIF MCP standard.
  name: VS Code
- description: Cursor IDE integrates MCP tool support for AI-assisted coding agents.
  name: Cursor
- description: AAIF operates under Linux Foundation governance alongside related projects in the LF AI & Data portfolio.
  name: Linux Foundation
json_schemas:
- name: MCPResource
  property_count: 5
  slug: agentic-ai-foundation-mcp-resource
- name: MCPTool
  property_count: 4
  slug: agentic-ai-foundation-mcp-tool
json_structures:
- name: Agentic Ai Foundation Mcp Resource Structure
  property_count: 5
  slug: agentic-ai-foundation-mcp-resource-structure
- name: Agentic Ai Foundation Mcp Tool Structure
  property_count: 4
  slug: agentic-ai-foundation-mcp-tool-structure
jsonld:
- class_count: 5
  name: Agentic Ai Foundation Context
  property_count: 7
  slug: agentic-ai-foundation-context
layout: provider
modified: '2026-04-19'
name: Agentic AI Foundation
nav: Providers
network: true
overview: 'Agentic AI Foundation publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Linux Foundation, Open Source, Standards, and MCP.


  The Agentic AI Foundation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agentic AI Foundation''s developer surface includes developer portal, documentation, and 8 more developer resources.'
plans:
- name: Agentic Ai Foundation Plans Pricing
  plan_count: 3
  slug: agentic-ai-foundation-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Agentic Ai Foundation Rate Limits
  slug: agentic-ai-foundation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Agentic AI Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: agentic-ai-foundation-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.7
  delta: -6.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 11.3
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 36.8
  previous_composite: 27.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/agentic-ai-foundation/refs/heads/main/screenshots/agentic-ai-foundation-2026-06-20T170026.png
security:
- kind: domain-security
  name: Agentic Ai Foundation Domain Security
  slug: agentic-ai-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agentic-ai-foundation
tags:
- AI Agents
- Linux Foundation
- Open Source
- Standards
- MCP
- Agentic AI
- Interoperability
use_cases:
- description: Build MCP-compatible tools once and make them available to any AI agent or client that supports the MCP standard, eliminating integration silos.
  name: Interoperable AI Tool Development
- description: Organizations adopt AAIF standards to ensure their AI agent infrastructure is portable, auditable, and not locked to a single AI vendor.
  name: Enterprise Agent Standardization
- description: Use AAIF protocols to connect specialized AI agents that collaborate on complex tasks, each contributing domain-specific capabilities.
  name: Multi-Agent Workflow Orchestration
- description: Developers build and extend open-source AI agents like goose using the AAIF ecosystem of standards and extensions.
  name: Open-Source Agent Development
website: https://lfaidata.foundation/
---
