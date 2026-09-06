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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 346
  human_in_the_loop: 8
  name: Letta Agentic Access
  operation_count: 604
  slug: letta-agentic-access
  summary_line: 604 operations · 346 acting · 8 human-in-the-loop
api_count: 2
apis:
- description: Letta's memory-first coding agent — a CLI plus a desktop app (and an action for GitHub repos). "The memory-first coding agent that remembers and learns." Builds on the Letta Code SDK and the broader L
  name: Letta Code
  slug: letta-code
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Administrative operations (org / billing / policy).
  name: Letta Admin API
  slug: letta-admin-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Create, list, modify, export, and delete stateful agents with memory and tools.
  name: Letta Agents API
  slug: letta-agents-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Manage archival memory archives and passages (RAG-style long-term store).
  name: Letta Archives API
  slug: letta-archives-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Manage in-context memory blocks (core memory) shared across agents.
  name: Letta Blocks API
  slug: letta-blocks-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Chat operations.
  name: Letta Chat API
  slug: letta-chat-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Mint short-lived client-side access tokens for browser/mobile use.
  name: Letta Client-Side Access Tokens API
  slug: letta-client-side-access-tokens-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Conversational session threads anchored to an agent.
  name: Letta Conversations API
  slug: letta-conversations-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Per-device storage for the Letta Code SDK and ADE.
  name: Letta Device Storage API
  slug: letta-device-storage-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: List configured embedding models.
  name: Letta Embeddings API
  slug: letta-embeddings-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Environment variables and configuration scoped to agents/tools.
  name: Letta Environments API
  slug: letta-environments-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Subscribed feeds that drive agents.
  name: Letta Feeds API
  slug: letta-feeds-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Organize agents and resources into folders.
  name: Letta Folders API
  slug: letta-folders-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Coordinate multi-agent groups (supervisor/worker, round-robin, sleep-time).
  name: Letta Groups API
  slug: letta-groups-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Service health/readiness endpoint.
  name: Letta Health API
  slug: letta-health-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Map external user identities to agents and memory contexts.
  name: Letta Identities API
  slug: letta-identities-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Internal Agents operations.
  name: Letta Internal Agents API
  slug: letta-internal-agents-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Internal Blocks operations.
  name: Letta Internal Blocks API
  slug: letta-internal-blocks-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Internal Runs operations.
  name: Letta Internal Runs API
  slug: letta-internal-runs-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Internal Templates operations.
  name: Letta Internal Templates API
  slug: letta-internal-templates-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Manage long-running background jobs (e.g., file ingestion).
  name: Letta Jobs API
  slug: letta-jobs-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: List available LLM models and configurations.
  name: Letta LLMs API
  slug: letta-llms-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Register external Model Context Protocol servers and expose their tools to agents.
  name: Letta MCP Servers API
  slug: letta-mcp-servers-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Memory-mapped file resources attached to agents.
  name: Letta Memory Files API
  slug: letta-memory-files-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Send messages, list message history, search, and batch operations.
  name: Letta Messages API
  slug: letta-messages-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Service/runtime metadata.
  name: Letta Metadata API
  slug: letta-metadata-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: List available chat and embedding models exposed by configured providers.
  name: Letta Models API
  slug: letta-models-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Individual archival memory passages (chunked context).
  name: Letta Passages API
  slug: letta-passages-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Composable agent pipelines.
  name: Letta Pipelines API
  slug: letta-pipelines-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Project-level scoping for agents and resources.
  name: Letta Projects API
  slug: letta-projects-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Configure LLM provider credentials (OpenAI, Anthropic, Azure, Ollama, etc.).
  name: Letta Providers API
  slug: letta-providers-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Inspect and manage agent runs (executions of an agent in response to a message).
  name: Letta Runs API
  slug: letta-runs-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Manage code-execution sandboxes used by sandbox tools.
  name: Letta Sandboxes API
  slug: letta-sandboxes-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Schedule one-time or recurring messages to drive agents over time.
  name: Letta Scheduled Messages API
  slug: letta-scheduled-messages-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Manage data sources (files, URLs) used to populate agent archival memory.
  name: Letta Sources API
  slug: letta-sources-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Per-step traces of an agent run.
  name: Letta Steps API
  slug: letta-steps-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Tag-based filtering metadata.
  name: Letta Tag API
  slug: letta-tag-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Run-step traces and observability data.
  name: Letta Telemetry API
  slug: letta-telemetry-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Reusable agent templates for instantiation.
  name: Letta Templates API
  slug: letta-templates-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Register and execute custom tools (sandboxed Python, client-side, MCP).
  name: Letta Tools API
  slug: letta-tools-api
- baseURL: https://api.letta.com
  baseurl_source: declared
  description: Voice (low-latency) chat completions endpoint for agents.
  name: Letta Voice API
  slug: letta-voice-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Cloud-only versioned agent configuration templates.
  name: Letta Agent Templates API
  slug: letta-agent-templates-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Out-of-context long-term memory archives and passages.
  name: Letta Archival Memory API
  slug: letta-archival-memory-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: OpenAI-compatible chat completions backed by a Letta agent.
  name: Letta Chat Completions API
  slug: letta-chat-completions-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Core-memory blocks shared across agents, groups, and identities.
  name: Letta Memory Blocks API
  slug: letta-memory-blocks-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Available models and configured BYOK model providers.
  name: Letta Models and Providers API
  slug: letta-models-and-providers-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Groups of agents coordinating around shared memory.
  name: Letta Multi-Agent Groups API
  slug: letta-multi-agent-groups-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Asynchronous execution history behind agent messages.
  name: Letta Runs, Jobs and Steps API
  slug: letta-runs-jobs-and-steps-api
- baseURL: https://chat.letta.com
  baseurl_source: declared
  description: Uploaded files and folders used for agent grounding and retrieval.
  name: Letta Sources and Files API
  slug: letta-sources-and-files-api
