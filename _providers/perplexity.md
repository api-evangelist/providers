---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Perplexity Agentic Access
  operation_count: 9
  slug: perplexity-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 12
apis:
- description: What do you want to know?
  name: Perplexity
  slug: perplexity
- description: The Async Chat Completions API enables developers to submit long-running chat completion requests for background processing. Requests are queued and processed asynchronously, returning a unique identi
  name: Perplexity Async Chat Completions API
  slug: async-chat-completions-api
- description: The Search API enables developers to perform ranked web searches with advanced filtering including domain, language, country, and date recency controls, returning structured results with titles, URLs,
  name: Perplexity Search API
  slug: search-api
- description: 'The Responses API (Agentic Research API) provides access to third-party frontier models from providers like OpenAI, Anthropic, Google, and xAI with integrated web search tools, URL fetching, function '
  name: Perplexity Responses API
  slug: responses-api
- description: The Embeddings API generates high-quality text embeddings for semantic search and retrieval, offering both standard embeddings for independent texts and contextualized embeddings for document chunks t
  name: Perplexity Embeddings API
  slug: embeddings-api
- description: The Agent API from Perplexity — 1 operation(s) for agent.
  name: Perplexity Agent API
  slug: perplexity-agent-api
- description: The Async API from Perplexity — 2 operation(s) for async.
  name: Perplexity Async API
  slug: perplexity-async-api
- description: The Contextualizedembeddings API from Perplexity — 1 operation(s) for contextualizedembeddings.
  name: Perplexity Contextualizedembeddings API
  slug: perplexity-contextualizedembeddings-api
- description: The Embeddings API from Perplexity — 1 operation(s) for embeddings.
  name: Perplexity Embeddings API
  slug: perplexity-embeddings-api
- description: The Models API from Perplexity — 1 operation(s) for models.
  name: Perplexity Models API
  slug: perplexity-models-api
- description: The Search API from Perplexity — 1 operation(s) for search.
  name: Perplexity Search API
  slug: perplexity-search-api
- description: The Sonar API from Perplexity — 1 operation(s) for sonar.
  name: Perplexity Sonar API
  slug: perplexity-sonar-api
artifact_total: 166
asyncapis:
- description: AsyncAPI description of Perplexity's HTTP-based streaming surface. IMPORTANT TRANSPORT NOTE ------------------------ Perplexity does NOT expose a WebSocket (ws://, wss://) API. Every streaming interac
  name: Perplexity Streaming API (HTTP + Server-Sent Events)
  slug: perplexity-asyncapi
collections:
- collection_type: postman
  name: Perplexity AI Agent API
  slug: postman-perplexity-agent-api
- collection_type: postman
  name: Perplexity AI Agent Async API
  slug: postman-perplexity-async-api
- collection_type: postman
  name: Perplexity AI Agent Contextualizedembeddings API
  slug: postman-perplexity-contextualizedembeddings-api
- collection_type: postman
  name: Perplexity AI Agent Embeddings API
  slug: postman-perplexity-embeddings-api
- collection_type: postman
  name: Perplexity AI Agent Models API
  slug: postman-perplexity-models-api
- collection_type: postman
  name: Perplexity AI Agent Search API
  slug: postman-perplexity-search-api
- collection_type: postman
  name: Perplexity AI Agent Sonar API
  slug: postman-perplexity-sonar-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Perplexity AI Agent API
  slug: open-perplexity-agent-api
- collection_type: open
  name: Perplexity AI Agent Async API
  slug: open-perplexity-async-api
- collection_type: open
  name: Perplexity AI Agent Contextualizedembeddings API
  slug: open-perplexity-contextualizedembeddings-api
- collection_type: open
  name: Perplexity AI Agent Embeddings API
  slug: open-perplexity-embeddings-api
- collection_type: open
  name: Perplexity AI Agent Models API
  slug: open-perplexity-models-api
- collection_type: open
  name: Perplexity AI Agent Search API
  slug: open-perplexity-search-api
- collection_type: open
  name: Perplexity AI Agent Sonar API
  slug: open-perplexity-sonar-api
