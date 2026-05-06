---
name: Claude
description: Anthropic's Claude AI assistant API for natural language processing and conversation.
image: https://www.anthropic.com/images/icons/anthropic-icon.png
url: https://www.anthropic.com
created: '2024'
modified: '2026-04-18'
tags:
  - Artificial Intelligence
  - Chatbot
  - Conversational AI
  - Generative AI
  - Large Language Models
  - Machine Learning
  - Natural Language Processing
apis:
  - name: Claude Messages API
    description: Primary API for sending messages to Claude and receiving responses.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/messages
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Conversational AI
      - Large Language Models
      - Natural Language Processing
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/messages
      - type: OpenAPI
        url: openapi/claude-messages-api.yml
      - type: Authentication
        url: https://docs.anthropic.com/claude/reference/authentication
      - type: Pricing
        url: https://www.anthropic.com/pricing
      - type: RateLimits
        url: https://docs.anthropic.com/en/api/rate-limits
      - type: GettingStarted
        url: https://docs.anthropic.com/en/api/getting-started
      - type: JSONSchema
        url: json-schema/claude-message-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-create-message-request-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-message-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-error-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-usage-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-tool-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-tool-use-block-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-content-block-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-text-block-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-thinking-block-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-token-count-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-count-tokens-request-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-metadata-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-output-config-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-thinking-config-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-tool-choice-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-cache-control-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-content-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-text-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-image-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-document-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-tool-use-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-tool-result-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-thinking-block-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-message-param-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-message-batch-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-message-batch-list-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-message-batch-result-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-create-message-batch-request-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-batch-request-item-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-deleted-message-batch-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-model-info-schema.json
      - type: JSONSchema
        url: json-schema/claude-messages-model-list-schema.json
      - type: JSONSchema
        url: json-schema/claude-tool-use-schema.json
      - type: JSONLD
        url: json-ld/claude-context.jsonld
      - type: JSONLD
        url: json-ld/claude-messages-context.jsonld
      - type: SDK
        url: https://github.com/anthropics/anthropic-sdk-python
        title: Python SDK
      - type: SDK
        url: https://github.com/anthropics/anthropic-sdk-typescript
        title: TypeScript SDK
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Create Message
        method: POST
        path: /messages
        description: Send a message to Claude and receive a response
      - name: Stream Message
        method: POST
        path: /messages
        description: Stream a message response from Claude using server-sent events
      - name: Count Message Tokens
        method: POST
        path: /messages/count_tokens
        description: Count the number of tokens in a message including tools images and documents without creating it
  - name: Claude Message Batches API
    description: API for asynchronously processing large volumes of message requests at reduced cost with 50 percent discount.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/creating-message-batches
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Asynchronous
      - Batch Processing
      - Large Language Models
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/creating-message-batches
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Create Message Batch
        method: POST
        path: /messages/batches
        description: Create a batch of message requests for asynchronous processing
      - name: List Message Batches
        method: GET
        path: /messages/batches
        description: List all message batches within a workspace
      - name: Retrieve Message Batch
        method: GET
        path: /messages/batches/{message_batch_id}
        description: Retrieve the status and details of a specific message batch
      - name: Retrieve Message Batch Results
        method: GET
        path: /messages/batches/{message_batch_id}/results
        description: Stream the results of a completed message batch as a JSONL file
      - name: Cancel Message Batch
        method: POST
        path: /messages/batches/{message_batch_id}/cancel
        description: Cancel an in-progress message batch
      - name: Delete Message Batch
        method: DELETE
        path: /messages/batches/{message_batch_id}
        description: Delete a completed message batch
  - name: Claude Models API
    description: API for listing and retrieving metadata about available Claude models including capabilities and context windows.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/models-list
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Large Language Models
      - Models
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/models-list
      - type: Models
        url: https://docs.anthropic.com/en/docs/about-claude/models
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: List Models
        method: GET
        path: /models
        description: List all available Claude models with their metadata
      - name: Get Model
        method: GET
        path: /models/{model_id}
        description: Retrieve metadata for a specific Claude model
  - name: Claude Files API
    description: API for uploading and managing files to reference in Claude API requests without re-uploading content each time.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/docs/build-with-claude/files
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Document Processing
      - File Management
      - Files
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/docs/build-with-claude/files
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Upload File
        method: POST
        path: /files
        description: Upload a file to be referenced in future API calls
      - name: List Files
        method: GET
        path: /files
        description: List uploaded files
      - name: Get File Metadata
        method: GET
        path: /files/{file_id}
        description: Retrieve metadata for a specific uploaded file
      - name: Download File
        method: GET
        path: /files/{file_id}/content
        description: Download file content created by skills or the code execution tool
      - name: Delete File
        method: DELETE
        path: /files/{file_id}
        description: Delete an uploaded file
  - name: Claude Admin API
    description: API for programmatically managing organization resources including members workspaces API keys and invites.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/administration-api
    baseURL: https://api.anthropic.com/v1
    tags:
      - Administration
      - AI
      - API Keys
      - Organization Management
      - Workspaces
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/administration-api
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Get Organization
        method: GET
        path: /organizations/me
        description: Retrieve information about your organization
      - name: List Organization Members
        method: GET
        path: /organizations/users
        description: List all members of the organization
      - name: Update Organization Member
        method: POST
        path: /organizations/users/{user_id}
        description: Update an organization member role
      - name: Remove Organization Member
        method: DELETE
        path: /organizations/users/{user_id}
        description: Remove a member from the organization
      - name: List Invites
        method: GET
        path: /organizations/invites
        description: List all pending invitations
      - name: Create Invite
        method: POST
        path: /organizations/invites
        description: Invite a user to the organization
      - name: Delete Invite
        method: DELETE
        path: /organizations/invites/{invite_id}
        description: Delete a pending invitation
      - name: List Workspaces
        method: GET
        path: /organizations/workspaces
        description: List all workspaces in the organization
      - name: Get Workspace
        method: GET
        path: /organizations/workspaces/{workspace_id}
        description: Retrieve details of a specific workspace
      - name: List Workspace Members
        method: GET
        path: /organizations/workspaces/{workspace_id}/members
        description: List all members of a workspace
      - name: Add Workspace Member
        method: POST
        path: /organizations/workspaces/{workspace_id}/members
        description: Add a member to a workspace
      - name: Update Workspace Member
        method: POST
        path: /organizations/workspaces/{workspace_id}/members/{user_id}
        description: Update a workspace member role
      - name: Remove Workspace Member
        method: DELETE
        path: /organizations/workspaces/{workspace_id}/members/{user_id}
        description: Remove a member from a workspace
      - name: List API Keys
        method: GET
        path: /organizations/api_keys
        description: List all API keys in the organization
      - name: Update API Key
        method: POST
        path: /organizations/api_keys/{api_key_id}
        description: Update an API key name or status
  - name: Claude Usage and Cost API
    description: API for tracking token consumption and costs across your organization with breakdowns by model workspace and service tier.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/usage-cost-api
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Analytics
      - Cost Tracking
      - Usage
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/usage-cost-api
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Get Usage Report
        method: GET
        path: /organizations/usage_report/messages
        description: Retrieve token usage report with breakdowns by model workspace and service tier
      - name: Get Cost Report
        method: GET
        path: /organizations/cost_report
        description: Retrieve service-level cost breakdowns in USD including token usage web search and code execution costs
  - name: Claude Text Completions API
    description: Legacy API for generating text completions - deprecated in favor of the Messages API.
    image: https://www.anthropic.com/images/icons/anthropic-icon.png
    humanURL: https://docs.anthropic.com/en/api/complete
    baseURL: https://api.anthropic.com/v1
    tags:
      - AI
      - Large Language Models
      - Legacy
      - Text Completion
    properties:
      - type: Documentation
        url: https://docs.anthropic.com/en/api/complete
    contact:
      - type: Support
        url: https://support.anthropic.com
    endpoints:
      - name: Create Text Completion
        method: POST
        path: /complete
        description: Generate a text completion from Claude (legacy - use Messages API instead)