artifact_total: 503
asyncapis:
- description: AsyncAPI 2.6 description of Letta's **agent message streaming** surface. Letta does not publish a WebSocket API. The only asynchronous / event-style transport documented in Letta's OpenAPI spec (https
  name: Letta Agent Message Streaming (HTTP + SSE)
  slug: letta-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Letta Admin API
  slug: open-letta-admin-api
- collection_type: open
  name: Letta Agent Templates API
  slug: open-letta-agent-templates-api
- collection_type: open
  name: Letta Admin Agents API
  slug: open-letta-agents-api
- collection_type: open
  name: Letta API
  slug: open-letta-ai
- collection_type: open
  name: Letta Agent Templates Archival Memory API
  slug: open-letta-archival-memory-api
- collection_type: open
  name: Letta Admin Archives API
  slug: open-letta-archives-api
- collection_type: open
  name: Letta Admin Blocks API
  slug: open-letta-blocks-api
- collection_type: open
  name: Letta Admin Chat API
  slug: open-letta-chat-api
- collection_type: open
  name: Letta Agent Templates Chat Completions API
  slug: open-letta-chat-completions-api
- collection_type: open
  name: Letta Admin Client-Side Access Tokens API
  slug: open-letta-client-side-access-tokens-api
- collection_type: open
  name: Letta Admin Conversations API
  slug: open-letta-conversations-api
- collection_type: open
  name: Letta Admin Device Storage API
  slug: open-letta-device-storage-api
- collection_type: open
  name: Letta Admin Embeddings API
  slug: open-letta-embeddings-api
- collection_type: open
  name: Letta Admin Environments API
  slug: open-letta-environments-api
- collection_type: open
  name: Letta Admin Feeds API
  slug: open-letta-feeds-api
- collection_type: open
  name: Letta Admin Folders API
  slug: open-letta-folders-api
- collection_type: open
  name: Letta Admin Groups API
  slug: open-letta-groups-api
- collection_type: open
  name: Letta Admin Health API
  slug: open-letta-health-api
- collection_type: open
  name: Letta Admin Identities API
  slug: open-letta-identities-api
- collection_type: open
  name: Letta Admin Internal Agents API
  slug: open-letta-internal-agents-api
- collection_type: open
  name: Letta Admin Internal Blocks API
  slug: open-letta-internal-blocks-api
- collection_type: open
  name: Letta Admin Internal Runs API
  slug: open-letta-internal-runs-api
- collection_type: open
  name: Letta Admin Internal Templates API
  slug: open-letta-internal-templates-api
- collection_type: open
  name: Letta Admin Jobs API
  slug: open-letta-jobs-api
- collection_type: open
  name: Letta Admin LLMs API
  slug: open-letta-llms-api
- collection_type: open
  name: Letta Admin MCP Servers API
  slug: open-letta-mcp-servers-api
- collection_type: open
  name: Letta Agent Templates Memory Blocks API
  slug: open-letta-memory-blocks-api
- collection_type: open
  name: Letta Admin Memory Files API
  slug: open-letta-memory-files-api
- collection_type: open
  name: Letta Admin Messages API
  slug: open-letta-messages-api
- collection_type: open
  name: Letta Admin Metadata API
  slug: open-letta-metadata-api
- collection_type: open
  name: Letta Agent Templates Models and Providers API
  slug: open-letta-models-and-providers-api
- collection_type: open
  name: Letta Admin Models API
  slug: open-letta-models-api
- collection_type: open
  name: Letta Agent Templates Multi-Agent Groups API
  slug: open-letta-multi-agent-groups-api
- collection_type: open
  name: Letta Admin Passages API
  slug: open-letta-passages-api
- collection_type: open
  name: Letta Admin Pipelines API
  slug: open-letta-pipelines-api
- collection_type: open
  name: Letta Admin Projects API
  slug: open-letta-projects-api
- collection_type: open
  name: Letta Admin Providers API
  slug: open-letta-providers-api
- collection_type: open
  name: Letta Admin Runs API
  slug: open-letta-runs-api
- collection_type: open
  name: Letta Agent Templates Runs, Jobs and Steps API
  slug: open-letta-runs-jobs-and-steps-api
- collection_type: open
  name: Letta Admin Sandboxes API
  slug: open-letta-sandboxes-api
- collection_type: open
  name: Letta Admin Scheduled Messages API
  slug: open-letta-scheduled-messages-api
- collection_type: open
  name: Letta Agent Templates Sources and Files API
  slug: open-letta-sources-and-files-api
- collection_type: open
  name: Letta Admin Sources API
  slug: open-letta-sources-api
- collection_type: open
  name: Letta Admin Steps API
  slug: open-letta-steps-api
- collection_type: open
  name: Letta Admin Tag API
  slug: open-letta-tag-api
- collection_type: open
  name: Letta Admin Telemetry API
  slug: open-letta-telemetry-api
- collection_type: open
  name: Letta Admin Templates API
  slug: open-letta-templates-api
- collection_type: open
  name: Letta Admin Tools API
  slug: open-letta-tools-api
- collection_type: open
  name: Letta Admin Voice API
  slug: open-letta-voice-api
- collection_type: open
  name: Letta API
  slug: open-letta
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/letta-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/letta-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/letta-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/letta-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/letta-ai
- group: company
  title: ''
  type: Website
  url: https://www.letta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.letta.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.letta.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.letta.com/llms-full.txt
- group: build
  title: ''
  type: GitHub
  url: https://github.com/letta-ai
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/letta-ai
- group: build
  title: ''
  type: PythonSDK
  url: https://github.com/letta-ai/letta-python
- group: build
  title: ''
  type: TypeScriptSDK
  url: https://github.com/letta-ai/letta-node
- group: start
  title: ''
  type: Login
  url: https://app.letta.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.letta.com/guides/api/plans
- group: commercial
  title: ''
  type: Plans
  url: plans/letta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/letta-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/letta-finops.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/letta-rules.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/letta-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/letta-vocabulary.yml
- group: other
  title: ''
  type: AgentFileFormat
  url: https://github.com/letta-ai/agent-file
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.letta.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/letta-ai
created: '2026-05-08'
description: Letta (formerly MemGPT) is a stateful AI agents platform built around long-term memory, tool execution, and multi-agent coordination. The Letta REST API exposes 239 endpoints across 36 public resource categories — agents, memory blocks, archival memory, sources (RAG), custom tools (sandboxed/client-side/MCP), MCP servers, multi-agent groups, identities, runs, scheduled messages, and a streaming voice-mode endpoint. Open-source server (Apache-2.0, 22.9k+ stars) is available on GitHub; Letta Cloud is the managed offering; the Agent Development Environment (ADE) provides a web UI for inspecting context windows, memory blocks, and run history. Python and TypeScript SDKs ship alongside the REST API, and the open `.af` agent file format lets agents migrate between deployments.
examples:
- key_count: 14
  name: Letta Agent Payload Example
  slug: letta-agent-payload-example
- key_count: 10
  name: Letta Block Payload Example
  slug: letta-block-payload-example
- key_count: 6
  name: Letta Create Agent Example
  slug: letta-create-agent-example
- key_count: 6
  name: Letta Create Identity Example
  slug: letta-create-identity-example
- key_count: 6
  name: Letta Create Memory Block Example
  slug: letta-create-memory-block-example
- key_count: 6
  name: Letta Create Multi Agent Group Example
  slug: letta-create-multi-agent-group-example
- key_count: 6
  name: Letta Create Source Example
  slug: letta-create-source-example
- key_count: 6
  name: Letta Create Tool Example
  slug: letta-create-tool-example
- key_count: 6
  name: Letta Create Voice Chat Completions Example
  slug: letta-create-voice-chat-completions-example
- key_count: 7
  name: Letta Group Payload Example
  slug: letta-group-payload-example
- key_count: 6
  name: Letta List Agents Example
  slug: letta-list-agents-example
- key_count: 6
  name: Letta List Chat Models Example
  slug: letta-list-chat-models-example
- key_count: 6
  name: Letta List Embedding Models Example
  slug: letta-list-embedding-models-example
- key_count: 6
  name: Letta List Mcp Servers Example
  slug: letta-list-mcp-servers-example
- key_count: 6
  name: Letta List Memory Blocks Example
  slug: letta-list-memory-blocks-example
- key_count: 6
  name: Letta List Runs Example
  slug: letta-list-runs-example
- key_count: 6
  name: Letta List Tools Example
  slug: letta-list-tools-example
- key_count: 10
  name: Letta Mcp Server Payload Example
  slug: letta-mcp-server-payload-example
- key_count: 6
  name: Letta Register Mcp Server Example
  slug: letta-register-mcp-server-example
- key_count: 6
  name: Letta Retrieve Agent Example
  slug: letta-retrieve-agent-example
- key_count: 6
  name: Letta Retrieve Run Example
  slug: letta-retrieve-run-example
- key_count: 8
  name: Letta Run Payload Example
  slug: letta-run-payload-example
- key_count: 6
  name: Letta Run Tool From Source Example
  slug: letta-run-tool-from-source-example
- key_count: 6
  name: Letta Send Agent Message Example
  slug: letta-send-agent-message-example
- key_count: 6
  name: Letta Source Payload Example
  slug: letta-source-payload-example
- key_count: 6
  name: Letta Stream Agent Message Sse Example
  slug: letta-stream-agent-message-sse-example
- key_count: 9
  name: Letta Tool Payload Example
  slug: letta-tool-payload-example
- key_count: 6
  name: Letta Upload File To Source Example
  slug: letta-upload-file-to-source-example
- key_count: 6
  name: Letta Voice Chat Completion Beta Example
  slug: letta-voice-chat-completion-beta-example
finops:
- name: Letta Finops
  service_category: AI
  slug: letta-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/letta.png
json_schemas:
- name: AgentState
  property_count: 45
  slug: letta-agent
- name: AgentEnvironmentVariable
  property_count: 10
  slug: letta-agentenvironmentvariable
- name: AgentFileAttachment
  property_count: 10
  slug: letta-agentfileattachment
- name: AgentFileSchema
  property_count: 10
  slug: letta-agentfileschema
- name: AgentState
  property_count: 45
  slug: letta-agentstate
- name: AgentType
  property_count: 0
  slug: letta-agenttype
- name: Annotation
  property_count: 2
  slug: letta-annotation
- name: AnnotationURLCitation
  property_count: 4
  slug: letta-annotationurlcitation
- name: AnthropicModelSettings
  property_count: 9
  slug: letta-anthropicmodelsettings
- name: AnthropicThinking
  property_count: 2
  slug: letta-anthropicthinking
- name: ApprovalCreate
  property_count: 7
  slug: letta-approvalcreate
- name: ApprovalRequestMessage
  property_count: 12
  slug: letta-approvalrequestmessage
- name: ApprovalResponseMessage
  property_count: 14
  slug: letta-approvalresponsemessage
- name: ApprovalReturn
  property_count: 4
  slug: letta-approvalreturn
- name: ArchivalMemorySearchResponse
  property_count: 2
  slug: letta-archivalmemorysearchresponse
- name: ArchivalMemorySearchResult
  property_count: 4
  slug: letta-archivalmemorysearchresult
- name: Archive
  property_count: 10
  slug: letta-archive
- name: ArchiveCreateRequest
  property_count: 4
  slug: letta-archivecreaterequest
- name: ArchiveUpdateRequest
  property_count: 2
  slug: letta-archiveupdaterequest
- name: AssistantMessage
  property_count: 11
  slug: letta-assistantmessage
- name: AssistantMessageListResult
  property_count: 6
  slug: letta-assistantmessagelistresult
- name: Audio
  property_count: 1
  slug: letta-audio
- name: AuthRequest
  property_count: 1
  slug: letta-authrequest
- name: AuthResponse
  property_count: 2
  slug: letta-authresponse
- name: AzureModelSettings
  property_count: 5
  slug: letta-azuremodelsettings
- name: Base64Image
  property_count: 4
  slug: letta-base64image
- name: BasetenModelSettings
  property_count: 4
  slug: letta-basetenmodelsettings
- name: BaseToolRuleSchema
  property_count: 2
  slug: letta-basetoolruleschema
- name: BatchJob
  property_count: 18
  slug: letta-batchjob
- name: BedrockModelSettings
  property_count: 5
  slug: letta-bedrockmodelsettings
- name: BillingContext
  property_count: 3
  slug: letta-billingcontext
- name: Block
  property_count: 19
  slug: letta-block
- name: BlockResponse
  property_count: 19
  slug: letta-blockresponse
- name: BlockSchema
  property_count: 17
  slug: letta-blockschema
- name: BlockUpdate
  property_count: 16
  slug: letta-blockupdate
- name: Body_export_agent
  property_count: 2
  slug: letta-body-export-agent
- name: Body_import_agent
  property_count: 13
  slug: letta-body-import-agent
- name: Body_upload_file_to_folder
  property_count: 1
  slug: letta-body-upload-file-to-folder
- name: Body_upload_file_to_source
  property_count: 1
  slug: letta-body-upload-file-to-source
- name: CancelAgentRunRequest
  property_count: 1
  slug: letta-cancelagentrunrequest
- name: ChatCompletion
  property_count: 8
  slug: letta-chatcompletion
- name: ChatCompletionAssistantMessageParam
  property_count: 7
  slug: letta-chatcompletionassistantmessageparam
- name: ChatCompletionAudio
  property_count: 4
  slug: letta-chatcompletionaudio
- name: ChatCompletionContentPartImageParam
  property_count: 2
  slug: letta-chatcompletioncontentpartimageparam
- name: ChatCompletionContentPartInputAudioParam
  property_count: 2
  slug: letta-chatcompletioncontentpartinputaudioparam
- name: ChatCompletionContentPartRefusalParam
  property_count: 2
  slug: letta-chatcompletioncontentpartrefusalparam
- name: ChatCompletionContentPartTextParam
  property_count: 2
  slug: letta-chatcompletioncontentparttextparam
- name: ChatCompletionDeveloperMessageParam
  property_count: 3
  slug: letta-chatcompletiondevelopermessageparam
- name: ChatCompletionFunctionMessageParam
  property_count: 3
  slug: letta-chatcompletionfunctionmessageparam
- name: ChatCompletionMessage
  property_count: 7
  slug: letta-chatcompletionmessage
- name: ChatCompletionMessageCustomToolCall
  property_count: 3
  slug: letta-chatcompletionmessagecustomtoolcall
- name: ChatCompletionMessageCustomToolCallParam
  property_count: 3
  slug: letta-chatcompletionmessagecustomtoolcallparam
- name: ChatCompletionMessageFunctionToolCall
  property_count: 3
  slug: letta-chatcompletionmessagefunctiontoolcall-input
- name: ChatCompletionMessageFunctionToolCall
  property_count: 3
  slug: letta-chatcompletionmessagefunctiontoolcall-output
- name: ChatCompletionMessageFunctionToolCallParam
  property_count: 3
  slug: letta-chatcompletionmessagefunctiontoolcallparam
- name: ChatCompletionRequest
  property_count: 11
  slug: letta-chatcompletionrequest
- name: ChatCompletionSystemMessageParam
  property_count: 3
  slug: letta-chatcompletionsystemmessageparam
- name: ChatCompletionToolMessageParam
  property_count: 3
  slug: letta-chatcompletiontoolmessageparam
- name: ChatCompletionUserMessageParam
  property_count: 3
  slug: letta-chatcompletionusermessageparam
- name: ChatGPTOAuthModelSettings
  property_count: 5
  slug: letta-chatgptoauthmodelsettings
- name: ChatGPTOAuthReasoning
  property_count: 1
  slug: letta-chatgptoauthreasoning
- name: ChildToolRule
  property_count: 5
  slug: letta-childtoolrule
- name: ChildToolRuleSchema
  property_count: 3
  slug: letta-childtoolruleschema
- name: Choice
  property_count: 4
  slug: letta-choice
- name: ClientSkillSchema
  property_count: 3
  slug: letta-clientskillschema
- name: ClientToolSchema
  property_count: 3
  slug: letta-clienttoolschema
- name: CodeInput
  property_count: 2
  slug: letta-codeinput
- name: CompactionResponse
  property_count: 3
  slug: letta-compactionresponse
- name: CompactionSettings
  property_count: 7
  slug: letta-compactionsettings-input
- name: CompactionSettings
  property_count: 7
  slug: letta-compactionsettings-output
- name: CompactionStats
  property_count: 6
  slug: letta-compactionstats
- name: ComparisonOperator
  property_count: 0
  slug: letta-comparisonoperator
- name: CompletionTokensDetails
  property_count: 4
  slug: letta-completiontokensdetails
- name: CompletionUsage
  property_count: 5
  slug: letta-completionusage
- name: ConditionalToolRule
  property_count: 6
  slug: letta-conditionaltoolrule
- name: ConditionalToolRuleSchema
  property_count: 5
  slug: letta-conditionaltoolruleschema
- name: ContextWindowOverview
  property_count: 23
  slug: letta-contextwindowoverview
- name: ContinueToolRule
  property_count: 3
  slug: letta-continuetoolrule
- name: Conversation
  property_count: 12
  slug: letta-conversation
- name: ConversationMessageRequest
  property_count: 21
  slug: letta-conversationmessagerequest
- name: CoreMemoryBlockSchema
  property_count: 9
  slug: letta-corememoryblockschema
- name: CreateAgentRequest
  property_count: 48
  slug: letta-createagentrequest
- name: CreateArchivalMemory
  property_count: 3
  slug: letta-createarchivalmemory
- name: CreateBatch
  property_count: 2
  slug: letta-createbatch
- name: CreateBlock
  property_count: 16
  slug: letta-createblock
- name: CreateConversation
  property_count: 4
  slug: letta-createconversation
- name: CreateMCPServerRequest
  property_count: 2
  slug: letta-createmcpserverrequest
- name: CreateSSEMCPServer
  property_count: 5
  slug: letta-createssemcpserver
- name: CreateStdioMCPServer
  property_count: 4
  slug: letta-createstdiomcpserver
- name: CreateStreamableHTTPMCPServer
  property_count: 5
  slug: letta-createstreamablehttpmcpserver
- name: Custom
  property_count: 2
  slug: letta-custom-input
- name: Custom
  property_count: 2
  slug: letta-custom-output
- name: DeepseekModelSettings
  property_count: 5
  slug: letta-deepseekmodelsettings
- name: DeleteDeploymentResponse
  property_count: 4
  slug: letta-deletedeploymentresponse
- name: DeploymentEntity
  property_count: 6
  slug: letta-deploymententity
- name: DuplicateFileHandling
  property_count: 0
  slug: letta-duplicatefilehandling
- name: DynamicManager
  property_count: 4
  slug: letta-dynamicmanager
- name: DynamicManagerSchema
  property_count: 4
  slug: letta-dynamicmanagerschema
- name: DynamicManagerUpdate
  property_count: 4
  slug: letta-dynamicmanagerupdate
- name: E2BSandboxConfig
  property_count: 3
  slug: letta-e2bsandboxconfig
- name: EmbeddingConfig
  property_count: 10
  slug: letta-embedding-config
- name: EmbeddingConfig
  property_count: 10
  slug: letta-embeddingconfig
- name: EmbeddingModel
  property_count: 15
  slug: letta-embeddingmodel
- name: EventMessage
  property_count: 12
  slug: letta-eventmessage
- name: ExportAgentRequest
  property_count: 3
  slug: letta-exportagentrequest
- name: FeedbackType
  property_count: 0
  slug: letta-feedbacktype
- name: File
  property_count: 2
  slug: letta-file
- name: FileAgentSchema
  property_count: 10
  slug: letta-fileagentschema
- name: FileBlock
  property_count: 23
  slug: letta-fileblock
- name: FileFile
  property_count: 3
  slug: letta-filefile
- name: FileMetadata
  property_count: 16
  slug: letta-filemetadata
- name: FileProcessingStatus
  property_count: 0
  slug: letta-fileprocessingstatus
- name: FileSchema
  property_count: 14
  slug: letta-fileschema
- name: FileStats
  property_count: 3
  slug: letta-filestats
- name: Folder
  property_count: 10
  slug: letta-folder
- name: Function
  property_count: 2
  slug: letta-function-output
- name: FunctionCall
  property_count: 2
  slug: letta-functioncall-input
- name: FunctionCall
  property_count: 2
  slug: letta-functioncall-output
- name: FunctionDefinition
  property_count: 4
  slug: letta-functiondefinition
- name: FunctionTool
  property_count: 2
  slug: letta-functiontool
- name: GeminiThinkingConfig
  property_count: 2
  slug: letta-geminithinkingconfig
- name: GenerateRequest
  property_count: 4
  slug: letta-generaterequest
- name: GenerateResponse
  property_count: 3
  slug: letta-generateresponse
- name: GenerateToolInput
  property_count: 5
  slug: letta-generatetoolinput
- name: GenerateToolOutput
  property_count: 3
  slug: letta-generatetooloutput
- name: GoogleAIModelSettings
  property_count: 6
  slug: letta-googleaimodelsettings
- name: GoogleVertexModelSettings
  property_count: 6
  slug: letta-googlevertexmodelsettings
- name: GroqModelSettings
  property_count: 5
  slug: letta-groqmodelsettings
- name: Group
  property_count: 18
  slug: letta-group
- name: GroupCreate
  property_count: 6
  slug: letta-groupcreate
- name: GroupSchema
  property_count: 7
  slug: letta-groupschema
- name: GroupUpdate
  property_count: 5
  slug: letta-groupupdate
- name: Health
  property_count: 2
  slug: letta-health
- name: HiddenReasoningMessage
  property_count: 12
  slug: letta-hiddenreasoningmessage
- name: HTTPValidationError
  property_count: 1
  slug: letta-httpvalidationerror
- name: Identity
  property_count: 8
  slug: letta-identity
- name: IdentityCreate
  property_count: 7
  slug: letta-identitycreate
- name: IdentityProperty
  property_count: 3
  slug: letta-identityproperty
- name: IdentityPropertyType
  property_count: 0
  slug: letta-identitypropertytype
- name: IdentityType
  property_count: 0
  slug: letta-identitytype
- name: IdentityUpdate
  property_count: 6
  slug: letta-identityupdate
- name: IdentityUpsert
  property_count: 7
  slug: letta-identityupsert
- name: ImageContent
  property_count: 2
  slug: letta-imagecontent
- name: ImageURL
  property_count: 2
  slug: letta-imageurl
- name: ImportedAgentsResponse
  property_count: 1
  slug: letta-importedagentsresponse
- name: InitToolRule
  property_count: 4
  slug: letta-inittoolrule
- name: InputAudio
  property_count: 2
  slug: letta-inputaudio
- name: InternalTemplateAgentCreate
  property_count: 50
  slug: letta-internaltemplateagentcreate
- name: InternalTemplateBlockCreate
  property_count: 16
  slug: letta-internaltemplateblockcreate
- name: InternalTemplateGroupCreate
  property_count: 9
  slug: letta-internaltemplategroupcreate
- name: Job
  property_count: 18
  slug: letta-job
- name: JobStatus
  property_count: 0
  slug: letta-jobstatus
- name: JobType
  property_count: 0
  slug: letta-jobtype
- name: JsonObjectResponseFormat
  property_count: 1
  slug: letta-jsonobjectresponseformat
- name: JsonSchemaResponseFormat
  property_count: 2
  slug: letta-jsonschemaresponseformat
- name: AgentSchema
  property_count: 53
  slug: letta-letta-schemas-agent-file-agentschema
- name: MessageSchema
  property_count: 19
  slug: letta-letta-schemas-agent-file-messageschema
- name: ToolSchema
  property_count: 18
  slug: letta-letta-schemas-agent-file-toolschema
- name: ToolReturn
  property_count: 6
  slug: letta-letta-schemas-letta-message-toolreturn
- name: ToolExecuteRequest
  property_count: 1
  slug: letta-letta-schemas-mcp-server-toolexecuterequest
- name: UpdateSSEMCPServer
  property_count: 5
  slug: letta-letta-schemas-mcp-server-updatessemcpserver
- name: UpdateStdioMCPServer
  property_count: 4
  slug: letta-letta-schemas-mcp-server-updatestdiomcpserver
- name: UpdateStreamableHTTPMCPServer
  property_count: 5
  slug: letta-letta-schemas-mcp-server-updatestreamablehttpmcpserver
- name: UpdateSSEMCPServer
  property_count: 4
  slug: letta-letta-schemas-mcp-updatessemcpserver
- name: UpdateStdioMCPServer
  property_count: 2
  slug: letta-letta-schemas-mcp-updatestdiomcpserver
- name: UpdateStreamableHTTPMCPServer
  property_count: 5
  slug: letta-letta-schemas-mcp-updatestreamablehttpmcpserver
- name: ToolReturn
  property_count: 5
  slug: letta-letta-schemas-message-toolreturn-input
- name: ToolReturn
  property_count: 5
  slug: letta-letta-schemas-message-toolreturn-output
- name: ChatCompletionTokenLogprob
  property_count: 4
  slug: letta-letta-schemas-openai-chat-completion-response-chatcompletion
- name: ChoiceLogprobs
  property_count: 2
  slug: letta-letta-schemas-openai-chat-completion-response-choicelogprobs
- name: TopLogprob
  property_count: 3
  slug: letta-letta-schemas-openai-chat-completion-response-toplogprob
- name: AgentSchema
  property_count: 19
  slug: letta-letta-serialize-schemas-pydantic-agent-schema-agentschema
- name: MessageSchema
  property_count: 10
  slug: letta-letta-serialize-schemas-pydantic-agent-schema-messageschema
- name: ToolSchema
  property_count: 12
  slug: letta-letta-serialize-schemas-pydantic-agent-schema-toolschema
- name: CompactionRequest
  property_count: 1
  slug: letta-letta-server-rest-api-routers-v1-agents-compactionrequest
- name: CompactionRequest
  property_count: 2
  slug: letta-letta-server-rest-api-routers-v1-conversations-compactionreq
- name: ToolExecuteRequest
  property_count: 1
  slug: letta-letta-server-rest-api-routers-v1-tools-toolexecuterequest
- name: LettaAssistantMessageContentUnion
  property_count: 0
  slug: letta-lettaassistantmessagecontentunion
- name: LettaAsyncRequest
  property_count: 17
  slug: letta-lettaasyncrequest
- name: LettaBatchMessages
  property_count: 1
  slug: letta-lettabatchmessages
- name: LettaBatchRequest
  property_count: 17
  slug: letta-lettabatchrequest
- name: LettaErrorMessage
  property_count: 6
  slug: letta-lettaerrormessage
- name: LettaImage
  property_count: 5
  slug: letta-lettaimage
- name: LettaMessageContentUnion
  property_count: 0
  slug: letta-lettamessagecontentunion
- name: LettaMessageUnion
  property_count: 0
  slug: letta-lettamessageunion
- name: LettaPing
  property_count: 10
  slug: letta-lettaping
- name: LettaRequest
  property_count: 16
  slug: letta-lettarequest
- name: LettaRequestConfig
  property_count: 4
  slug: letta-lettarequestconfig
- name: LettaResponse
  property_count: 5
  slug: letta-lettaresponse
- name: LettaStopReason
  property_count: 2
  slug: letta-lettastopreason
- name: LettaStreamingRequest
  property_count: 20
  slug: letta-lettastreamingrequest
- name: LettaStreamingResponse
  property_count: 0
  slug: letta-lettastreamingresponse
- name: LettaToolReturnContentUnion
  property_count: 0
  slug: letta-lettatoolreturncontentunion
- name: LettaUsageStatistics
  property_count: 10
  slug: letta-lettausagestatistics
- name: LettaUserMessageContentUnion
  property_count: 0
  slug: letta-lettausermessagecontentunion
- name: ListDeploymentEntitiesResponse
  property_count: 4
  slug: letta-listdeploymententitiesresponse
- name: LLMConfig
  property_count: 27
  slug: letta-llm-config
- name: LLMConfig
  property_count: 27
  slug: letta-llmconfig
- name: LocalSandboxConfig
  property_count: 4
  slug: letta-localsandboxconfig
- name: ManagerType
  property_count: 0
  slug: letta-managertype
- name: MaxCountPerStepToolRule
  property_count: 4
  slug: letta-maxcountpersteptoolrule
- name: MaxCountPerStepToolRuleSchema
  property_count: 3
  slug: letta-maxcountpersteptoolruleschema
- name: MCPServerSchema
  property_count: 6
  slug: letta-mcpserverschema
- name: MCPServerType
  property_count: 0
  slug: letta-mcpservertype
- name: MCPTool
  property_count: 8
  slug: letta-mcptool
- name: MCPToolHealth
  property_count: 2
  slug: letta-mcptoolhealth
- name: Memory
  property_count: 5
  slug: letta-memory
- name: Message
  property_count: 25
  slug: letta-message
- name: MessageCreate
  property_count: 8
  slug: letta-messagecreate
- name: MessageRole
  property_count: 0
  slug: letta-messagerole
- name: MessageSearchCacheWarmScope
  property_count: 0
  slug: letta-messagesearchcachewarmscope
- name: MessageSearchRequest
  property_count: 10
  slug: letta-messagesearchrequest
- name: MessageSearchResult
  property_count: 5
  slug: letta-messagesearchresult
- name: MessageType
  property_count: 0
  slug: letta-messagetype
- name: ModalSandboxConfig
  property_count: 4
  slug: letta-modalsandboxconfig
- name: Model
  property_count: 31
  slug: letta-model
- name: ModifyApprovalRequest
  property_count: 1
  slug: letta-modifyapprovalrequest
- name: ModifyFeedbackRequest
  property_count: 2
  slug: letta-modifyfeedbackrequest
- name: NpmRequirement
  property_count: 2
  slug: letta-npmrequirement
- name: OmittedReasoningContent
  property_count: 2
  slug: letta-omittedreasoningcontent
- name: ChoiceLogprobs
  property_count: 2
  slug: letta-openai-types-chat-chat-completion-choicelogprobs
- name: Function
  property_count: 2
  slug: letta-openai-types-chat-chat-completion-message-function-tool-call
- name: ChatCompletionTokenLogprob
  property_count: 4
  slug: letta-openai-types-chat-chat-completion-token-logprob-chatcompleti
- name: TopLogprob
  property_count: 3
  slug: letta-openai-types-chat-chat-completion-token-logprob-toplogprob
- name: OpenAIModelSettings
  property_count: 7
  slug: letta-openaimodelsettings
- name: OpenAIReasoning
  property_count: 1
  slug: letta-openaireasoning
- name: OpenRouterModelSettings
  property_count: 5
  slug: letta-openroutermodelsettings
- name: Organization
  property_count: 4
  slug: letta-organization
- name: OrganizationCreate
  property_count: 2
  slug: letta-organizationcreate
- name: OrganizationSourcesStats
  property_count: 4
  slug: letta-organizationsourcesstats
- name: OrganizationUpdate
  property_count: 2
  slug: letta-organizationupdate
- name: PaginatedAgentFiles
  property_count: 3
  slug: letta-paginatedagentfiles
- name: ParameterProperties
  property_count: 2
  slug: letta-parameterproperties
- name: ParametersSchema
  property_count: 3
  slug: letta-parametersschema
- name: ParentToolRule
  property_count: 4
  slug: letta-parenttoolrule
- name: Passage
  property_count: 15
  slug: letta-passage
- name: PassageBatchCreateRequest
  property_count: 1
  slug: letta-passagebatchcreaterequest
- name: PassageCreateRequest
  property_count: 4
  slug: letta-passagecreaterequest
- name: PassageSearchRequest
  property_count: 8
  slug: letta-passagesearchrequest
- name: PassageSearchResult
  property_count: 3
  slug: letta-passagesearchresult
- name: PipRequirement
  property_count: 2
  slug: letta-piprequirement
- name: PromptTokensDetails
  property_count: 2
  slug: letta-prompttokensdetails
- name: Provider
  property_count: 13
  slug: letta-provider
- name: ProviderCategory
  property_count: 0
  slug: letta-providercategory
- name: ProviderCheck
  property_count: 6
  slug: letta-providercheck
- name: ProviderCreate
  property_count: 7
  slug: letta-providercreate
- name: ProviderTrace
  property_count: 17
  slug: letta-providertrace
- name: ProviderType
  property_count: 0
  slug: letta-providertype
- name: ProviderUpdate
  property_count: 5
  slug: letta-providerupdate
- name: ReasoningContent
  property_count: 4
  slug: letta-reasoningcontent
- name: ReasoningMessage
  property_count: 13
  slug: letta-reasoningmessage
- name: ReasoningMessageListResult
  property_count: 6
  slug: letta-reasoningmessagelistresult
- name: RedactedReasoningContent
  property_count: 2
  slug: letta-redactedreasoningcontent
- name: RequiredBeforeExitToolRule
  property_count: 3
  slug: letta-requiredbeforeexittoolrule
- name: RequiresApprovalToolRule
  property_count: 3
  slug: letta-requiresapprovaltoolrule
- name: ResetMessagesRequest
  property_count: 1
  slug: letta-resetmessagesrequest
- name: RetrieveStreamRequest
  property_count: 7
  slug: letta-retrievestreamrequest
- name: RoundRobinManager
  property_count: 2
  slug: letta-roundrobinmanager
- name: RoundRobinManagerUpdate
  property_count: 2
  slug: letta-roundrobinmanagerupdate
- name: Run
  property_count: 17
  slug: letta-run
- name: RunMetrics
  property_count: 9
  slug: letta-runmetrics
- name: RunStatus
  property_count: 0
  slug: letta-runstatus
- name: SandboxConfig
  property_count: 7
  slug: letta-sandboxconfig
- name: SandboxConfigCreate
  property_count: 1
  slug: letta-sandboxconfigcreate
- name: SandboxConfigUpdate
  property_count: 1
  slug: letta-sandboxconfigupdate
- name: SandboxEnvironmentVariable
  property_count: 10
  slug: letta-sandboxenvironmentvariable
- name: SandboxEnvironmentVariableCreate
  property_count: 3
  slug: letta-sandboxenvironmentvariablecreate
- name: SandboxEnvironmentVariableUpdate
  property_count: 3
  slug: letta-sandboxenvironmentvariableupdate
- name: SandboxType
  property_count: 0
  slug: letta-sandboxtype
- name: SearchAllMessagesRequest
  property_count: 7
  slug: letta-searchallmessagesrequest
- name: SearchCacheWarmRequest
  property_count: 2
  slug: letta-searchcachewarmrequest
- name: SearchCacheWarmResponse
  property_count: 3
  slug: letta-searchcachewarmresponse
- name: SGLangModelSettings
  property_count: 8
  slug: letta-sglangmodelsettings
- name: SkillSchema
  property_count: 3
  slug: letta-skillschema
- name: SleeptimeManager
  property_count: 3
  slug: letta-sleeptimemanager
- name: SleeptimeManagerSchema
  property_count: 3
  slug: letta-sleeptimemanagerschema
- name: SleeptimeManagerUpdate
  property_count: 3
  slug: letta-sleeptimemanagerupdate
- name: Source
  property_count: 11
  slug: letta-source
- name: SourceCreate
  property_count: 7
  slug: letta-sourcecreate
- name: SourceSchema
  property_count: 8
  slug: letta-sourceschema
- name: SourceStats
  property_count: 5
  slug: letta-sourcestats
- name: SourceUpdate
  property_count: 5
  slug: letta-sourceupdate
- name: SSEMCPServer
  property_count: 7
  slug: letta-ssemcpserver
- name: SSEServerConfig
  property_count: 6
  slug: letta-sseserverconfig
- name: StdioMCPServer
  property_count: 6
  slug: letta-stdiomcpserver
- name: StdioServerConfig
  property_count: 5
  slug: letta-stdioserverconfig
- name: Step
  property_count: 30
  slug: letta-step
- name: StepMetrics
  property_count: 12
  slug: letta-stepmetrics
- name: StepStatus
  property_count: 0
  slug: letta-stepstatus
- name: StopReasonType
  property_count: 0
  slug: letta-stopreasontype
- name: StreamableHTTPMCPServer
  property_count: 7
  slug: letta-streamablehttpmcpserver
- name: StreamableHTTPServerConfig
  property_count: 6
  slug: letta-streamablehttpserverconfig
- name: SummarizedReasoningContent
  property_count: 4
  slug: letta-summarizedreasoningcontent
- name: SummarizedReasoningContentPart
  property_count: 2
  slug: letta-summarizedreasoningcontentpart
- name: SummaryMessage
  property_count: 12
  slug: letta-summarymessage
- name: SupervisorManager
  property_count: 2
  slug: letta-supervisormanager
- name: SupervisorManagerSchema
  property_count: 2
  slug: letta-supervisormanagerschema
- name: SupervisorManagerUpdate
  property_count: 2
  slug: letta-supervisormanagerupdate
- name: SystemMessage
  property_count: 11
  slug: letta-systemmessage
- name: SystemMessageListResult
  property_count: 6
  slug: letta-systemmessagelistresult
- name: TagSchema
  property_count: 1
  slug: letta-tagschema
- name: TerminalToolRule
  property_count: 3
  slug: letta-terminaltoolrule
- name: TextContent
  property_count: 3
  slug: letta-textcontent
- name: TextResponseFormat
  property_count: 1
  slug: letta-textresponseformat
- name: TogetherModelSettings
  property_count: 5
  slug: letta-togethermodelsettings
- name: Tool
  property_count: 18
  slug: letta-tool
- name: ToolAnnotations
  property_count: 5
  slug: letta-toolannotations
- name: ToolCall
  property_count: 3
  slug: letta-toolcall
- name: ToolCallContent
  property_count: 5
  slug: letta-toolcallcontent
- name: ToolCallDelta
  property_count: 3
  slug: letta-toolcalldelta
- name: ToolCallMessage
  property_count: 12
  slug: letta-toolcallmessage
- name: ToolCallNode
  property_count: 2
  slug: letta-toolcallnode
- name: ToolCreate
  property_count: 11
  slug: letta-toolcreate
- name: ToolEnvVarSchema
  property_count: 5
  slug: letta-toolenvvarschema
- name: ToolExecutionResult
  property_count: 6
  slug: letta-toolexecutionresult
- name: ToolJSONSchema
  property_count: 5
  slug: letta-tooljsonschema
- name: ToolReturnContent
  property_count: 4
  slug: letta-toolreturncontent
- name: ToolReturnCreate
  property_count: 4
  slug: letta-toolreturncreate
- name: ToolReturnMessage
  property_count: 16
  slug: letta-toolreturnmessage
- name: ToolRunFromSource
  property_count: 9
  slug: letta-toolrunfromsource
- name: ToolSearchRequest
  property_count: 5
  slug: letta-toolsearchrequest
- name: ToolSearchResult
  property_count: 5
  slug: letta-toolsearchresult
- name: ToolType
  property_count: 0
  slug: letta-tooltype
- name: ToolUpdate
  property_count: 12
  slug: letta-toolupdate
- name: TurnTokenData
  property_count: 5
  slug: letta-turntokendata
- name: UpdateAgent
  property_count: 37
  slug: letta-updateagent
- name: UpdateAssistantMessage
  property_count: 2
  slug: letta-updateassistantmessage
- name: UpdateConversation
  property_count: 4
  slug: letta-updateconversation
- name: UpdateMCPServerRequest
  property_count: 2
  slug: letta-updatemcpserverrequest
- name: UpdateReasoningMessage
  property_count: 2
  slug: letta-updatereasoningmessage
- name: UpdateSystemMessage
  property_count: 2
  slug: letta-updatesystemmessage
- name: UpdateUserMessage
  property_count: 2
  slug: letta-updateusermessage
- name: UrlImage
  property_count: 2
  slug: letta-urlimage
- name: UsageStatistics
  property_count: 5
  slug: letta-usagestatistics
- name: UsageStatisticsCompletionTokenDetails
  property_count: 1
  slug: letta-usagestatisticscompletiontokendetails
- name: UsageStatisticsPromptTokenDetails
  property_count: 3
  slug: letta-usagestatisticsprompttokendetails
- name: User
  property_count: 5
  slug: letta-user
- name: UserCreate
  property_count: 1
  slug: letta-usercreate
- name: UserMessage
  property_count: 11
  slug: letta-usermessage
- name: UserMessageListResult
  property_count: 6
  slug: letta-usermessagelistresult
- name: UserUpdate
  property_count: 2
  slug: letta-userupdate
- name: ValidationError
  property_count: 3
  slug: letta-validationerror
- name: VectorDBProvider
  property_count: 0
  slug: letta-vectordbprovider
- name: VoiceSleeptimeManager
  property_count: 4
  slug: letta-voicesleeptimemanager
- name: VoiceSleeptimeManagerSchema
  property_count: 4
  slug: letta-voicesleeptimemanagerschema
- name: VoiceSleeptimeManagerUpdate
  property_count: 4
  slug: letta-voicesleeptimemanagerupdate
- name: XAIModelSettings
  property_count: 5
  slug: letta-xaimodelsettings
- name: ZAIModelSettings
  property_count: 6
  slug: letta-zaimodelsettings
- name: ZAIThinking
  property_count: 2
  slug: letta-zaithinking
json_structures:
- name: Letta Agent Structure
  property_count: 0
  slug: letta-agent-structure
- name: Letta Archive Structure
  property_count: 0
  slug: letta-archive-structure
- name: Letta Block Structure
  property_count: 0
  slug: letta-block-structure
- name: Letta Embedding Config Structure
  property_count: 0
  slug: letta-embedding-config-structure
- name: Letta Group Structure
  property_count: 0
  slug: letta-group-structure
- name: Letta Identity Structure
  property_count: 0
  slug: letta-identity-structure
- name: Letta Job Structure
  property_count: 0
  slug: letta-job-structure
- name: Letta Llm Config Structure
  property_count: 0
  slug: letta-llm-config-structure
- name: Letta Message Structure
  property_count: 0
  slug: letta-message-structure
- name: Letta Passage Structure
  property_count: 0
  slug: letta-passage-structure
- name: Letta Provider Structure
  property_count: 0
  slug: letta-provider-structure
- name: Letta Run Structure
  property_count: 0
  slug: letta-run-structure
- name: Letta Source Structure
  property_count: 0
  slug: letta-source-structure
- name: Letta Structure
  property_count: 0
  slug: letta-structure
- name: Letta Tool Structure
  property_count: 0
  slug: letta-tool-structure
jsonld:
- class_count: 35
  name: Letta Context
  property_count: 34
  slug: letta-context
layout: provider
modified: '2026-08-08'
name: Letta
nav: Providers
network: true
overview: 'Letta publishes 48 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Agents API, Archives API, and 45 more. Tagged areas include Artificial Intelligence, Agents, Stateful Agents, Memory, and MemGPT.


  The Letta catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Letta''s developer surface includes authentication, engineering blog, documentation, GitHub presence, pricing, and 19 more developer resources.'
plans:
- name: Letta Plans Pricing
  plan_count: 3
  slug: letta-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Letta Rate Limits
  slug: letta-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Letta API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: letta-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Letta API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: letta-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.5
    catalog_earned_first_party: 0.0
    catalog_gap: 42.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 28.8
    contract_quality: 79.8
    developer_ergonomics: 31.0
    discoverability: 70.4
    governance: 28.8
    operational_transparency: 23.7
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/letta/refs/heads/main/screenshots/letta-2026-07-25T224937.png
security:
- kind: authentication
  name: Letta Authentication
  slug: letta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Letta Domain Security
  slug: letta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: letta
tags:
- Artificial Intelligence
- Agents
- Stateful Agents
- Memory
- MemGPT
- Continual Learning
- MCP
- Multi-Agent
- RAG
- Open-Source
website: https://www.letta.com/
---
