---
aid: agentic-ai-foundation
name: Agentic AI Foundation
description: The Agentic AI Foundation (AAIF) is a Linux Foundation project formed in December 2025 that brings together critical open standards and projects for AI agents under neutral governance. It hosts Anthropic's Model Context Protocol (MCP), Block's goose AI agent, and OpenAI's AGENTS.md to enable interoperable, open AI agent ecosystems. The foundation drives standardization of agent communication protocols, tool interfaces, and cross-platform agent portability.
url: https://raw.githubusercontent.com/api-evangelist/agentic-ai-foundation/refs/heads/main/apis.yml
humanURL: https://lfaidata.foundation/
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - Linux Foundation
  - Open Source
  - Standards
  - MCP
  - Agentic AI
  - Interoperability
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agentic-ai-foundation:model-context-protocol
    name: Model Context Protocol (MCP)
    description: The Model Context Protocol (MCP) is an open-source standard for connecting AI applications to external systems including data sources, tools, and workflows. Originally developed by Anthropic and donated to the Agentic AI Foundation, MCP enables agents to discover and invoke tools, access resources, and use reusable prompt templates through a standardized protocol.
    humanURL: https://modelcontextprotocol.io/introduction
    tags:
      - MCP
      - Model Context Protocol
      - Open Standard
      - Tool Use
      - AI Agents
    properties:
      - type: Documentation
        url: https://modelcontextprotocol.io/introduction
      - type: GettingStarted
        url: https://modelcontextprotocol.io/docs/develop/build-server
      - type: GitHubRepository
        url: https://github.com/modelcontextprotocol/specification
  - aid: agentic-ai-foundation:goose
    name: Goose AI Agent
    description: Goose is a general-purpose, open-source AI agent that runs locally on your machine. Originally from Block and now under AAIF governance, goose supports 15+ LLM providers, 70+ MCP extensions, and provides a native desktop app, CLI, and API. Built in Rust for cross-platform portability across macOS, Linux, and Windows.
    humanURL: https://github.com/block/goose
    tags:
      - AI Agent
      - Open Source
      - MCP
      - CLI
      - Desktop App
      - Rust
    properties:
      - type: Documentation
        url: https://block.github.io/goose/
      - type: GitHubRepository
        url: https://github.com/block/goose
common:
  - type: GitHubOrganization
    url: https://github.com/agentic-ai-foundation
  - type: Portal
    url: https://lfaidata.foundation/
  - type: Documentation
    url: https://modelcontextprotocol.io/introduction
  - type: Features
    data:
      - name: Neutral Open Governance
        description: All AAIF projects operate under Linux Foundation neutral governance, ensuring no single vendor controls the direction of AI agent standards.
      - name: Model Context Protocol (MCP)
        description: MCP is a universal adapter standard enabling AI agents to connect to any external tool, data source, or workflow through a consistent protocol.
      - name: Cross-Platform Agent Portability
        description: AAIF standards enable AI agents to run consistently across different platforms, environments, and LLM providers without vendor lock-in.
      - name: Tool and Extension Ecosystem
        description: The MCP standard enables a rich ecosystem of 70+ tools and extensions that any compliant agent can discover and invoke.
      - name: Multi-LLM Provider Support
        description: AAIF projects support 15+ LLM providers including Anthropic, OpenAI, Google, Azure, and Ollama through standardized provider interfaces.
      - name: Open Agent Communication
        description: The Agent Communication Protocol (ACP) enables agents to authenticate and communicate with each other and LLM providers through open standards.
  - type: UseCases
    data:
      - name: Interoperable AI Tool Development
        description: Build MCP-compatible tools once and make them available to any AI agent or client that supports the MCP standard, eliminating integration silos.
      - name: Enterprise Agent Standardization
        description: Organizations adopt AAIF standards to ensure their AI agent infrastructure is portable, auditable, and not locked to a single AI vendor.
      - name: Multi-Agent Workflow Orchestration
        description: Use AAIF protocols to connect specialized AI agents that collaborate on complex tasks, each contributing domain-specific capabilities.
      - name: Open-Source Agent Development
        description: Developers build and extend open-source AI agents like goose using the AAIF ecosystem of standards and extensions.
  - type: Integrations
    data:
      - name: Claude (Anthropic)
        description: Native MCP support via the Anthropic Messages API, the originating implementation of the MCP standard.
      - name: ChatGPT (OpenAI)
        description: MCP tool integration via the OpenAI Responses API, enabling ChatGPT to invoke MCP-compatible tools.
      - name: VS Code
        description: GitHub Copilot in VS Code supports MCP servers for AI-assisted development through the AAIF MCP standard.
      - name: Cursor
        description: Cursor IDE integrates MCP tool support for AI-assisted coding agents.
      - name: Linux Foundation
        description: AAIF operates under Linux Foundation governance alongside related projects in the LF AI & Data portfolio.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
