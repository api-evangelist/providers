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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 3
  name: Dify Agentic Access
  operation_count: 82
  slug: dify-agentic-access
  summary_line: 82 operations · 49 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to managing conversations. 6 operation(s) from the Dify Service API.
  name: Dify Conversations API
  phrasing_intents:
  - id: getConversationsList
    intent: List an end user's conversations
    question: How do I show a user their past chat conversations, most recent first?
  - id: getConversationHistory
    intent: Read a conversation's message history
    question: What messages were exchanged in a given conversation?
  - id: getConversationVariables
    intent: List the variables stored in a conversation
    question: Which conversation variables has my chatflow stored for this chat?
  - id: renameConversation
    intent: Rename or auto-title a conversation
    question: Can I give a conversation a custom title shown in the chat list?
  - id: updateChatConversationVariable
    intent: Change a conversation variable's value
    question: How do I overwrite the value of a conversation variable mid-chat?
  - id: deleteConversation
    intent: Delete a conversation
    question: How do I delete a chat conversation a user no longer wants?
  phrasing_ops: 6
  slug: dify-conversations-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: File upload and preview operations. 2 operation(s) from the Dify Service API.
  name: Dify Files API
  phrasing_intents:
  - id: uploadChatFile
    intent: Upload a file to attach to messages or runs
    question: How do I upload a local file so I can attach it to a chat message or workflow run?
  - id: previewChatFile
    intent: Download or preview an uploaded file
    question: Can I get back the raw bytes of a file that was uploaded to my app?
  phrasing_ops: 2
  slug: dify-files-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations to retrieve application settings and information. 4 operation(s) from the Dify Service API.
  name: Dify Applications API
  phrasing_intents:
  - id: getChatAppInfo
    intent: Get an app's name, mode and author
    question: What is the name, description and mode of the Dify app behind my API key?
  - id: getChatAppParameters
    intent: Get an app's input form and feature settings
    question: Which input variables does my app's user input form expect?
  - id: getChatAppMeta
    intent: Get the icons of the tools an app uses
    question: What icons should I display for the tools this app calls?
  - id: getChatWebAppSettings
    intent: Get the hosted web app's branding settings
    question: What title, icon and theme colors does the app's hosted web app use?
  phrasing_ops: 4
  slug: dify-applications-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to managing annotations for direct replies. 6 operation(s) from the Dify Service API.
  name: Dify Annotations API
  phrasing_intents:
  - id: createAnnotation
    intent: Add a predefined question-answer annotation
    question: How do I make my chatbot always give a fixed answer to a specific question?
  - id: getAnnotationList
    intent: List a chat app's annotations
    question: Which canned question-answer annotations does my Dify chatbot currently have?
  - id: updateAnnotation
    intent: Edit an existing annotation's question and answer
    question: Can I change the answer on an annotation I already created?
  - id: deleteAnnotation
    intent: Delete an annotation and its hit history
    question: What happens to an annotation's hit history when I remove it?
  - id: initialAnnotationReplySettings
    intent: Turn annotation reply on or off for an app
    question: How do I switch on annotation reply so my app answers from saved annotations?
  - id: getInitialAnnotationReplySettingsStatus
    intent: Check an annotation reply setup job's progress
    question: Has the job that enables annotation reply finished yet?
  phrasing_ops: 6
  slug: dify-annotations-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Text-to-Speech and Speech-to-Text operations. 2 operation(s) from the Dify Service API.
  name: Dify Audio API
  phrasing_intents:
  - id: audioToText
    intent: Transcribe an audio file to text
    question: How do I turn a voice recording into text with my Dify app?
  - id: textToAudioChat
    intent: Convert text or a message answer to speech
    question: Can I have an existing chat answer read aloud as audio?
  phrasing_ops: 2
  slug: dify-audio-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: User feedback operations. 2 operation(s) from the Dify Service API.
  name: Dify Feedback API
  phrasing_intents:
  - id: postChatMessageFeedback
    intent: Like, dislike or revoke feedback on a message
    question: How do I record a thumbs up or thumbs down on an assistant reply?
  - id: getChatAppFeedbacks
    intent: List all feedback on an app's messages
    question: What feedback have users and admins left across my Dify app?
  phrasing_ops: 2
  slug: dify-feedback-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to end user information. 1 operation(s) from the Dify Service API.
  name: Dify End Users API
  phrasing_intents:
  - id: getEndUserChat
    intent: Look up an end user by ID
    question: Who is the end user behind a created_by ID returned by another call?
  phrasing_ops: 1
  slug: dify-end-users-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Endpoints for resuming paused workflows that require human input. 2 operation(s) from the Dify Service API.
  name: Dify Human Input API
  phrasing_intents:
  - id: getChatflowHumanInputForm
    intent: Read a paused human input form
    question: What does the human input form that paused my workflow ask for?
  - id: submitChatflowHumanInputForm
    intent: Submit a human input form and resume the run
    question: How do I send a reviewer's answer so a paused Dify workflow continues?
  phrasing_ops: 2
  slug: dify-human-input-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for creating, updating, and managing documents within a knowledge base. 12 operation(s) from the Dify Service API.
  name: Dify Documents API
  phrasing_intents:
  - id: createDocumentFromText
    intent: Add a document to a knowledge base from raw text
    question: How do I add pasted text as a new document in my Dify knowledge base?
  - id: createDocumentFromFile
    intent: Add a document to a knowledge base from a file
    question: Can I upload a PDF or DOCX straight into a knowledge base as a new document?
  - id: listDocuments
    intent: List the documents in a knowledge base
    question: Which documents are in my knowledge base?
  - id: getDocumentDetail
    intent: Get details of a single knowledge base document
    question: What are the details and metadata of one document in my knowledge base?
  - id: deleteDocument
    intent: Delete a document and all its chunks
    question: How do I permanently remove a document from a knowledge base?
  - id: updateDocument
    intent: Replace a document's file and re-index it
    question: What is the recommended way to replace a document with a newer version of its file?
  - id: downloadDocument
    intent: Get a download link for a document's original file
    question: How do I download the original file I uploaded for a single document?
  - id: getDocumentIndexingStatus
    intent: Check indexing progress for a batch of documents
    question: Has my newly uploaded document finished indexing yet?
  phrasing_ops: 12
  slug: dify-documents-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing document chunks and child chunks. 9 operation(s) from the Dify Service API.
  name: Dify Chunks API
  phrasing_intents:
  - id: createSegments
    intent: Add new chunks to a document
    question: Can I manually add my own chunks of text to an existing document?
  - id: listSegments
    intent: List the chunks in a document
    question: How do I see how a knowledge base document was split into chunks?
  - id: getSegmentDetail
    intent: Get the full details of one chunk
    question: What is the full content and metadata of a single chunk?
  - id: updateSegment
    intent: Edit a chunk and re-index it
    question: Can I fix the text of a parent chunk that was split badly?
  - id: deleteSegment
    intent: Permanently delete a chunk
    question: How do I remove an irrelevant chunk from a document so it is never retrieved?
  - id: createChildChunk
    intent: Add a child chunk to a parent chunk
    question: How do I add a child chunk under a parent chunk in hierarchical chunking mode?
  - id: getChildChunks
    intent: List child chunks under a parent chunk
    question: Which child chunks sit under a given parent chunk in a parent-child document?
  - id: updateChildChunk
    intent: Edit the text of a child chunk
    question: How do I correct the wording of an existing child chunk?
  phrasing_ops: 9
  slug: dify-chunks-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge base tags and tag bindings. 7 operation(s) from the Dify Service API.
  name: Dify Knowledge Tags API
  phrasing_intents:
  - id: createKnowledgeTag
    intent: Create a knowledge base tag
    question: How do I create a new tag for grouping knowledge bases?
  - id: getKnowledgeTags
    intent: List all knowledge base tags
    question: Which tags exist for organizing knowledge bases in my workspace?
  - id: updateKnowledgeTag
    intent: Rename a knowledge base tag
    question: Can I rename a knowledge tag without re-tagging every knowledge base?
  - id: deleteKnowledgeTag
    intent: Delete a knowledge base tag
    question: Are tagged knowledge bases deleted when I delete the tag itself?
  - id: bindTagsToDataset
    intent: Attach tags to a knowledge base
    question: How do I tag a knowledge base with one or more tags?
  - id: unbindTagFromDataset
    intent: Remove tags from a knowledge base
    question: Can I untag a knowledge base without deleting the tag from the workspace?
  - id: queryDatasetTags
    intent: Get the tags on one knowledge base
    question: Which tags are currently bound to a specific knowledge base?
  phrasing_ops: 7
  slug: dify-tags-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge base metadata fields and document metadata values. 7 operation(s) from the Dify Service API.
  name: Dify Metadata API
  phrasing_intents:
  - id: createMetadataField
    intent: Create a custom metadata field
    question: How do I add a custom metadata field like author or date to my documents?
  - id: listMetadataFields
    intent: List a knowledge base's metadata fields
    question: Which metadata fields, custom and built-in, does my knowledge base have?
  - id: updateMetadataField
    intent: Rename a custom metadata field
    question: Can I rename a custom metadata field without losing its values?
  - id: deleteMetadataField
    intent: Delete a custom metadata field
    question: Do documents lose their values when I delete a custom metadata field?
  - id: getBuiltInMetadataFields
    intent: List the system's built-in metadata fields
    question: What built-in metadata fields does the system provide for documents?
  - id: toggleBuiltInMetadataField
    intent: Enable or disable built-in metadata fields
    question: How do I turn on the built-in metadata fields for a knowledge base?
  - id: batchUpdateDocumentMetadata
    intent: Set metadata values on many documents at once
    question: Can I tag many documents with metadata values in one request?
  phrasing_ops: 7
  slug: dify-metadata-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for retrieving available models. 1 operation(s) from the Dify Service API.
  name: Dify Models API
  phrasing_intents:
  - id: getAvailableModels
    intent: List available models of a given type
    question: Which embedding models can I configure on a Dify knowledge base?
  phrasing_ops: 1
  slug: dify-models-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing and running knowledge pipelines, including datasource plugins and pipeline execution. 4 operation(s) from the Dify Service API.
  name: Dify Knowledge Pipeline API
  phrasing_intents:
  - id: uploadPipelineFile
    intent: Upload a file for a knowledge pipeline run
    question: How do I upload a local file to feed into a knowledge pipeline?
  - id: listDatasourcePlugins
    intent: List a pipeline's datasource nodes and plugins
    question: Which datasource nodes and plugins are configured in my knowledge pipeline?
  - id: runDatasourceNode
    intent: Run a single datasource node in a pipeline
    question: Can I test just one datasource node of my knowledge pipeline on its own?
  - id: runPipeline
    intent: Run the full knowledge pipeline
    question: How do I run my whole knowledge pipeline over a set of datasources?
  phrasing_ops: 4
  slug: dify-knowledge-pipeline-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to chat messages and interactions.
  name: Dify Chat Messages API
  phrasing_intents:
  - id: sendChatMessage
    intent: Send a message to a chat app and get a reply
    question: How do I send a user's message to my Dify chatbot and get the assistant's reply?
  - id: stopChatMessageGeneration
    intent: Stop a streaming chat reply mid-generation
    question: Can I cancel a chat response that is still streaming?
  - id: getSuggestedQuestions
    intent: Get suggested follow-up questions for a message
    question: What follow-up questions does the app suggest after a given answer?
  phrasing_ops: 3
  slug: dify-chat-messages-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations related to text generation and completion.
  name: Dify Completion Messages API
  phrasing_intents:
  - id: createCompletionMessage
    intent: Generate text with a text generator app
    question: How do I get generated text from my Dify text generator app?
  - id: stopGenerate
    intent: Stop a streaming text completion
    question: Can I cancel a text generator completion that is still streaming?
  phrasing_ops: 2
  slug: dify-completion-messages-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for managing knowledge bases, including creation, configuration, and retrieval.
  name: Dify Knowledge Bases API
  phrasing_intents:
  - id: createDataset
    intent: Create an empty knowledge base
    question: How do I create a new, empty knowledge base before adding documents?
  - id: listDatasets
    intent: List knowledge bases in the workspace
    question: Which knowledge bases exist in my Dify workspace?
  - id: getDatasetDetail
    intent: Get a knowledge base's settings and stats
    question: What embedding model and retrieval settings does a knowledge base use?
  - id: updateDataset
    intent: Change a knowledge base's name or settings
    question: Can I rename an existing knowledge base or change its description?
  - id: deleteDataset
    intent: Permanently delete a knowledge base
    question: What happens to the documents when I delete an entire knowledge base?
  - id: retrieveSegments
    intent: Search a knowledge base for relevant chunks
    question: How do I test which chunks my knowledge base returns for a question?
  phrasing_ops: 6
  slug: dify-knowledge-bases-api