- collection_type: open
  name: Perplexity AI API
  slug: open-perplexity
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/perplexity/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/perplexity-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/perplexity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/perplexity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/perplexity-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/perplexity-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.perplexity.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.perplexity.ai/reference/post_chat_completions
- group: other
  title: ''
  type: Models
  url: https://docs.perplexity.ai/docs/model-cards
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.perplexity.ai/docs/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perplexity.ai/hub/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perplexity.ai/hub/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.perplexity.ai/hub/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.perplexity.ai/docs/getting-started/quickstart
- group: commercial
  title: ''
  type: Pricing Page
  url: https://docs.perplexity.ai/docs/getting-started/pricing
- group: other
  title: ''
  type: Model Directory
  url: https://docs.perplexity.ai/docs/getting-started/models
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.perplexity.ai/docs/resources/changelog
- group: operate
  title: ''
  type: Product Change Log
  url: https://www.perplexity.ai/changelog
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.perplexity.ai/guides/usage-tiers
- group: start
  title: ''
  type: Signup
  url: https://perplexity.ai/account/api
- group: other
  title: ''
  type: Dashboard
  url: https://www.perplexity.ai/account/api/group
- group: other
  title: ''
  type: API Playground
  url: https://perplexity.ai/account/api/playground/search
- group: build
  title: ''
  type: SDKs
  url: https://docs.perplexity.ai/guides/perplexity-sdk
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/perplexityai
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/perplexityai/perplexity-py
- group: other
  title: ''
  type: Best Practices
  url: https://docs.perplexity.ai/guides/search-best-practices
- group: agent
  title: ''
  type: MCP Server
  url: https://docs.perplexity.ai/guides/mcp-server
- group: operate
  title: ''
  type: Support
  url: https://www.perplexity.ai/help-center/en
- group: operate
  title: ''
  type: Forums
  url: https://community.perplexity.ai
- group: start
  title: ''
  type: Portal
  url: https://www.perplexity.ai/api-platform
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.perplexity.ai/llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.perplexity.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.perplexity.ai
- group: auth
  title: ''
  type: Authentication
  url: https://docs.perplexity.ai/guides/api-key-management
- group: operate
  title: ''
  type: StatusPage
  url: https://status.perplexity.com
- group: operate
  title: ''
  type: RoadMap
  url: https://docs.perplexity.ai/feature-roadmap
- group: learn
  title: ''
  type: Cookbook
  url: https://docs.perplexity.ai/docs/cookbook
- group: docs
  title: ''
  type: Prompt Guide
  url: https://docs.perplexity.ai/guides/prompt-guide
- group: docs
  title: ''
  type: Structured Outputs Guide
  url: https://docs.perplexity.ai/guides/structured-outputs
- group: docs
  title: ''
  type: Performance Guide
  url: https://docs.perplexity.ai/guides/perplexity-sdk-performance
- group: docs
  title: ''
  type: Date Range Filter Guide
  url: https://docs.perplexity.ai/guides/date-range-filter-guide
- group: docs
  title: ''
  type: Academic Filter Guide
  url: https://docs.perplexity.ai/guides/academic-filter-guide
- group: other
  title: ''
  type: Crawlers
  url: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- group: commercial
  title: ''
  type: API Terms of Service
  url: https://www.perplexity.ai/hub/legal/perplexity-api-terms-of-service
- group: operate
  title: ''
  type: Forums
  url: https://docs.perplexity.ai/discussions/discussions
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/perplexity-ai
- group: other
  title: ''
  type: X
  url: https://x.com/perplexity_ai
created: '2025-02-21'
description: Perplexity AI is an answer engine that delivers accurate answers to complex questions using large language models with real-time web search capabilities.
examples:
- key_count: 6
  name: Perplexity Create Async Chat Completions Async Chat Completions Post Example
  slug: perplexity-create-async-chat-completions-async-chat-completions-post-example
- key_count: 6
  name: Perplexity Listmodels Example
  slug: perplexity-listmodels-example
