---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Chatgpt Agentic Access
  operation_count: 5
  slug: chatgpt-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: API for accessing OpenAI's ChatGPT language models for chat completions and conversations.
  name: ChatGPT API
  slug: chatgpt-api
- description: The Responses API is OpenAI's recommended API primitive for new projects, an evolution of Chat Completions with built-in tools like web search, file search, code interpreter, and support for agentic w
  name: OpenAI Responses API
  slug: openai-responses-api
arazzos:
- description: Run a chat completion offering a function tool and resolve the tool call.
  name: ChatGPT Chat Completion With Tool Calling
  slug: chatgpt-chat-completion-tool-call-workflow
- description: Create a stored response and poll it until generation completes.
  name: ChatGPT Create and Poll a Response
  slug: chatgpt-create-and-poll-response-workflow
- description: Send an image URL to the Responses API and retrieve a text description.
  name: ChatGPT Describe an Image Input
  slug: chatgpt-image-input-describe-workflow
- description: Classify input safety with a chat completion, then generate only if it is safe.
  name: ChatGPT Moderation Gate Before Generation
  slug: chatgpt-moderation-gate-generate-workflow
- description: Start a conversation and continue it by chaining previous_response_id.
  name: ChatGPT Multi-Turn Conversation
  slug: chatgpt-multi-turn-conversation-workflow
- description: Create a stored response, read its output, then delete it.
  name: ChatGPT Response Lifecycle With Cleanup
  slug: chatgpt-response-lifecycle-cleanup-workflow
- description: Generate a response constrained to a caller-supplied JSON schema.
  name: ChatGPT Structured JSON Output Response
  slug: chatgpt-structured-output-response-workflow
- description: Answer a question with the built-in web search tool and return citations.
  name: ChatGPT Web Search Grounded Answer
  slug: chatgpt-web-search-answer-workflow
artifact_total: 160
collections:
- collection_type: postman
  name: ChatGPT Chat Completions API
  slug: postman-chatgpt-chat-completions-api
- collection_type: postman
  name: ChatGPT Responses API
  slug: postman-chatgpt-responses-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ChatGPT Chat Completions API
  slug: open-chatgpt-chat-completions-api
- collection_type: open
  name: ChatGPT Chat Completions Responses API
  slug: open-chatgpt-responses-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/chatgpt-capability-edges.yml
- group: build
  title: ''
  type: Packages
  url: packages/chatgpt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/chatgpt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/chatgpt-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chatgpt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chatgpt-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/chatgpt-chat-completions-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/chatgpt-responses-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/chatgpt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chatgpt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chatgpt-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chatgpt-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/chatgpt-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/chatgpt-cli.yml
- group: design
  title: ''
  type: Components
  url: components/chatgpt-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chatgpt-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chatgpt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/chatgpt-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chatgpt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatgpt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chatgpt-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chatgpt/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-chat-completion-tool-call-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-create-and-poll-response-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-image-input-describe-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-moderation-gate-generate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-multi-turn-conversation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-response-lifecycle-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-structured-output-response-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/chatgpt-web-search-answer-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://platform.openai.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.openai.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://platform.openai.com/docs/api-reference/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://openai.com/pricing
- group: operate
  title: ''
  type: RateLimits
  url: https://platform.openai.com/docs/guides/rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://platform.openai.com/docs/changelog
- group: company
  title: ''
  type: Blog
  url: https://openai.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openai.com
- group: operate
  title: ''
  type: Support
  url: https://help.openai.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openai
- group: build
  title: ''
  type: SDKs
  url: https://developers.openai.com/api/docs/libraries/
- group: build
  title: ''
  type: CodeExamples
  url: https://cookbook.openai.com/
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/openai/openai-openapi/blob/master/openapi.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openai.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://openai.com/business-data/
- group: other
  title: ''
  type: Models
  url: https://platform.openai.com/docs/models
- group: start
  title: ''
  type: Signup
  url: https://platform.openai.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.openai.com/login
created: '2024'
description: OpenAI's ChatGPT API for conversational AI and language model interactions.
examples:
- key_count: 4
  name: Chatgpt Chat Completions Chat Completion Assistant Message Example
  slug: chatgpt-chat-completions-chat-completion-assistant-message-example
- key_count: 3
  name: Chatgpt Chat Completions Chat Completion Choice Example
  slug: chatgpt-chat-completions-chat-completion-choice-example
