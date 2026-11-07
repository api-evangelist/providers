---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 154
  human_in_the_loop: 6
  name: Openai Agentic Access
  operation_count: 265
  slug: openai-agentic-access
  summary_line: 265 operations · 154 acting · 6 human-in-the-loop
api_count: 16
apis:
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Responses API is OpenAI's most advanced interface for generating model responses. It combines the strengths of the Chat Completions and Assistants APIs into a single streamlined interface, support
  name: OpenAI Responses API
  phrasing_intents:
  - id: createResponse
    intent: Generate a model response
    question: How do I send a prompt to a model and get text or JSON back?
  - id: getResponse
    intent: Retrieve a model response
    question: Can I fetch the output of a response I generated earlier by its ID?
  - id: deleteResponse
    intent: Delete a stored model response
    question: How do I delete a stored response so it's no longer kept?
  - id: cancelResponse
    intent: Cancel a background response
    question: Can I stop a background response that is still generating?
  - id: listInputItems
    intent: List the input items of a response
    question: What inputs were sent to the model to produce a given response?
  - id: Getinputtokencounts
    intent: Count input tokens before sending a request
    question: How many input tokens will my prompt use before I actually run it?
  - id: Compactconversation
    intent: Compact a long conversation
    question: My conversation is getting too long for the context window — how can I shrink it?
  phrasing_ops: 7
  slug: openai-responses-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Moderations API can be used to check whether text or images are potentially harmful. It classifies content across several categories including harassment, hate speech, sexual content, self-harm, v
  name: OpenAI Moderations API
  phrasing_intents:
  - id: createModeration
    intent: Check text or images for harmful content
    question: How do I check whether a user's message is harmful before showing it?
  phrasing_ops: 1
  slug: openai-moderations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Batch API enables asynchronous processing of requests with 50% cost discount, higher rate limits, and completion within 24 hours. It supports /v1/responses, /v1/chat/completions, /v1/embeddings, /
  name: OpenAI Batch API
  phrasing_intents:
  - id: createBatch
    intent: Submit a batch of requests from a file
    question: How do I run a large file of API requests asynchronously as a batch?
  - id: listBatches
    intent: List my organization's batches
    question: Which batch jobs has my organization submitted?
  - id: retrieveBatch
    intent: Check the status of a batch
    question: Has my batch finished, and where is its output file?
  - id: cancelBatch
    intent: Cancel an in-progress batch
    question: How do I stop a batch that is still running?
  phrasing_ops: 4
  slug: openai-batch-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Vector stores are collections of processed files that power semantic search for the file_search tool in the Responses and Assistants APIs. When you add a file to a vector store it is automatically chu
  name: OpenAI Vector Stores API
  phrasing_intents:
  - id: listVectorStores
    intent: List my vector stores
    question: Which vector stores have I created for file search?
  - id: createVectorStore
    intent: Create a vector store
    question: How do I set up a new vector store so my assistant can search my documents?
  - id: getVectorStore
    intent: Retrieve a vector store
    question: How many files are in a vector store and are they done processing?
  - id: modifyVectorStore
    intent: Rename or update a vector store
    question: Can I rename a vector store after creating it?
  - id: deleteVectorStore
    intent: Delete a vector store
    question: How do I get rid of a vector store I'm done with?
  - id: createVectorStoreFileBatch
    intent: Add many files to a vector store at once
    question: What's the most efficient way to add hundreds of files to a vector store in one go?
  - id: getVectorStoreFileBatch
    intent: Check a vector store file batch
    question: Has my batch of files finished indexing into the vector store?
  - id: cancelVectorStoreFileBatch
    intent: Cancel a vector store file batch
    question: Can I stop a file batch that's still being processed into a vector store?
  phrasing_ops: 16
  slug: openai-vector-stores-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Uploads API creates an intermediate Upload object that you can add Parts to, enabling large file uploads. Currently an Upload can accept at most 8 GB in total and expires after an hour. Once you c
  name: OpenAI Uploads API
  phrasing_intents:
  - id: createUpload
    intent: Start a multipart upload for a large file
    question: How do I upload a file too large for a single request?
  - id: cancelUpload
    intent: Cancel a multipart upload
    question: Can I abandon a large upload partway through?
  - id: completeUpload
    intent: Finish a multipart upload into a usable file
    question: Once all parts are uploaded, how do I turn them into a usable file?
  - id: addUploadPart
    intent: Add a chunk to a multipart upload
    question: How do I send the next chunk of bytes for a large file upload?
  phrasing_ops: 4
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
  phrasing_intents:
  - id: listEvals
    intent: List evaluations in a project
    question: Which evals have I set up in this project?
  - id: createEval
    intent: Create an evaluation
    question: How do I define an eval to test how well a model performs on my data?
  - id: getEval
    intent: Retrieve an evaluation
    question: What testing criteria does one of my evals use?
  - id: updateEval
    intent: Rename or retag an evaluation
    question: Can I rename an evaluation after I've created it?
  - id: deleteEval
    intent: Delete an evaluation
    question: How do I remove an evaluation I no longer need?
  - id: getEvalRuns
    intent: List the runs of an evaluation
    question: What runs have been executed against one of my evals?
  - id: createEvalRun
    intent: Start an evaluation run
    question: How do I kick off a run to test a model against an existing eval?
  - id: getEvalRun
    intent: Check an evaluation run
    question: Has my eval run finished, and what were the results?
  phrasing_ops: 12
  slug: openai-evals-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Videos API enables programmatic creation, extension, and remixing of videos using Sora models. It provides endpoints for creating a new render job from a text prompt, checking video status, downlo
  name: OpenAI Videos API
  phrasing_intents:
  - id: createVideo
    intent: Generate a new video from a prompt
    question: How do I generate a video from a text prompt?
  - id: ListVideos
    intent: List recently generated videos
    question: Which videos have I generated recently in this project?
  - id: CreateVideoCharacter
    intent: Create a reusable character from a video
    question: Can I turn someone in an uploaded video into a character I can reuse?
  - id: GetVideoCharacter
    intent: Get a saved video character
    question: What details are stored for a video character I created?
  - id: CreateVideoEdit
    intent: Edit a video with a prompt
    question: How do I change something in an existing video using a prompt?
  - id: CreateVideoExtend
    intent: Extend a completed video
    question: Can I make a finished video longer by continuing it?
  - id: GetVideo
    intent: Check a video generation job's status
    question: Is my video still rendering or has it completed?
  - id: DeleteVideo
    intent: Delete a video and its stored assets
    question: How do I permanently delete a generated video?
  phrasing_ops: 10
  slug: openai-videos-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Conversations API allows you to create and manage stateful conversations for use with the Responses API. A conversation object contains an id, a created_at timestamp, and metadata. Because convers
  name: OpenAI Conversations API
  phrasing_intents:
  - id: createConversationItems
    intent: Add items to a conversation
    question: Can I append new messages to an existing conversation?
  - id: listConversationItems
    intent: List the items in a conversation
    question: How do I read back everything said in a stored conversation?
  - id: getConversationItem
    intent: Retrieve one item from a conversation
    question: What does a single message in a conversation contain?
  - id: deleteConversationItem
    intent: Delete an item from a conversation
    question: Can I remove one message from a conversation's history?
  - id: createConversation
    intent: Create a conversation
    question: How do I create a persistent conversation to keep state across responses?
  - id: getConversation
    intent: Retrieve a conversation
    question: What metadata is attached to one of my conversations?
  - id: deleteConversation
    intent: Delete a conversation
    question: Does deleting a conversation also delete the items inside it?
  - id: updateConversation
    intent: Update a conversation's metadata
    question: Can I tag a conversation with my own customer or session IDs?
  phrasing_ops: 8
  slug: openai-conversations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: 'The Containers API manages sandboxed containers used by Code Interpreter for running Python, data work, file transforms, and iterative debugging. Containers can be created explicitly or auto-managed, '
  name: OpenAI Containers API
  phrasing_intents:
  - id: ListContainers
    intent: List my code containers
    question: Which containers do I have running for code execution?
  - id: CreateContainer
    intent: Create a container for running code
    question: How do I spin up a new container for code execution?
  - id: RetrieveContainer
    intent: Get a container's details
    question: What is the status of a particular container?
  - id: DeleteContainer
    intent: Delete a container
    question: How do I shut down and delete a container I'm done with?
  - id: CreateContainerFile
    intent: Add a file to a container
    question: How do I put a file into a container so code can read it?
  - id: ListContainerFiles
    intent: List files inside a container
    question: What files are inside one of my containers?
  - id: RetrieveContainerFile
    intent: Get metadata for a file in a container
    question: What are the path and size of a file inside a container?
  - id: DeleteContainerFile
    intent: Delete a file from a container
    question: How do I remove one file from a container?
  phrasing_ops: 9
  slug: openai-containers-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: ChatKit is the best way to build agentic chat experiences. It provides session and thread management for building internal knowledge base assistants, research companions, support agents, and more. Cha
  name: OpenAI ChatKit API
  phrasing_intents:
  - id: CancelChatSessionMethod
    intent: Cancel an active ChatKit session
    question: How do I shut down a ChatKit session so its client secret stops working?
  - id: CreateChatSessionMethod
    intent: Start a ChatKit session for a user
    question: How do I create a ChatKit session to embed chat for one of my users?
  - id: ListThreadItemsMethod
    intent: List the items in a ChatKit thread
    question: What messages and items are in a particular ChatKit thread?
  - id: GetThreadMethod
    intent: Retrieve a ChatKit thread
    question: Can I fetch a ChatKit thread by its identifier?
  - id: DeleteThreadMethod
    intent: Delete a ChatKit thread and its attachments
    question: How do I delete a ChatKit conversation along with its stored attachments?
  - id: ListThreadsMethod
    intent: List ChatKit threads
    question: Which ChatKit threads exist for my app?
  phrasing_ops: 6
  slug: openai-chatkit-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Skills API surfaces OpenAI's Agent Skills — discoverable folders of instructions, scripts, and resources that agents (notably Codex) can use to perform specific tasks. Operations cover creating, r
  name: OpenAI Skills API
  phrasing_intents:
  - id: CreateSkill
    intent: Create a new skill from files
    question: How do I upload a brand-new skill for my agents to use?
  - id: ListSkills
    intent: List the skills in my project
    question: Which skills have been uploaded to my current project?
  - id: DeleteSkill
    intent: Delete a skill
    question: How do I remove a skill entirely, all versions included?
  - id: GetSkill
    intent: Get a skill's details
    question: What is the current default version of one of my skills?
  - id: UpdateSkillDefaultVersion
    intent: Change which version of a skill is the default
    question: How do I roll a skill back to an earlier version?
  - id: GetSkillContent
    intent: Download a skill's default zip bundle
    question: Can I download the zip bundle for a skill's current default?
  - id: CreateSkillVersion
    intent: Publish a new version of a skill
    question: How do I upload an updated version of an existing skill?
  - id: ListSkillVersions
    intent: List the versions of a skill
    question: What versions of a skill have been published?
  phrasing_ops: 11
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
  phrasing_intents:
  - id: listAssistants
    intent: List my assistants
    question: Which assistants have I already built in my OpenAI account?
  - id: createAssistant
    intent: Create an assistant
    question: How do I set up a new assistant with its own model and instructions?
  - id: getAssistant
    intent: Retrieve an assistant
    question: What model and instructions is a particular assistant configured with?
  - id: modifyAssistant
    intent: Update an existing assistant
    question: Can I switch an existing assistant to a different model without recreating it?
  - id: deleteAssistant
    intent: Delete an assistant
    question: Can I permanently remove an assistant I no longer use?
  - id: listAssistantFiles
    intent: List files attached to an assistant
    question: Which files are attached to one of my assistants?
  - id: createAssistantFile
    intent: Attach a file to an assistant
    question: How do I give an assistant access to a file I already uploaded?
  - id: getAssistantFile
    intent: Retrieve a file attached to an assistant
    question: Is a specific file still attached to my assistant?
  phrasing_ops: 27
  slug: openai-assistants-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Learn how to turn audio into text or text into audio.
  name: OpenAI Audio API
  phrasing_intents:
  - id: createSpeech
    intent: Turn text into spoken audio
    question: How do I convert a paragraph of text into an MP3 voiceover?
  - id: createTranscription
    intent: Transcribe an audio recording
    question: What's the way to turn a meeting recording into text in its original language?
  - id: createTranslation
    intent: Translate spoken audio into English text
    question: Can I take a Spanish audio clip and get an English transcript back?
  - id: createVoiceConsent
    intent: Upload a voice consent recording
    question: What do I need to upload before I'm allowed to create a custom voice?
  - id: listVoiceConsents
    intent: List voice consent recordings
    question: Which voice consent recordings has my organization uploaded for custom voices?
  - id: getVoiceConsent
    intent: Retrieve a voice consent recording
    question: What metadata is stored for one of our voice consent recordings?
  - id: updateVoiceConsent
    intent: Rename a voice consent recording
    question: Can I rename a consent recording without re-uploading the audio?
  - id: deleteVoiceConsent
    intent: Delete a voice consent recording
    question: How do I remove a speaker's consent recording if they withdraw permission?
  phrasing_ops: 9
  slug: openai-audio-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: List user actions and configuration changes within this organization.
  name: OpenAI Audit Logs API
  phrasing_intents:
  - id: list-audit-logs
    intent: Review user actions and config changes in the org
    question: Who changed settings in my organization recently?
  phrasing_ops: 1
  slug: openai-audit-logs-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Create large batches of API requests to run asynchronously.
  name: OpenAI Batch API
  phrasing_intents:
  - id: createBatch
    intent: Submit a batch of requests from a file
    question: How do I run a large file of API requests asynchronously as a batch?
  - id: listBatches
    intent: List my organization's batches
    question: Which batch jobs has my organization submitted?
  - id: retrieveBatch
    intent: Check the status of a batch
    question: Has my batch finished, and where is its output file?
  - id: cancelBatch
    intent: Cancel an in-progress batch
    question: How do I stop a batch that is still running?
  phrasing_ops: 4
  slug: openai-batch-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Certificates API from OpenAI — 7 operation(s) for certificates.
  name: OpenAI Certificates API
  phrasing_intents:
  - id: listOrganizationCertificates
    intent: List the organization's certificates
    question: Which certificates have been uploaded to my organization?
  - id: uploadCertificate
    intent: Upload a certificate to the organization
    question: How do I upload a certificate to my OpenAI organization?
  - id: activateOrganizationCertificates
    intent: Activate certificates for the whole organization
    question: How do I turn on uploaded certificates across my entire organization?
  - id: deactivateOrganizationCertificates
    intent: Deactivate certificates for the whole organization
    question: Can I switch off certificates across my whole organization?
  - id: getCertificate
    intent: Retrieve an uploaded certificate
    question: Can I look up a certificate even if it isn't active?
  - id: modifyCertificate
    intent: Rename a certificate
    question: Can I rename a certificate after uploading it?
  - id: deleteCertificate
    intent: Delete a certificate
    question: Why can't I delete a certificate that is still active?
  - id: listProjectCertificates
    intent: List a project's certificates
    question: Which certificates are active for a particular project?
  phrasing_ops: 10
  slug: openai-certificates-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Chatkit API from OpenAI — 5 operation(s) for chatkit.
  name: OpenAI Chatkit API
  phrasing_intents:
  - id: CancelChatSessionMethod
    intent: Cancel an active ChatKit session
    question: How do I shut down a ChatKit session so its client secret stops working?
  - id: CreateChatSessionMethod
    intent: Start a ChatKit session for a user
    question: How do I create a ChatKit session to embed chat for one of my users?
  - id: ListThreadItemsMethod
    intent: List the items in a ChatKit thread
    question: What messages and items are in a particular ChatKit thread?
  - id: GetThreadMethod
    intent: Retrieve a ChatKit thread
    question: Can I fetch a ChatKit thread by its identifier?
  - id: DeleteThreadMethod
    intent: Delete a ChatKit thread and its attachments
    question: How do I delete a ChatKit conversation along with its stored attachments?
  - id: ListThreadsMethod
    intent: List ChatKit threads
    question: Which ChatKit threads exist for my app?
  phrasing_ops: 6
  slug: openai-chatkit-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position.
  name: OpenAI Completions API
  phrasing_intents:
  - id: createCompletion
    intent: Generate a text completion for a prompt
    question: How do I get a model to continue a piece of text with the legacy completions endpoint?
  phrasing_ops: 1
  slug: openai-completions-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Containers API from OpenAI — 5 operation(s) for containers.
  name: OpenAI Containers API
  phrasing_intents:
  - id: ListContainers
    intent: List my code containers
    question: Which containers do I have running for code execution?
  - id: CreateContainer
    intent: Create a container for running code
    question: How do I spin up a new container for code execution?
  - id: RetrieveContainer
    intent: Get a container's details
    question: What is the status of a particular container?
  - id: DeleteContainer
    intent: Delete a container
    question: How do I shut down and delete a container I'm done with?
  - id: CreateContainerFile
    intent: Add a file to a container
    question: How do I put a file into a container so code can read it?
  - id: ListContainerFiles
    intent: List files inside a container
    question: What files are inside one of my containers?
  - id: RetrieveContainerFile
    intent: Get metadata for a file in a container
    question: What are the path and size of a file inside a container?
  - id: DeleteContainerFile
    intent: Delete a file from a container
    question: How do I remove one file from a container?
  phrasing_ops: 9
  slug: openai-containers-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Manage conversations and conversation items.
  name: OpenAI Conversations API
  phrasing_intents:
  - id: createConversationItems
    intent: Add items to a conversation
    question: Can I append new messages to an existing conversation?
  - id: listConversationItems
    intent: List the items in a conversation
    question: How do I read back everything said in a stored conversation?
  - id: getConversationItem
    intent: Retrieve one item from a conversation
    question: What does a single message in a conversation contain?
  - id: deleteConversationItem
    intent: Delete an item from a conversation
    question: Can I remove one message from a conversation's history?
  - id: createConversation
    intent: Create a conversation
    question: How do I create a persistent conversation to keep state across responses?
  - id: getConversation
    intent: Retrieve a conversation
    question: What metadata is attached to one of my conversations?
  - id: deleteConversation
    intent: Delete a conversation
    question: Does deleting a conversation also delete the items inside it?
  - id: updateConversation
    intent: Update a conversation's metadata
    question: Can I tag a conversation with my own customer or session IDs?
  phrasing_ops: 8
  slug: openai-conversations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.
  name: OpenAI Embeddings API
  phrasing_intents:
  - id: createEmbedding
    intent: Turn text into an embedding vector
    question: How do I convert text into a vector for semantic search?
  phrasing_ops: 1
  slug: openai-embeddings-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Manage and run evals in the OpenAI platform.
  name: OpenAI Evals API
  phrasing_intents:
  - id: listEvals
    intent: List evaluations in a project
    question: Which evals have I set up in this project?
  - id: createEval
    intent: Create an evaluation
    question: How do I define an eval to test how well a model performs on my data?
  - id: getEval
    intent: Retrieve an evaluation
    question: What testing criteria does one of my evals use?
  - id: updateEval
    intent: Rename or retag an evaluation
    question: Can I rename an evaluation after I've created it?
  - id: deleteEval
    intent: Delete an evaluation
    question: How do I remove an evaluation I no longer need?
  - id: getEvalRuns
    intent: List the runs of an evaluation
    question: What runs have been executed against one of my evals?
  - id: createEvalRun
    intent: Start an evaluation run
    question: How do I kick off a run to test a model against an existing eval?
  - id: getEvalRun
    intent: Check an evaluation run
    question: Has my eval run finished, and what were the results?
  phrasing_ops: 12
  slug: openai-evals-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Files are used to upload documents that can be used with features like Assistants and Fine-tuning.
  name: OpenAI Files API
  phrasing_intents:
  - id: listFiles
    intent: List my organization's uploaded files
    question: Which files have been uploaded to my organization?
  - id: createFile
    intent: Upload a file
    question: How do I upload a JSONL file to use for fine-tuning or a batch job?
  - id: deleteFile
    intent: Delete an uploaded file
    question: How do I delete a file I uploaded so it stops counting against storage?
  - id: retrieveFile
    intent: Get details about an uploaded file
    question: What's the size, name and purpose of one of my uploaded files?
  - id: downloadFile
    intent: Download a file's contents
    question: Can I download the actual contents of a file, like batch job results?
  phrasing_ops: 5
  slug: openai-files-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Fine Tuning API from OpenAI — 11 operation(s) for fine tuning.
  name: OpenAI Fine Tuning API
  phrasing_intents:
  - id: runGrader
    intent: Run a grader against a model sample
    question: How do I score a single model output with a grader before fine-tuning?
  - id: validateGrader
    intent: Check that a grader definition is valid
    question: Is my grader configuration valid before I use it in a fine-tuning job?
  - id: listFineTuningCheckpointPermissions
    intent: List who can use a fine-tuned checkpoint
    question: Which projects have access to one of my fine-tuned model checkpoints?
  - id: createFineTuningCheckpointPermission
    intent: Share a fine-tuned checkpoint with other projects
    question: How do I share a fine-tuned model with other projects in my organization?
  - id: deleteFineTuningCheckpointPermission
    intent: Revoke a project's access to a checkpoint
    question: How do I stop another project from using my fine-tuned checkpoint?
  - id: createFineTuningJob
    intent: Start a fine-tuning job to train a custom model
    question: How do I fine-tune a model on my own training file?
  - id: listPaginatedFineTuningJobs
    intent: List my organization's fine-tuning jobs
    question: Which fine-tuning jobs has my organization run?
  - id: retrieveFineTuningJob
    intent: Get the status of a fine-tuning job
    question: Is my fine-tuning job finished, and what is the new model called?
  phrasing_ops: 13
  slug: openai-fine-tuning-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Group organization role assignments API from OpenAI — 2 operation(s) for group organization role assignments.
  name: OpenAI Group organization role assignments API
  phrasing_intents:
  - id: list-group-role-assignments
    intent: List a group's organization roles
    question: Which organization roles does a particular group hold?
  - id: assign-group-role
    intent: Give a group an organization role
    question: How do I grant an organization-level role to a whole group at once?
  - id: unassign-group-role
    intent: Remove an organization role from a group
    question: Can I take an org role away from a group?
  phrasing_ops: 3
  slug: openai-group-organization-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Group users API from OpenAI — 2 operation(s) for group users.
  name: OpenAI Group users API
  phrasing_intents:
  - id: list-group-users
    intent: List the members of a group
    question: Who belongs to a particular group in my organization?
  - id: add-group-user
    intent: Add a user to a group
    question: How do I put a teammate into a group?
  - id: remove-group-user
    intent: Remove a user from a group
    question: Can I take someone out of a group without removing them from the organization?
  phrasing_ops: 3
  slug: openai-group-users-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Groups API from OpenAI — 2 operation(s) for groups.
  name: OpenAI Groups API
  phrasing_intents:
  - id: list-groups
    intent: List the groups in my organization
    question: Which user groups exist in my organization?
  - id: create-group
    intent: Create a user group
    question: How do I create a group to manage access for a team?
  - id: update-group
    intent: Rename a group
    question: Can I rename an existing group?
  - id: delete-group
    intent: Delete a group
    question: How do I delete a group from the organization?
  phrasing_ops: 4
  slug: openai-groups-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given a prompt and/or an input image, the model will generate a new image.
  name: OpenAI Images API
  phrasing_intents:
  - id: createImageEdit
    intent: Edit or extend an existing image with a prompt
    question: How do I change part of an existing picture by describing the edit?
  - id: createImage
    intent: Generate an image from a text prompt
    question: How do I create a brand-new image from a text description?
  - id: createImageVariation
    intent: Create variations of an existing image
    question: Can I get a few alternative versions of a picture without writing a prompt?
  phrasing_ops: 3
  slug: openai-images-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Invites API from OpenAI — 2 operation(s) for invites.
  name: OpenAI Invites API
  phrasing_intents:
  - id: list-invites
    intent: List organization invites
    question: Who has been invited to my organization?
  - id: inviteUser
    intent: Invite a user to the organization
    question: How do I invite a teammate to my OpenAI organization?
  - id: retrieve-invite
    intent: Retrieve an invite
    question: Has a particular invite been accepted yet?
  - id: delete-invite
    intent: Revoke an organization invite
    question: Can I cancel an invite I sent to the wrong email?
  phrasing_ops: 4
  slug: openai-invites-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: List and describe the various models available in the API.
  name: OpenAI Models API
  phrasing_intents:
  - id: listModels
    intent: List available models
    question: Which models can I use with my API key right now?
  - id: retrieveModel
    intent: Look up a model
    question: Who owns a particular model and can I access it?
  - id: deleteModel
    intent: Delete a fine-tuned model
    question: How do I delete a fine-tuned model I no longer need?
  phrasing_ops: 3
  slug: openai-models-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Given text and/or image inputs, classifies if those inputs are potentially harmful.
  name: OpenAI Moderations API
  phrasing_intents:
  - id: createModeration
    intent: Check text or images for harmful content
    question: How do I check whether a user's message is harmful before showing it?
  phrasing_ops: 1
  slug: openai-moderations-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Organization API from OpenAI — 2 operation(s) for organization.
  name: OpenAI Organization API
  phrasing_intents:
  - id: admin-api-keys-list
    intent: List the organization's admin API keys
    question: Which admin API keys exist for my organization?
  - id: admin-api-keys-create
    intent: Create an organization admin API key
    question: How do I create an admin key for managing my organization programmatically?
  - id: admin-api-keys-get
    intent: Get one admin API key's details
    question: Who created a particular admin key and when was it last used?
  - id: admin-api-keys-delete
    intent: Delete an organization admin API key
    question: How do I revoke an admin key that may have been exposed?
  phrasing_ops: 4
  slug: openai-organization-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project group role assignments API from OpenAI — 2 operation(s) for project group role assignments.
  name: OpenAI Project group role assignments API
  phrasing_intents:
  - id: list-project-group-role-assignments
    intent: List the project roles a group holds
    question: Which project roles has a particular group been given in a project?
  - id: assign-project-group-role
    intent: Give a group a role in a project
    question: How do I grant a whole group a role inside a project?
  - id: unassign-project-group-role
    intent: Remove a project role from a group
    question: How do I take a project role away from a group?
  phrasing_ops: 3
  slug: openai-project-group-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project groups API from OpenAI — 2 operation(s) for project groups.
  name: OpenAI Project groups API
  phrasing_intents:
  - id: list-project-groups
    intent: List groups with access to a project
    question: Which groups have access to a given project?
  - id: add-project-group
    intent: Grant a group access to a project
    question: How do I give an entire group access to a project?
  - id: remove-project-group
    intent: Revoke a group's access to a project
    question: Can I cut off a group's access to a single project?
  phrasing_ops: 3
  slug: openai-project-groups-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Project user role assignments API from OpenAI — 2 operation(s) for project user role assignments.
  name: OpenAI Project user role assignments API
  phrasing_intents:
  - id: list-project-user-role-assignments
    intent: List the project roles a user holds
    question: Which project roles has a specific person been assigned in a project?
  - id: assign-project-user-role
    intent: Give a user a role in a project
    question: How do I grant an individual user a custom role inside a project?
  - id: unassign-project-user-role
    intent: Remove a project role from a user
    question: How do I take a project role away from one person?
  phrasing_ops: 3
  slug: openai-project-user-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Projects API from OpenAI — 11 operation(s) for projects.
  name: OpenAI Projects API
  phrasing_intents:
  - id: list-projects
    intent: List the projects in my organization
    question: Which projects exist in my OpenAI organization?
  - id: create-project
    intent: Create a new project in the organization
    question: How do I set up a new project in my organization?
  - id: retrieve-project
    intent: Get the details of one project
    question: What are the name and status of a specific project?
  - id: modify-project
    intent: Rename or reconfigure an existing project
    question: How do I rename a project that already exists?
  - id: list-project-api-keys
    intent: List the API keys in a project
    question: Which API keys have been issued inside one of my projects?
  - id: retrieve-project-api-key
    intent: Get details of one project API key
    question: Who owns a particular API key in my project and when was it created?
  - id: delete-project-api-key
    intent: Delete an API key from a project
    question: How do I revoke a leaked API key in one of my projects?
  - id: archive-project
    intent: Archive a project
    question: How do I retire a project I no longer use, since projects can't be deleted?
  phrasing_ops: 19
  slug: openai-projects-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Realtime API from OpenAI — 9 operation(s) for realtime.
  name: OpenAI Realtime API
  phrasing_intents:
  - id: create-realtime-call
    intent: Start a realtime voice call over WebRTC
    question: How do I connect a browser to a realtime voice session over WebRTC?
  - id: accept-realtime-call
    intent: Accept an incoming SIP call
    question: When a phone call comes in over SIP, how do I answer it with a realtime model?
  - id: hangup-realtime-call
    intent: Hang up an active realtime call
    question: How do I end a live realtime call from my server?
  - id: refer-realtime-call
    intent: Transfer a SIP call to another destination
    question: Can I transfer a caller from the voice agent to a human's phone line?
  - id: reject-realtime-call
    intent: Decline an incoming SIP call
    question: Can I refuse an incoming phone call instead of answering it?
  - id: create-realtime-client-secret
    intent: Create a short-lived realtime client secret
    question: How can my web or mobile app talk to the realtime model without exposing my API key?
  - id: create-realtime-session
    intent: Create an ephemeral realtime session token
    question: Can I preconfigure voice, instructions and tools when creating a realtime session token?
  - id: create-realtime-transcription-session
    intent: Create a realtime transcription session
    question: How do I set up live speech-to-text streaming from a client app?
  phrasing_ops: 9
  slug: openai-realtime-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Responses API from OpenAI — 6 operation(s) for responses.
  name: OpenAI Responses API
  phrasing_intents:
  - id: createResponse
    intent: Generate a model response
    question: How do I send a prompt to a model and get text or JSON back?
  - id: getResponse
    intent: Retrieve a model response
    question: Can I fetch the output of a response I generated earlier by its ID?
  - id: deleteResponse
    intent: Delete a stored model response
    question: How do I delete a stored response so it's no longer kept?
  - id: cancelResponse
    intent: Cancel a background response
    question: Can I stop a background response that is still generating?
  - id: listInputItems
    intent: List the input items of a response
    question: What inputs were sent to the model to produce a given response?
  - id: Getinputtokencounts
    intent: Count input tokens before sending a request
    question: How many input tokens will my prompt use before I actually run it?
  - id: Compactconversation
    intent: Compact a long conversation
    question: My conversation is getting too long for the context window — how can I shrink it?
  phrasing_ops: 7
  slug: openai-responses-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Roles API from OpenAI — 4 operation(s) for roles.
  name: OpenAI Roles API
  phrasing_intents:
  - id: list-roles
    intent: List the organization's roles
    question: Which roles are configured at the organization level?
  - id: create-role
    intent: Create a custom organization role
    question: How do I define a custom role for my whole organization?
  - id: update-role
    intent: Update an organization role
    question: Can I change the permissions on an existing organization role?
  - id: delete-role
    intent: Delete a custom organization role
    question: How do I remove a custom role from the organization?
  - id: list-project-roles
    intent: List the roles in a project
    question: Which roles are defined inside a particular project?
  - id: create-project-role
    intent: Create a custom role in a project
    question: How do I create a role that only applies within one project?
  - id: update-project-role
    intent: Update a role in a project
    question: Can I change what a project-level role is allowed to do?
  - id: delete-project-role
    intent: Delete a custom role from a project
    question: How do I delete a custom role from a single project?
  phrasing_ops: 8
  slug: openai-roles-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Skills API from OpenAI — 6 operation(s) for skills.
  name: OpenAI Skills API
  phrasing_intents:
  - id: CreateSkill
    intent: Create a new skill from files
    question: How do I upload a brand-new skill for my agents to use?
  - id: ListSkills
    intent: List the skills in my project
    question: Which skills have been uploaded to my current project?
  - id: DeleteSkill
    intent: Delete a skill
    question: How do I remove a skill entirely, all versions included?
  - id: GetSkill
    intent: Get a skill's details
    question: What is the current default version of one of my skills?
  - id: UpdateSkillDefaultVersion
    intent: Change which version of a skill is the default
    question: How do I roll a skill back to an earlier version?
  - id: GetSkillContent
    intent: Download a skill's default zip bundle
    question: Can I download the zip bundle for a skill's current default?
  - id: CreateSkillVersion
    intent: Publish a new version of a skill
    question: How do I upload an updated version of an existing skill?
  - id: ListSkillVersions
    intent: List the versions of a skill
    question: What versions of a skill have been published?
  phrasing_ops: 11
  slug: openai-skills-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Threads API from OpenAI — 13 operation(s) for threads.
  name: OpenAI Threads API
  phrasing_intents:
  - id: listMessageFiles
    intent: List files attached to a thread message
    question: Which files are attached to a particular message in an Assistants thread?
  - id: getMessageFile
    intent: Get one file attached to a thread message
    question: How do I look up a single file attached to a thread message?
  - id: createThread
    intent: Start a new conversation thread
    question: How do I start a new conversation thread for an assistant?
  - id: getThread
    intent: Retrieve a conversation thread
    question: What metadata is stored on one of my assistant threads?
  - id: modifyThread
    intent: Update a conversation thread
    question: Is it possible to change the metadata on a thread after it was created?
  - id: deleteThread
    intent: Delete a conversation thread
    question: How do I permanently remove a conversation thread?
  - id: listMessages
    intent: List the messages in a thread
    question: What messages have been exchanged in a thread so far?
  - id: createMessage
    intent: Add a message to a thread
    question: How do I post a user message into an existing thread?
  phrasing_ops: 19
  slug: openai-threads-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: Use Uploads to upload large files in multiple parts.
  name: OpenAI Uploads API
  phrasing_intents:
  - id: createUpload
    intent: Start a multipart upload for a large file
    question: How do I upload a file too large for a single request?
  - id: cancelUpload
    intent: Cancel a multipart upload
    question: Can I abandon a large upload partway through?
  - id: completeUpload
    intent: Finish a multipart upload into a usable file
    question: Once all parts are uploaded, how do I turn them into a usable file?
  - id: addUploadPart
    intent: Add a chunk to a multipart upload
    question: How do I send the next chunk of bytes for a large file upload?
  phrasing_ops: 4
  slug: openai-uploads-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Usage API from OpenAI — 9 operation(s) for usage.
  name: OpenAI Usage API
  phrasing_intents:
  - id: usage-costs
    intent: Report the organization's spend over time
    question: How much has my organization spent on the API since the start of the month?
  - id: usage-audio-speeches
    intent: Report text-to-speech usage
    question: How many characters of text-to-speech did we generate this month?
  - id: usage-audio-transcriptions
    intent: Report speech-to-text transcription usage
    question: How many seconds of audio have we transcribed recently?
  - id: usage-code-interpreter-sessions
    intent: Report code interpreter session usage
    question: How many code interpreter sessions has our organization opened?
  - id: usage-completions
    intent: Report token usage for completions
    question: How many input and output tokens did we use on chat and completions this week?
  - id: usage-embeddings
    intent: Report embeddings usage
    question: How many tokens have we sent to embedding models lately?
  - id: usage-images
    intent: Report image generation usage
    question: How many images did we generate or edit this month?
  - id: usage-moderations
    intent: Report moderation usage
    question: How much have we used the moderation endpoint recently?
  phrasing_ops: 9
  slug: openai-usage-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The User organization role assignments API from OpenAI — 2 operation(s) for user organization role assignments.
  name: OpenAI User organization role assignments API
  phrasing_intents:
  - id: list-user-role-assignments
    intent: List a user's organization roles
    question: Which organization roles does a particular user have?
  - id: assign-user-role
    intent: Give a user an organization role
    question: How do I grant an organization role to one specific user?
  - id: unassign-user-role
    intent: Remove an organization role from a user
    question: Can I take an org role away from one user?
  phrasing_ops: 3
  slug: openai-user-organization-role-assignments-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Users API from OpenAI — 2 operation(s) for users.
  name: OpenAI Users API
  phrasing_intents:
  - id: list-users
    intent: List the users in my organization
    question: Who are all the members of my organization?
  - id: retrieve-user
    intent: Get an organization user's details
    question: What role does a specific person have in my organization?
  - id: modify-user
    intent: Change a user's role in the organization
    question: How do I make someone an owner of the organization?
  - id: delete-user
    intent: Remove a user from the organization
    question: How do I remove someone who has left the company from our organization?
  phrasing_ops: 4
  slug: openai-users-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Vector stores API from OpenAI — 10 operation(s) for vector stores.
  name: OpenAI Vector stores API
  phrasing_intents:
  - id: listVectorStores
    intent: List my vector stores
    question: Which vector stores have I created for file search?
  - id: createVectorStore
    intent: Create a vector store
    question: How do I set up a new vector store so my assistant can search my documents?
  - id: getVectorStore
    intent: Retrieve a vector store
    question: How many files are in a vector store and are they done processing?
  - id: modifyVectorStore
    intent: Rename or update a vector store
    question: Can I rename a vector store after creating it?
  - id: deleteVectorStore
    intent: Delete a vector store
    question: How do I get rid of a vector store I'm done with?
  - id: createVectorStoreFileBatch
    intent: Add many files to a vector store at once
    question: What's the most efficient way to add hundreds of files to a vector store in one go?
  - id: getVectorStoreFileBatch
    intent: Check a vector store file batch
    question: Has my batch of files finished indexing into the vector store?
  - id: cancelVectorStoreFileBatch
    intent: Cancel a vector store file batch
    question: Can I stop a file batch that's still being processed into a vector store?
  phrasing_ops: 16
  slug: openai-vector-stores-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Videos API from OpenAI — 8 operation(s) for videos.
  name: OpenAI Videos API
  phrasing_intents:
  - id: createVideo
    intent: Generate a new video from a prompt
    question: How do I generate a video from a text prompt?
  - id: ListVideos
    intent: List recently generated videos
    question: Which videos have I generated recently in this project?
  - id: CreateVideoCharacter
    intent: Create a reusable character from a video
    question: Can I turn someone in an uploaded video into a character I can reuse?
  - id: GetVideoCharacter
    intent: Get a saved video character
    question: What details are stored for a video character I created?
  - id: CreateVideoEdit
    intent: Edit a video with a prompt
    question: How do I change something in an existing video using a prompt?
  - id: CreateVideoExtend
    intent: Extend a completed video
    question: Can I make a finished video longer by continuing it?
  - id: GetVideo
    intent: Check a video generation job's status
    question: Is my video still rendering or has it completed?
  - id: DeleteVideo
    intent: Delete a video and its stored assets
    question: How do I permanently delete a generated video?
  phrasing_ops: 10
  slug: openai-videos-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Agents API from OpenAI — 21 operation(s) for agents.
  name: OpenAI Agents API
  slug: openai-agents-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Content Provenance Checks API from OpenAI — 1 operation(s) for content provenance checks.
  name: OpenAI Content Provenance Checks API
  slug: openai-content-provenance-checks-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Data retention API from OpenAI — 2 operation(s) for data retention.
  name: OpenAI Data retention API
  slug: openai-data-retention-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Hosted tools API from OpenAI — 1 operation(s) for hosted tools.
  name: OpenAI Hosted tools API
  slug: openai-hosted-tools-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Live API from OpenAI — 7 operation(s) for live.
  name: OpenAI Live API
  slug: openai-live-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Safety API from OpenAI — 2 operation(s) for safety.
  name: OpenAI Safety API
  slug: openai-safety-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Spend alerts API from OpenAI — 4 operation(s) for spend alerts.
  name: OpenAI Spend alerts API
  slug: openai-spend-alerts-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Vaults API from OpenAI — 4 operation(s) for vaults.
  name: OpenAI Vaults API
  slug: openai-vaults-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Webhook Endpoints API from OpenAI — 4 operation(s) for webhook endpoints.
  name: OpenAI Webhook Endpoints API
  slug: openai-webhook-endpoints-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Webhook Event Types API from OpenAI — 1 operation(s) for webhook event types.
  name: OpenAI Webhook Event Types API
  slug: openai-webhook-event-types-api