features:
- Sonar at $1/$1 MTok + $5-$12/1K searches
- Sonar Pro at $3/$15 MTok + $6-$14/1K searches
- Sonar Reasoning Pro at $2/$8 MTok
- Sonar Deep Research at $2/$8 MTok + $5/1K queries + $2/MTok citations
- Web-grounded answers with inline citations
- OpenAI-compatible Chat Completions
- Search context size affects pricing
- Default 50 req/min Sonar, 5 req/min Deep Research
- Tiered spend limits starting at $5/mo
- Citation tokens and reasoning tokens billed separately on Deep Research
- Multi-step research synthesis
- Filter by date, domain, recency
- Structured output (JSON schema)
- Image input on Sonar Pro
- Streaming responses
- Asynchronous batch endpoint (beta)
finops:
- name: Perplexity Finops
  service_category: AI Search
  slug: perplexity-finops
graphqls:
- description: Perplexity AI is a conversational AI search engine. Their API provides access to online and offline AI models for answering questions with real-time search grounding, citation attribution, and streami
  name: Perplexity GraphQL API
  slug: perplexity-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/perplexity.png
json_schemas:
- name: Annotation
  property_count: 5
  slug: perplexity-annotation
- name: ApiChatCompletionsRequest
  property_count: 26
  slug: perplexity-apichatcompletionsrequest
- name: ApiPublicSearchResult
  property_count: 6
  slug: perplexity-apipublicsearchresult
- name: ApiSearchPage
  property_count: 5
  slug: perplexity-apisearchpage
- name: ApiSearchRequest
  property_count: 0
  slug: perplexity-apisearchrequest
- name: ApiSearchResponse
  property_count: 3
  slug: perplexity-apisearchresponse
- name: AsyncApiChatCompletionsRequest
  property_count: 2
  slug: perplexity-asyncapichatcompletionsrequest
- name: AsyncApiChatCompletionsResponse
  property_count: 9
  slug: perplexity-asyncapichatcompletionsresponse
- name: AsyncApiChatCompletionsResponseSummary
  property_count: 7
  slug: perplexity-asyncapichatcompletionsresponsesummary
- name: AsyncProcessingStatus
  property_count: 0
  slug: perplexity-asyncprocessingstatus
- name: ChatMessage
  property_count: 2
  slug: perplexity-chatmessage-input
- name: ChatMessage
  property_count: 2
  slug: perplexity-chatmessage-output
- name: ChatMessageContentFileChunk
  property_count: 3
  slug: perplexity-chatmessagecontentfilechunk
- name: ChatMessageContentImageChunk
  property_count: 2
  slug: perplexity-chatmessagecontentimagechunk
- name: ChatMessageContentPDFChunk
  property_count: 2
  slug: perplexity-chatmessagecontentpdfchunk
- name: ChatMessageContentTextChunk
  property_count: 2
  slug: perplexity-chatmessagecontenttextchunk
- name: ChatMessageContentVideoChunk
  property_count: 2
  slug: perplexity-chatmessagecontentvideochunk
- name: ChatMessageRole
  property_count: 0
  slug: perplexity-chatmessagerole
- name: Choice
  property_count: 4
  slug: perplexity-choice
- name: CompletionResponse
  property_count: 10
  slug: perplexity-completionresponse
- name: CompletionResponseStatus
  property_count: 0
  slug: perplexity-completionresponsestatus
- name: CompletionResponseType
  property_count: 0
  slug: perplexity-completionresponsetype
- name: ContentPart
  property_count: 3
  slug: perplexity-contentpart
- name: ContentPartType
  property_count: 0
  slug: perplexity-contentparttype
- name: Contextualized Embedding Object
  property_count: 3
  slug: perplexity-contextualizedembeddingobject
- name: Contextualized Embeddings Request
  property_count: 4
  slug: perplexity-contextualizedembeddingsrequest
- name: Contextualized Embeddings Response
  property_count: 4
  slug: perplexity-contextualizedembeddingsresponse
- name: Cost
  property_count: 7
  slug: perplexity-cost
- name: Currency
  property_count: 0
  slug: perplexity-currency
- name: Date
  property_count: 0
  slug: perplexity-date
- name: DateFilters
  property_count: 5
  slug: perplexity-datefilters