- key_count: 4
  name: Chatgpt Chat Completions Chat Completion Content Part Example
  slug: chatgpt-chat-completions-chat-completion-content-part-example
- key_count: 6
  name: Chatgpt Chat Completions Chat Completion Message Example
  slug: chatgpt-chat-completions-chat-completion-message-example
- key_count: 2
  name: Chatgpt Chat Completions Chat Completion Named Tool Choice Example
  slug: chatgpt-chat-completions-chat-completion-named-tool-choice-example
- key_count: 3
  name: Chatgpt Chat Completions Chat Completion Tool Call Example
  slug: chatgpt-chat-completions-chat-completion-tool-call-example
- key_count: 1
  name: Chatgpt Chat Completions Chat Completion Tool Example
  slug: chatgpt-chat-completions-chat-completion-tool-example
- key_count: 5
  name: Chatgpt Chat Completions Completion Usage Example
  slug: chatgpt-chat-completions-completion-usage-example
- key_count: 21
  name: Chatgpt Chat Completions Create Chat Completion Request Example
  slug: chatgpt-chat-completions-create-chat-completion-request-example
- key_count: 7
  name: Chatgpt Chat Completions Create Chat Completion Response Example
  slug: chatgpt-chat-completions-create-chat-completion-response-example
- key_count: 1
  name: Chatgpt Chat Completions Error Response Example
  slug: chatgpt-chat-completions-error-response-example
- key_count: 4
  name: Chatgpt Chat Completions Function Definition Example
  slug: chatgpt-chat-completions-function-definition-example
- key_count: 2
  name: Chatgpt Chat Completions Response Format Example
  slug: chatgpt-chat-completions-response-format-example
- key_count: 4
  name: Chatgpt Chat Completions Token Logprob Example
  slug: chatgpt-chat-completions-token-logprob-example
- key_count: 6
  name: Chatgpt Createchatcompletion Example
  slug: chatgpt-createchatcompletion-example
- key_count: 6
  name: Chatgpt Createresponse Example
  slug: chatgpt-createresponse-example
- key_count: 6
  name: Chatgpt Deleteresponse Example
  slug: chatgpt-deleteresponse-example
- key_count: 6
  name: Chatgpt Getresponse Example
  slug: chatgpt-getresponse-example
- key_count: 6
  name: Chatgpt Listresponseinputitems Example
  slug: chatgpt-listresponseinputitems-example
- key_count: 7
  name: Chatgpt Responses Annotation Example
  slug: chatgpt-responses-annotation-example
- key_count: 17
  name: Chatgpt Responses Create Response Request Example
  slug: chatgpt-responses-create-response-request-example
- key_count: 1
  name: Chatgpt Responses Error Response Example
  slug: chatgpt-responses-error-response-example
- key_count: 6
  name: Chatgpt Responses Response Input Content Part Example
  slug: chatgpt-responses-response-input-content-part-example
- key_count: 7
  name: Chatgpt Responses Response Input Item Example
  slug: chatgpt-responses-response-input-item-example
- key_count: 5
  name: Chatgpt Responses Response Input Item List Example
  slug: chatgpt-responses-response-input-item-list-example
- key_count: 21
  name: Chatgpt Responses Response Object Example
  slug: chatgpt-responses-response-object-example
- key_count: 4
  name: Chatgpt Responses Response Output Content Part Example
  slug: chatgpt-responses-response-output-content-part-example
- key_count: 9
  name: Chatgpt Responses Response Output Item Example
  slug: chatgpt-responses-response-output-item-example
- key_count: 2
  name: Chatgpt Responses Response Tool Choice Example
  slug: chatgpt-responses-response-tool-choice-example
- key_count: 16
  name: Chatgpt Responses Response Tool Example
  slug: chatgpt-responses-response-tool-example
- key_count: 5
  name: Chatgpt Responses Response Usage Example
  slug: chatgpt-responses-response-usage-example
features:
- description: Generate conversational responses using GPT models with support for text, function calling, structured outputs, vision inputs, and streaming.
  name: Chat Completions
- description: Next-generation API with built-in tools for web search, file search, computer use, and code interpreter supporting agentic workflows.
  name: Responses API
- description: Generate vector representations of text for search, clustering, classification, and recommendation use cases.
  name: Embeddings
- description: Create and edit images from text prompts using DALL-E and GPT Image models.
  name: Image Generation
- description: Text-to-speech generation, speech transcription, and translation using Whisper and other audio models.
  name: Audio and Speech
- description: Classify text and images to detect potentially harmful content across safety categories.
  name: Content Moderation
