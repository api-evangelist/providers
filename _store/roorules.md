---
aid: roorules
name: .Roorules
description: .roorules is a configuration file convention for Roo Code, an open-source AI-powered autonomous coding assistant built for VS Code. The .roorules file allows developers to define project-specific coding conventions, style rules, architecture guidelines, and behavioral instructions that guide Roo Code AI agents when working within a codebase. Roo Code supports multiple AI providers including Anthropic Claude, OpenAI GPT-4, Google Gemini, and local LLMs via OpenAI-compatible APIs.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/roorules/refs/heads/main/apis.yml
tags:
  - AI Agents
  - AI Copilot
  - Coding Assistant
  - Coding Standards
  - Developer Workflow
  - LLM
  - MCP
  - Roo Code
  - VS Code
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: roorules:roo-code-extension-api
    name: Roo Code VS Code Extension
    description: Roo Code is an AI-powered autonomous coding agent for VS Code that reads and writes code across multiple files, executes terminal commands, manages browser interactions, and adapts to custom modes defined through .roorules and .roomodes configuration files. It supports API configuration profiles enabling switching between different AI providers and models per workflow.
    humanURL: https://roocode.com/
    properties:
      - type: Documentation
        url: https://docs.roocode.com/
      - type: GitHub
        url: https://github.com/RooCodeInc/Roo-Code
      - type: Vocabulary
        url: vocabulary/roorules-vocabulary.yml
      - type: JSONSchema
        url: json-schema/roorules-config-schema.json
      - type: JSONStructure
        url: json-structure/roorules-config-structure.json
    tags:
      - AI Agents
      - AI Copilot
      - Coding Assistant
      - Developer Workflow
      - VS Code
  - aid: roorules:roo-code-mcp-integration
    name: Roo Code MCP Integration
    description: Roo Code supports the Model Context Protocol (MCP), allowing it to connect to external MCP servers for extended tool access including file systems, databases, APIs, and cloud services. MCP servers are configured in the Roo Code settings and expose tools that AI agents can use during coding workflows.
    humanURL: https://docs.roocode.com/features/mcp/
    properties:
      - type: Documentation
        url: https://docs.roocode.com/features/mcp/
    tags:
      - AI Agents
      - Integration
      - MCP
      - Model Context Protocol
  - aid: roorules:roo-code-api-configuration
    name: Roo Code API Configuration Profiles
    description: API Configuration Profiles allow Roo Code users to create and switch between different sets of AI provider settings. Each profile configures a specific model and provider (e.g., Claude 3.7 Sonnet on Anthropic, GPT-4o on OpenAI, Gemini Pro on Google) and can be mapped to specific Roo Code modes (Architect, Code, Debug, Ask).
    humanURL: https://docs.roocode.com/features/api-configuration-profiles
    properties:
      - type: Documentation
        url: https://docs.roocode.com/features/api-configuration-profiles
    tags:
      - AI Agents
      - Configuration
      - Developer Workflow
      - LLM
common:
  - type: Website
    url: https://roocode.com/
  - type: Documentation
    url: https://docs.roocode.com/
  - type: GitHub Organization
    url: https://github.com/RooCodeInc
  - type: GitHubRepository
    url: https://github.com/RooCodeInc/Roo-Code
  - type: Vocabulary
    url: vocabulary/roorules-vocabulary.yml
  - type: JSON-LD
    url: json-ld/roorules-context.jsonld
  - type: JSONSchema
    url: json-schema/roorules-config-schema.json
  - type: JSONStructure
    url: json-structure/roorules-config-structure.json
  - type: Marketplace
    url: https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline
  - type: Discord
    url: https://discord.gg/roocode
  - type: X
    url: https://twitter.com/roo_code
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
