---
aid: anthropic
url: https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/apis.yml
apis:
  - aid: anthropic:anthropic-messages-api
    name: Anthropic Messages API
    tags:
      - AI
      - Artificial Intelligence
      - Messages
    humanURL: https://docs.anthropic.com/en/api/messages
    properties:
      - url: https://docs.anthropic.com/en/api/messages
        type: Documentation
      - url: https://docs.anthropic.com/en/api/messages-streaming
        type: Documentation
      - url: openapi/anthropic-messages-api-openapi.yml
        type: OpenAPI
      - url: json-schema/anthropic-message-schema.json
        type: JSONSchema
      - url: json-schema/anthropic-tool-use-schema.json
        type: JSONSchema
      - url: json-ld/anthropic-context.jsonld
        type: JSONLD
    description: Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation. The Messages API supports text, images, tool use, extended thinking, streaming, and structured output.
  - aid: anthropic:anthropic-models-api
    name: Anthropic Models API
    tags:
      - AI
      - Artificial Intelligence
      - Models
    humanURL: https://docs.anthropic.com/en/api/models-list
    properties:
      - url: https://docs.anthropic.com/en/api/models-list
        type: Documentation
      - url: properties/anthropic-models-api-openapi.yml
        type: OpenAPI
    description: Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation.
  - aid: anthropic:anthropic-message-batches-api
    name: Anthropic Message Batches API
    tags:
      - AI
      - Artificial Intelligence
      - Batches
      - Messages
    humanURL: https://docs.anthropic.com/en/api/creating-message-batches
    properties:
      - url: https://docs.anthropic.com/en/api/creating-message-batches
        type: Documentation
      - url: properties/anthropic-message-batches-api-openapi.yml
        type: OpenAPI
    description: Send a batch of Message creation requests. The Message Batches API can be used to process multiple Messages API requests at once. Once a Message Batch is created, it begins processing immediately. Batches can take up to 24 hours to complete.
  - aid: anthropic:anthropic-files-api
    name: Anthropic Files API
    tags:
      - AI
      - Artificial Intelligence
      - Files
    humanURL: https://docs.anthropic.com/en/api/files-create
    properties:
      - url: https://docs.anthropic.com/en/api/files-create
        type: Documentation
      - url: properties/anthropic-files-api-openapi.yml
        type: OpenAPI
    description: The Files API allows you to upload and manage files to use with the Anthropic API without having to re-upload content with each request. For more information about the Files API, see the developer guide for files.
  - aid: anthropic:anthropic-admin-api
    name: Anthropic Admin API
    tags:
      - Administrative
      - AI
      - Artificial Intelligence
    humanURL: https://docs.anthropic.com/en/api/admin-api/users/get-user
    properties:
      - url: https://docs.anthropic.com/en/api/admin-api/users/get-user
        type: Documentation
      - url: properties/anthropic-admin-api-openapi.yml
        type: OpenAPI
    description: Manage administrative functions.
  - aid: anthropic:anthropic-prompts-api
    name: Anthropic Prompts API
    tags:
      - AI
      - Artificial Intelligence
      - Prompts
    humanURL: https://docs.anthropic.com/en/api/prompt-tools-generate
    properties:
      - url: https://docs.anthropic.com/en/api/prompt-tools-generate
        type: Documentation
      - url: properties/anthropic-prompts-api-openapi.yml
        type: OpenAPI
    description: Manage prompts.
  - aid: anthropic:anthropic-token-counting-api
    name: Anthropic Token Counting API
    tags:
      - AI
      - Artificial Intelligence
      - Counting
      - Tokens
    humanURL: https://docs.anthropic.com/en/api/messages-count-tokens
    properties:
      - url: https://docs.anthropic.com/en/api/messages-count-tokens
        type: Documentation
      - url: properties/anthropic-token-counting-api-openapi.yml
        type: OpenAPI
    description: Count the number of tokens in a Message, including tools, images, and documents, without creating it. The Token Count API accepts the same structured list of inputs for creating a message, including support for system prompts, tools, images, and PDFs. Token counting is free to use but subject to requests per minute rate limits.
  - aid: anthropic:anthropic-skills-api
    name: Anthropic Skills API
    tags:
      - Agents
      - AI
      - Artificial Intelligence
      - Skills
    humanURL: https://docs.anthropic.com/en/api/skills/create-skill
    properties:
      - url: https://docs.anthropic.com/en/api/skills/create-skill
        type: Documentation
      - url: properties/anthropic-skills-api-openapi.yml
        type: OpenAPI
    description: Create and manage custom agent skills. Skills allow you to package domain expertise and organizational workflows for use with Claude. The Skills API is currently in beta and requires the skills-2025-10-02 beta header.
  - aid: anthropic:anthropic-usage-cost-api
    name: Anthropic Usage & Cost API
    tags:
      - Administration
      - AI
      - Artificial Intelligence
      - Cost
      - Usage
    humanURL: https://docs.anthropic.com/en/api/usage-cost-api
    properties:
      - url: https://docs.anthropic.com/en/api/usage-cost-api
        type: Documentation
    description: Programmatically access your organization's API usage and cost data with the Usage & Cost Admin API. The Usage API tracks token consumption across your organization with detailed breakdowns by model, workspace, and service tier via the /v1/organizations/usage_report/messages endpoint. The Cost API retrieves service-level cost breakdowns in USD via the /v1/organizations/cost_report endpoint. Requires an Admin API key.
  - aid: anthropic:anthropic-claude-code-analytics-api
    name: Anthropic Claude Code Analytics API
    tags:
      - Administration
      - AI
      - Analytics
      - Artificial Intelligence
      - Claude Code
    humanURL: https://docs.anthropic.com/en/api/claude-code-analytics-api
    properties:
      - url: https://docs.anthropic.com/en/api/claude-code-analytics-api
        type: Documentation
    description: Programmatically access your organization's Claude Code usage analytics and productivity metrics with the Claude Code Analytics Admin API. Track sessions, lines of code, commits, pull requests, and tool usage via the /v1/organizations/usage_report/claude_code endpoint. Provides daily aggregated user-level data with model breakdowns and estimated costs. Requires an Admin API key.
