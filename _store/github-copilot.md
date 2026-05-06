---
name: GitHub Copilot
description: APIs and resources for GitHub Copilot, an AI pair programmer that helps you write code faster.
image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
url: https://api.github.com/apis.yaml
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
type: Contract
access: 3rd-Party
apis:
  - name: GitHub Copilot API
    description: REST API for managing GitHub Copilot seats, usage, and organization settings.
    image: https://github.githubassets.com/images/modules/site/copilot/copilot-logo.png
    humanURL: https://docs.github.com/en/copilot
    baseURL: https://api.github.com
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
      - type: GettingStarted
        url: https://docs.github.com/en/copilot/quickstart
      - type: Features
        url: https://docs.github.com/en/copilot/get-started/features
      - type: Plans
        url: https://docs.github.com/en/copilot/get-started/plans
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/github-copilot-seat-schema.json
      - type: JSONSchema
        url: json-schema/github-copilot-metrics-schema.json
      - type: JSONLD
        url: json-ld/github-copilot-context.jsonld
    contact:
      - FN: GitHub Support
        email: support@github.com
        url: https://support.github.com
  - name: GitHub Copilot for Business API
    description: Manage Copilot for Business subscriptions, seat assignments, and usage metrics.
    humanURL: https://docs.github.com/en/copilot/managing-copilot-for-business
    baseURL: https://api.github.com
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
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/github-copilot-seat-schema.json
  - name: GitHub Copilot Chat API
    description: API for GitHub Copilot Chat interactions and conversations.
    humanURL: https://docs.github.com/en/copilot/github-copilot-chat
    baseURL: https://api.github.com
    tags:
      - Chat
      - Conversational AI
      - IDE Integration
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/github-copilot-chat
      - type: GettingStarted
        url: https://docs.github.com/en/copilot/quickstart
      - type: Authentication
        url: https://docs.github.com/en/rest/authentication
  - name: GitHub Copilot User Management API
    description: REST API for managing GitHub Copilot seat assignments, billing information, and subscription details for organizations including adding and removing users and teams.
    humanURL: https://docs.github.com/en/rest/copilot/copilot-user-management
    baseURL: https://api.github.com
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
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/github-copilot-seat-schema.json
      - type: JSONLD
        url: json-ld/github-copilot-context.jsonld
  - name: GitHub Copilot Metrics API
    description: REST API for retrieving aggregated Copilot usage metrics at the organization and team level, including data on active users, engaged users, and breakdowns by language and editor.
    humanURL: https://docs.github.com/en/rest/copilot/copilot-metrics
    baseURL: https://api.github.com
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
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/github-copilot-metrics-schema.json
      - type: JSONLD
        url: json-ld/github-copilot-context.jsonld
  - name: GitHub Copilot Usage Metrics API
    description: REST API for retrieving detailed Copilot usage metrics reports at the enterprise and organization level, including daily and 28-day aggregated reports for both entity-level and user-level data.
    humanURL: https://docs.github.com/en/rest/copilot/copilot-usage-metrics
    baseURL: https://api.github.com
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
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONSchema
        url: json-schema/github-copilot-metrics-schema.json
      - type: JSONLD
        url: json-ld/github-copilot-context.jsonld
  - name: GitHub Copilot Content Exclusion API
    description: REST API for programmatically managing Copilot content exclusion path rules at both the organization and enterprise level, enabling automation and governance of which content Copilot can access.
    humanURL: https://docs.github.com/en/rest/copilot/copilot-content-exclusion-management
    baseURL: https://api.github.com
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
      - type: OpenAPI
        url: openapi/github-copilot-openapi.yml
      - type: JSONLD
        url: json-ld/github-copilot-context.jsonld
  - name: GitHub Copilot Extensions API
    description: Platform for building Copilot Extensions that integrate third-party tools, services, and custom agents into GitHub Copilot Chat, using GitHub Apps with agent or skillset configurations.
    humanURL: https://docs.github.com/en/copilot/building-copilot-extensions
    baseURL: https://api.github.com
    tags:
      - Agents
      - Extensions
      - Integrations
      - Skillsets
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/building-copilot-extensions/about-building-copilot-extensions
      - type: GettingStarted
        url: https://docs.github.com/en/copilot/building-copilot-extensions/creating-a-copilot-extension
      - type: SDK
        url: https://github.com/github/copilot-sdk
      - type: GitHubOrganization
        url: https://github.com/copilot-extensions
      - type: CodeExamples
        url: https://github.com/copilot-extensions/skillset-example
  - name: GitHub Copilot Coding Agent
    description: Autonomous coding agent that works in the background to complete tasks, spinning up secure development environments powered by GitHub Actions to explore code, make changes, run tests, and open pull requests.
    humanURL: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
    baseURL: https://api.github.com
    tags:
      - Agents
      - Automation
      - Code Generation
      - GitHub Actions
      - Pull Requests
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent
    contact:
      - FN: GitHub Support
        email: support@github.com
        url: https://support.github.com
  - name: GitHub Copilot Code Review
    description: AI-powered code review agent that analyzes pull requests for issues, suggests fixes, and provides feedback across any programming language with agentic context gathering capabilities.
    humanURL: https://docs.github.com/en/copilot/concepts/agents/code-review
    baseURL: https://api.github.com
    tags:
      - Agents
      - Code Quality
      - Code Review
      - Pull Requests
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/concepts/agents/code-review
    contact:
      - FN: GitHub Support
        email: support@github.com
        url: https://support.github.com
  - name: GitHub MCP Server
    description: GitHub official Model Context Protocol server that enables AI tools to interact with GitHub repositories, issues, pull requests, and other resources through a standardized protocol.
    humanURL: https://docs.github.com/en/copilot/concepts/context/mcp
    baseURL: https://api.github.com
    tags:
      - Agents
      - Context
      - Integrations
      - MCP
      - Model Context Protocol
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/concepts/context/mcp
      - type: GitHubRepository
        url: https://github.com/github/github-mcp-server
      - type: GettingStarted
        url: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server
    contact:
      - FN: GitHub Support
        email: support@github.com
        url: https://support.github.com
  - name: GitHub Copilot Custom Instructions
    description: Configuration system for providing repository-level, path-specific, and organization-level custom instructions to guide Copilot behavior, code style, and response formatting.
    humanURL: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions
    baseURL: https://api.github.com
    tags:
      - Configuration
      - Customization
      - Instructions
      - Organizations
    properties:
      - type: Documentation
        url: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions
    contact:
      - FN: GitHub Support
        email: support@github.com
        url: https://support.github.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: http://apievangelist.com
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
common:
  - type: Portal
    url: https://github.com/features/copilot
  - type: StatusPage
    url: https://www.githubstatus.com/
  - type: TermsOfService
    url: https://docs.github.com/en/site-policy/github-terms/github-terms-of-service
  - type: PrivacyPolicy
    url: https://docs.github.com/en/site-policy/privacy-policies/github-privacy-statement
  - type: GettingStarted
    url: https://docs.github.com/en/copilot/quickstart
  - type: Blog
    url: https://github.blog/tag/github-copilot/
  - type: SignUp
    url: https://github.com/github-copilot/signup
  - type: Pricing
    url: https://github.com/features/copilot/plans
  - type: ChangeLog
    url: https://github.blog/changelog/label/copilot/
  - type: Support
    url: https://support.github.com
  - type: SDK
    url: https://github.com/github/copilot-sdk
  - type: TrustCenter
    url: https://copilot.github.trust.page/
  - type: RateLimits
    url: https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api
  - type: Authentication
    url: https://docs.github.com/en/rest/authentication
  - type: OpenAPI
    url: https://github.com/github/rest-api-description
  - type: Documentation
    url: https://docs.github.com/en/copilot
  - type: Marketplace
    url: https://github.com/marketplace?type=apps&copilot_app=true
  - type: Features
    data:
      - name: Code Completion
        description: AI-powered inline code suggestions that complete lines, functions, and entire blocks as you type in your IDE.
      - name: Chat
        description: Conversational AI assistant for asking questions about code, generating solutions, and debugging directly in your editor.
      - name: Coding Agent
        description: Autonomous agent that explores code, makes changes, runs tests, and opens pull requests from issue assignments.
      - name: Code Review
        description: AI-powered pull request review that analyzes changes, identifies issues, and suggests fixes across any language.
      - name: Extensions
        description: Third-party integrations that extend Copilot Chat with custom tools, services, and domain-specific agents.
      - name: Custom Instructions
        description: Repository-level and organization-level configuration to guide Copilot behavior, code style, and conventions.
      - name: MCP Server
        description: Model Context Protocol server enabling AI tools to interact with GitHub repositories, issues, and pull requests.
      - name: Content Exclusion
        description: Governance controls to specify which files and repositories Copilot can access at organization and enterprise level.
      - name: Usage Metrics
        description: Detailed analytics on Copilot adoption, usage patterns, and productivity impact across organizations and enterprises.
      - name: Seat Management
        description: Programmatic management of Copilot seat assignments, billing, and subscription details for organizations and teams.
  - type: UseCases
    data:
      - name: Developer Productivity
        description: Accelerate software development with AI-powered code completions, chat assistance, and automated code review.
      - name: Enterprise Copilot Governance
        description: Manage Copilot deployments at scale with seat management, content exclusion, usage metrics, and compliance controls.
      - name: Custom AI Tooling
        description: Build domain-specific Copilot Extensions and agents that integrate third-party tools and services into the developer workflow.
      - name: Code Quality Automation
        description: Automate code review, identify potential issues, and enforce coding standards using the Copilot Code Review agent.
  - type: Integrations
    data:
      - name: Visual Studio Code
        description: Full Copilot integration in VS Code including code completion, chat, code review, and MCP support.
      - name: JetBrains IDEs
        description: Copilot code completion and chat support across IntelliJ, PyCharm, WebStorm, and other JetBrains IDEs.
      - name: GitHub.com
        description: Copilot Chat, code review, and coding agent capabilities directly in the GitHub web interface.
      - name: GitHub Actions
        description: Copilot coding agent uses GitHub Actions to spin up secure environments for autonomous coding tasks.
      - name: Model Context Protocol
        description: Standard protocol integration enabling AI tools to access GitHub data through the official MCP server.
---
