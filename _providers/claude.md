---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Claude Agentic Access
  operation_count: 10
  slug: claude-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 1
apis:
- description: API for asynchronously processing large volumes of message requests at reduced cost with 50 percent discount.
  name: Claude Message Batches API
  slug: claude-message-batches-api
- description: API for listing and retrieving metadata about available Claude models including capabilities and context windows.
  name: Claude Models API
  slug: claude-models-api
- description: API for uploading and managing files to reference in Claude API requests without re-uploading content each time.
  name: Claude Files API
  slug: claude-files-api
- description: API for programmatically managing organization resources including members workspaces API keys and invites.
  name: Claude Admin API
  slug: claude-admin-api
- description: API for tracking token consumption and costs across your organization with breakdowns by model workspace and service tier.
  name: Claude Usage and Cost API
  slug: claude-usage-and-cost-api
- description: Legacy API for generating text completions - deprecated in favor of the Messages API.
  name: Claude Text Completions API
  slug: claude-text-completions-api
- description: Create and manage asynchronous message batches
  name: Claude Message Batches API
  slug: claude-message-batches-api
- description: Create messages and count tokens
  name: Claude Messages API
  slug: claude-messages-api
- description: List and retrieve available Claude models
  name: Claude Models API
  slug: claude-models-api
arazzos:
- description: Count tokens for a URL-referenced document, then ask Claude a question about it.
  name: Claude Analyze Document From URL
  slug: claude-analyze-document-from-url-workflow
- description: Submit a message batch, poll until it ends, then retrieve the JSONL results.
  name: Claude Batch Process and Retrieve Results
  slug: claude-batch-process-and-retrieve-results-workflow
- description: Submit a batch, request cancellation, poll until it ends, then delete it.
  name: Claude Cancel and Delete Batch
  slug: claude-cancel-and-delete-batch-workflow
- description: Pre-flight a prompt through token counting before sending it to the Messages API.
  name: Claude Count Tokens Then Create Message
  slug: claude-count-tokens-then-create-message-workflow
- description: List recent message batches, inspect the most recent one, and retrieve its results if it has ended.
  name: Claude Find Latest Batch Results
  slug: claude-find-latest-batch-results-workflow
- description: Send a first user turn, then continue the conversation with a follow-up that includes the assistant's reply.
  name: Claude Multi-Turn Conversation
  slug: claude-multi-turn-conversation-workflow
- description: Discover an available Claude model, confirm its metadata, then generate a message with it.
  name: Claude Select Model and Create Message
  slug: claude-select-model-and-create-message-workflow
- description: Offer the model a tool, capture its tool_use request, then return a tool_result for a final answer.
  name: Claude Tool Use Round Trip
  slug: claude-tool-use-round-trip-workflow
artifact_total: 180
collections:
- collection_type: postman
  name: Claude Messages API
  slug: postman-claude-messages-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Claude Messages Message Batches API
  slug: open-claude-message-batches-api
- collection_type: open
  name: Claude Message Batches Messages API
  slug: open-claude-messages-api
- collection_type: open
  name: Claude Messages Message Batches Models API
  slug: open-claude-models-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/claude-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/claude-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/claude-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/claude-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/claude/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-analyze-document-from-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-batch-process-and-retrieve-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-cancel-and-delete-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-count-tokens-then-create-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-find-latest-batch-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-multi-turn-conversation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-select-model-and-create-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/claude-tool-use-round-trip-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/claude
- group: start
  title: ''
  type: Portal
  url: https://console.anthropic.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.anthropic.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.anthropic.com/en/docs/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anthropic.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.anthropic.com/en/api/rate-limits
- group: auth
  title: ''
  type: Authentication
  url: https://docs.anthropic.com/en/api/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.anthropic.com/en/release-notes/api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anthropic.com
- group: company
  title: ''
  type: Blog
  url: https://www.anthropic.com/news
- group: operate
  title: ''
  type: Support
  url: https://support.anthropic.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anthropic.com/legal/commercial-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthropic.com/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anthropics