name: Anthropic
tags:
  - AI
  - Artificial Intelligence
  - Claude
  - Foundation Models
  - Large Language Models
  - Machine Learning
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/anthropics/anthropic-quickstarts
    name: Quickstarts
    type: Documentation
  - url: https://docs.anthropic.com/en/home
    name: Home - Anthropic
    type: Portal
    description: 'null'
  - url: https://docs.anthropic.com/en/api/messages
    name: Messages - Anthropic
    type: Documentation
    description: 'null'
  - url: https://status.anthropic.com/
    name: Anthropic Status
    type: Documentation
    description: 'null'
  - url: https://docs.anthropic.com/en/release-notes/api
    name: API - Anthropic
    type: ChangeLog
    description: 'null'
  - url: https://console.anthropic.com/login
    name: Anthropic Console
    type: Documentation
    description: 'null'
  - url: https://docs.anthropic.com/en/api/rate-limits
    name: Rate limits - Anthropic
    type: RateLimits
    description: 'null'
  - url: https://docs.anthropic.com/en/api/service-tiers
    name: Service tiers - Anthropic
    type: Tiers
    description: 'null'
  - url: https://docs.anthropic.com/en/api/errors
    name: Errors - Anthropic
    type: Errors
    description: 'null'
  - url: https://docs.anthropic.com/en/api/client-sdks
    name: Client SDKs - Anthropic
    type: Documentation
    description: 'null'
  - url: https://docs.anthropic.com/en/api/versioning
    name: Versions - Anthropic
    type: Versioning
    description: 'null'
  - url: https://docs.anthropic.com/en/api/supported-regions
    name: Supported regions - Anthropic
    type: Regions
    description: 'null'
  - url: https://docs.anthropic.com/en/api/getting-help
    name: Getting help - Anthropic
    type: Support
    description: 'null'
  - url: https://www.anthropic.com/pricing
    data:
      - id: free
        name: Free
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: Chat on web, iOS, Android, and on your desktop
          - name: Generate code and visualize data
          - name: Write, edit, and create content
          - name: Analyze text and images
          - name: Ability to search the web
          - name: Unlock more from Claude with desktop extensions
        description: Try Claude
      - id: pro
        name: Pro
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 20
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: More usage
          - name: Access Claude Code directly in your terminal
          - name: Access to unlimited Projects to organize chats and documents
          - name: Access to Research
          - name: Connect Google Workspace email, calendar, and docs
          - name: Connect your everyday tools in just a few clicks (with remote MCP servers)
          - name: Extended thinking for complex work
          - name: Ability to use more Claude models
        description: For everyday productivity.
      - id: max
        name: Max
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 100
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: Choose 5x or 20x more usage per session than Pro*
          - name: Higher output limits for all tasks
          - name: Early access to advanced Claude features
          - name: Priority access at high traffic times
        description: Get the most out of Claude.
      - id: team
        name: Team
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: 25
            metric: user
            timeFrame: month
            description: Usage based pricing.
        elements:
          - name: More usage
          - name: Central billing and administration
          - name: Early access to collaboration features
          - name: Claude Code available separately through Anthropic Console
        description: For collaboration across organizations
      - id: enterprise
        name: Enterprise
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Call
            metric: user
            timeFrame: month
            description: For businesses operating at scale
        elements:
          - name: More usage
          - name: Enhanced context window
          - name: Single sign-on (SSO) and domain capture
          - name: Role-based access with fine grained permissioning
          - name: System for Cross-domain Identity Management (SCIM)
          - name: Audit logs
          - name: Google Docs cataloging
          - name: Claude Code available separately through Anthropic Console
        description: For collaboration across organizations
    name: Plans
    type: Plans
  - url: https://www.anthropic.com/pricing#api
    data:
      - id: claude-opus-4-6
        name: Claude Opus 4.6
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 5
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 25
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching
            price: 0.5
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching 5min
            price: 6.25
            metric: token
            timeFrame: usage
            description: Write prompt caching 5-minute TTL for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching 1hr
            price: 10
            metric: token
            timeFrame: usage
            description: Write prompt caching 1-hour TTL for model.
        description: Most capable model with fast mode support and 1M context window
      - id: claude-opus-4-1
        name: Claude Opus 4.1
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 15
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 75
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching
            price: 1.5
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching
            price: 18.75
            metric: token
            timeFrame: usage
            description: Write prompt caching for model.
        description: Most intelligent model for complex tasks
      - id: claude-sonnet-4-6
        name: Claude Sonnet 4.6
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Prompts Input < 200K
            price: 3
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Input token less than 200K token usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Input > 200K
            price: 6
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Input token greater than 200K token usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Output < 200K
            price: 15
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Output token less than 200k usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Output > 200K
            price: 22.5
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Output token greater than 200k usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching < 200K
            price: 0.3
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Read prompt caching for less than 200K tokens model.
          - geo: US
            unit: 1M
            label: Read Prompt Caching > 200K
            price: 0.6
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Read prompt caching for greater than 200K tokens model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching < 200K
            price: 3.75
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Write prompt caching for less than 200K tokens model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching > 200K
            price: 7.5
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Write prompt caching for greater than 200K tokens model.
        description: High performance model with 1M context window support
      - id: claude-sonnet-4
        name: Claude Sonnet 4
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Prompts Input < 200K
            price: 3
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Input token less than 200K token usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Input > 200K
            price: 6
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Input token greater than 200K token usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Output < 200K
            price: 15
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Output token less than 200k usage-based pricing.
          - geo: US
            unit: 1M
            label: Prompts Output > 200K
            price: 22.5
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Output token greater than 200k usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching < 200K
            price: 0.3
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Read prompt caching for less than 200K tokens model.
          - geo: US
            unit: 1M
            label: Read Prompt Caching > 200K
            price: 0.6
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Read prompt caching for greater than 200K tokens model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching < 200K
            price: 3.75
            metric: token
            maximum: 200000
            timeFrame: usage
            description: Write prompt caching for less than 200K tokens model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching > 200K
            price: 7.5
            metric: token
            minimum: 200000
            timeFrame: usage
            description: Write prompt caching for greater than 200K tokens model.
        description: Optimal balance of intelligence, cost, and speed
      - id: claude-haiku-4-5
        name: Claude Haiku 4.5
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 1
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 5
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching
            price: 0.1
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching 5min
            price: 1.25
            metric: token
            timeFrame: usage
            description: Write prompt caching 5-minute TTL for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching 1hr
            price: 2
            metric: token
            timeFrame: usage
            description: Write prompt caching 1-hour TTL for model.
        description: Fast and cost-effective model for everyday tasks
      - id: claude-haiku-3-5
        name: Claude Haiku 3.5
        type: Latest
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 0.8
            metric: token
            timeFrame: usage
            description: Input token usage-based pricing.
          - geo: US
            unit: 1M
            label: Output
            price: 4
            metric: token
            timeFrame: usage
            description: Output token usage-based pricing.
          - geo: US
            unit: 1M
            label: Read Prompt Caching
            price: 0.08
            metric: token
            timeFrame: usage
            description: Read prompt caching for model.
          - geo: US
            unit: 1M
            label: Write Prompt Caching
            price: 1
            metric: token
            timeFrame: usage
            description: Write prompt caching for model.
        description: Fastest, most cost-effective model.
      - id: web-search
        name: Web Search
        type: Tools
        entries:
          - geo: US
            unit: 1K
            label: Searches
            price: 10
            metric: search
            timeFrame: usage
            description: Usage based search pricing.
        description: Give Claude access to the latest information from the web. Does not include input and output tokens required to process requests.
      - id: code-execution
        name: Code Execution
        type: Tools
        entries:
          - geo: US
            unit: 1K
            label: Per Hour Per Container
            price: 0.05
            metric: container
            timeFrame: hour
            description: Usage based for containers by hour.
        description: Run Python code in a sandboxed environment for advanced data analysis. 50 free hours of usage daily per organization.
      - id: fast-mode
        name: Fast Mode
        type: Features
        entries:
          - geo: US
            unit: 1M
            label: Input
            price: 30
            metric: token
            timeFrame: usage
            description: Fast mode input token pricing for Claude Opus 4.6.
          - geo: US
            unit: 1M
            label: Output
            price: 150
            metric: token
            timeFrame: usage
            description: Fast mode output token pricing for Claude Opus 4.6.
        description: Significantly faster output for Claude Opus 4.6 at premium pricing (6x standard rates). Currently in research preview.
      - id: web-fetch
        name: Web Fetch
        type: Tools
        entries:
          - geo: US
            unit: 1
            label: Requests
            price: 0
            metric: request
            timeFrame: usage
            description: No additional cost beyond standard token pricing.
        description: Fetch web page content for Claude to process. No additional charges beyond standard token costs for fetched content.
    name: Pricing
    type: Pricing
  - url: https://www.anthropic.com/api
    name: Build with Claude  Anthropic
    type: Portal
    description: 'null'
  - url: https://docs.anthropic.com/en/docs/get-started
    name: Get started with Claude - Anthropic
    type: GettingStarted
    description: 'null'
  - url: https://docs.anthropic.com/en/docs/about-claude/glossary
    name: Glossary - Anthropic
    type: Glossary
    description: 'null'
  - url: https://www.anthropic.com/legal/terms
    type: Documentation
  - url: https://www.anthropic.com/legal/privacy
    type: PrivacyPolicy
  - url: https://status.anthropic.com
    type: StatusPage
  - url: https://www.anthropic.com/news
    type: Blog
  - url: https://www.anthropic.com/engineering
    type: Blog
  - url: https://console.anthropic.com/
    type: SignUp
  - url: https://console.anthropic.com/workbench
    type: Sandbox
  - url: https://docs.anthropic.com/en/api/beta-headers
    type: Documentation
  - url: https://trust.anthropic.com/
    type: TrustCenter
  - url: https://www.anthropic.com/legal/aup
    type: TermsOfService
  - url: https://docs.anthropic.com/en/api/administration-api
    type: Documentation
  - url: https://docs.anthropic.com/en/api/usage-cost-api
    type: Documentation
  - url: https://github.com/anthropics
    type: GitHubOrganization
  - url: https://github.com/anthropics/anthropic-sdk-python
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-typescript
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-java
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-go
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-ruby
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-csharp
    type: SDK
  - url: https://github.com/anthropics/anthropic-sdk-php
    type: SDK
  - url: https://github.com/anthropics/claude-cookbooks
    type: CodeExamples
  - url: https://github.com/anthropics/courses
    type: Courses
  - url: https://www.anthropic.com/learn
    type: Training
  - url: https://discord.com/invite/6PPFFzqPDZ
    type: Forum
  - url: https://www.postman.com/postman/anthropic-apis/overview
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/token-counting
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/data-residency
    type: Documentation
  - url: https://docs.anthropic.com/en/api/claude-code-analytics-api
    type: Documentation
  - url: https://privacy.claude.com/
    type: PrivacyPolicy
  - url: https://docs.anthropic.com/en/api/messages-streaming
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/agents-and-tools/computer-use
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/citations
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/batch-processing
    type: Documentation
  - url: https://docs.anthropic.com/en/api/openai-sdk
    type: Documentation
  - url: https://docs.anthropic.com/en/api/claude-on-amazon-bedrock
    type: Documentation
  - url: https://docs.anthropic.com/en/api/claude-on-vertex-ai
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/about-claude/models/all-models
    type: Models
  - url: https://docs.anthropic.com/en/docs/claude-code/sdk
    type: SDK
  - url: https://docs.anthropic.com/en/api/complete
    type: Documentation
  - url: https://modelcontextprotocol.io
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/structured-output
    type: Documentation
  - url: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
    type: Documentation
  - type: Portal
    url: https://www.anthropic.com
  - type: Documentation
    url: https://docs.anthropic.com/
  - type: GettingStarted
    url: https://docs.anthropic.com/en/api/getting-started
  - type: Features
    data:
      - Claude Opus 4.7 with 1M context window and fast mode
      - Claude Sonnet 4.6 balanced model with 1M context window
      - Claude Haiku 4.5 fast and cost-effective model
      - Messages API with text, vision, tool use, extended thinking, and streaming
      - 'Prompt caching: 5-minute and 1-hour TTLs with cache reads at 10% of input price'
      - Batch API with 50% discount on both input and output tokens
      - Files API for upload-once / reuse-many content
      - Skills API (beta) for packaging domain expertise as agent skills
      - Web Search tool at $10 per 1,000 searches
      - Code Execution tool with 1,550 free container-hours/month per organization
      - Computer Use tool for browser and desktop automation (beta)
      - Token-bucket rate limiting with cache-aware ITPM (cache reads excluded on most models)
      - Five usage tiers (Tier 1-4 plus Monthly Invoicing) with automatic advancement
      - Usage & Cost Admin API for FinOps reporting
      - Available via Claude API, AWS Bedrock, Google Vertex AI, and Microsoft Foundry
    sources:
      - https://www.anthropic.com/pricing
      - https://platform.claude.com/docs/en/docs/about-claude/pricing
      - https://platform.claude.com/docs/en/api/rate-limits
    updated: '2026-05-04'
created: '2025-08-14T00:00:00.000Z'
modified: '2026-05-04'
position: Consuming
description: Anthropic is an AI safety company and creator of the Claude family of large language models. The Anthropic API provides access to Claude models for text generation, vision, tool use, extended thinking, batch processing, and agentic workflows. Anthropic also publishes the Model Context Protocol (MCP) for standardized AI tool integration.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
specificationVersion: '0.16'
---
