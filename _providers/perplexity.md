---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 67.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Perplexity Agentic Access
  operation_count: 9
  slug: perplexity-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 2
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
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Agent API from Perplexity — 1 operation(s) for agent.
  name: Perplexity Agent API
  slug: perplexity-agent-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Async API from Perplexity — 2 operation(s) for async.
  name: Perplexity Async API
  slug: perplexity-async-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Contextualizedembeddings API from Perplexity — 1 operation(s) for contextualizedembeddings.
  name: Perplexity Contextualizedembeddings API
  slug: perplexity-contextualizedembeddings-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Embeddings API from Perplexity — 1 operation(s) for embeddings.
  name: Perplexity Embeddings API
  slug: perplexity-embeddings-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Models API from Perplexity — 1 operation(s) for models.
  name: Perplexity Models API
  slug: perplexity-models-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Search API from Perplexity — 1 operation(s) for search.
  name: Perplexity Search API
  slug: perplexity-search-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Decisions API from Perplexity — 1 operation(s) for decisions. Ask yes/no, multiple-choice, and rating questions about your content and get probabilities back (gateway preview).
  name: Perplexity Decisions API
  slug: perplexity-decisions-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Sonar API from Perplexity — 1 operation(s) for sonar.
  name: Perplexity Sonar API
  slug: perplexity-sonar-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Admin API from Perplexity — 1 operation(s) for admin.
  name: Perplexity Admin API
  slug: perplexity-admin-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Analytics API from Perplexity — 2 operation(s) for analytics.
  name: Perplexity Analytics API
  slug: perplexity-analytics-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Batches API from Perplexity — 6 operation(s) for batches.
  name: Perplexity Batches API
  slug: perplexity-batches-api
- baseURL: https://api.perplexity.ai
  baseurl_source: declared
  description: The Skills API from Perplexity — 4 operation(s) for skills.
  name: Perplexity Skills API
  slug: perplexity-skills-api
artifact_total: 170
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
- group: operate
  href: https://artifacts.apis.io/perplexity/rate-limits/perplexity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/perplexity-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/perplexity/rules/perplexity-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/perplexity-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/perplexity/rules/perplexity-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/perplexity-asyncapi-spectral-rules.yml
- group: docs
  href: https://artifacts.apis.io/perplexity/asyncapi/perplexity-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/perplexity-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/perplexity/data-model/perplexity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/perplexity-data-model.yml
- group: operate
  href: https://artifacts.apis.io/perplexity/changelog/perplexity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/perplexity-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.perplexity.ai/security
- group: design
  href: https://artifacts.apis.io/perplexity/lifecycle/perplexity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/perplexity-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/perplexity/errors/perplexity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/perplexity-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/perplexity/llms/perplexity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/perplexity-llms.txt
- group: other
  href: https://artifacts.apis.io/perplexity/a2a/perplexity-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/perplexity-a2a.yml
- group: agent
  href: https://artifacts.apis.io/perplexity/mcp/perplexity-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/perplexity-mcp.yml
- group: agent
  href: https://artifacts.apis.io/perplexity/well-known/perplexity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/perplexity-well-known.yml
- group: other
  href: https://artifacts.apis.io/perplexity/hosts/perplexity-hosts.yml
  title: ''
  type: Hosts
  url: hosts/perplexity-hosts.yml
- group: build
  href: https://artifacts.apis.io/perplexity/integrations/perplexity-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/perplexity-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/perplexity/vendors/perplexity-vendors.yml
  title: ''
  type: Vendors
  url: vendors/perplexity-vendors.yml
- group: build
  href: https://artifacts.apis.io/perplexity/packages/perplexity-packages.yml
  title: ''
  type: Packages
  url: packages/perplexity-packages.yml
- group: other
  href: https://artifacts.apis.io/perplexity/capabilities/perplexity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/perplexity-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/perplexity/finops/perplexity-finops.yml
  title: ''
  type: FinOps
  url: finops/perplexity-finops.yml
- group: commercial
  href: https://artifacts.apis.io/perplexity/plans/perplexity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/perplexity-plans-pricing.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/perplexity/overview
- group: agent
  href: https://artifacts.apis.io/perplexity/agentic-access/perplexity-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/perplexity-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/perplexity/security/perplexity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/perplexity-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/perplexity/security/perplexity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/perplexity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/perplexity/authentication/perplexity-authentication.yml
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
  url: https://docs.perplexity.ai/api-reference/chat-completions-post
- group: other
  title: ''
  type: Models
  url: https://docs.perplexity.ai/docs/agent-api/models
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.perplexity.ai/docs/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.perplexity.ai/hub/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.perplexity.ai/hub/legal/privacy-policy
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
- has_sources: true
  method: derived
  name: Perplexity Finops
  primary_unit: invocation
  service_category: ''
  slug: perplexity-finops
  template: false
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
  property_count: 6
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
mcp_servers:
- description: Remote MCP server at api.perplexity.ai over streamable HTTP requiring OAuth; 4 tools listed.
  name: Perplexity MCP servers
  slug: perplexity
modified: '2026-09-16'
name: Perplexity
nav: Providers
network: true
overview: 'Perplexity publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Async Chat Completions API, Responses API, Agent API, and 14 more. Tagged areas include Artificial Intelligence, LLM, Search, Agents, and Embeddings.


  The Perplexity catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Perplexity''s developer surface includes changelog, authentication, getting-started guide, API reference, pricing, engineering blog, signup flow, and 59 more developer resources.'
plans:
- name: Perplexity Plans Pricing
  plan_count: 15
  slug: perplexity-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 26
  name: Perplexity Rate Limits
  slug: perplexity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Perplexity — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: perplexity-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Perplexity — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: perplexity-jsonschema-spectral-rules
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 58.5
    catalog_earned_first_party: 24.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 60.3
    developer_ergonomics: 65.5
    discoverability: 58.3
    operational_transparency: 78.9
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/perplexity/perplexity-2026-06-20T191624.png
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
tags:
- Artificial Intelligence
- LLM
- Search
- Agents
- Embeddings
- Research
- Agentic Commerce
- Foundation Models
website: https://www.perplexity.ai
---