- baseURL: https://api.openai.com
  baseurl_source: declared
  description: The Decisions API from OpenAI — 1 operation(s) for decisions. Ask classification or scoring questions about the same input and get the answers back in order (public beta).
  name: OpenAI Decisions API
  slug: openai-decisions-api
- baseURL: https://api.openai.com/v1
  baseurl_source: declared
  description: Given a list of messages comprising a conversation, the model will return a response.
  name: OpenAI Chat Completions API
  slug: openai-chat-completions-api
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
artifact_total: 320
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
- group: build
  href: https://artifacts.apis.io/openai/integrations/openai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/openai-integration-edges.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.openai.com/api/docs/pricing.md
- group: design
  href: https://artifacts.apis.io/openai/rules/openai-rules.yml
  title: ''
  type: Spectral
  url: rules/openai-rules.yml
- group: design
  href: https://artifacts.apis.io/openai/vocabulary/openai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openai/conventions/openai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/openai-conventions.yml
- group: build
  href: https://artifacts.apis.io/openai/mcp/openai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/openai-tool-crosswalk.yml
- group: company
  title: ''
  type: Newsroom
  url: https://openai.com/news/
- group: commercial
  href: https://artifacts.apis.io/openai/finops/openai-finops.yml
  title: ''
  type: FinOps
  url: finops/openai-finops.yml