- group: design
  title: ''
  type: SpectralRules
  url: rules/claude-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/claude-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/anthropics/claude-ai-mcp
created: '2024'
description: Anthropic's Claude AI assistant API for natural language processing and conversation.
examples:
- key_count: 1
  name: Claude Messages Batch Request Item Example
  slug: claude-messages-batch-request-item-example
- key_count: 2
  name: Claude Messages Cache Control Example
  slug: claude-messages-cache-control-example
- key_count: 0
  name: Claude Messages Content Block Example
  slug: claude-messages-content-block-example
- key_count: 0
  name: Claude Messages Content Block Param Example
  slug: claude-messages-content-block-param-example
- key_count: 4
  name: Claude Messages Count Tokens Request Example
  slug: claude-messages-count-tokens-request-example
- key_count: 1
  name: Claude Messages Create Message Batch Request Example
  slug: claude-messages-create-message-batch-request-example
- key_count: 11
  name: Claude Messages Create Message Request Example
  slug: claude-messages-create-message-request-example
- key_count: 2
  name: Claude Messages Deleted Message Batch Example
  slug: claude-messages-deleted-message-batch-example
- key_count: 5
  name: Claude Messages Document Block Param Example
  slug: claude-messages-document-block-param-example
- key_count: 2
  name: Claude Messages Error Example
  slug: claude-messages-error-example
- key_count: 2
  name: Claude Messages Image Block Param Example
  slug: claude-messages-image-block-param-example
- key_count: 8
  name: Claude Messages Message Batch Example
  slug: claude-messages-message-batch-example
- key_count: 4
  name: Claude Messages Message Batch List Example
  slug: claude-messages-message-batch-list-example
- key_count: 2
  name: Claude Messages Message Batch Result Example
  slug: claude-messages-message-batch-result-example
- key_count: 7
  name: Claude Messages Message Example
  slug: claude-messages-message-example
- key_count: 2
  name: Claude Messages Message Param Example
  slug: claude-messages-message-param-example
- key_count: 1
  name: Claude Messages Metadata Example
  slug: claude-messages-metadata-example
- key_count: 4
  name: Claude Messages Model Info Example
  slug: claude-messages-model-info-example
- key_count: 4
  name: Claude Messages Model List Example
  slug: claude-messages-model-list-example
- key_count: 2
  name: Claude Messages Output Config Example
  slug: claude-messages-output-config-example
- key_count: 3
  name: Claude Messages Text Block Example
  slug: claude-messages-text-block-example
- key_count: 2
  name: Claude Messages Text Block Param Example
  slug: claude-messages-text-block-param-example
- key_count: 3
  name: Claude Messages Thinking Block Example
  slug: claude-messages-thinking-block-example
- key_count: 3
  name: Claude Messages Thinking Block Param Example
  slug: claude-messages-thinking-block-param-example
- key_count: 2
  name: Claude Messages Thinking Config Example
  slug: claude-messages-thinking-config-example
- key_count: 1
  name: Claude Messages Token Count Example
  slug: claude-messages-token-count-example
- key_count: 3
  name: Claude Messages Tool Choice Example
  slug: claude-messages-tool-choice-example
- key_count: 4
  name: Claude Messages Tool Example
  slug: claude-messages-tool-example
- key_count: 4
  name: Claude Messages Tool Result Block Param Example
  slug: claude-messages-tool-result-block-param-example
- key_count: 4
  name: Claude Messages Tool Use Block Example
  slug: claude-messages-tool-use-block-example
- key_count: 4
  name: Claude Messages Tool Use Block Param Example
  slug: claude-messages-tool-use-block-param-example
- key_count: 4
  name: Claude Messages Usage Example
  slug: claude-messages-usage-example
features:
- description: Maintain context across multiple message exchanges for natural dialogue interactions.
  name: Multi-Turn Conversations
- description: Enable Claude to call external tools and functions to perform actions and retrieve data.
  name: Tool Use
- description: Process and analyze images alongside text for multimodal understanding.
  name: Vision