common:
  - type: Portal
    url: https://console.anthropic.com
  - type: Documentation
    url: https://docs.anthropic.com
  - type: GettingStarted
    url: https://docs.anthropic.com/en/docs/get-started
  - type: Pricing
    url: https://www.anthropic.com/pricing
  - type: RateLimits
    url: https://docs.anthropic.com/en/api/rate-limits
  - type: Authentication
    url: https://docs.anthropic.com/en/api/getting-started
  - type: ChangeLog
    url: https://docs.anthropic.com/en/release-notes/api
  - type: StatusPage
    url: https://status.anthropic.com
  - type: Blog
    url: https://www.anthropic.com/news
  - type: Support
    url: https://support.anthropic.com
  - type: TermsOfService
    url: https://www.anthropic.com/legal/commercial-terms
  - type: PrivacyPolicy
    url: https://www.anthropic.com/legal/privacy
  - type: GitHubOrganization
    url: https://github.com/anthropics
  - type: SpectralRules
    url: rules/claude-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/claude-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ai-messaging.yaml
  - type: Features
    data:
      - name: Multi-Turn Conversations
        description: Maintain context across multiple message exchanges for natural dialogue interactions.
      - name: Tool Use
        description: Enable Claude to call external tools and functions to perform actions and retrieve data.
      - name: Vision
        description: Process and analyze images alongside text for multimodal understanding.
      - name: Extended Thinking
        description: Allow Claude to reason step-by-step for complex tasks with visible thinking process.
      - name: Streaming Responses
        description: Receive responses in real-time via server-sent events for responsive user experiences.
      - name: Message Batches
        description: Process large volumes of requests asynchronously at 50 percent reduced cost.
      - name: Token Counting
        description: Pre-calculate token usage for messages including tools, images, and documents.
  - type: UseCases
    data:
      - name: AI-Powered Chat Applications
        description: Build conversational interfaces with context-aware responses and tool integration.
      - name: Content Generation
        description: Generate, edit, and transform text content for marketing, documentation, and creative writing.
      - name: Code Assistance
        description: Use Claude for code generation, review, debugging, and technical documentation.
      - name: Document Analysis
        description: Extract information, summarize, and answer questions about documents and images.
      - name: Batch Processing
        description: Process large datasets of prompts efficiently using the Message Batches API.
  - type: Integrations
    data:
      - name: Amazon Bedrock
        description: Access Claude models through AWS Bedrock for enterprise deployment with AWS infrastructure.
      - name: Google Cloud Vertex AI
        description: Use Claude on Google Cloud through Vertex AI integration.
      - name: LangChain
        description: Integrate Claude into LangChain pipelines for advanced AI application development.
      - name: MCP Protocol
        description: Connect Claude to external data sources and tools via the Model Context Protocol.
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
  - name: Anthropic
    email: support@anthropic.com
    url: https://www.anthropic.com
---