- baseURL: https://api.dify.ai/v1
  baseurl_source: declared
  description: Operations for executing and managing workflows.
  name: Dify Workflow Runs API
  phrasing_intents:
  - id: getWorkflowRunDetail
    intent: Get a workflow run's status and outputs
    question: What were the inputs, outputs and status of a specific workflow run?
  - id: getWorkflowLogs
    intent: List past workflow runs with filters
    question: Which workflow runs failed in my Dify app this week?
  - id: streamWorkflowEvents
    intent: Resume a workflow run's event stream
    question: How do I reconnect to a workflow run's event stream after my connection drops?
  - id: executeWorkflow
    intent: Run the app's latest published workflow
    question: How do I trigger my published workflow from code and get its outputs?
  - id: runWorkflowById
    intent: Run a specific published workflow version
    question: Can I pin a run to an older published workflow version instead of the latest?
  - id: stopWorkflowTaskGeneration
    intent: Stop a running streaming workflow task
    question: How do I cancel a workflow task that is still running in streaming mode?
  phrasing_ops: 6
  slug: dify-workflow-runs-api
artifact_total: 40
asyncapis:
- description: ''
  name: Dify Events
  slug: dify-events
collections:
- collection_type: open
  name: Dify Chat API
  slug: open-dify-chat-api