- group: design
  href: https://artifacts.apis.io/openai/rules/openai-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/openai-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/openai/rules/openai-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/openai-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/openai/rules/openai-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/openai-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/openai/json-ld/openai-images-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openai-images-context.jsonld
- group: design
  href: https://artifacts.apis.io/openai/json-ld/openai-embeddings-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openai-embeddings-context.jsonld
- group: design
  href: https://artifacts.apis.io/openai/json-ld/openai-chat-completions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openai-chat-completions-context.jsonld
- group: design
  href: https://artifacts.apis.io/openai/json-ld/openai-audio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openai-audio-context.jsonld
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-tart-guest-agent-rpc.proto
  title: ''
  type: Protobuf
  url: grpc/openai-tart-guest-agent-rpc.proto
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-orchard-rpc.proto
  title: ''
  type: Protobuf
  url: grpc/openai-orchard-rpc.proto
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-codex-thread-config-v1.proto
  title: ''
  type: Protobuf
  url: grpc/openai-codex-thread-config-v1.proto
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-codex-exec-server-relay-v1.proto
  title: ''
  type: Protobuf
  url: grpc/openai-codex-exec-server-relay-v1.proto
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-codex-code-mode-v1.proto
  title: ''
  type: Protobuf
  url: grpc/openai-codex-code-mode-v1.proto