- description: Customize OpenAI models on your own training data for domain-specific performance improvements.
  name: Fine-Tuning
- description: Send asynchronous groups of requests at lower cost with higher rate limits.
  name: Batch Processing
- description: Ultra-low latency multimodal communication over WebRTC, WebSocket, and SIP.
  name: Realtime Communication
- description: Manage collections of processed files for retrieval-augmented generation with the file search tool.
  name: Vector Stores
finops:
- name: Chatgpt Finops
  service_category: AI / LLM
  slug: chatgpt-finops
image: https://openai.com/content/images/2023/05/openai-avatar.png
integrations:
- description: Deploy OpenAI models on Azure infrastructure with enterprise security, compliance, and regional availability.
  name: Microsoft Azure OpenAI
- description: Build LLM-powered applications using the LangChain framework with OpenAI model providers.
  name: LangChain
- description: Connect ChatGPT to thousands of apps for automated workflows without code.
  name: Zapier
- description: Integrate ChatGPT into Slack workspaces for team collaboration and AI-assisted communication.
  name: Slack
json_schemas:
- name: Annotation
  property_count: 7
  slug: chatgpt-annotation
- name: ChatGPT Chat Completion
  property_count: 8
  slug: chatgpt-chat-completion
- name: ChatCompletionAssistantMessage
  property_count: 4
  slug: chatgpt-chat-completions-chat-completion-assistant-message
- name: ChatCompletionChoice
  property_count: 3
  slug: chatgpt-chat-completions-chat-completion-choice
- name: ChatCompletionContentPart
  property_count: 4
  slug: chatgpt-chat-completions-chat-completion-content-part
- name: ChatCompletionMessage
  property_count: 6
  slug: chatgpt-chat-completions-chat-completion-message
- name: ChatCompletionNamedToolChoice
  property_count: 2
  slug: chatgpt-chat-completions-chat-completion-named-tool-choice
- name: ChatCompletionToolCall
  property_count: 3
  slug: chatgpt-chat-completions-chat-completion-tool-call
- name: ChatCompletionTool
  property_count: 1
  slug: chatgpt-chat-completions-chat-completion-tool
- name: CompletionUsage
  property_count: 5
  slug: chatgpt-chat-completions-completion-usage
- name: CreateChatCompletionRequest
  property_count: 21
  slug: chatgpt-chat-completions-create-chat-completion-request
- name: CreateChatCompletionResponse
  property_count: 7
  slug: chatgpt-chat-completions-create-chat-completion-response
- name: ErrorResponse
  property_count: 1
  slug: chatgpt-chat-completions-error-response
- name: FunctionDefinition
  property_count: 4
  slug: chatgpt-chat-completions-function-definition
- name: ResponseFormat
  property_count: 2
  slug: chatgpt-chat-completions-response-format
- name: TokenLogprob
  property_count: 4
  slug: chatgpt-chat-completions-token-logprob
- name: ChatCompletionAssistantMessage
  property_count: 4
  slug: chatgpt-chatcompletionassistantmessage
- name: ChatCompletionChoice
  property_count: 4
  slug: chatgpt-chatcompletionchoice
- name: ChatCompletionContentPart
  property_count: 4
  slug: chatgpt-chatcompletioncontentpart
- name: ChatCompletionMessage
  property_count: 6
  slug: chatgpt-chatcompletionmessage
- name: ChatCompletionNamedToolChoice
  property_count: 2
  slug: chatgpt-chatcompletionnamedtoolchoice
- name: ChatCompletionTool
  property_count: 2
  slug: chatgpt-chatcompletiontool
- name: ChatCompletionToolCall
  property_count: 3
  slug: chatgpt-chatcompletiontoolcall
- name: CompletionUsage
  property_count: 5
  slug: chatgpt-completionusage
- name: CreateChatCompletionRequest
  property_count: 22
  slug: chatgpt-createchatcompletionrequest
- name: CreateChatCompletionResponse
  property_count: 8
  slug: chatgpt-createchatcompletionresponse
- name: CreateResponseRequest
  property_count: 17
  slug: chatgpt-createresponserequest
- name: ErrorResponse
  property_count: 1
  slug: chatgpt-errorresponse
- name: FunctionDefinition
  property_count: 4
  slug: chatgpt-functiondefinition
- name: ChatGPT Response
  property_count: 21
  slug: chatgpt-response
- name: ResponseFormat
  property_count: 2
  slug: chatgpt-responseformat
