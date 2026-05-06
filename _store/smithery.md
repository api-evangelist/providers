---
aid: smithery
name: Smithery
description: Smithery is a platform for discovering, deploying, and managing Model Context Protocol (MCP) servers and skills. It provides a registry of 6000+ community-built MCP extensions that AI agents can use to access external tools, data sources, and services. The platform offers APIs for server management, skill discovery, connection management, and AI-agent integration.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Large Language Models
  - MCP
  - Model Context Protocol
  - AI Agents
  - Developer Tools
created: '2025-08-19'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/smithery/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: smithery:registry-api
    name: Smithery Registry API
    description: The Smithery Registry API provides access to the MCP server registry, enabling search and discovery of community-built MCP servers and skills. Supports server management, skill publishing, namespace management, connection handling, and token-based machine-to-machine authentication.
    humanURL: https://smithery.ai/docs
    baseURL: https://api.smithery.ai
    tags:
      - Artificial Intelligence
      - MCP
      - Registry
      - Servers
      - Skills
    properties:
      - type: Documentation
        url: https://smithery.ai/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/smithery/refs/heads/main/openapi/smithery-openapi.json
      - type: OpenAPI Specification
        url: https://smithery.ai/docs/openapi.json
common:
  - url: https://github.com/smithery-ai
    name: GitHub Organization
    type: GitHubOrganization
  - name: Smithery Documentation
    description: Complete API documentation and developer guides
    url: https://smithery.ai/docs
    type: Documentation
  - name: Smithery CLI
    description: Command-line interface for managing MCP servers and skills
    url: https://smithery.ai/docs/concepts/cli
    type: CLI
  - name: Smithery Website
    description: Main platform for discovering and using MCP extensions
    url: https://smithery.ai/
    type: Website
  - name: Smithery Playground
    description: Interactive playground for testing MCP servers
    url: https://smithery.ai/playground
    type: Playground
  - name: Smithery Blog
    description: Blog covering MCP, AI agents, and platform updates
    url: https://smithery.ai/blog
    type: Blog
  - name: API Keys
    description: Manage API keys for Smithery platform access
    url: https://smithery.ai/account/api-keys
    type: Authentication
  - name: Skills Directory
    description: Browse reusable skills and prompt-based AI capabilities
    url: https://smithery.ai/skills
    type: Documentation
  - name: CLI GitHub Repository
    description: Smithery CLI source code and documentation
    url: https://github.com/smithery-ai/cli
    type: SDK
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