- description: Allow Claude to reason step-by-step for complex tasks with visible thinking process.
  name: Extended Thinking
- description: Receive responses in real-time via server-sent events for responsive user experiences.
  name: Streaming Responses
- description: Process large volumes of requests asynchronously at 50 percent reduced cost.
  name: Message Batches
- description: Pre-calculate token usage for messages including tools, images, and documents.
  name: Token Counting
finops:
- name: Claude Finops
  service_category: AI Infrastructure
  slug: claude-finops
image: https://www.anthropic.com/images/icons/anthropic-icon.png
integrations:
- description: Access Claude models through AWS Bedrock for enterprise deployment with AWS infrastructure.
  name: Amazon Bedrock
- description: Use Claude on Google Cloud through Vertex AI integration.
  name: Google Cloud Vertex AI
- description: Integrate Claude into LangChain pipelines for advanced AI application development.
  name: LangChain
- description: Connect Claude to external data sources and tools via the Model Context Protocol.
  name: MCP Protocol
json_schemas:
- name: BatchRequestItem
  property_count: 2
  slug: claude-batchrequestitem
- name: CacheControl
  property_count: 2
  slug: claude-cachecontrol
- name: ContentBlock
  property_count: 0
  slug: claude-contentblock
- name: ContentBlockParam
  property_count: 0
  slug: claude-contentblockparam
- name: CountTokensRequest
  property_count: 5
  slug: claude-counttokensrequest
- name: CreateMessageBatchRequest
  property_count: 1
  slug: claude-createmessagebatchrequest
- name: CreateMessageRequest
  property_count: 16
  slug: claude-createmessagerequest
- name: DeletedMessageBatch
  property_count: 2
  slug: claude-deletedmessagebatch
- name: DocumentBlockParam
  property_count: 6
  slug: claude-documentblockparam
- name: Error
  property_count: 2
  slug: claude-error
- name: ImageBlockParam
  property_count: 3
  slug: claude-imageblockparam
- name: Claude Message
  property_count: 0
  slug: claude-message
- name: MessageBatch
  property_count: 8
  slug: claude-messagebatch
- name: MessageBatchList
  property_count: 4
  slug: claude-messagebatchlist
- name: MessageBatchResult
  property_count: 2
  slug: claude-messagebatchresult
- name: MessageParam
  property_count: 2
  slug: claude-messageparam
- name: BatchRequestItem
  property_count: 1
  slug: claude-messages-batch-request-item
- name: CacheControl
  property_count: 2
  slug: claude-messages-cache-control
- name: ContentBlockParam
  property_count: 0
  slug: claude-messages-content-block-param
- name: ContentBlock
  property_count: 0
  slug: claude-messages-content-block
- name: CountTokensRequest
  property_count: 4
  slug: claude-messages-count-tokens-request
- name: CreateMessageBatchRequest
  property_count: 1
  slug: claude-messages-create-message-batch-request
- name: CreateMessageRequest
  property_count: 11
  slug: claude-messages-create-message-request
- name: DeletedMessageBatch
  property_count: 2
  slug: claude-messages-deleted-message-batch
- name: DocumentBlockParam
  property_count: 5
  slug: claude-messages-document-block-param
- name: Error
  property_count: 2
  slug: claude-messages-error
- name: ImageBlockParam
  property_count: 2
  slug: claude-messages-image-block-param
- name: MessageBatchList
  property_count: 4
  slug: claude-messages-message-batch-list
- name: MessageBatchResult
  property_count: 2
  slug: claude-messages-message-batch-result
- name: MessageBatch
  property_count: 8
  slug: claude-messages-message-batch
- name: MessageParam
  property_count: 2
  slug: claude-messages-message-param
- name: Message
  property_count: 7
  slug: claude-messages-message
- name: Metadata
  property_count: 1
  slug: claude-messages-metadata
- name: ModelInfo
  property_count: 4
  slug: claude-messages-model-info
- name: ModelList
  property_count: 4
  slug: claude-messages-model-list
- name: OutputConfig
  property_count: 2
  slug: claude-messages-output-config