- group: other
  href: https://artifacts.apis.io/openai/hosts/openai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openai-hosts.yml
- group: other
  href: https://artifacts.apis.io/openai/vendors/openai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openai-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://openai.com/
- group: other
  href: https://artifacts.apis.io/openai/capabilities/openai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/openai-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/openai/agentic-access/openai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/openai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/openai/security/openai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/openai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/openai/security/openai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/openai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/openai/security/openai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/openai/authentication/openai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openai-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openai/overview
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-assistant-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-assistant-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-batch-job-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-batch-job-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-cancel-fine-tuning-job-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-cancel-fine-tuning-job-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-chat-then-speak-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-chat-then-speak-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-create-embedding-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-create-embedding-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-download-batch-results-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-download-batch-results-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-fine-tuning-job-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-fine-tuning-job-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-generate-image-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-generate-image-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-list-models-then-chat-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-list-models-then-chat-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-moderate-then-chat-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-moderate-then-chat-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-retrieve-and-delete-model-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-retrieve-and-delete-model-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-thread-and-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-thread-and-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-transcribe-then-summarize-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-transcribe-then-summarize-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-upload-and-verify-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-upload-and-verify-file-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-vector-store-file-batch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-vector-store-file-batch-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-vector-store-ingest-file-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/openai-vector-store-ingest-file-workflow.yml
- group: design
  href: https://artifacts.apis.io/openai/arazzo/openai-vector-store-search-workflow.yml
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
  href: https://artifacts.apis.io/openai/json-schema/openai-chat-completion-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/openai-chat-completion-schema.json