- collection_type: open
  name: Dify Chat Completion API
  slug: open-dify-completion-api
- collection_type: open
  name: Dify Chat Conversations API
  slug: open-dify-conversations-api
- collection_type: open
  name: Dify Chat Datasets API
  slug: open-dify-datasets-api
- collection_type: open
  name: Dify Chat Files API
  slug: open-dify-files-api
- collection_type: open
  name: Dify Chat Workflows API
  slug: open-dify-workflows-api
- collection_type: open
  name: Dify API
  slug: open-dify
common:
- group: other
  href: https://artifacts.apis.io/dify/capabilities/dify-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dify-capability-edges.yml
- group: docs
  href: https://artifacts.apis.io/dify/openapi/_original/dify-service-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/dify-service-api-openapi.json
- group: other
  href: https://artifacts.apis.io/dify/overlays/dify-service-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dify-service-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/dify/authentication/dify-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dify-authentication.yml
- group: design
  href: https://artifacts.apis.io/dify/conventions/dify-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dify-conventions.yml
- group: design
  href: https://artifacts.apis.io/dify/errors/dify-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dify-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dify/data-model/dify-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dify-data-model.yml
- group: design
  href: https://artifacts.apis.io/dify/lifecycle/dify-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dify-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/dify/changelog/dify-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dify-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dify.ai/