- name: ResponseInputContentPart
  property_count: 6
  slug: chatgpt-responseinputcontentpart
- name: ResponseInputItem
  property_count: 7
  slug: chatgpt-responseinputitem
- name: ResponseInputItemList
  property_count: 5
  slug: chatgpt-responseinputitemlist
- name: ResponseObject
  property_count: 22
  slug: chatgpt-responseobject
- name: ResponseOutputContentPart
  property_count: 4
  slug: chatgpt-responseoutputcontentpart
- name: ResponseOutputItem
  property_count: 9
  slug: chatgpt-responseoutputitem
- name: Annotation
  property_count: 7
  slug: chatgpt-responses-annotation
- name: CreateResponseRequest
  property_count: 17
  slug: chatgpt-responses-create-response-request
- name: ErrorResponse
  property_count: 1
  slug: chatgpt-responses-error-response
- name: ResponseInputContentPart
  property_count: 6
  slug: chatgpt-responses-response-input-content-part
- name: ResponseInputItemList
  property_count: 5
  slug: chatgpt-responses-response-input-item-list
- name: ResponseInputItem
  property_count: 7
  slug: chatgpt-responses-response-input-item
- name: ResponseObject
  property_count: 21
  slug: chatgpt-responses-response-object
- name: ResponseOutputContentPart
  property_count: 4
  slug: chatgpt-responses-response-output-content-part
- name: ResponseOutputItem
  property_count: 9
  slug: chatgpt-responses-response-output-item
- name: ResponseToolChoice
  property_count: 2
  slug: chatgpt-responses-response-tool-choice
- name: ResponseTool
  property_count: 16
  slug: chatgpt-responses-response-tool
- name: ResponseUsage
  property_count: 5
  slug: chatgpt-responses-response-usage
- name: ResponseTool
  property_count: 16
  slug: chatgpt-responsetool
- name: ResponseToolChoice
  property_count: 2
  slug: chatgpt-responsetoolchoice
- name: ResponseUsage
  property_count: 5
  slug: chatgpt-responseusage
- name: TokenLogprob
  property_count: 4
  slug: chatgpt-tokenlogprob
json_structures:
- name: Chatgpt Chat Completions Chat Completion Assistant Message Structure
  property_count: 4
  slug: chatgpt-chat-completions-chat-completion-assistant-message-structure
- name: Chatgpt Chat Completions Chat Completion Choice Structure
  property_count: 3
  slug: chatgpt-chat-completions-chat-completion-choice-structure
- name: Chatgpt Chat Completions Chat Completion Content Part Structure
  property_count: 4
  slug: chatgpt-chat-completions-chat-completion-content-part-structure
- name: Chatgpt Chat Completions Chat Completion Message Structure
  property_count: 6
  slug: chatgpt-chat-completions-chat-completion-message-structure
- name: Chatgpt Chat Completions Chat Completion Named Tool Choice Structure
  property_count: 2
  slug: chatgpt-chat-completions-chat-completion-named-tool-choice-structure
- name: Chatgpt Chat Completions Chat Completion Tool Call Structure
  property_count: 3
  slug: chatgpt-chat-completions-chat-completion-tool-call-structure
- name: Chatgpt Chat Completions Chat Completion Tool Structure
  property_count: 1
  slug: chatgpt-chat-completions-chat-completion-tool-structure
- name: Chatgpt Chat Completions Completion Usage Structure
  property_count: 5
  slug: chatgpt-chat-completions-completion-usage-structure
- name: Chatgpt Chat Completions Create Chat Completion Request Structure
  property_count: 21
  slug: chatgpt-chat-completions-create-chat-completion-request-structure
- name: Chatgpt Chat Completions Create Chat Completion Response Structure
  property_count: 7
  slug: chatgpt-chat-completions-create-chat-completion-response-structure
- name: Chatgpt Chat Completions Error Response Structure
  property_count: 1
  slug: chatgpt-chat-completions-error-response-structure
- name: Chatgpt Chat Completions Function Definition Structure
  property_count: 4
  slug: chatgpt-chat-completions-function-definition-structure
- name: Chatgpt Chat Completions Response Format Structure
  property_count: 2
  slug: chatgpt-chat-completions-response-format-structure
- name: Chatgpt Chat Completions Token Logprob Structure
  property_count: 4
  slug: chatgpt-chat-completions-token-logprob-structure
- name: Chatgpt Responses Annotation Structure
  property_count: 7
  slug: chatgpt-responses-annotation-structure