- group: docs
  href: https://artifacts.apis.io/openai/json-schema/openai-embedding-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/openai-embedding-schema.json
- group: design
  href: https://artifacts.apis.io/openai/json-ld/openai-context.jsonld
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
  href: https://artifacts.apis.io/openai/openapi/_original/openai-openapi-master.yml
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
  href: https://artifacts.apis.io/openai/rules/openai-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/openai-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/openai/vocabulary/openai-vocabulary.yaml
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
  href: https://artifacts.apis.io/openai/packages/openai-packages.yml
  title: ''
  type: Packages
  url: packages/openai-packages.yml
- group: build
  href: https://artifacts.apis.io/openai/packages/openai-packages.yml
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
  href: https://artifacts.apis.io/openai/well-known/openai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/openai/well-known/openai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openai-security.txt
- group: agent
  href: https://artifacts.apis.io/openai/mcp/openai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/openai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/openai/llms/openai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openai-llms.txt
- group: other
  href: https://artifacts.apis.io/openai/overlays/openai-responses-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openai-responses-overlay.yaml
- group: other
  href: https://artifacts.apis.io/openai/overlays/openai-chat-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openai-chat-overlay.yaml
- group: other
  href: https://artifacts.apis.io/openai/overlays/openai-embeddings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/openai-embeddings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/openai/grpc/openai-grpc.yml
  title: ''
  type: Protobuf
  url: grpc/openai-grpc.yml
