---
aid: anthropic
url: >-
  https://raw.githubusercontent.com/api-evangelist/anthropic/refs/heads/main/apis.yml
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
      - url: openapi/anthropic-messages-api-openapi.yml
        type: OpenAPI
    description: >-
      List available models. The Models API response can be used to determine
      which models are available for use in the API. More recently released
      models are listed first.
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
      - url: openapi/anthropic-models-api-openapi.yml
        type: OpenAPI
    description: >-
      Send a structured list of input messages with text and/or image content,
      and the model will generate the next message in the conversation.    
  - aid: anthropic:anthropic-message-batches-api
    name: Anthropic Message Batches API
    tags:
      - AI
      - Artificial Intelligence
      - Messages
      - Batches
    humanURL: https://docs.anthropic.com/en/api/creating-message-batches
    properties:
      - url: https://docs.anthropic.com/en/api/creating-message-batches
        type: Documentation
      - url: openapi/anthropic-message-batches-api-openapi.yml
        type: OpenAPI
    description: >-
      Send a batch of Message creation requests. The Message Batches API can be
      used to process multiple Messages API requests at once. Once a Message
      Batch is created, it begins processing immediately. Batches can take up to
      24 hours to complete.       
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
      - url: openapi/anthropic-files-api-openapi.yml
        type: OpenAPI
    description: >-
      The Files API allows you to upload and manage files to use with the
      Anthropic API without having to re-upload content with each request. For
      more information about the Files API, see the developer guide for
      files.      
  - aid: anthropic:anthropic-admin-api
    name: Anthropic Admin API
    tags:
      - AI
      - Artificial Intelligence
      - Administrative
    humanURL: https://docs.anthropic.com/en/api/admin-api/users/get-user
    properties:
      - url: https://docs.anthropic.com/en/api/admin-api/users/get-user
        type: Documentation
      - url: openapi/anthropic-admin-api-openapi.yml
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
      - url: openapi/anthropic-prompts-api-openapi.yml
        type: OpenAPI
    description: 'Manage prompts.             '
name: Anthropic
tags:
  - AI
  - Artificial Intelligence
  - T1
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - url: https://github.com/anthropics/anthropic-quickstarts
    name: Quickstarts
    type: Quickstarts
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
    type: Status
    description: 'null'
  - url: https://docs.anthropic.com/en/release-notes/api
    name: API - Anthropic
    type: ChangeLog
    description: 'null'
  - url: https://console.anthropic.com/login
    name: Anthropic Console
    type: Login
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
    type: SDKs
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
          - name: >-
              Connect your everyday tools in just a few clicks (with remote MCP
              servers)
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
        description: >-
          Give Claude access to the latest information from the web. Does not
          include input and output tokens required to process requests.
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
        description: >-
          Run Python code in a sandboxed environment for advanced data analysis.
          50 free hours of usage daily per organization.
    name: Pricing
    type: Pricing
  - url: https://docs.anthropic.com/en/api/service-tiers
    data:
      - name: Standard
        description: >-
          The standard tier is the default service tier for all API requests.
          Requests in this tier are prioritized alongside all other requests and
          observe best-effort availability.
      - name: Priority
        description: >-
          Requests in this tier are prioritized over all other requests to
          Anthropic. This prioritization helps minimize server overloaded
          errors, even during peak times.
      - name: Batch
        description: >-
          Best for asynchronous workflows which can wait or benefit from being
          outside your normal capacity.
    name: Tiers
    type: Tiers
    description: >-
      Different tiers of service allow you to balance availability, performance,
      and predictable costs based on your applications needs.
  - url: https://docs.anthropic.com/en/api/rate-limits
    data:
      - name: Claude Opus 4 Input Tokens
        type: Model
        limit: 30000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The input token limits for the Claude Opus 4 model.
        userMultiplied: false
      - name: Claude Opus 4 Output Tokens
        type: Model
        limit: 80000
        metric: tokens
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The output token limits for the Claude Opus 4 model.
        userMultiplied: false
      - name: Claude Opus 4 Requests
        type: Model
        limit: 50
        metric: request
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The request limits for the Claude Opus 4 model.
        userMultiplied: false
      - name: Claude Sonnet 4 Input Tokens
        type: Model
        limit: 30000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The input token limits for the Claude Sonnet 4 model.
        userMultiplied: false
      - name: Claude Sonnet 4 Output Tokens
        type: Model
        limit: 80000
        metric: tokens
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The output token limits for the Claude Sonnet 4 model.
        userMultiplied: false
      - name: Claude Sonnet 4 Requests
        type: Model
        limit: 50
        metric: request
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The request limits for the Claude Sonnet 4 model.
        userMultiplied: false
      - name: Claude Haiku 4 Input Tokens
        type: Model
        limit: 50000
        metric: token
        domains:
          - api.openai.com
        timeframe: minute
        description: The input token limits for the Claude Haiku 4 model.
        userMultiplied: false
      - name: Claude Haiku 4 Output Tokens
        type: Model
        limit: 10000
        metric: tokens
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The output token limits for the Claude Haiku 4 model.
        userMultiplied: false
      - name: Claude Haiku 4 Requests
        type: Model
        limit: 50
        metric: request
        domains:
          - api.anthropic.com
        timeframe: minute
        description: The request limits for the Claude Haiku 4 model.
        userMultiplied: false
    name: Rate Limits
    type: RateLimits
    description: The rate limits for this API.
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
  - url: https://docs.anthropic.com/en/api/service-tiers
    name: Service tiers - Anthropic
    type: Tiers
    description: 'null'
created: '2025-08-14T00:00:00.000Z'
modified: '2025-10-25'
position: Consuming
description: >-
  Claude is an AI assistant created by Anthropic that helps people with a wide
  variety of tasks through natural conversation. I can assist with writing and
  editing, answer questions on many topics, help with analysis and research,
  provide coding support, engage in creative projects, and offer explanations of
  complex concepts.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---