- name: Chatgpt Responses Create Response Request Structure
  property_count: 17
  slug: chatgpt-responses-create-response-request-structure
- name: Chatgpt Responses Error Response Structure
  property_count: 1
  slug: chatgpt-responses-error-response-structure
- name: Chatgpt Responses Response Input Content Part Structure
  property_count: 6
  slug: chatgpt-responses-response-input-content-part-structure
- name: Chatgpt Responses Response Input Item List Structure
  property_count: 5
  slug: chatgpt-responses-response-input-item-list-structure
- name: Chatgpt Responses Response Input Item Structure
  property_count: 7
  slug: chatgpt-responses-response-input-item-structure
- name: Chatgpt Responses Response Object Structure
  property_count: 21
  slug: chatgpt-responses-response-object-structure
- name: Chatgpt Responses Response Output Content Part Structure
  property_count: 4
  slug: chatgpt-responses-response-output-content-part-structure
- name: Chatgpt Responses Response Output Item Structure
  property_count: 9
  slug: chatgpt-responses-response-output-item-structure
- name: Chatgpt Responses Response Tool Choice Structure
  property_count: 2
  slug: chatgpt-responses-response-tool-choice-structure
- name: Chatgpt Responses Response Tool Structure
  property_count: 16
  slug: chatgpt-responses-response-tool-structure
- name: Chatgpt Responses Response Usage Structure
  property_count: 5
  slug: chatgpt-responses-response-usage-structure
- name: Chatgpt Structure
  property_count: 0
  slug: chatgpt-structure
jsonld:
- class_count: 0
  name: Chatgpt Chat Completions Context
  property_count: 0
  slug: chatgpt-chat-completions-context
- class_count: 0
  name: Chatgpt Context
  property_count: 16
  slug: chatgpt-context
- class_count: 0
  name: Chatgpt Responses Context
  property_count: 0
  slug: chatgpt-responses-context
layout: provider
mcp_servers:
- description: OpenAI publishes an official hosted MCP server that exposes its developer documentation (search + page retrieval) over Streamable HTTP with no authentication. It is documentation-only and does not cal
  name: openaiDeveloperDocs
  slug: openaideveloperdocs
modified: '2026-06-20'
name: ChatGPT
nav: Providers
network: true
overview: 'ChatGPT publishes 2 APIs on the [APIs.io](https://apis.io/) network, including OpenAI Responses API, and 1 more. Tagged areas include Agents, Artificial Intelligence, ChatGPT, Embeddings, and Fine-Tuning.


  The ChatGPT catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  ChatGPT''s developer surface includes changelog, CLI, authentication, developer portal, documentation, getting-started guide, pricing, and 43 more developer resources.'
plans:
- name: Chatgpt Plans Pricing
  plan_count: 7
  slug: chatgpt-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Chatgpt Rate Limits
  slug: chatgpt-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: ChatGPT API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: chatgpt-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: ChatGPT API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: chatgpt-spectral-rules
score:
  band: strong
  composite: 56.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 59.5
    catalog_earned_first_party: 0.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 58.7
    developer_ergonomics: 65.5
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 57.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatgpt/refs/heads/main/screenshots/chatgpt-2026-08-17T082057.png
security:
- kind: authentication
  name: Chatgpt Authentication
  slug: chatgpt-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chatgpt Domain Security
  slug: chatgpt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chatgpt Vulnerability Disclosure
  slug: chatgpt-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Chatgpt Trust Center
  slug: chatgpt-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: chatgpt
tags:
- Agents
- Artificial Intelligence
- ChatGPT
- Embeddings
- Fine-Tuning
- GPT-4
- GPT-5
- Language Model
- OpenAI
- Real-Time
use_cases:
- description: Build AI-powered chatbots and support agents that handle customer inquiries, troubleshoot issues, and escalate complex cases.
  name: Customer Support Automation
- description: Generate marketing copy, blog posts, product descriptions, and creative content at scale.
  name: Content Generation
- description: Help developers write, review, debug, and explain code across multiple programming languages.
  name: Code Assistance
- description: Extract insights from unstructured text, summarize documents, and perform sentiment analysis.
  name: Data Analysis
- description: Build applications that process text, images, and audio inputs together for richer user experiences.
  name: Multimodal Applications
- description: Create autonomous AI agents that use tools, search the web, and execute multi-step tasks.
  name: Agentic Workflows
website: https://platform.openai.com
---