- group: design
  href: https://artifacts.apis.io/openai/conformance/openai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/openai/security/openai-trust-center.yml
  title: ''
  type: Compliance
  url: security/openai-trust-center.yml
- group: design
  href: https://artifacts.apis.io/openai/errors/openai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/openai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/openai/lifecycle/openai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/openai-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/openai/scopes/openai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/openai-scopes.yml
- group: start
  href: https://artifacts.apis.io/openai/sandbox/openai-sandbox.yml
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
  href: https://artifacts.apis.io/openai/conventions/openai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/openai-conventions.yml
- group: operate
  href: https://artifacts.apis.io/openai/changelog/openai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openai-changelog.yml
- group: build
  href: https://artifacts.apis.io/openai/cli/openai-cli.yml
  title: ''
  type: CLI
  url: cli/openai-cli.yml
- group: build
  title: ''
  type: CLI
  url: https://learn.chatgpt.com/docs/codex/cli
- group: design
  href: https://artifacts.apis.io/openai/components/openai-components.yml
  title: ''
  type: Components
  url: components/openai-components.yml
- group: design
  href: https://artifacts.apis.io/openai/data-model/openai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openai-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/openai/plans/openai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/openai/rate-limits/openai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/openai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/openai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/openai/asyncapi/openai-realtime-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/openai-realtime-asyncapi.yml
