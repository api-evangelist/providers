---
name: Agent Skills
description: A collection of resources, APIs, and standards related to AI agent skills and capabilities. Agent skills represent the tools, functions, and capabilities that AI agents can invoke to accomplish tasks — spanning web search, code execution, file management, memory, and external API integrations. This topic covers the major platforms and frameworks that define how agent skills are declared, discovered, and invoked.
url: https://github.com/api-evangelist/agent-skills
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.18'
tags:
  - Agent Skills
  - AI Agents
  - Tool Use
  - Function Calling
  - MCP
  - Agentic AI
  - Automation
apis:
  - name: Anthropic Tool Use API
    description: The Anthropic Tool Use API allows AI agents built on Claude to call client-defined functions or Anthropic-provided server tools such as web search, code execution, and web fetch. Tools are declared in the API request and Claude decides when to invoke them based on context. Server tools run on Anthropic infrastructure while client tools execute in the calling application.
    humanURL: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview
    baseURL: https://api.anthropic.com
    tags:
      - Anthropic
      - Tool Use
      - Function Calling
      - Claude
      - AI Agents
    properties:
      - type: Documentation
        url: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/overview
      - type: APIReference
        url: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/tool-reference
      - type: GettingStarted
        url: https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/build-a-tool-using-agent
  - name: Google Agent Development Kit (ADK)
    description: Google's Agent Development Kit (ADK) is a flexible framework for building AI agents and multi-agent systems. It supports LLM agents, workflow agents, and custom agents with capabilities including MCP tool integration, OpenAPI tools, function tools, grounding via Google Search, streaming via Gemini Live API, and Agent-to-Agent (A2A) protocol for inter-agent communication. Available in Python, TypeScript, Go, and Java.
    humanURL: https://adk.dev/
    baseURL: https://adk.dev
    tags:
      - Google
      - Agent Development Kit
      - ADK
      - Multi-Agent
      - Gemini
      - Tool Use
    properties:
      - type: Documentation
        url: https://adk.dev/
      - type: GettingStarted
        url: https://adk.dev/get-started
      - type: GitHubRepository
        url: https://github.com/google/adk-python
  - name: Model Context Protocol (MCP)
    description: The Model Context Protocol (MCP) is an open-source standard for connecting AI applications to external systems. MCP defines a standardized way for AI agents to access data sources, tools, and workflows. It enables agents to call external tools, access files, databases, and APIs through a consistent protocol supported by Claude, ChatGPT, VS Code, Cursor, and many other AI clients.
    humanURL: https://modelcontextprotocol.io/introduction
    baseURL: https://modelcontextprotocol.io
    tags:
      - MCP
      - Model Context Protocol
      - Standards
      - Tool Use
      - Open Source
    properties:
      - type: Documentation
        url: https://modelcontextprotocol.io/introduction
      - type: GettingStarted
        url: https://modelcontextprotocol.io/docs/develop/build-server
      - type: GitHubRepository
        url: https://github.com/modelcontextprotocol/specification
common:
  - type: GitHubOrganization
    url: https://github.com/api-evangelist
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-schema.json
    title: Tool Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-call-schema.json
    title: Tool Call Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-tool-result-schema.json
    title: Tool Result Schema
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-schema/agent-skills-mcp-server-schema.json
    title: MCP Server Schema
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/json-ld/agent-skills-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/agent-skills/refs/heads/main/vocabulary/agent-skills-vocabulary.yaml
  - type: Features
    data:
      - name: Function Calling
        description: AI agents can invoke user-defined or platform-provided functions based on natural language instructions, with structured input/output schemas.
      - name: Server-Side Tool Execution
        description: Platforms like Anthropic and OpenAI run certain agent skills (web search, code execution) on their own infrastructure, removing the need for client-side execution.
      - name: MCP Integration
        description: The Model Context Protocol provides a universal adapter layer enabling agents to discover and call any MCP-compatible server as a skill.
      - name: Multi-Agent Orchestration
        description: Frameworks like Google ADK support coordinating multiple specialized agents, with skills delegated across agent boundaries via protocols like A2A.
      - name: Strict Schema Enforcement
        description: Agent skill definitions can enforce strict JSON Schema compliance to ensure agents produce well-formed tool calls matching the declared parameter schema.
      - name: Tool Discovery
        description: Anthropic's tool_search server tool enables agents to discover available tools at runtime without statically declaring all tool schemas upfront.
  - type: UseCases
    data:
      - name: Automated Research
        description: Agents use web search and fetch skills to retrieve, synthesize, and summarize information from the internet in response to user queries.
      - name: Code Generation and Execution
        description: Agents invoke code execution skills to write, run, and debug code within sandboxed environments, returning results to the user.
      - name: Data Integration
        description: Agents use OpenAPI-backed skills to read and write data across enterprise systems — CRMs, ERPs, databases — through standardized API calls.
      - name: File and Document Management
        description: Agents invoke file system skills to read, write, and organize documents, images, and structured data on behalf of users.
      - name: Multi-Step Workflow Automation
        description: Agents chain multiple skills in sequence — searching, retrieving, transforming, and storing data — to complete complex multi-step tasks autonomously.
      - name: AI-Assisted Customer Support
        description: Customer service agents use CRM lookup, ticketing, and knowledge base skills to resolve customer issues without human escalation.
  - type: Integrations
    data:
      - name: Claude (Anthropic)
        description: Native support for tool use and MCP via the Anthropic Messages API.
      - name: ChatGPT (OpenAI)
        description: Function calling and MCP tool integration via the OpenAI Responses API.
      - name: Gemini (Google)
        description: Tool use and ADK integration for Gemini-based agents.
      - name: VS Code Copilot
        description: GitHub Copilot supports MCP servers as agent skill providers within the VS Code development environment.
      - name: Cursor
        description: Cursor IDE supports MCP tool integration for AI-assisted coding agents.
      - name: LangChain
        description: Open-source framework for composing agent skills into chains and graphs across multiple LLM providers.
      - name: LlamaIndex
        description: Data framework enabling agents to index and retrieve from external data sources as structured skills.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