- name: Embedding Object
  property_count: 3
  slug: perplexity-embeddingobject
- name: Embeddings Request
  property_count: 4
  slug: perplexity-embeddingsrequest
- name: Embeddings Response
  property_count: 4
  slug: perplexity-embeddingsresponse
- name: Embeddings Usage
  property_count: 3
  slug: perplexity-embeddingsusage
- name: ErrorInfo
  property_count: 3
  slug: perplexity-errorinfo
- name: EventType
  property_count: 0
  slug: perplexity-eventtype
- name: ExecutePythonStepDetails
  property_count: 2
  slug: perplexity-executepythonstepdetails
- name: FetchUrlContentStepDetails
  property_count: 1
  slug: perplexity-fetchurlcontentstepdetails
- name: FetchUrlQueriesEvent
  property_count: 4
  slug: perplexity-fetchurlqueriesevent
- name: FetchUrlResultsEvent
  property_count: 4
  slug: perplexity-fetchurlresultsevent
- name: FetchUrlResultsOutputItem
  property_count: 2
  slug: perplexity-fetchurlresultsoutputitem
- name: FetchUrlTool
  property_count: 2
  slug: perplexity-fetchurltool
- name: FinanceSearchStepDetails
  property_count: 2
  slug: perplexity-financesearchstepdetails
- name: FinanceSearchTool
  property_count: 1
  slug: perplexity-financesearchtool
- name: FunctionCallInput
  property_count: 5
  slug: perplexity-functioncallinput
- name: FunctionCallOutputInput
  property_count: 5
  slug: perplexity-functioncalloutputinput
- name: FunctionCallOutputItem
  property_count: 7
  slug: perplexity-functioncalloutputitem
- name: FunctionTool
  property_count: 5
  slug: perplexity-functiontool
- name: HTTPValidationError
  property_count: 1
  slug: perplexity-httpvalidationerror
- name: ImageResult
  property_count: 5
  slug: perplexity-imageresult
- name: Input
  property_count: 0
  slug: perplexity-input
- name: InputContent
  property_count: 0
  slug: perplexity-inputcontent
- name: InputContentPart
  property_count: 3
  slug: perplexity-inputcontentpart
- name: InputItem
  property_count: 0
  slug: perplexity-inputitem
- name: InputMessage
  property_count: 3
  slug: perplexity-inputmessage
- name: JSONSchema
  property_count: 4
  slug: perplexity-jsonschema
- name: JSONSchemaFormat
  property_count: 4
  slug: perplexity-jsonschemaformat
- name: ListAsyncApiChatCompletionsResponse
  property_count: 2
  slug: perplexity-listasyncapichatcompletionsresponse
- name: ListModelsResponse
  property_count: 2
  slug: perplexity-listmodelsresponse
- name: MessageOutputItem
  property_count: 5
  slug: perplexity-messageoutputitem
- name: Model
  property_count: 4
  slug: perplexity-model
- name: OutputItem
  property_count: 0
  slug: perplexity-outputitem
- name: OutputItemAddedEvent
  property_count: 4
  slug: perplexity-outputitemaddedevent
- name: OutputItemDoneEvent
  property_count: 4
  slug: perplexity-outputitemdoneevent
- name: ReasoningConfig
  property_count: 1
  slug: perplexity-reasoningconfig
- name: ReasoningStartedEvent
  property_count: 3
  slug: perplexity-reasoningstartedevent
- name: ReasoningStep
  property_count: 6
  slug: perplexity-reasoningstep-output
- name: ReasoningStoppedEvent
  property_count: 3
  slug: perplexity-reasoningstoppedevent
- name: ResponseCompletedEvent
  property_count: 3
  slug: perplexity-responsecompletedevent
- name: ResponseCreatedEvent
  property_count: 3
  slug: perplexity-responsecreatedevent
- name: ResponseFailedEvent
  property_count: 3
  slug: perplexity-responsefailedevent
- name: ResponseFormat
  property_count: 2
  slug: perplexity-responseformat
- name: ResponseFormatJSONSchema
  property_count: 2
  slug: perplexity-responseformatjsonschema
