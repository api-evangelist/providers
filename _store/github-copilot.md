---
aid: github-copilot
url: https://raw.githubusercontent.com/api-evangelist/github-copilot/refs/heads/main/apis.yml
apis:
- name: GitHub Copilot API
  description: REST API for managing GitHub Copilot seats, usage, and organization settings.
  image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
  humanUrl: https://docs.github.com/en/copilot
  baseUrl: https://api.github.com
  tags:
  - AI
  - Code Completion
  - Developer Tools
  - Machine Learning
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: Getting Started
    url: https://docs.github.com/en/copilot/quickstart
  - type: Features
    url: https://docs.github.com/en/copilot/get-started/features
  - type: Plans
    url: https://docs.github.com/en/copilot/get-started/plans
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON Schema
    url: json-schema/github-copilot-seat-schema.json
  - type: JSON Schema
    url: json-schema/github-copilot-metrics-schema.json
  - type: JSON-LD Context
    url: json-ld/github-copilot-context.jsonld
  contact:
  - FN: GitHub Support
    email: support@github.com
    url: https://support.github.com
- name: GitHub Copilot for Business API
  description: Manage Copilot for Business subscriptions, seat assignments, and usage metrics.
  humanUrl: https://docs.github.com/en/copilot/managing-copilot-for-business
  baseUrl: https://api.github.com
  tags:
  - Enterprise
  - Seat Management
  - Usage Analytics
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot/copilot-for-business
  - type: Pricing
    url: https://github.com/features/copilot#pricing
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Seat Assignment
    url: https://docs.github.com/en/copilot/reference/copilot-billing/seat-assignment
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON Schema
    url: json-schema/github-copilot-seat-schema.json
- name: GitHub Copilot Chat API
  description: API for GitHub Copilot Chat interactions and conversations.
  humanUrl: https://docs.github.com/en/copilot/github-copilot-chat
  baseUrl: https://api.github.com
  tags:
  - Chat
  - Conversational AI
  - IDE Integration
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/github-copilot-chat
  - type: Getting Started
    url: https://docs.github.com/en/copilot/quickstart
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
- name: GitHub Copilot User Management API
  description: REST API for managing GitHub Copilot seat assignments, billing information, and subscription details for organizations including adding and removing users and teams.
  humanUrl: https://docs.github.com/en/rest/copilot/copilot-user-management
  baseUrl: https://api.github.com
  tags:
  - Billing
  - Organizations
  - Seat Management
  - User Management
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot/copilot-user-management
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: Enterprise Cloud Documentation
    url: https://docs.github.com/en/enterprise-cloud@latest/rest/copilot/copilot-user-management
  - type: Seat Assignment
    url: https://docs.github.com/en/copilot/reference/copilot-billing/seat-assignment
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON Schema
    url: json-schema/github-copilot-seat-schema.json
  - type: JSON-LD Context
    url: json-ld/github-copilot-context.jsonld
- name: GitHub Copilot Metrics API
  description: REST API for retrieving aggregated Copilot usage metrics at the organization and team level, including data on active users, engaged users, and breakdowns by language and editor.
  humanUrl: https://docs.github.com/en/rest/copilot/copilot-metrics
  baseUrl: https://api.github.com
  tags:
  - Analytics
  - Metrics
  - Organizations
  - Usage
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot/copilot-metrics
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: Enterprise Cloud Documentation
    url: https://docs.github.com/en/enterprise-cloud@latest/rest/copilot/copilot-metrics
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON Schema
    url: json-schema/github-copilot-metrics-schema.json
  - type: JSON-LD Context
    url: json-ld/github-copilot-context.jsonld
- name: GitHub Copilot Usage Metrics API
  description: REST API for retrieving detailed Copilot usage metrics reports at the enterprise and organization level, including daily and 28-day aggregated reports for both entity-level and user-level data.
  humanUrl: https://docs.github.com/en/rest/copilot/copilot-usage-metrics
  baseUrl: https://api.github.com
  tags:
  - Analytics
  - Enterprise
  - Reporting
  - Usage Metrics
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot/copilot-usage-metrics
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: Enterprise Cloud Documentation
    url: https://docs.github.com/en/enterprise-cloud@latest/rest/copilot
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON Schema
    url: json-schema/github-copilot-metrics-schema.json
  - type: JSON-LD Context
    url: json-ld/github-copilot-context.jsonld
- name: GitHub Copilot Content Exclusion API
  description: REST API for programmatically managing Copilot content exclusion path rules at both the organization and enterprise level, enabling automation and governance of which content Copilot can access.
  humanUrl: https://docs.github.com/en/rest/copilot/copilot-content-exclusion-management
  baseUrl: https://api.github.com
  tags:
  - Content Exclusion
  - Governance
  - Policy
  - Security
  properties:
  - type: Documentation
    url: https://docs.github.com/en/rest/copilot/copilot-content-exclusion-management
  - type: OpenAPI
    url: https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: Content Exclusion Concepts
    url: https://docs.github.com/en/copilot/concepts/context/content-exclusion
  - type: Configuration Guide
    url: https://docs.github.com/en/copilot/how-tos/configure-content-exclusion
  - type: OpenAPI
    url: openapi/github-copilot-openapi.yml
  - type: JSON-LD Context
    url: json-ld/github-copilot-context.jsonld