- group: design
  href: https://artifacts.apis.io/dify/conformance/dify-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dify/conformance/dify-conformance.yml
  title: ''
  type: Compliance
  url: conformance/dify-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dify/security/dify-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dify-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dify/security/dify-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dify-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dify/security/dify-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dify-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dify/security/dify-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dify-domain-security.yml
- group: build
  href: https://artifacts.apis.io/dify/packages/dify-packages.yml
  title: ''
  type: Packages
  url: packages/dify-packages.yml
- group: build
  href: https://artifacts.apis.io/dify/packages/dify-packages.yml
  title: ''
  type: SDKs
  url: packages/dify-packages.yml
- group: build
  href: https://artifacts.apis.io/dify/cli/dify-cli.yml
  title: ''
  type: CLI
  url: cli/dify-cli.yml
- group: design
  href: https://artifacts.apis.io/dify/components/dify-components.yml
  title: ''
  type: Components
  url: components/dify-components.yml
- group: start
  href: https://artifacts.apis.io/dify/sandbox/dify-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dify-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/dify/plans/dify-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dify-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dify/rate-limits/dify-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dify-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dify/finops/dify-finops.yml
  title: ''
  type: FinOps
  url: finops/dify-finops.yml
- group: design
  href: https://artifacts.apis.io/dify/asyncapi/dify-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/dify-events.yml