- group: build
  href: https://artifacts.apis.io/openai/examples/
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
- has_sources: true
  method: derived
  name: Openai Finops
  primary_unit: ''
  service_category: ''
  slug: openai-finops
  template: true
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
- name: AgentResource
  property_count: 13
  slug: openai-agent-resource
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
- name: CreateContentProvenanceBody
  property_count: 1
  slug: openai-create-content-provenance-body
- name: CreateEnvironmentTemplateParams
  property_count: 9
  slug: openai-create-environment-template-params
- name: CreateSpendAlertBody
  property_count: 4
  slug: openai-create-spend-alert-body
- name: CreateVaultCredentialParams
  property_count: 3
  slug: openai-create-vault-credential-params
- name: DecisionRequest
  property_count: 4
  slug: openai-decision-request
- name: DecisionResponse
  property_count: 3
  slug: openai-decision-response
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
- name: EnvironmentTemplateResource
  property_count: 11
  slug: openai-environment-template-resource
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
- name: LiveCallAcceptRequest
  property_count: 1
  slug: openai-live-call-accept-request
- name: LiveCallReferRequest
  property_count: 1
  slug: openai-live-call-refer-request
- name: LiveCallRejectRequest
  property_count: 1
  slug: openai-live-call-reject-request
- name: LiveCreateRequest
  property_count: 2
  slug: openai-live-create-request