- name: GitHub Copilot Extensions API
  description: Platform for building Copilot Extensions that integrate third-party tools, services, and custom agents into GitHub Copilot Chat, using GitHub Apps with agent or skillset configurations.
  humanUrl: https://docs.github.com/en/copilot/building-copilot-extensions
  baseUrl: https://api.github.com
  tags:
  - Agents
  - Extensions
  - Integrations
  - Skillsets
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions
  - type: Getting Started
    url: https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension
  - type: SDKs
    url: https://github.com/github/copilot-sdk
  - type: GitHub Org
    url: https://github.com/copilot-extensions
  - type: JavaScript SDK
    url: https://github.com/copilot-extensions/preview-sdk.js
  - type: Skillset Example
    url: https://github.com/copilot-extensions/skillset-example
- name: GitHub Copilot Coding Agent
  description: Autonomous coding agent that works in the background to complete tasks, spinning up secure development environments powered by GitHub Actions to explore code, make changes, run tests, and open pull requests.
  humanUrl: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
  baseUrl: https://api.github.com
  tags:
  - Agents
  - Automation
  - Code Generation
  - GitHub Actions
  - Pull Requests
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
  - type: About
    url: https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent
  - type: Access Management
    url: https://docs.github.com/en/copilot/concepts/agents/coding-agent/access-management
  - type: Piloting Guide
    url: https://docs.github.com/en/copilot/tutorials/coding-agent/pilot-coding-agent
  - type: Reviewing Pull Requests
    url: https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/reviewing-a-pull-request-created-by-copilot
  - type: MCP Integration
    url: https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp
  - type: Landing Page
    url: https://github.com/features/copilot/agents
  contact:
  - FN: GitHub Support
    email: support@github.com
    url: https://support.github.com
- name: GitHub Copilot Code Review
  description: AI-powered code review agent that analyzes pull requests for issues, suggests fixes, and provides feedback across any programming language with agentic context gathering capabilities.
  humanUrl: https://docs.github.com/en/copilot/concepts/agents/code-review
  baseUrl: https://api.github.com
  tags:
  - Agents
  - Code Quality
  - Code Review
  - Pull Requests
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/concepts/agents/code-review
  - type: Usage Guide
    url: https://docs.github.com/copilot/using-github-copilot/code-review/using-copilot-code-review
  - type: Custom Instructions
    url: https://docs.github.com/en/copilot/tutorials/use-custom-instructions
  - type: Pull Request Summaries
    url: https://docs.github.com/en/copilot/responsible-use/pull-request-summaries
  contact:
  - FN: GitHub Support
    email: support@github.com
    url: https://support.github.com
- name: GitHub MCP Server
  description: GitHub official Model Context Protocol server that enables AI tools to interact with GitHub repositories, issues, pull requests, and other resources through a standardized protocol.
  humanUrl: https://docs.github.com/en/copilot/concepts/context/mcp
  baseUrl: https://api.github.com
  tags:
  - Agents
  - Context
  - Integrations
  - MCP
  - Model Context Protocol
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/concepts/context/mcp
  - type: GitHub Repository
    url: https://github.com/github/github-mcp-server
  - type: Setup Guide
    url: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server
  - type: Usage Guide
    url: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/use-the-github-mcp-server
  - type: Extending Copilot Chat with MCP
    url: https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol/extending-copilot-chat-with-mcp
  - type: MCP and Coding Agent
    url: https://docs.github.com/en/copilot/concepts/agents/coding-agent/mcp-and-coding-agent
  contact:
  - FN: GitHub Support
    email: support@github.com
    url: https://support.github.com
- name: GitHub Copilot Custom Instructions
  description: Configuration system for providing repository-level, path-specific, and organization-level custom instructions to guide Copilot behavior, code style, and response formatting.
  humanUrl: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions
  baseUrl: https://api.github.com
  tags:
  - Configuration
  - Customization
  - Instructions
  - Organizations
  properties:
  - type: Documentation
    url: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions
  - type: Repository Instructions
    url: https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot
  - type: Organization Instructions
    url: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions
  - type: CLI Instructions
    url: https://docs.github.com/en/copilot/how-tos/copilot-cli/add-repository-instructions
  - type: Support Reference
    url: https://docs.github.com/en/copilot/reference/custom-instructions-support
  contact:
  - FN: GitHub Support
    email: support@github.com
    url: https://support.github.com
name: GitHub Copilot
tags:
- Agents
- AI
- Artificial Intelligence
- Code Generation
- Code Review
- Coding Agent
- Custom Instructions
- Developer Tools
- Extensions
- IDE
- Machine Learning
- MCP
- Metrics
- Model Context Protocol
- Productivity
type: Contract
image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs and resources for GitHub Copilot, an AI pair programmer that helps you write code faster.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