- name: TextBlockParam
  property_count: 2
  slug: claude-messages-text-block-param
- name: TextBlock
  property_count: 3
  slug: claude-messages-text-block
- name: ThinkingBlockParam
  property_count: 3
  slug: claude-messages-thinking-block-param
- name: ThinkingBlock
  property_count: 3
  slug: claude-messages-thinking-block
- name: ThinkingConfig
  property_count: 2
  slug: claude-messages-thinking-config
- name: TokenCount
  property_count: 1
  slug: claude-messages-token-count
- name: ToolChoice
  property_count: 3
  slug: claude-messages-tool-choice
- name: ToolResultBlockParam
  property_count: 4
  slug: claude-messages-tool-result-block-param
- name: Tool
  property_count: 4
  slug: claude-messages-tool
- name: ToolUseBlockParam
  property_count: 4
  slug: claude-messages-tool-use-block-param
- name: ToolUseBlock
  property_count: 4
  slug: claude-messages-tool-use-block
- name: Usage
  property_count: 4
  slug: claude-messages-usage
- name: Metadata
  property_count: 1
  slug: claude-metadata
- name: ModelInfo
  property_count: 4
  slug: claude-modelinfo
- name: ModelList
  property_count: 4
  slug: claude-modellist
- name: OutputConfig
  property_count: 2
  slug: claude-outputconfig
- name: TextBlock
  property_count: 3
  slug: claude-textblock
- name: TextBlockParam
  property_count: 3
  slug: claude-textblockparam
- name: ThinkingBlock
  property_count: 3
  slug: claude-thinkingblock
- name: ThinkingBlockParam
  property_count: 3
  slug: claude-thinkingblockparam
- name: ThinkingConfig
  property_count: 2
  slug: claude-thinkingconfig
- name: TokenCount
  property_count: 1
  slug: claude-tokencount
- name: Tool
  property_count: 5
  slug: claude-tool
- name: Claude Tool Use
  property_count: 0
  slug: claude-tool-use
- name: ToolChoice
  property_count: 3
  slug: claude-toolchoice
- name: ToolResultBlockParam
  property_count: 5
  slug: claude-toolresultblockparam
- name: ToolUseBlock
  property_count: 4
  slug: claude-tooluseblock
- name: ToolUseBlockParam
  property_count: 5
  slug: claude-tooluseblockparam
- name: Usage
  property_count: 4
  slug: claude-usage
json_structures:
- name: Claude Messages Batch Request Item Structure
  property_count: 1
  slug: claude-messages-batch-request-item-structure
- name: Claude Messages Cache Control Structure
  property_count: 2
  slug: claude-messages-cache-control-structure
- name: Claude Messages Content Block Param Structure
  property_count: 0
  slug: claude-messages-content-block-param-structure
- name: Claude Messages Content Block Structure
  property_count: 0
  slug: claude-messages-content-block-structure
- name: Claude Messages Count Tokens Request Structure
  property_count: 4
  slug: claude-messages-count-tokens-request-structure
- name: Claude Messages Create Message Batch Request Structure
  property_count: 1
  slug: claude-messages-create-message-batch-request-structure
- name: Claude Messages Create Message Request Structure
  property_count: 11
  slug: claude-messages-create-message-request-structure
- name: Claude Messages Deleted Message Batch Structure
  property_count: 2
  slug: claude-messages-deleted-message-batch-structure
- name: Claude Messages Document Block Param Structure
  property_count: 5
  slug: claude-messages-document-block-param-structure
- name: Claude Messages Error Structure
  property_count: 2
  slug: claude-messages-error-structure
- name: Claude Messages Image Block Param Structure
  property_count: 2
  slug: claude-messages-image-block-param-structure
- name: Claude Messages Message Batch List Structure
  property_count: 4
  slug: claude-messages-message-batch-list-structure
- name: Claude Messages Message Batch Result Structure
  property_count: 2
  slug: claude-messages-message-batch-result-structure
- name: Claude Messages Message Batch Structure
  property_count: 8
  slug: claude-messages-message-batch-structure