- group: agent
  href: https://artifacts.apis.io/dify/mcp/dify-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dify-mcp.yml
- group: build
  href: https://artifacts.apis.io/dify/mcp/dify-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dify-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/dify/a2a/dify-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dify-a2a.yml
- group: agent
  href: https://artifacts.apis.io/dify/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dify/well-known/dify-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dify-well-known.yml
- group: agent
  href: https://artifacts.apis.io/dify/agentic-access/dify-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dify-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/dify/llms/dify-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dify-llms.txt
- group: company
  title: ''
  type: Website
  url: https://dify.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dify.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dify.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dify.ai/en/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dify.ai/en/api-reference/guides/get-started
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dify.ai/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://dify.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.dify.ai/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.dify.ai/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dify.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dify.ai/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/FngNHpbcY7
- group: operate
  title: ''
  type: Community
  url: https://github.com/langgenius/dify/discussions
- group: company
  title: ''
  type: Blog
  url: https://dify.ai/blog
- group: operate
  title: ''
  type: RoadMap
  url: https://roadmap.dify.ai/roadmap
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.dify.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/langgenius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langgenius
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dify_ai
created: '2025-02-08'
description: Dify is an open-source platform for building AI applications, combining Backend-as-a-Service and LLMOps to streamline the development of generative AI solutions for developers and non-technical innovators alike. Teams build agentic workflows, chatflows, agents and RAG knowledge pipelines on a visual canvas, then publish each one as a web app, an embeddable widget, a REST API or an MCP server. Dify is operated by Langgenius, Inc. and ships as Dify Cloud, a self-hosted Community Edition and a commercial Enterprise edition.
finops:
- has_sources: true
  method: derived
  name: Dify Finops
  primary_unit: workspace
  service_category: ''
  slug: dify-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dify.png
layout: provider
mcp_servers:
- description: Dify's MCP posture has two distinct surfaces. (1) A live, anonymous, remote documentation MCP server at https://docs.dify.ai/mcp, confirmed by an unauthenticated tools/list call that returned three re
  name: Dify Docs MCP
  slug: dify-docs-mcp
modified: '2026-09-06'
name: Dify
nav: Providers
network: true
overview: 'Dify publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Conversations API, Files API, Applications API, and 15 more. Tagged areas include Artificial Intelligence, LLMOps, Backend-as-a-Service, Agents, and Workflows.


  The Dify catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Dify''s developer surface includes authentication, changelog, CLI, sandbox, documentation, API reference, getting-started guide, and 44 more developer resources.'
plans:
- name: Dify Plans Pricing
  plan_count: 5
  slug: dify-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Dify Rate Limits
  slug: dify-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Dify API Rules
  rule_count: 64
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 10
  slug: dify-rules
score:
  band: exemplar
  composite: 78.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 65.9
    developer_ergonomics: 85.0
    discoverability: 75.0
    operational_transparency: 89.5
  previous_composite: 77.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 94.7
      total: 19
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dify/dify-2026-06-20T180051.png
security:
- kind: authentication
  name: Dify Authentication
  slug: dify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dify Domain Security
  slug: dify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dify Vulnerability Disclosure
  slug: dify-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Dify Trust Center
  slug: dify-trust-center
  summary_line: SOC 2
skill_count: 4
skills:
- name: dify-chat-app-conversation
  slug: dify-chat-app-conversation
- name: dify-knowledge-base-ingest
  slug: dify-knowledge-base-ingest
- name: Dify
  slug: dify-provider-published-skill
- name: dify-workflow-run
  slug: dify-workflow-run
slug: dify
tags:
- Artificial Intelligence
- LLMOps
- Backend-as-a-Service
- Agents
- Workflows
- Knowledge Management
- RAG
- MCP
- Low-Code
- Open Source
- A2A
website: https://dify.ai/
---