- name: LiveCreateResponse
  property_count: 2
  slug: openai-live-create-response
- name: LiveForkRequest
  property_count: 2
  slug: openai-live-fork-request
- name: OrganizationDataRetention
  property_count: 2
  slug: openai-organization-data-retention
- name: OrganizationSpendAlertDeletedResource
  property_count: 3
  slug: openai-organization-spend-alert-deleted-resource
- name: OrganizationSpendAlertListResource
  property_count: 5
  slug: openai-organization-spend-alert-list-resource
- name: OrganizationSpendAlert
  property_count: 6
  slug: openai-organization-spend-alert
- name: ProjectDataRetention
  property_count: 2
  slug: openai-project-data-retention
- name: ProjectHostedToolPermissions
  property_count: 5
  slug: openai-project-hosted-tool-permissions
- name: ProjectHostedToolPermissionsUpdateRequest
  property_count: 5
  slug: openai-project-hosted-tool-permissions-update-request
- name: ProjectSpendAlertListResource
  property_count: 5
  slug: openai-project-spend-alert-list-resource
- name: ProjectSpendAlert
  property_count: 6
  slug: openai-project-spend-alert
- name: ProvenanceResource
  property_count: 3
  slug: openai-provenance-resource
- name: PublicCreateEndpointBody
  property_count: 3
  slug: openai-public-create-endpoint-body
- name: PublicUpdateEndpointBody
  property_count: 3
  slug: openai-public-update-endpoint-body
- name: RotateVaultCredentialParams
  property_count: 2
  slug: openai-rotate-vault-credential-params
- name: SafetyAlertResource
  property_count: 9
  slug: openai-safety-alert-resource
- name: SafetyCaseResource
  property_count: 6
  slug: openai-safety-case-resource
- name: SessionEvent
  property_count: 0
  slug: openai-session-event
- name: SessionResource
  property_count: 12
  slug: openai-session-resource
- name: UpdateEnvironmentTemplateParams
  property_count: 9
  slug: openai-update-environment-template-params
- name: UpdateOrganizationDataRetentionBody
  property_count: 1
  slug: openai-update-organization-data-retention-body
- name: UpdateProjectDataRetentionBody
  property_count: 1
  slug: openai-update-project-data-retention-body
- name: VaultCredentialListResource
  property_count: 5
  slug: openai-vault-credential-list-resource
- name: VaultCredentialResource
  property_count: 8
  slug: openai-vault-credential-resource
- name: VaultListResource
  property_count: 5
  slug: openai-vault-list-resource
- name: VaultResource
  property_count: 5
  slug: openai-vault-resource
- name: WebhookEndpointBody
  property_count: 8
  slug: openai-webhook-endpoint-body
- name: WebhookEndpointListResource
  property_count: 5
  slug: openai-webhook-endpoint-list-resource
- name: WebhookEndpointTestResultResource
  property_count: 5
  slug: openai-webhook-endpoint-test-result-resource
- name: WebhookEndpointWithSecretResource
  property_count: 9
  slug: openai-webhook-endpoint-with-secret-resource
- name: WebhookEventTypeListResource
  property_count: 2
  slug: openai-webhook-event-type-list-resource
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
  slug: openai-docs-mcp
modified: '2026-09-16'
name: OpenAI
nav: Providers
network: true
overview: 'OpenAI publishes 62 API contracts indexed on the [APIs.io](https://apis.io/) network, including Responses API, Moderations API, Batch API, and 59 more. Tagged areas include LLM, OpenAI, Artificial Intelligence, Generative AI, and Chatbots.


  The OpenAI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 5 JSON-LD contexts, and 4 Spectral governance rulesets.


  OpenAI''s developer surface includes pricing, authentication, developer portal, getting-started guide, documentation, support, signup flow, and 151 more developer resources.'
plans:
- name: Openai Plans Pricing
  plan_count: 27
  slug: openai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Openai Rate Limits
  slug: openai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: OpenAI — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: openai-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: OpenAI — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: openai-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: OpenAI API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 2
  slug: openai-rules
- authorship: generated
  effective_rule_count: 57
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
  scope_count: 4
  slug: openai-scopes
  summary_line: 4 scopes
score:
  band: exemplar
  composite: 81.8
  coverage:
    artifact_dirs: 45
    catalog_earned: 71.0
    catalog_earned_first_party: 24.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.1
  facets:
    access_clarity: 86.8
    contract_governance: 45.5
    contract_quality: 72.5
    developer_ergonomics: 96.4
    discoverability: 64.2
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/openai/openai-2026-08-17T082822.png
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
- LLM
- OpenAI
- Artificial Intelligence
- Generative AI
- Chatbots
- Foundation Models
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
website: https://openai.com/
---