- name: ResponseFormatText
  property_count: 1
  slug: perplexity-responseformattext
- name: ResponseInProgressEvent
  property_count: 3
  slug: perplexity-responseinprogressevent
- name: ResponsesCost
  property_count: 7
  slug: perplexity-responsescost
- name: ResponsesObjectType
  property_count: 0
  slug: perplexity-responsesobjecttype
- name: ResponsesRequest
  property_count: 12
  slug: perplexity-responsesrequest
- name: ResponsesResponse
  property_count: 8
  slug: perplexity-responsesresponse
- name: ResponseStreamEvent
  property_count: 0
  slug: perplexity-responsestreamevent
- name: ResponsesUsage
  property_count: 6
  slug: perplexity-responsesusage
- name: RoleType
  property_count: 0
  slug: perplexity-roletype
- name: SearchDomainFilter
  property_count: 1
  slug: perplexity-searchdomainfilter
- name: SearchQueriesEvent
  property_count: 4
  slug: perplexity-searchqueriesevent
- name: SearchRecencyFilter
  property_count: 0
  slug: perplexity-searchrecencyfilter
- name: SearchResult
  property_count: 7
  slug: perplexity-searchresult
- name: SearchResultsEvent
  property_count: 5
  slug: perplexity-searchresultsevent
- name: SearchResultsOutputItem
  property_count: 3
  slug: perplexity-searchresultsoutputitem
- name: SearchSource
  property_count: 0
  slug: perplexity-searchsource
- name: Status
  property_count: 0
  slug: perplexity-status
- name: TextDeltaEvent
  property_count: 6
  slug: perplexity-textdeltaevent
- name: TextDoneEvent
  property_count: 6
  slug: perplexity-textdoneevent
- name: Tool
  property_count: 0
  slug: perplexity-tool
- name: ToolCall
  property_count: 3
  slug: perplexity-toolcall
- name: ToolCallDetails
  property_count: 1
  slug: perplexity-toolcalldetails
- name: ToolCallFunction
  property_count: 2
  slug: perplexity-toolcallfunction
- name: ToolUserLocation
  property_count: 5
  slug: perplexity-tooluserlocation
- name: URL
  property_count: 1
  slug: perplexity-url
- name: UrlContent
  property_count: 3
  slug: perplexity-urlcontent
- name: UsageInfo
  property_count: 8
  slug: perplexity-usageinfo
- name: UserLocation
  property_count: 5
  slug: perplexity-userlocation
- name: ValidationError
  property_count: 3
  slug: perplexity-validationerror
- name: VideoURL
  property_count: 2
  slug: perplexity-videourl
- name: WebSearchFilters
  property_count: 0
  slug: perplexity-websearchfilters
- name: WebSearchOptions
  property_count: 4
  slug: perplexity-websearchoptions
- name: WebSearchStepDetails
  property_count: 2
  slug: perplexity-websearchstepdetails
- name: WebSearchTool
  property_count: 5
  slug: perplexity-websearchtool
json_structures:
- name: Perplexity Structure
  property_count: 0
  slug: perplexity-structure
layout: provider
modified: '2026-05-29'
name: Perplexity
nav: Providers
network: true
overview: 'Perplexity publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Async Chat Completions API, Responses API, Agent API, and 6 more.


  The Perplexity catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Perplexity''s developer surface includes authentication, getting-started guide, API reference, pricing, engineering blog, changelog, signup flow, and 40 more developer resources.'
plans:
- name: Perplexity Plans Pricing
  plan_count: 4
  slug: perplexity-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Perplexity Rate Limits
  slug: perplexity-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Perplexity API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: perplexity-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Perplexity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: perplexity-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.3
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 67.4
    developer_ergonomics: 69.0
    discoverability: 53.7
    governance: 13.6
    operational_transparency: 50.0
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/perplexity/refs/heads/main/screenshots/perplexity-2026-06-20T191624.png
security:
- kind: authentication
  name: Perplexity Authentication
  slug: perplexity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Perplexity Domain Security
  slug: perplexity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Perplexity Vulnerability Disclosure
  slug: perplexity-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: perplexity
website: https://www.perplexity.ai
---
