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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.4
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 183
  human_in_the_loop: 6
  name: Openai Agentic Access
  operation_count: 307
  slug: openai-agentic-access
  summary_line: 307 operations · 183 acting · 6 human-in-the-loop
api_count: 15
apis:
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs into a single streamlined interface, support
  name: OpenAI Responses API
  slug: openai-responses-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including harassment, hate speech, sexual content, self-harm, v
  name: OpenAI Moderations API
  slug: openai-moderations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports /v1/responses, /v1/chat/completions, /v1/embeddings, /
  name: OpenAI Batch API
  slug: openai-batch-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a file to a vector store it is automatically chu
  name: OpenAI Vector Stores API
  slug: openai-vector-stores-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in total and expires after an hour. Once you c
  name: OpenAI Uploads API
  slug: openai-uploads-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Realtime API enables low-latency, bidirectional communication with models that natively support speech-to-speech interactions as well as multimodal inputs (audio, images, and text) and outputs (au
  name: OpenAI Realtime API
  slug: openai-realtime-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Evals API allows you to programmatically configure and run evaluations to test model outputs against your expectations. Evaluations ensure model responses meet style and content criteria you speci
  name: OpenAI Evals API
  slug: openai-evals-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from a text prompt, checking video status, downlo
  name: OpenAI Videos API
  slug: openai-videos-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a created_at timestamp, and metadata. Because convers
  name: OpenAI Conversations API
  slug: openai-conversations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: 'The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers can be created explicitly or auto-managed, '
  name: OpenAI Containers API
  slug: openai-containers-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants, research companions, support agents, and more. Cha
  name: OpenAI ChatKit API
  slug: openai-chatkit-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Skills API surfaces OpenAI's Agent Skills — discoverable folders of instructions, scripts, and resources that agents (notably Codex) can use to perform specific tasks. Operations cover creating, r
  name: OpenAI Skills API
  slug: openai-skills-api
- description: The OpenAI Agents SDK is a lightweight framework for building multi-agent workflows in Python and TypeScript. Primitives include agents (LLMs with instructions, tools, guardrails), handoffs between sp
  name: OpenAI Agents SDK
  slug: openai-agents-sdk
- description: OpenAI Codex is a lightweight coding agent that runs in the terminal, with companion IDE extensions, a desktop app, and a web experience at chatgpt.com/codex. Codex authenticates with a ChatGPT Plus/P
  name: OpenAI Codex
  slug: openai-codex
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Build Assistants that can call models and use tools.
  name: OpenAI Assistants API
  slug: openai-assistants-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Learn how to turn audio into text or text into audio.
  name: OpenAI Audio API
  slug: openai-audio-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: List user actions and configuration changes within this organization.
  name: OpenAI Audit Logs API
  slug: openai-audit-logs-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Create large batches of API requests to run asynchronously.
  name: OpenAI Batch API
  slug: openai-batch-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Certificates API from OpenAI — 7 operation(s) for certificates.
  name: OpenAI Certificates API
  slug: openai-certificates-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given a list of messages comprising a conversation, the model will return a response.
  name: OpenAI Chat API
  slug: openai-chat-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Chatkit API from OpenAI — 5 operation(s) for chatkit.
  name: OpenAI Chatkit API
  slug: openai-chatkit-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.
  name: OpenAI Completions API
  slug: openai-completions-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Containers API from OpenAI — 5 operation(s) for containers.
  name: OpenAI Containers API
  slug: openai-containers-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Manage conversations and conversation items.
  name: OpenAI Conversations API
  slug: openai-conversations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
  name: OpenAI Embeddings API
  slug: openai-embeddings-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Manage and run evals in the OpenAI platform.
  name: OpenAI Evals API
  slug: openai-evals-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Files are used to upload documents that can be used with features like Assistants and Fine-tuning.
  name: OpenAI Files API
  slug: openai-files-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Fine Tuning API from OpenAI — 11 operation(s) for fine tuning.
  name: OpenAI Fine Tuning API
  slug: openai-fine-tuning-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Group organization role assignments API from OpenAI — 2 operation(s) for group organization role assignments.
  name: OpenAI Group organization role assignments API
  slug: openai-group-organization-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Group users API from OpenAI — 2 operation(s) for group users.
  name: OpenAI Group users API
  slug: openai-group-users-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Groups API from OpenAI — 2 operation(s) for groups.
  name: OpenAI Groups API
  slug: openai-groups-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given a prompt and/or an input image, the model will generate a new image.
  name: OpenAI Images API
  slug: openai-images-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Invites API from OpenAI — 2 operation(s) for invites.
  name: OpenAI Invites API
  slug: openai-invites-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: List and describe the various models available in the API.
  name: OpenAI Models API
  slug: openai-models-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given text and/or image inputs, classifies if those inputs are potentially harmful.
  name: OpenAI Moderations API
  slug: openai-moderations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Organization API from OpenAI — 2 operation(s) for organization.
  name: OpenAI Organization API
  slug: openai-organization-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project group role assignments API from OpenAI — 2 operation(s) for project group role assignments.
  name: OpenAI Project group role assignments API
  slug: openai-project-group-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project groups API from OpenAI — 2 operation(s) for project groups.
  name: OpenAI Project groups API
  slug: openai-project-groups-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project user role assignments API from OpenAI — 2 operation(s) for project user role assignments.
  name: OpenAI Project user role assignments API
  slug: openai-project-user-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Projects API from OpenAI — 11 operation(s) for projects.
  name: OpenAI Projects API
  slug: openai-projects-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Realtime API from OpenAI — 9 operation(s) for realtime.
  name: OpenAI Realtime API
  slug: openai-realtime-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Responses API from OpenAI — 6 operation(s) for responses.
  name: OpenAI Responses API
  slug: openai-responses-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Roles API from OpenAI — 4 operation(s) for roles.
  name: OpenAI Roles API
  slug: openai-roles-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Skills API from OpenAI — 6 operation(s) for skills.
  name: OpenAI Skills API
  slug: openai-skills-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Threads API from OpenAI — 13 operation(s) for threads.
  name: OpenAI Threads API
  slug: openai-threads-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Use Uploads to upload large files in multiple parts.
  name: OpenAI Uploads API
  slug: openai-uploads-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Usage API from OpenAI — 9 operation(s) for usage.
  name: OpenAI Usage API
  slug: openai-usage-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The User organization role assignments API from OpenAI — 2 operation(s) for user organization role assignments.
  name: OpenAI User organization role assignments API
  slug: openai-user-organization-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Users API from OpenAI — 2 operation(s) for users.
  name: OpenAI Users API
  slug: openai-users-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Vector stores API from OpenAI — 10 operation(s) for vector stores.
  name: OpenAI Vector stores API
  slug: openai-vector-stores-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Videos API from OpenAI — 8 operation(s) for videos.
  name: OpenAI Videos API
  slug: openai-videos-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The OpenAI API API from OpenAI — 0 operation(s) for openai api.
  name: OpenAI OpenAI API
  slug: openai-openai-api-api
arazzos:
- description: Create an assistant, open a thread, add a message, run it, poll the run, and read the reply.
  name: OpenAI Assistant Run
  slug: openai-assistant-run-workflow
- description: Upload a batch input file, create a batch, poll until complete, and read the output file id.
  name: OpenAI Batch Job
  slug: openai-batch-job-workflow
- description: Inspect a running fine-tuning job and cancel it only if it is still in progress.
  name: OpenAI Cancel Fine-Tuning Job
  slug: openai-cancel-fine-tuning-job-workflow
- description: Generate a chat reply, then synthesize it to spoken audio.
  name: OpenAI Chat then Speak
  slug: openai-chat-then-speak-workflow
- description: Confirm an embedding model exists, then embed input text.
  name: OpenAI Create Embedding
  slug: openai-create-embedding-workflow
- description: Retrieve a completed batch and download its output file contents.
  name: OpenAI Download Batch Results
  slug: openai-download-batch-results-workflow
- description: Upload a training file, start a fine-tuning job, poll until terminal, and read the result.
  name: OpenAI Fine-Tuning Job
  slug: openai-fine-tuning-job-workflow
- description: Screen an image prompt, then generate an image only when it is allowed.
  name: OpenAI Moderate then Generate Image
  slug: openai-generate-image-workflow
- description: Discover an available model, then generate a chat completion with it.
  name: OpenAI List Models then Create Chat Completion
  slug: openai-list-models-then-chat-workflow
- description: Screen user input with the moderation endpoint, then chat only if it is safe.
  name: OpenAI Moderate then Chat
  slug: openai-moderate-then-chat-workflow
- description: Inspect a model and delete it only when it is an owned fine-tuned model.
  name: OpenAI Retrieve and Delete Fine-Tuned Model
  slug: openai-retrieve-and-delete-model-workflow
- description: Start a thread and run in one request against an existing assistant, then poll and read the reply.
  name: OpenAI Create Thread and Run
  slug: openai-thread-and-run-workflow
- description: Transcribe an audio file, then summarize the transcript with a chat completion.
  name: OpenAI Transcribe then Summarize
  slug: openai-transcribe-then-summarize-workflow
- description: Upload a file, confirm it appears in the file list, and retrieve its metadata.
  name: OpenAI Upload and Verify File
  slug: openai-upload-and-verify-file-workflow
- description: Create a vector store, attach a batch of files, and poll the batch to completion.
  name: OpenAI Vector Store File Batch
  slug: openai-vector-store-file-batch-workflow
- description: Create a vector store, upload a file, attach it, and poll until it is indexed.
  name: OpenAI Vector Store Ingest File
  slug: openai-vector-store-ingest-file-workflow
- description: Attach a file to a vector store, wait until it is indexed, then run a semantic search.
  name: OpenAI Vector Store Search
  slug: openai-vector-store-search-workflow
artifact_total: 268
asyncapis:
- description: The OpenAI Realtime API provides low-latency, bidirectional, event-driven communication with multimodal models that natively support speech-to-speech, text, and audio in a single conversation. This As
  name: OpenAI Realtime API
  slug: openai-realtime-asyncapi
collections:
- collection_type: postman
  name: OpenAI Assistants
  slug: postman-assistants-openapi-original
- collection_type: postman
  name: OpenAI audio
  slug: postman-audio-openapi-original
- collection_type: postman
  name: OpenAI Chat
  slug: postman-chat-openapi-original
- collection_type: postman
  name: OpenAI Completions
  slug: postman-completions-openapi-original
- collection_type: postman
  name: OpenAI embeddings
  slug: postman-embeddings-openapi-original
- collection_type: postman
  name: OpenAI files
  slug: postman-files-openapi-original
- collection_type: postman
  name: OpenAI fine tuning
  slug: postman-fine-tuning-openapi-original
- collection_type: postman
  name: OpenAI images
  slug: postman-images-openapi-original
- collection_type: postman
  name: OpenAI models
  slug: postman-models-openapi-original
- collection_type: postman
  name: OpenAI Audio API
  slug: postman-openai-audio
- collection_type: postman
  name: OpenAI Chat Completions API
  slug: postman-openai-chat-completions
- collection_type: postman
  name: OpenAI Embeddings API
  slug: postman-openai-embeddings
- collection_type: postman
  name: OpenAI Images API
  slug: postman-openai-images
- collection_type: postman
  name: OpenAI threads
  slug: postman-threads-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenAI Assistants API
  slug: open-openai-assistants-api
- collection_type: open
  name: OpenAI Assistants Audio API
  slug: open-openai-audio-api
- collection_type: open
  name: OpenAI Audio API
  slug: open-openai-audio
- collection_type: open
  name: OpenAI Assistants Audit Logs API
  slug: open-openai-audit-logs-api
- collection_type: open
  name: OpenAI Assistants Batch API
  slug: open-openai-batch-api
- collection_type: open
  name: OpenAI Assistants Certificates API
  slug: open-openai-certificates-api
- collection_type: open
  name: OpenAI Assistants Chat API
  slug: open-openai-chat-api
- collection_type: open
  name: OpenAI Chat Completions API
  slug: open-openai-chat-completions
- collection_type: open
  name: OpenAI Assistants Chatkit API
  slug: open-openai-chatkit-api
- collection_type: open
  name: OpenAI Assistants Completions API
  slug: open-openai-completions-api
- collection_type: open
  name: OpenAI Assistants Containers API
  slug: open-openai-containers-api
- collection_type: open
  name: OpenAI Assistants Conversations API
  slug: open-openai-conversations-api
- collection_type: open
  name: OpenAI Assistants Embeddings API
  slug: open-openai-embeddings-api
- collection_type: open
  name: OpenAI Embeddings API
  slug: open-openai-embeddings
- collection_type: open
  name: OpenAI Assistants Evals API
  slug: open-openai-evals-api
- collection_type: open
  name: OpenAI Assistants Files API
  slug: open-openai-files-api
- collection_type: open
  name: OpenAI Assistants Fine Tuning API
  slug: open-openai-fine-tuning-api
- collection_type: open
  name: OpenAI Assistants Group organization role assignments API
  slug: open-openai-group-organization-role-assignments-api
- collection_type: open
  name: OpenAI Assistants Group users API
  slug: open-openai-group-users-api
- collection_type: open
  name: OpenAI Assistants Groups API
  slug: open-openai-groups-api
- collection_type: open
  name: OpenAI Assistants Images API
  slug: open-openai-images-api
- collection_type: open
  name: OpenAI Images API
  slug: open-openai-images
- collection_type: open
  name: OpenAI Assistants Invites API
  slug: open-openai-invites-api
- collection_type: open
  name: OpenAI Assistants Models API
  slug: open-openai-models-api
- collection_type: open
  name: OpenAI Assistants Moderations API
  slug: open-openai-moderations-api
- collection_type: open
  name: OpenAI API
  slug: open-openai-openapi-master
- collection_type: open
  name: OpenAI Assistants Organization API
  slug: open-openai-organization-api
- collection_type: open
  name: OpenAI Assistants Project group role assignments API
  slug: open-openai-project-group-role-assignments-api
- collection_type: open
  name: OpenAI Assistants Project groups API
  slug: open-openai-project-groups-api
- collection_type: open
  name: OpenAI Assistants Project user role assignments API
  slug: open-openai-project-user-role-assignments-api
- collection_type: open
  name: OpenAI Assistants Projects API
  slug: open-openai-projects-api
- collection_type: open
  name: OpenAI Assistants Realtime API
  slug: open-openai-realtime-api
- collection_type: open
  name: OpenAI Assistants Responses API
  slug: open-openai-responses-api
- collection_type: open
  name: OpenAI Assistants Roles API
  slug: open-openai-roles-api
- collection_type: open
  name: OpenAI Assistants Skills API
  slug: open-openai-skills-api
- collection_type: open
  name: OpenAI Assistants Threads API
  slug: open-openai-threads-api
- collection_type: open
  name: OpenAI Assistants Uploads API
  slug: open-openai-uploads-api
- collection_type: open
  name: OpenAI Assistants Usage API
  slug: open-openai-usage-api
- collection_type: open
  name: OpenAI Assistants User organization role assignments API
  slug: open-openai-user-organization-role-assignments-api
- collection_type: open
  name: OpenAI Assistants Users API
  slug: open-openai-users-api
- collection_type: open
  name: OpenAI Assistants Vector stores API
  slug: open-openai-vector-stores-api
- collection_type: open
  name: OpenAI Assistants Videos API
  slug: open-openai-videos-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/openai-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/openai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openai-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openai/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-assistant-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-batch-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-cancel-fine-tuning-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-chat-then-speak-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-create-embedding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-download-batch-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-fine-tuning-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-generate-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-list-models-then-chat-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-moderate-then-chat-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-retrieve-and-delete-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-thread-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-transcribe-then-summarize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-upload-and-verify-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-vector-store-file-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-vector-store-ingest-file-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/openai-vector-store-search-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openai
- group: start
  title: ''
  type: Portal
  url: https://platform.openai.com/docs/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.openai.com/docs/quickstart
- group: build
  title: ''
  type: SDKs
  url: https://platform.openai.com/docs/libraries
- group: operate
  title: ''
  type: Forums
  url: https://community.openai.com/categories
- group: operate
  title: ''
  type: RateLimits
  url: https://platform.openai.com/docs/guides/rate-limits
- group: operate
  title: ''
  type: Deprecations
  url: https://platform.openai.com/docs/deprecations
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openai.com/policies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openai.com/policies/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openai.com/policies/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/overview
- group: operate
  title: ''
  type: Support
  url: https://help.openai.com/en
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openai.com/
- group: auth
  title: ''
  type: Authentication
  url: https://platform.openai.com/docs/api-reference/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://platform.openai.com/docs/api-reference/webhook_events/response
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openai-chat-completion-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openai-embedding-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/openai-context.jsonld
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openai
- group: commercial
  title: ''
  type: Plans
  url: https://openai.com/api/pricing/
- group: commercial
  title: ''
  type: Pricing
  url: https://openai.com/api/pricing/
- group: other
  title: ''
  type: Tiers
  url: https://openai.com/api/pricing/
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.openai.com/api/docs/guides/rate-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openai.com/
- group: auth
  title: ''
  type: API Keys
  url: https://platform.openai.com/api-keys
- group: start
  title: ''
  type: Signup
  url: https://platform.openai.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.openai.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.openai.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://developers.openai.com/blog/
- group: learn
  title: ''
  type: Cookbook
  url: https://cookbook.openai.com/
- group: other
  title: ''
  type: SafetyBestPractices
  url: https://platform.openai.com/docs/guides/safety-best-practices
- group: other
  title: ''
  type: BestPractices
  url: https://platform.openai.com/docs/guides/production-best-practices
- group: auth
  title: ''
  type: Security
  url: https://openai.com/security-and-privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/administration
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/audit-logs
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/usage
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/function-calling
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/structured-outputs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-openapi
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/openai-openapi-master.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-node
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-go
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-dotnet
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-java
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-ruby
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-agents-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-agents-js
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/codex
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/skills
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/gpt-oss
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/openai-realtime-agents
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/whisper
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/tiktoken
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openai.com/policies/service-terms/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/webhook-events
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/deep-research/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/voice-agents/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/code-generation/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/guides/images-vision
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/conversation-state/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/docs/guides/migrate-to-responses/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/containers
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/container-files
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/chatkit
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/videos
- group: docs
  title: ''
  type: Documentation
  url: https://platform.openai.com/docs/api-reference/conversations/create
- group: start
  title: ''
  type: Portal
  url: https://developers.openai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/api/reference/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.openai.com/codex
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/openai/chatkit-js
- group: design
  title: ''
  type: SpectralRules
  url: rules/openai-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openai-vocabulary.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/openai/skills
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.openai.com/llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/openai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/openai-packages.yml
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/openai/openai-python
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/openai/openai-node
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/openai/openai-go
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/openai/openai-java
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/openai/openai-ruby
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/openai-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/openai-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openai-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/openai-responses-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/openai-chat-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/openai-embeddings-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/openai-grpc.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/openai-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/openai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/openai-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openai-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/openai-sandbox.yml
- group: other
  title: ''
  type: Playground
  url: https://platform.openai.com/playground
- group: start
  title: ''
  type: Console
  url: https://platform.openai.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/openai-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/openai-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/openai-cli.yml
- group: build
  title: ''
  type: CLI
  url: https://learn.chatgpt.com/docs/codex/cli
- group: design
  title: ''
  type: Components
  url: components/openai-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/openai-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/openai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openai-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/openai-realtime-asyncapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.openai.com/api/reference/
created: '2024-04-14'
description: OpenAI publishes a single unversioned REST API at https://api.openai.com/v1 covering text and reasoning (Responses, Chat Completions), embeddings, images, audio and speech, video, moderation, file storage, vector stores and file search, containers, batch inference at half price, fine-tuning, evals, ChatKit, agent skills, and a full organization administration plane for projects, users, groups, roles, API keys, certificates, usage and audit logs. The contract is OpenAPI 3.1.0 with 242 operations, published by OpenAI itself under MIT at github.com/openai/openai-openapi. Realtime is a separate WebSocket surface at wss://api.openai.com/v1/realtime. Authentication is a project-scoped bearer API key; OAuth 2.0 / OIDC at auth.openai.com grants user identity only, not API authority. First-party SDKs ship for Python, JavaScript, Go, Java, .NET and Ruby, alongside the Codex CLI and an anonymous documentation MCP server at developers.openai.com/mcp.
examples:
- key_count: 6
  name: Openai Audio Create Speech Request Example
  slug: openai-audio-create-speech-request-example
- key_count: 7
  name: Openai Audio Create Transcription Request Example
  slug: openai-audio-create-transcription-request-example
- key_count: 5
  name: Openai Audio Create Translation Request Example
  slug: openai-audio-create-translation-request-example
- key_count: 6
  name: Openai Audio Transcription Response Example
  slug: openai-audio-transcription-response-example
- key_count: 5
  name: Openai Audio Translation Response Example
  slug: openai-audio-translation-response-example
- key_count: 4
  name: Openai Chat Completions Chat Completion Choice Example
  slug: openai-chat-completions-chat-completion-choice-example
- key_count: 5
  name: Openai Chat Completions Chat Completion Message Example
  slug: openai-chat-completions-chat-completion-message-example
- key_count: 2
  name: Openai Chat Completions Chat Completion Tool Example
  slug: openai-chat-completions-chat-completion-tool-example
- key_count: 5
  name: Openai Chat Completions Completion Usage Example
  slug: openai-chat-completions-completion-usage-example
- key_count: 3
  name: Openai Chat Completions Content Part Example
  slug: openai-chat-completions-content-part-example
- key_count: 21
  name: Openai Chat Completions Create Chat Completion Request Example
  slug: openai-chat-completions-create-chat-completion-request-example
- key_count: 7
  name: Openai Chat Completions Create Chat Completion Response Example
  slug: openai-chat-completions-create-chat-completion-response-example
- key_count: 3
  name: Openai Chat Completions Tool Call Example
  slug: openai-chat-completions-tool-call-example
- key_count: 5
  name: Openai Embeddings Create Embedding Request Example
  slug: openai-embeddings-create-embedding-request-example
- key_count: 3
  name: Openai Embeddings Create Embedding Response Example
  slug: openai-embeddings-create-embedding-response-example
- key_count: 3
  name: Openai Embeddings Embedding Example
  slug: openai-embeddings-embedding-example
- key_count: 2
  name: Openai Embeddings Embedding Usage Example
  slug: openai-embeddings-embedding-usage-example
- key_count: 8
  name: Openai Images Create Image Edit Request Example
  slug: openai-images-create-image-edit-request-example
- key_count: 8
  name: Openai Images Create Image Request Example
  slug: openai-images-create-image-request-example
- key_count: 6
  name: Openai Images Create Image Variation Request Example
  slug: openai-images-create-image-variation-request-example
- key_count: 3
  name: Openai Images Image Example
  slug: openai-images-image-example
- key_count: 2
  name: Openai Images Images Response Example
  slug: openai-images-images-response-example
features:
- GPT-5.5 flagship model at $5/$30 per MTok input/output
- GPT-5.5 Pro for highest reasoning at $30/$180 per MTok
- GPT-5.4 mid-tier balanced model at $2.50/$15 per MTok
- GPT-5.4 Mini at $0.75/$4.50 per MTok
- GPT-5.4 Nano cheapest model at $0.20/$1.25 per MTok
- GPT Realtime 1.5 for low-latency voice with separate audio pricing
- Cached input at ~10x discount vs uncached
- Batch API at 50% discount on input and output
- Flex tier for reduced cost / lower priority workloads
- Vision, tool use, structured outputs, and function calling
- Six usage tiers (Free + Tier 1-5) with automatic spend-based advancement
- 'Five rate limit metrics: RPM, RPD, TPM, TPD, IPM'
- Per-model rate ceilings; X-RateLimit-* headers on every response
- Project-level API keys for cost allocation
- Cost Tracking API and per-project hard spend limits
- Regional data residency with 10% uplift
finops:
- name: Openai Finops
  service_category: AI and Machine Learning
  slug: openai-finops
graphqls:
- description: OpenAI does not offer a native public GraphQL endpoint. All official API access is provided through the OpenAI REST API at `https://api.openai.com/v1`. This schema is a comprehensive conceptual GraphQ
  name: OpenAI GraphQL
  slug: openai-graphql
image: https://openai.com/favicon.ico
integrations:
- description: Official Python client library for accessing all OpenAI API endpoints with async support and streaming.
  name: Python SDK
- description: Official TypeScript and JavaScript client library for server-side and edge runtime OpenAI API integration.
  name: Node.js SDK
- description: Run OpenAI models on Azure infrastructure with enterprise security, compliance, and regional data residency.
  name: Microsoft Azure OpenAI
- description: Framework integration for building LLM-powered applications with chains, agents, and retrieval-augmented generation.
  name: LangChain
- description: Integration with Vercel AI SDK for building streaming AI-powered web applications with React and Next.js.
  name: Vercel AI SDK
- description: No-code automation integration connecting OpenAI to thousands of apps for automated AI-powered workflows.
  name: Zapier
json_schemas:
- name: CreateSpeechRequest
  property_count: 6
  slug: openai-audio-create-speech-request
- name: CreateTranscriptionRequest
  property_count: 7
  slug: openai-audio-create-transcription-request
- name: CreateTranslationRequest
  property_count: 5
  slug: openai-audio-create-translation-request
- name: TranscriptionResponse
  property_count: 6
  slug: openai-audio-transcription-response
- name: TranslationResponse
  property_count: 5
  slug: openai-audio-translation-response
- name: OpenAI Chat Completion
  property_count: 8
  slug: openai-chat-completion
- name: ChatCompletionChoice
  property_count: 4
  slug: openai-chat-completions-chat-completion-choice
- name: ChatCompletionMessage
  property_count: 5
  slug: openai-chat-completions-chat-completion-message
- name: ChatCompletionTool
  property_count: 2
  slug: openai-chat-completions-chat-completion-tool
- name: CompletionUsage
  property_count: 5
  slug: openai-chat-completions-completion-usage
- name: ContentPart
  property_count: 3
  slug: openai-chat-completions-content-part
- name: CreateChatCompletionRequest
  property_count: 21
  slug: openai-chat-completions-create-chat-completion-request
- name: CreateChatCompletionResponse
  property_count: 7
  slug: openai-chat-completions-create-chat-completion-response
- name: ToolCall
  property_count: 3
  slug: openai-chat-completions-tool-call
- name: OpenAI Embedding Response
  property_count: 4
  slug: openai-embedding
- name: CreateEmbeddingRequest
  property_count: 5
  slug: openai-embeddings-create-embedding-request
- name: CreateEmbeddingResponse
  property_count: 3
  slug: openai-embeddings-create-embedding-response
- name: Embedding
  property_count: 3
  slug: openai-embeddings-embedding
- name: EmbeddingUsage
  property_count: 2
  slug: openai-embeddings-embedding-usage
- name: CreateImageEditRequest
  property_count: 8
  slug: openai-images-create-image-edit-request
- name: CreateImageRequest
  property_count: 8
  slug: openai-images-create-image-request
- name: CreateImageVariationRequest
  property_count: 6
  slug: openai-images-create-image-variation-request
- name: Image
  property_count: 3
  slug: openai-images-image
- name: ImagesResponse
  property_count: 2
  slug: openai-images-images-response
json_structures:
- name: Openai Audio Create Speech Request Structure
  property_count: 6
  slug: openai-audio-create-speech-request-structure
- name: Openai Audio Create Transcription Request Structure
  property_count: 7
  slug: openai-audio-create-transcription-request-structure
- name: Openai Audio Create Translation Request Structure
  property_count: 5
  slug: openai-audio-create-translation-request-structure
- name: Openai Audio Transcription Response Structure
  property_count: 6
  slug: openai-audio-transcription-response-structure
- name: Openai Audio Translation Response Structure
  property_count: 5
  slug: openai-audio-translation-response-structure
- name: Openai Chat Completions Chat Completion Choice Structure
  property_count: 4
  slug: openai-chat-completions-chat-completion-choice-structure
- name: Openai Chat Completions Chat Completion Message Structure
  property_count: 5
  slug: openai-chat-completions-chat-completion-message-structure
- name: Openai Chat Completions Chat Completion Tool Structure
  property_count: 2
  slug: openai-chat-completions-chat-completion-tool-structure
- name: Openai Chat Completions Completion Usage Structure
  property_count: 5
  slug: openai-chat-completions-completion-usage-structure
- name: Openai Chat Completions Content Part Structure
  property_count: 3
  slug: openai-chat-completions-content-part-structure
- name: Openai Chat Completions Create Chat Completion Request Structure
  property_count: 21
  slug: openai-chat-completions-create-chat-completion-request-structure
- name: Openai Chat Completions Create Chat Completion Response Structure
  property_count: 7
  slug: openai-chat-completions-create-chat-completion-response-structure
- name: Openai Chat Completions Tool Call Structure
  property_count: 3
  slug: openai-chat-completions-tool-call-structure
- name: Openai Embeddings Create Embedding Request Structure
  property_count: 5
  slug: openai-embeddings-create-embedding-request-structure
- name: Openai Embeddings Create Embedding Response Structure
  property_count: 3
  slug: openai-embeddings-create-embedding-response-structure
- name: Openai Embeddings Embedding Structure
  property_count: 3
  slug: openai-embeddings-embedding-structure
- name: Openai Embeddings Embedding Usage Structure
  property_count: 2
  slug: openai-embeddings-embedding-usage-structure
- name: Openai Images Create Image Edit Request Structure
  property_count: 8
  slug: openai-images-create-image-edit-request-structure
- name: Openai Images Create Image Request Structure
  property_count: 8
  slug: openai-images-create-image-request-structure
- name: Openai Images Create Image Variation Request Structure
  property_count: 6
  slug: openai-images-create-image-variation-request-structure
- name: Openai Images Image Structure
  property_count: 3
  slug: openai-images-image-structure
- name: Openai Images Images Response Structure
  property_count: 2
  slug: openai-images-images-response-structure
jsonld:
- class_count: 0
  name: Openai Audio Context
  property_count: 0
  slug: openai-audio-context
- class_count: 0
  name: Openai Chat Completions Context
  property_count: 0
  slug: openai-chat-completions-context
- class_count: 0
  name: Openai Context
  property_count: 15
  slug: openai-context
- class_count: 0
  name: Openai Embeddings Context
  property_count: 0
  slug: openai-embeddings-context
- class_count: 0
  name: Openai Images Context
  property_count: 0
  slug: openai-images-context
layout: provider
mcp_servers:
- description: OpenAI runs one remote MCP server of its own and it is a DOCUMENTATION server, not an API-control server. `openai-docs-mcp` lets an agent search, browse and fetch the markdown behind platform.openai.c
  name: OpenAI MCP Server
  slug: openai-mcp-server
modified: '2026-08-27'
name: OpenAI
nav: Providers
network: true
overview: 'OpenAI publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Responses API, Moderations API, Batch API, and 47 more. Tagged areas include Artificial Intelligence, Large Language Models, and T1.


  The OpenAI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 5 JSON-LD contexts, and 3 Spectral governance rulesets.


  OpenAI''s developer surface includes authentication, developer portal, getting-started guide, documentation, support, pricing, signup flow, and 129 more developer resources.'
plans:
- name: Openai Plans Pricing
  plan_count: 13
  slug: openai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 7
  name: Openai Rate Limits
  slug: openai-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: OpenAI API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: openai-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: OpenAI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: openai-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: OpenAI API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: openai-spectral-rules
scopes:
- name: Openai Scopes
  scope_count: 0
  slug: openai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 84.3
  coverage:
    artifact_dirs: 39
    catalog_gap: 28.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 47.0
    contract_quality: 78.9
    developer_ergonomics: 100.0
    discoverability: 66.7
    governance: 47.0
    operational_transparency: 94.7
  previous_composite: 84.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openai/refs/heads/main/screenshots/openai-2026-08-17T082822.png
security:
- kind: authentication
  name: Openai Authentication
  slug: openai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openai Domain Security
  slug: openai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Openai Vulnerability Disclosure
  slug: openai-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
- kind: trust-center
  name: Openai Trust Center
  slug: openai-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, FedRAMP, GDPR, CSA STAR
skill_count: 44
skills:
- name: aspnet-core
  slug: aspnet-core
- name: chatgpt-apps
  slug: chatgpt-apps
- name: cli-creator
  slug: cli-creator
- name: cloudflare-deploy
  slug: cloudflare-deploy
- name: define-goal
  slug: define-goal
- name: figma-code-connect-components
  slug: figma-code-connect-components
- name: figma-create-design-system-rules
  slug: figma-create-design-system-rules
- name: figma-create-new-file
  slug: figma-create-new-file
- name: figma-generate-design
  slug: figma-generate-design
- name: figma-generate-library
  slug: figma-generate-library
- name: figma-implement-design
  slug: figma-implement-design
- name: figma-use
  slug: figma-use
- name: figma
  slug: figma
- name: gh-address-comments
  slug: gh-address-comments
- name: gh-fix-ci
  slug: gh-fix-ci
- name: hatch-pet
  slug: hatch-pet
- name: imagegen
  slug: imagegen
- name: jupyter-notebook
  slug: jupyter-notebook
- name: linear
  slug: linear
- name: migrate-to-codex
  slug: migrate-to-codex
- name: netlify-deploy
  slug: netlify-deploy
- name: notion-knowledge-capture
  slug: notion-knowledge-capture
- name: notion-meeting-intelligence
  slug: notion-meeting-intelligence
- name: notion-research-documentation
  slug: notion-research-documentation
slug: openai
tags:
- Artificial Intelligence
- Large Language Models
- T1
use_cases:
- description: Build chatbots, virtual assistants, and customer support agents using Chat Completions or Responses API.
  name: Conversational AI
- description: Generate marketing copy, articles, product descriptions, and creative writing with controllable tone and style.
  name: Content Generation
- description: Automate code writing, debugging, refactoring, and documentation generation across programming languages.
  name: Code Generation
- description: Extract, summarize, and answer questions from uploaded documents using Assistants with file search.
  name: Document Analysis
- description: Build real-time voice-based AI agents for customer service, sales, and interactive experiences.
  name: Voice Agents
- description: Implement intelligent search using embeddings and vector stores for knowledge bases and document retrieval.
  name: Semantic Search
- description: Automatically classify and filter harmful content across text and images using the Moderations API.
  name: Content Moderation
- description: Extract structured data from unstructured text using function calling and structured outputs.
  name: Data Extraction
website: https://platform.openai.com/docs/overview
---