- name: Claude Messages Message Param Structure
  property_count: 2
  slug: claude-messages-message-param-structure
- name: Claude Messages Message Structure
  property_count: 7
  slug: claude-messages-message-structure
- name: Claude Messages Metadata Structure
  property_count: 1
  slug: claude-messages-metadata-structure
- name: Claude Messages Model Info Structure
  property_count: 4
  slug: claude-messages-model-info-structure
- name: Claude Messages Model List Structure
  property_count: 4
  slug: claude-messages-model-list-structure
- name: Claude Messages Output Config Structure
  property_count: 2
  slug: claude-messages-output-config-structure
- name: Claude Messages Text Block Param Structure
  property_count: 2
  slug: claude-messages-text-block-param-structure
- name: Claude Messages Text Block Structure
  property_count: 3
  slug: claude-messages-text-block-structure
- name: Claude Messages Thinking Block Param Structure
  property_count: 3
  slug: claude-messages-thinking-block-param-structure
- name: Claude Messages Thinking Block Structure
  property_count: 3
  slug: claude-messages-thinking-block-structure
- name: Claude Messages Thinking Config Structure
  property_count: 2
  slug: claude-messages-thinking-config-structure
- name: Claude Messages Token Count Structure
  property_count: 1
  slug: claude-messages-token-count-structure
- name: Claude Messages Tool Choice Structure
  property_count: 3
  slug: claude-messages-tool-choice-structure
- name: Claude Messages Tool Result Block Param Structure
  property_count: 4
  slug: claude-messages-tool-result-block-param-structure
- name: Claude Messages Tool Structure
  property_count: 4
  slug: claude-messages-tool-structure
- name: Claude Messages Tool Use Block Param Structure
  property_count: 4
  slug: claude-messages-tool-use-block-param-structure
- name: Claude Messages Tool Use Block Structure
  property_count: 4
  slug: claude-messages-tool-use-block-structure
- name: Claude Messages Usage Structure
  property_count: 4
  slug: claude-messages-usage-structure
- name: Claude Structure
  property_count: 0
  slug: claude-structure
jsonld:
- class_count: 0
  name: Claude Context
  property_count: 20
  slug: claude-context
- class_count: 0
  name: Claude Messages Context
  property_count: 0
  slug: claude-messages-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Claude
nav: Providers
network: true
overview: 'Claude publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Message Batches API, Models API, and 3 more. Tagged areas include Artificial Intelligence, Chatbots, Conversational AI, Generative AI, and Large Language Models.


  The Claude catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Claude''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, changelog, engineering blog, and 23 more developer resources.'
plans:
- name: Claude Plans Pricing
  plan_count: 13
  slug: claude-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 38
  name: Claude Rate Limits
  slug: claude-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Claude API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: claude-jsonschema-spectral-rules
- effective_rule_count: 60
  extends:
  - spectral:oas
  name: Claude API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 11
  slug: claude-spectral-rules
score:
  band: strong
  composite: 55.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 71.2
    developer_ergonomics: 61.9
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/claude/refs/heads/main/screenshots/claude-2026-06-20T174448.png
security:
- kind: authentication
  name: Claude Authentication
  slug: claude-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Claude Domain Security
  slug: claude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Claude Vulnerability Disclosure
  slug: claude-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: claude
tags:
- Artificial Intelligence
- Chatbots
- Conversational AI
- Generative AI
- Large Language Models
- Machine-Learning
- Natural Language Processing
use_cases:
- description: Build conversational interfaces with context-aware responses and tool integration.
  name: AI-Powered Chat Applications
- description: Generate, edit, and transform text content for marketing, documentation, and creative writing.
  name: Content Generation
- description: Use Claude for code generation, review, debugging, and technical documentation.
  name: Code Assistance
- description: Extract information, summarize, and answer questions about documents and images.
  name: Document Analysis
- description: Process large datasets of prompts efficiently using the Message Batches API.
  name: Batch Processing
website: https://console.anthropic.com
---
