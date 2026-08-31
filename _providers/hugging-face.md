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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Hugging Face Agentic Access
  operation_count: 68
  slug: hugging-face-agentic-access
  summary_line: 68 operations · 35 acting
api_count: 6
apis:
- description: Speech recognition, audio classification, and text-to-speech tasks
  name: Hugging Face Audio API
  slug: hugging-face-audio-api
- description: OpenAI-compatible chat completion endpoints
  name: Hugging Face Chat API
  slug: hugging-face-chat-api
- description: OpenAI-compatible chat completion endpoints
  name: Hugging Face Chat Completions API
  slug: hugging-face-chat-completions-api
- description: Image classification, object detection, and segmentation tasks
  name: Hugging Face Computer Vision API
  slug: hugging-face-computer-vision-api
- description: Row-level data access and preview endpoints
  name: Hugging Face Data Access API
  slug: hugging-face-data-access-api
- description: Dataset validity and structure endpoints
  name: Hugging Face Dataset Info API
  slug: hugging-face-dataset-info-api
- description: Operations for managing and querying datasets on the Hub
  name: Hugging Face Datasets API
  slug: hugging-face-datasets-api
- description: Text embedding endpoints
  name: Hugging Face Embeddings API
  slug: hugging-face-embeddings-api
- description: Manage dedicated inference endpoints
  name: Hugging Face Endpoints API
  slug: hugging-face-endpoints-api
- description: Parquet files, size, statistics, and metadata
  name: Hugging Face Files & Metadata API
  slug: hugging-face-files-metadata-api
- description: Text-to-image generation
  name: Hugging Face Image Generation API
  slug: hugging-face-image-generation-api
- description: Server and model information
  name: Hugging Face Info API
  slug: hugging-face-info-api
- description: Operations for managing and querying models on the Hub
  name: Hugging Face Models API
  slug: hugging-face-models-api
- description: Tasks involving multiple modalities
  name: Hugging Face Multimodal API
  slug: hugging-face-multimodal-api
- description: NLP tasks including text generation, classification, and translation
  name: Hugging Face Natural Language Processing API
  slug: hugging-face-natural-language-processing-api
- description: Available cloud providers and hardware
  name: Hugging Face Providers API
  slug: hugging-face-providers-api
- description: General repository management operations
  name: Hugging Face Repos API
  slug: hugging-face-repos-api
- description: Search and filter dataset contents
  name: Hugging Face Search & Filter API
  slug: hugging-face-search-filter-api
- description: Operations for managing and querying Spaces on the Hub
  name: Hugging Face Spaces API
  slug: hugging-face-spaces-api
- description: Text generation endpoints
  name: Hugging Face Text Generation API
  slug: hugging-face-text-generation-api
- description: User account and organization management
  name: Hugging Face Users API
  slug: hugging-face-users-api
arazzos:
- description: Discover an available router model, confirm it exists, then run an OpenAI-compatible chat completion.
  name: Hugging Face Chat Completion with Model Discovery
  slug: hugging-face-chat-completion-with-model-discovery-workflow
- description: Identify the authenticated user, create a new repository, then set its visibility and gating.
  name: Hugging Face Create Repository and Configure
  slug: hugging-face-create-repo-and-configure-workflow
- description: Confirm a dataset supports filtering, resolve its split, then apply a SQL-like filter.
  name: Hugging Face Dataset Filter Rows
  slug: hugging-face-dataset-filter-rows-workflow
- description: Resolve a dataset split, full-text search within it, then pull column statistics.
  name: Hugging Face Dataset Search and Statistics
  slug: hugging-face-dataset-search-and-statistics-workflow
- description: Confirm a dataset on the Hub, read its size profile, then list its Parquet files.
  name: Hugging Face Dataset Size and Parquet Files
  slug: hugging-face-dataset-size-and-parquet-workflow
- description: Check a dataset is viewer-ready, list its splits, then preview the first rows.
  name: Hugging Face Dataset Validate and Preview
  slug: hugging-face-dataset-validate-and-preview-workflow
- description: Create a dedicated Inference Endpoint, then poll its status until it is running.
  name: Hugging Face Deploy Inference Endpoint and Wait
  slug: hugging-face-deploy-inference-endpoint-workflow
- description: Search Hub Spaces by SDK and query, then load the top Space's details.
  name: Hugging Face Discover a Space
  slug: hugging-face-discover-space-workflow
- description: Confirm an embedding model is available, then embed a query and a document for comparison.
  name: Hugging Face Embeddings Pair
  slug: hugging-face-embeddings-pair-workflow
- description: Find a text-generation model on the Hub, confirm it, then run hosted text generation.
  name: Hugging Face Grounded Text Generation
  slug: hugging-face-grounded-text-generation-workflow
- description: Search the Hub for a model, fetch its full record, then inspect a specific revision.
  name: Hugging Face Search and Inspect a Model
  slug: hugging-face-search-and-inspect-model-workflow
- description: Summarize a long document with one model, then translate the summary with another.
  name: Hugging Face Summarize Then Translate
  slug: hugging-face-summarize-then-translate-workflow
- description: Read a TGI server's info, tokenize a prompt to check its length, then generate text.
  name: Hugging Face TGI Inspect and Generate
  slug: hugging-face-tgi-inspect-and-generate-workflow
- description: Read an endpoint's current state, then pause it if running or resume it if paused.
  name: Hugging Face Toggle Inference Endpoint State
  slug: hugging-face-toggle-endpoint-state-workflow
artifact_total: 458
collections:
- collection_type: postman
  name: Hugging Face Dataset Viewer API
  slug: postman-hugging-face-dataset-viewer-api
- collection_type: postman
  name: Hugging Face Hub API
  slug: postman-hugging-face-hub-api
- collection_type: postman
  name: Hugging Face Inference API
  slug: postman-hugging-face-inference-api
- collection_type: postman
  name: Hugging Face Inference Endpoints API
  slug: postman-hugging-face-inference-endpoints-api
- collection_type: postman
  name: Hugging Face Inference Providers API
  slug: postman-hugging-face-inference-providers-api
- collection_type: postman
  name: Hugging Face Text Generation Inference API
  slug: postman-hugging-face-text-generation-inference-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Hugging Face Dataset Viewer Audio API
  slug: open-hugging-face-audio-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Chat API
  slug: open-hugging-face-chat-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Chat Completions API
  slug: open-hugging-face-chat-completions-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Computer Vision API
  slug: open-hugging-face-computer-vision-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Data Access API
  slug: open-hugging-face-data-access-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Dataset Info API
  slug: open-hugging-face-dataset-info-api
- collection_type: open
  name: Hugging Face Dataset Viewer API
  slug: open-hugging-face-dataset-viewer-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Datasets API
  slug: open-hugging-face-datasets-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Embeddings API
  slug: open-hugging-face-embeddings-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Endpoints API
  slug: open-hugging-face-endpoints-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Files & Metadata API
  slug: open-hugging-face-files-metadata-api
- collection_type: open
  name: Hugging Face Hub API
  slug: open-hugging-face-hub-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Image Generation API
  slug: open-hugging-face-image-generation-api
- collection_type: open
  name: Hugging Face Inference API
  slug: open-hugging-face-inference-api
- collection_type: open
  name: Hugging Face Inference Endpoints API
  slug: open-hugging-face-inference-endpoints-api
- collection_type: open
  name: Hugging Face Inference Providers API
  slug: open-hugging-face-inference-providers-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Info API
  slug: open-hugging-face-info-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Models API
  slug: open-hugging-face-models-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Multimodal API
  slug: open-hugging-face-multimodal-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Natural Language Processing API
  slug: open-hugging-face-natural-language-processing-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Providers API
  slug: open-hugging-face-providers-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Repos API
  slug: open-hugging-face-repos-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Search & Filter API
  slug: open-hugging-face-search-filter-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Spaces API
  slug: open-hugging-face-spaces-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Text Generation API
  slug: open-hugging-face-text-generation-api
- collection_type: open
  name: Hugging Face Text Generation Inference API
  slug: open-hugging-face-text-generation-inference-api
- collection_type: open
  name: Hugging Face Dataset Viewer Audio Users API
  slug: open-hugging-face-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/hugging-face-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/huggingface/dataset-viewer/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/huggingface/dataset-viewer/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/huggingface/dataset-viewer/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/huggingface/dataset-viewer/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/huggingface/dataset-viewer/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/huggingface/dataset-viewer/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hugging-face-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hugging-face-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hugging-face-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hugging-face-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hugging-face/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-chat-completion-with-model-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-create-repo-and-configure-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-dataset-filter-rows-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-dataset-search-and-statistics-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-dataset-size-and-parquet-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-dataset-validate-and-preview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-deploy-inference-endpoint-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-discover-space-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-embeddings-pair-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-grounded-text-generation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-search-and-inspect-model-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-summarize-then-translate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-tgi-inspect-and-generate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/hugging-face-toggle-endpoint-state-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://huggingface.co
- group: docs
  title: ''
  type: Documentation
  url: https://huggingface.co/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://huggingface.co/inference/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://huggingface.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://huggingface.co/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://huggingface.co/changelog
- group: start
  title: ''
  type: Signup
  url: https://huggingface.co/signup
- group: start
  title: ''
  type: Login
  url: https://huggingface.co/login
- group: operate
  title: ''
  type: Support
  url: https://huggingface.co/support
- group: operate
  title: ''
  type: Contact
  url: https://huggingface.co/contact/sales
- group: operate
  title: ''
  type: Support
  url: https://discuss.huggingface.co
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/huggingface
- group: other
  title: ''
  type: X
  url: https://twitter.com/huggingface
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/huggingface
- group: operate
  title: ''
  type: Support
  url: https://huggingface.co/join/discord
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@HuggingFace
- group: operate
  title: ''
  type: StatusPage
  url: https://status.huggingface.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://huggingface.co/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://huggingface.co/privacy
- group: build
  title: ''
  type: SDKs
  url: https://huggingface.co/docs/huggingface_hub/index
- group: build
  title: ''
  type: SDKs
  url: https://huggingface.co/docs/huggingface.js/en/index
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hugging-face-model-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hugging-face-dataset-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hugging-face-space-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hugging-face-inference-endpoint-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/hugging-face-user-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/hugging-face-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/huggingface/hf-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/huggingface/skills
- group: other
  title: ''
  type: AICatalog
  url: ai-catalog/hugging-face-ai-catalog.yml
created: '2024'
description: The AI community building the future with open-source machine learning models, datasets, and applications.
examples:
- key_count: 6
  name: Hugging Face Automaticspeechrecognition Example
  slug: hugging-face-automaticspeechrecognition-example
- key_count: 6
  name: Hugging Face Chatcompletions Example
  slug: hugging-face-chatcompletions-example
- key_count: 6
  name: Hugging Face Completions Example
  slug: hugging-face-completions-example
- key_count: 6
  name: Hugging Face Createchatcompletion Example
  slug: hugging-face-createchatcompletion-example
- key_count: 6
  name: Hugging Face Createcompletion Example
  slug: hugging-face-createcompletion-example
- key_count: 6
  name: Hugging Face Createembeddings Example
  slug: hugging-face-createembeddings-example
- key_count: 6
  name: Hugging Face Createendpoint Example
  slug: hugging-face-createendpoint-example
- key_count: 6
  name: Hugging Face Createimagegeneration Example
  slug: hugging-face-createimagegeneration-example
- key_count: 6
  name: Hugging Face Createrepo Example
  slug: hugging-face-createrepo-example
- key_count: 6
  name: Hugging Face Createspeech Example
  slug: hugging-face-createspeech-example
- key_count: 6
  name: Hugging Face Createtranscription Example
  slug: hugging-face-createtranscription-example
- key_count: 4
  name: Hugging Face Dataset Viewer Error Example
  slug: hugging-face-dataset-viewer-error-example
- key_count: 2
  name: Hugging Face Dataset Viewer Parquet Response Example
  slug: hugging-face-dataset-viewer-parquet-response-example
- key_count: 5
  name: Hugging Face Dataset Viewer Rows Response Example
  slug: hugging-face-dataset-viewer-rows-response-example
- key_count: 5
  name: Hugging Face Dataset Viewer Search Response Example
  slug: hugging-face-dataset-viewer-search-response-example
- key_count: 2
  name: Hugging Face Dataset Viewer Size Response Example
  slug: hugging-face-dataset-viewer-size-response-example
- key_count: 3
  name: Hugging Face Dataset Viewer Splits Response Example
  slug: hugging-face-dataset-viewer-splits-response-example
- key_count: 3
  name: Hugging Face Dataset Viewer Statistics Response Example
  slug: hugging-face-dataset-viewer-statistics-response-example
- key_count: 5
  name: Hugging Face Dataset Viewer Validity Response Example
  slug: hugging-face-dataset-viewer-validity-response-example
- key_count: 6
  name: Hugging Face Deleteendpoint Example
  slug: hugging-face-deleteendpoint-example
- key_count: 6
  name: Hugging Face Deleterepo Example
  slug: hugging-face-deleterepo-example
- key_count: 6
  name: Hugging Face Featureextraction Example
  slug: hugging-face-featureextraction-example
- key_count: 6
  name: Hugging Face Fillmask Example
  slug: hugging-face-fillmask-example
- key_count: 6
  name: Hugging Face Filterrows Example
  slug: hugging-face-filterrows-example
- key_count: 6
  name: Hugging Face Generate Example
  slug: hugging-face-generate-example
- key_count: 6
  name: Hugging Face Generatestream Example
  slug: hugging-face-generatestream-example
- key_count: 6
  name: Hugging Face Getcroissantmetadata Example
  slug: hugging-face-getcroissantmetadata-example
- key_count: 6
  name: Hugging Face Getdataset Example
  slug: hugging-face-getdataset-example
- key_count: 6
  name: Hugging Face Getdatasetparquet Example
  slug: hugging-face-getdatasetparquet-example
- key_count: 6
  name: Hugging Face Getdatasetsize Example
  slug: hugging-face-getdatasetsize-example
- key_count: 6
  name: Hugging Face Getendpoint Example
  slug: hugging-face-getendpoint-example
- key_count: 6
  name: Hugging Face Getendpointlogs Example
  slug: hugging-face-getendpointlogs-example
- key_count: 6
  name: Hugging Face Getendpointmetrics Example
  slug: hugging-face-getendpointmetrics-example
- key_count: 6
  name: Hugging Face Getfirstrows Example
  slug: hugging-face-getfirstrows-example
- key_count: 6
  name: Hugging Face Getinfo Example
  slug: hugging-face-getinfo-example
- key_count: 6
  name: Hugging Face Getmetrics Example
  slug: hugging-face-getmetrics-example
- key_count: 6
  name: Hugging Face Getmodel Example
  slug: hugging-face-getmodel-example
- key_count: 6
  name: Hugging Face Getmodelrevision Example
  slug: hugging-face-getmodelrevision-example
- key_count: 6
  name: Hugging Face Getparquetfiles Example
  slug: hugging-face-getparquetfiles-example
- key_count: 6
  name: Hugging Face Getrows Example
  slug: hugging-face-getrows-example
- key_count: 6
  name: Hugging Face Getspace Example
  slug: hugging-face-getspace-example
- key_count: 6
  name: Hugging Face Getsplits Example
  slug: hugging-face-getsplits-example
- key_count: 6
  name: Hugging Face Getstatistics Example
  slug: hugging-face-getstatistics-example
- key_count: 5
  name: Hugging Face Hub Create Repo Request Example
  slug: hugging-face-hub-create-repo-request-example
- key_count: 0
  name: Hugging Face Hub Dataset Info Example
  slug: hugging-face-hub-dataset-info-example
- key_count: 13
  name: Hugging Face Hub Dataset Summary Example
  slug: hugging-face-hub-dataset-summary-example
- key_count: 2
  name: Hugging Face Hub Error Example
  slug: hugging-face-hub-error-example
- key_count: 0
  name: Hugging Face Hub Model Info Example
  slug: hugging-face-hub-model-info-example
- key_count: 15
  name: Hugging Face Hub Model Summary Example
  slug: hugging-face-hub-model-summary-example
- key_count: 1
  name: Hugging Face Hub Repo Url Example
  slug: hugging-face-hub-repo-url-example
- key_count: 0
  name: Hugging Face Hub Space Info Example
  slug: hugging-face-hub-space-info-example
- key_count: 11
  name: Hugging Face Hub Space Summary Example
  slug: hugging-face-hub-space-summary-example
- key_count: 11
  name: Hugging Face Hub User Info Example
  slug: hugging-face-hub-user-info-example
- key_count: 6
  name: Hugging Face Imageclassification Example
  slug: hugging-face-imageclassification-example
- key_count: 2
  name: Hugging Face Inference Classification Result Example
  slug: hugging-face-inference-classification-result-example
- key_count: 5
  name: Hugging Face Inference Endpoints Create Endpoint Request Example
  slug: hugging-face-inference-endpoints-create-endpoint-request-example
- key_count: 8
  name: Hugging Face Inference Endpoints Endpoint Example
  slug: hugging-face-inference-endpoints-endpoint-example
- key_count: 4
  name: Hugging Face Inference Endpoints Endpoint Metrics Example
  slug: hugging-face-inference-endpoints-endpoint-metrics-example
- key_count: 2
  name: Hugging Face Inference Endpoints Error Example
  slug: hugging-face-inference-endpoints-error-example
- key_count: 4
  name: Hugging Face Inference Endpoints Provider Example
  slug: hugging-face-inference-endpoints-provider-example
- key_count: 3
  name: Hugging Face Inference Endpoints Update Endpoint Request Example
  slug: hugging-face-inference-endpoints-update-endpoint-request-example
- key_count: 2
  name: Hugging Face Inference Error Example
  slug: hugging-face-inference-error-example
- key_count: 1
  name: Hugging Face Inference Feature Extraction Request Example
  slug: hugging-face-inference-feature-extraction-request-example
- key_count: 1
  name: Hugging Face Inference Fill Mask Request Example
  slug: hugging-face-inference-fill-mask-request-example
- key_count: 4
  name: Hugging Face Inference Fill Mask Response Example
  slug: hugging-face-inference-fill-mask-response-example
- key_count: 3
  name: Hugging Face Inference Inference Request Example
  slug: hugging-face-inference-inference-request-example
- key_count: 0
  name: Hugging Face Inference Inference Response Example
  slug: hugging-face-inference-inference-response-example
- key_count: 2
  name: Hugging Face Inference Model Loading Response Example
  slug: hugging-face-inference-model-loading-response-example
- key_count: 3
  name: Hugging Face Inference Object Detection Result Example
  slug: hugging-face-inference-object-detection-result-example
- key_count: 18
  name: Hugging Face Inference Providers Chat Completion Request Example
  slug: hugging-face-inference-providers-chat-completion-request-example
- key_count: 6
  name: Hugging Face Inference Providers Chat Completion Response Example
  slug: hugging-face-inference-providers-chat-completion-response-example
- key_count: 6
  name: Hugging Face Inference Providers Chat Completion Stream Response Example
  slug: hugging-face-inference-providers-chat-completion-stream-response-example
- key_count: 8
  name: Hugging Face Inference Providers Completion Request Example
  slug: hugging-face-inference-providers-completion-request-example
- key_count: 5
  name: Hugging Face Inference Providers Completion Response Example
  slug: hugging-face-inference-providers-completion-response-example
- key_count: 5
  name: Hugging Face Inference Providers Completion Stream Response Example
  slug: hugging-face-inference-providers-completion-stream-response-example
- key_count: 3
  name: Hugging Face Inference Providers Embedding Request Example
  slug: hugging-face-inference-providers-embedding-request-example
- key_count: 4
  name: Hugging Face Inference Providers Embedding Response Example
  slug: hugging-face-inference-providers-embedding-response-example
- key_count: 1
  name: Hugging Face Inference Providers Error Example
  slug: hugging-face-inference-providers-error-example
- key_count: 8
  name: Hugging Face Inference Providers Image Generation Request Example
  slug: hugging-face-inference-providers-image-generation-request-example
- key_count: 2
  name: Hugging Face Inference Providers Image Generation Response Example
  slug: hugging-face-inference-providers-image-generation-response-example
- key_count: 3
  name: Hugging Face Inference Providers Usage Example
  slug: hugging-face-inference-providers-usage-example
- key_count: 1
  name: Hugging Face Inference Question Answering Request Example
  slug: hugging-face-inference-question-answering-request-example
- key_count: 4
  name: Hugging Face Inference Question Answering Response Example
  slug: hugging-face-inference-question-answering-response-example
- key_count: 1
  name: Hugging Face Inference Sentence Similarity Request Example
  slug: hugging-face-inference-sentence-similarity-request-example
- key_count: 1
  name: Hugging Face Inference Speech Recognition Response Example
  slug: hugging-face-inference-speech-recognition-response-example
- key_count: 2
  name: Hugging Face Inference Summarization Request Example
  slug: hugging-face-inference-summarization-request-example
- key_count: 1
  name: Hugging Face Inference Summarization Response Example
  slug: hugging-face-inference-summarization-response-example
- key_count: 1
  name: Hugging Face Inference Text Classification Request Example
  slug: hugging-face-inference-text-classification-request-example
- key_count: 3
  name: Hugging Face Inference Text Generation Request Example
  slug: hugging-face-inference-text-generation-request-example
- key_count: 1
  name: Hugging Face Inference Text Generation Response Example
  slug: hugging-face-inference-text-generation-response-example
- key_count: 2
  name: Hugging Face Inference Text To Image Request Example
  slug: hugging-face-inference-text-to-image-request-example
- key_count: 1
  name: Hugging Face Inference Translation Request Example
  slug: hugging-face-inference-translation-request-example
- key_count: 1
  name: Hugging Face Inference Translation Response Example
  slug: hugging-face-inference-translation-response-example
- key_count: 2
  name: Hugging Face Inference Zero Shot Classification Request Example
  slug: hugging-face-inference-zero-shot-classification-request-example
- key_count: 3
  name: Hugging Face Inference Zero Shot Classification Response Example
  slug: hugging-face-inference-zero-shot-classification-response-example
- key_count: 6
  name: Hugging Face Isvalid Example
  slug: hugging-face-isvalid-example
- key_count: 6
  name: Hugging Face Listdatasets Example
  slug: hugging-face-listdatasets-example
- key_count: 6
  name: Hugging Face Listdatasettags Example
  slug: hugging-face-listdatasettags-example
- key_count: 6
  name: Hugging Face Listendpoints Example
  slug: hugging-face-listendpoints-example
- key_count: 6
  name: Hugging Face Listmetrics Example
  slug: hugging-face-listmetrics-example
- key_count: 6
  name: Hugging Face Listmodels Example
  slug: hugging-face-listmodels-example
- key_count: 6
  name: Hugging Face Listmodeltags Example
  slug: hugging-face-listmodeltags-example
- key_count: 6
  name: Hugging Face Listproviders Example
  slug: hugging-face-listproviders-example
- key_count: 6
  name: Hugging Face Listspaces Example
  slug: hugging-face-listspaces-example
- key_count: 6
  name: Hugging Face Objectdetection Example
  slug: hugging-face-objectdetection-example
- key_count: 6
  name: Hugging Face Pauseendpoint Example
  slug: hugging-face-pauseendpoint-example
- key_count: 6
  name: Hugging Face Questionanswering Example
  slug: hugging-face-questionanswering-example
- key_count: 6
  name: Hugging Face Resumeendpoint Example
  slug: hugging-face-resumeendpoint-example
- key_count: 6
  name: Hugging Face Runinference Example
  slug: hugging-face-runinference-example
- key_count: 6
  name: Hugging Face Runpipelineinference Example
  slug: hugging-face-runpipelineinference-example
- key_count: 6
  name: Hugging Face Scaletozero Example
  slug: hugging-face-scaletozero-example
- key_count: 6
  name: Hugging Face Searchrows Example
  slug: hugging-face-searchrows-example
- key_count: 6
  name: Hugging Face Sentencesimilarity Example
  slug: hugging-face-sentencesimilarity-example
- key_count: 6
  name: Hugging Face Summarization Example
  slug: hugging-face-summarization-example
- key_count: 17
  name: Hugging Face Text Generation Inference Chat Completion Request Example
  slug: hugging-face-text-generation-inference-chat-completion-request-example
- key_count: 6
  name: Hugging Face Text Generation Inference Chat Completion Response Example
  slug: hugging-face-text-generation-inference-chat-completion-response-example
- key_count: 6
  name: Hugging Face Text Generation Inference Chat Completion Stream Response Example
  slug: hugging-face-text-generation-inference-chat-completion-stream-response-example
- key_count: 9
  name: Hugging Face Text Generation Inference Completion Request Example
  slug: hugging-face-text-generation-inference-completion-request-example
- key_count: 5
  name: Hugging Face Text Generation Inference Completion Response Example
  slug: hugging-face-text-generation-inference-completion-response-example
- key_count: 5
  name: Hugging Face Text Generation Inference Completion Stream Response Example
  slug: hugging-face-text-generation-inference-completion-stream-response-example
- key_count: 2
  name: Hugging Face Text Generation Inference Error Response Example
  slug: hugging-face-text-generation-inference-error-response-example
- key_count: 2
  name: Hugging Face Text Generation Inference Generate Request Example
  slug: hugging-face-text-generation-inference-generate-request-example
- key_count: 2
  name: Hugging Face Text Generation Inference Generate Response Example
  slug: hugging-face-text-generation-inference-generate-response-example
- key_count: 18
  name: Hugging Face Text Generation Inference Info Example
  slug: hugging-face-text-generation-inference-info-example
- key_count: 3
  name: Hugging Face Text Generation Inference Stream Response Example
  slug: hugging-face-text-generation-inference-stream-response-example
- key_count: 3
  name: Hugging Face Text Generation Inference Usage Example
  slug: hugging-face-text-generation-inference-usage-example
- key_count: 6
  name: Hugging Face Textclassification Example
  slug: hugging-face-textclassification-example
- key_count: 6
  name: Hugging Face Textgeneration Example
  slug: hugging-face-textgeneration-example
- key_count: 6
  name: Hugging Face Texttoimage Example
  slug: hugging-face-texttoimage-example
- key_count: 6
  name: Hugging Face Tokenize Example
  slug: hugging-face-tokenize-example
- key_count: 6
  name: Hugging Face Translation Example
  slug: hugging-face-translation-example
- key_count: 6
  name: Hugging Face Updateendpoint Example
  slug: hugging-face-updateendpoint-example
- key_count: 6
  name: Hugging Face Updatereposettings Example
  slug: hugging-face-updatereposettings-example
- key_count: 6
  name: Hugging Face Whoami Example
  slug: hugging-face-whoami-example
- key_count: 6
  name: Hugging Face Zeroshotclassification Example
  slug: hugging-face-zeroshotclassification-example
features:
- description: Run inference on 200,000+ ML models with a simple HTTP request across NLP, vision, audio, and multimodal tasks.
  name: Model Inference
- description: Programmatically manage models, datasets, and spaces including creation, versioning, and access control.
  name: Hub Repository Management
- description: Deploy models on dedicated infrastructure with autoscaling, custom hardware, and private networking.
  name: Dedicated Endpoints
- description: Unified OpenAI-compatible API routing to 15+ inference providers with automatic model selection.
  name: Multi-Provider Routing
- description: Query, search, filter, and visualize datasets without downloading via the Dataset Viewer API.
  name: Dataset Exploration
- description: High-performance LLM serving with streaming, tool calling, structured output, and grammar constraints.
  name: Text Generation Inference
- description: Drop-in replacement for OpenAI API with chat completions, embeddings, and image generation endpoints.
  name: OpenAI Compatibility
finops:
- name: Hugging Face Finops
  service_category: AI Infrastructure
  slug: hugging-face-finops
graphqls:
- description: 'This conceptual GraphQL schema models the Hugging Face AI platform, covering the full surface area of its public APIs: the Hub API for managing models, datasets, and spaces; the Inference API for runn'
  name: Hugging Face GraphQL Schema
  slug: hugging-face-graphql
image: https://huggingface.co/front/assets/huggingface_logo.svg
json_schemas:
- name: ChatCompletionRequest
  property_count: 18
  slug: hugging-face-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 7
  slug: hugging-face-chatcompletionresponse
- name: ChatCompletionStreamResponse
  property_count: 7
  slug: hugging-face-chatcompletionstreamresponse
- name: ClassificationResult
  property_count: 2
  slug: hugging-face-classificationresult
- name: CompletionRequest
  property_count: 8
  slug: hugging-face-completionrequest
- name: CompletionResponse
  property_count: 6
  slug: hugging-face-completionresponse
- name: CompletionStreamResponse
  property_count: 5
  slug: hugging-face-completionstreamresponse
- name: CreateEndpointRequest
  property_count: 5
  slug: hugging-face-createendpointrequest
- name: CreateRepoRequest
  property_count: 5
  slug: hugging-face-createreporequest
- name: Hugging Face Dataset
  property_count: 16
  slug: hugging-face-dataset
- name: Error
  property_count: 4
  slug: hugging-face-dataset-viewer-error
- name: ParquetResponse
  property_count: 2
  slug: hugging-face-dataset-viewer-parquet-response
- name: RowsResponse
  property_count: 5
  slug: hugging-face-dataset-viewer-rows-response
- name: SearchResponse
  property_count: 5
  slug: hugging-face-dataset-viewer-search-response
- name: SizeResponse
  property_count: 2
  slug: hugging-face-dataset-viewer-size-response
- name: SplitsResponse
  property_count: 3
  slug: hugging-face-dataset-viewer-splits-response
- name: StatisticsResponse
  property_count: 3
  slug: hugging-face-dataset-viewer-statistics-response
- name: ValidityResponse
  property_count: 5
  slug: hugging-face-dataset-viewer-validity-response
- name: DatasetInfo
  property_count: 0
  slug: hugging-face-datasetinfo
- name: DatasetSummary
  property_count: 13
  slug: hugging-face-datasetsummary
- name: EmbeddingRequest
  property_count: 3
  slug: hugging-face-embeddingrequest
- name: EmbeddingResponse
  property_count: 4
  slug: hugging-face-embeddingresponse
- name: Endpoint
  property_count: 8
  slug: hugging-face-endpoint
- name: EndpointMetrics
  property_count: 4
  slug: hugging-face-endpointmetrics
- name: Error
  property_count: 4
  slug: hugging-face-error
- name: ErrorResponse
  property_count: 2
  slug: hugging-face-errorresponse
- name: FeatureExtractionRequest
  property_count: 1
  slug: hugging-face-featureextractionrequest
- name: FillMaskRequest
  property_count: 1
  slug: hugging-face-fillmaskrequest
- name: FillMaskResponse
  property_count: 4
  slug: hugging-face-fillmaskresponse
- name: GenerateRequest
  property_count: 2
  slug: hugging-face-generaterequest
- name: GenerateResponse
  property_count: 2
  slug: hugging-face-generateresponse
- name: CreateRepoRequest
  property_count: 5
  slug: hugging-face-hub-create-repo-request
- name: DatasetInfo
  property_count: 0
  slug: hugging-face-hub-dataset-info
- name: DatasetSummary
  property_count: 13
  slug: hugging-face-hub-dataset-summary
- name: Error
  property_count: 2
  slug: hugging-face-hub-error
- name: ModelInfo
  property_count: 0
  slug: hugging-face-hub-model-info
- name: ModelSummary
  property_count: 15
  slug: hugging-face-hub-model-summary
- name: RepoUrl
  property_count: 1
  slug: hugging-face-hub-repo-url
- name: SpaceInfo
  property_count: 0
  slug: hugging-face-hub-space-info
- name: SpaceSummary
  property_count: 11
  slug: hugging-face-hub-space-summary
- name: UserInfo
  property_count: 11
  slug: hugging-face-hub-user-info
- name: ImageGenerationRequest
  property_count: 8
  slug: hugging-face-imagegenerationrequest
- name: ImageGenerationResponse
  property_count: 2
  slug: hugging-face-imagegenerationresponse
- name: ClassificationResult
  property_count: 2
  slug: hugging-face-inference-classification-result
- name: Hugging Face Inference Endpoint
  property_count: 7
  slug: hugging-face-inference-endpoint
- name: CreateEndpointRequest
  property_count: 5
  slug: hugging-face-inference-endpoints-create-endpoint-request
- name: EndpointMetrics
  property_count: 4
  slug: hugging-face-inference-endpoints-endpoint-metrics
- name: Endpoint
  property_count: 8
  slug: hugging-face-inference-endpoints-endpoint
- name: Error
  property_count: 2
  slug: hugging-face-inference-endpoints-error
- name: Provider
  property_count: 4
  slug: hugging-face-inference-endpoints-provider
- name: UpdateEndpointRequest
  property_count: 3
  slug: hugging-face-inference-endpoints-update-endpoint-request
- name: Error
  property_count: 2
  slug: hugging-face-inference-error
- name: FeatureExtractionRequest
  property_count: 1
  slug: hugging-face-inference-feature-extraction-request
- name: FillMaskRequest
  property_count: 1
  slug: hugging-face-inference-fill-mask-request
- name: FillMaskResponse
  property_count: 4
  slug: hugging-face-inference-fill-mask-response
- name: InferenceRequest
  property_count: 3
  slug: hugging-face-inference-inference-request
- name: InferenceResponse
  property_count: 0
  slug: hugging-face-inference-inference-response
- name: ModelLoadingResponse
  property_count: 2
  slug: hugging-face-inference-model-loading-response
- name: ObjectDetectionResult
  property_count: 3
  slug: hugging-face-inference-object-detection-result
- name: ChatCompletionRequest
  property_count: 18
  slug: hugging-face-inference-providers-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: hugging-face-inference-providers-chat-completion-response
- name: ChatCompletionStreamResponse
  property_count: 6
  slug: hugging-face-inference-providers-chat-completion-stream-response
- name: CompletionRequest
  property_count: 8
  slug: hugging-face-inference-providers-completion-request
- name: CompletionResponse
  property_count: 5
  slug: hugging-face-inference-providers-completion-response
- name: CompletionStreamResponse
  property_count: 5
  slug: hugging-face-inference-providers-completion-stream-response
- name: EmbeddingRequest
  property_count: 3
  slug: hugging-face-inference-providers-embedding-request
- name: EmbeddingResponse
  property_count: 4
  slug: hugging-face-inference-providers-embedding-response
- name: Error
  property_count: 1
  slug: hugging-face-inference-providers-error
- name: ImageGenerationRequest
  property_count: 8
  slug: hugging-face-inference-providers-image-generation-request
- name: ImageGenerationResponse
  property_count: 2
  slug: hugging-face-inference-providers-image-generation-response
- name: Usage
  property_count: 3
  slug: hugging-face-inference-providers-usage
- name: QuestionAnsweringRequest
  property_count: 1
  slug: hugging-face-inference-question-answering-request
- name: QuestionAnsweringResponse
  property_count: 4
  slug: hugging-face-inference-question-answering-response
- name: SentenceSimilarityRequest
  property_count: 1
  slug: hugging-face-inference-sentence-similarity-request
- name: SpeechRecognitionResponse
  property_count: 1
  slug: hugging-face-inference-speech-recognition-response
- name: SummarizationRequest
  property_count: 2
  slug: hugging-face-inference-summarization-request
- name: SummarizationResponse
  property_count: 1
  slug: hugging-face-inference-summarization-response
- name: TextClassificationRequest
  property_count: 1
  slug: hugging-face-inference-text-classification-request
- name: TextGenerationRequest
  property_count: 3
  slug: hugging-face-inference-text-generation-request
- name: TextGenerationResponse
  property_count: 1
  slug: hugging-face-inference-text-generation-response
- name: TextToImageRequest
  property_count: 2
  slug: hugging-face-inference-text-to-image-request
- name: TranslationRequest
  property_count: 1
  slug: hugging-face-inference-translation-request
- name: TranslationResponse
  property_count: 1
  slug: hugging-face-inference-translation-response
- name: ZeroShotClassificationRequest
  property_count: 2
  slug: hugging-face-inference-zero-shot-classification-request
- name: ZeroShotClassificationResponse
  property_count: 3
  slug: hugging-face-inference-zero-shot-classification-response
- name: InferenceRequest
  property_count: 3
  slug: hugging-face-inferencerequest
- name: InferenceResponse
  property_count: 0
  slug: hugging-face-inferenceresponse
- name: Info
  property_count: 18
  slug: hugging-face-info
- name: Hugging Face Model
  property_count: 23
  slug: hugging-face-model
- name: ModelInfo
  property_count: 0
  slug: hugging-face-modelinfo
- name: ModelLoadingResponse
  property_count: 2
  slug: hugging-face-modelloadingresponse
- name: ModelSummary
  property_count: 15
  slug: hugging-face-modelsummary
- name: ObjectDetectionResult
  property_count: 3
  slug: hugging-face-objectdetectionresult
- name: ParquetResponse
  property_count: 2
  slug: hugging-face-parquetresponse
- name: Provider
  property_count: 4
  slug: hugging-face-provider
- name: QuestionAnsweringRequest
  property_count: 1
  slug: hugging-face-questionansweringrequest
- name: QuestionAnsweringResponse
  property_count: 4
  slug: hugging-face-questionansweringresponse
- name: RepoUrl
  property_count: 1
  slug: hugging-face-repourl
- name: RowsResponse
  property_count: 5
  slug: hugging-face-rowsresponse
- name: SearchResponse
  property_count: 5
  slug: hugging-face-searchresponse
- name: SentenceSimilarityRequest
  property_count: 1
  slug: hugging-face-sentencesimilarityrequest
- name: SizeResponse
  property_count: 2
  slug: hugging-face-sizeresponse
- name: Hugging Face Space
  property_count: 26
  slug: hugging-face-space
- name: SpaceInfo
  property_count: 0
  slug: hugging-face-spaceinfo
- name: SpaceSummary
  property_count: 11
  slug: hugging-face-spacesummary
- name: SpeechRecognitionResponse
  property_count: 1
  slug: hugging-face-speechrecognitionresponse
- name: SplitsResponse
  property_count: 3
  slug: hugging-face-splitsresponse
- name: StatisticsResponse
  property_count: 3
  slug: hugging-face-statisticsresponse
- name: StreamResponse
  property_count: 3
  slug: hugging-face-streamresponse
- name: SummarizationRequest
  property_count: 2
  slug: hugging-face-summarizationrequest
- name: SummarizationResponse
  property_count: 1
  slug: hugging-face-summarizationresponse
- name: ChatCompletionRequest
  property_count: 17
  slug: hugging-face-text-generation-inference-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: hugging-face-text-generation-inference-chat-completion-response
- name: ChatCompletionStreamResponse
  property_count: 6
  slug: hugging-face-text-generation-inference-chat-completion-stream-response
- name: CompletionRequest
  property_count: 9
  slug: hugging-face-text-generation-inference-completion-request
- name: CompletionResponse
  property_count: 5
  slug: hugging-face-text-generation-inference-completion-response
- name: CompletionStreamResponse
  property_count: 5
  slug: hugging-face-text-generation-inference-completion-stream-response
- name: ErrorResponse
  property_count: 2
  slug: hugging-face-text-generation-inference-error-response
- name: GenerateRequest
  property_count: 2
  slug: hugging-face-text-generation-inference-generate-request
- name: GenerateResponse
  property_count: 2
  slug: hugging-face-text-generation-inference-generate-response
- name: Info
  property_count: 18
  slug: hugging-face-text-generation-inference-info
- name: StreamResponse
  property_count: 3
  slug: hugging-face-text-generation-inference-stream-response
- name: Usage
  property_count: 3
  slug: hugging-face-text-generation-inference-usage
- name: TextClassificationRequest
  property_count: 1
  slug: hugging-face-textclassificationrequest
- name: TextGenerationRequest
  property_count: 3
  slug: hugging-face-textgenerationrequest
- name: TextGenerationResponse
  property_count: 1
  slug: hugging-face-textgenerationresponse
- name: TextToImageRequest
  property_count: 2
  slug: hugging-face-texttoimagerequest
- name: TranslationRequest
  property_count: 1
  slug: hugging-face-translationrequest
- name: TranslationResponse
  property_count: 1
  slug: hugging-face-translationresponse
- name: UpdateEndpointRequest
  property_count: 3
  slug: hugging-face-updateendpointrequest
- name: Usage
  property_count: 3
  slug: hugging-face-usage
- name: Hugging Face User
  property_count: 12
  slug: hugging-face-user
- name: UserInfo
  property_count: 11
  slug: hugging-face-userinfo
- name: ValidityResponse
  property_count: 5
  slug: hugging-face-validityresponse
- name: ZeroShotClassificationRequest
  property_count: 2
  slug: hugging-face-zeroshotclassificationrequest
- name: ZeroShotClassificationResponse
  property_count: 3
  slug: hugging-face-zeroshotclassificationresponse
json_structures:
- name: Hugging Face Dataset Viewer Error Structure
  property_count: 4
  slug: hugging-face-dataset-viewer-error-structure
- name: Hugging Face Dataset Viewer Parquet Response Structure
  property_count: 2
  slug: hugging-face-dataset-viewer-parquet-response-structure
- name: Hugging Face Dataset Viewer Rows Response Structure
  property_count: 5
  slug: hugging-face-dataset-viewer-rows-response-structure
- name: Hugging Face Dataset Viewer Search Response Structure
  property_count: 5
  slug: hugging-face-dataset-viewer-search-response-structure
- name: Hugging Face Dataset Viewer Size Response Structure
  property_count: 2
  slug: hugging-face-dataset-viewer-size-response-structure
- name: Hugging Face Dataset Viewer Splits Response Structure
  property_count: 3
  slug: hugging-face-dataset-viewer-splits-response-structure
- name: Hugging Face Dataset Viewer Statistics Response Structure
  property_count: 3
  slug: hugging-face-dataset-viewer-statistics-response-structure
- name: Hugging Face Dataset Viewer Validity Response Structure
  property_count: 5
  slug: hugging-face-dataset-viewer-validity-response-structure
- name: Hugging Face Hub Create Repo Request Structure
  property_count: 5
  slug: hugging-face-hub-create-repo-request-structure
- name: Hugging Face Hub Dataset Info Structure
  property_count: 0
  slug: hugging-face-hub-dataset-info-structure
- name: Hugging Face Hub Dataset Summary Structure
  property_count: 13
  slug: hugging-face-hub-dataset-summary-structure
- name: Hugging Face Hub Error Structure
  property_count: 2
  slug: hugging-face-hub-error-structure
- name: Hugging Face Hub Model Info Structure
  property_count: 0
  slug: hugging-face-hub-model-info-structure
- name: Hugging Face Hub Model Summary Structure
  property_count: 15
  slug: hugging-face-hub-model-summary-structure
- name: Hugging Face Hub Repo Url Structure
  property_count: 1
  slug: hugging-face-hub-repo-url-structure
- name: Hugging Face Hub Space Info Structure
  property_count: 0
  slug: hugging-face-hub-space-info-structure
- name: Hugging Face Hub Space Summary Structure
  property_count: 11
  slug: hugging-face-hub-space-summary-structure
- name: Hugging Face Hub User Info Structure
  property_count: 11
  slug: hugging-face-hub-user-info-structure
- name: Hugging Face Inference Classification Result Structure
  property_count: 2
  slug: hugging-face-inference-classification-result-structure
- name: Hugging Face Inference Endpoints Create Endpoint Request Structure
  property_count: 5
  slug: hugging-face-inference-endpoints-create-endpoint-request-structure
- name: Hugging Face Inference Endpoints Endpoint Metrics Structure
  property_count: 4
  slug: hugging-face-inference-endpoints-endpoint-metrics-structure
- name: Hugging Face Inference Endpoints Endpoint Structure
  property_count: 8
  slug: hugging-face-inference-endpoints-endpoint-structure
- name: Hugging Face Inference Endpoints Error Structure
  property_count: 2
  slug: hugging-face-inference-endpoints-error-structure
- name: Hugging Face Inference Endpoints Provider Structure
  property_count: 4
  slug: hugging-face-inference-endpoints-provider-structure
- name: Hugging Face Inference Endpoints Update Endpoint Request Structure
  property_count: 3
  slug: hugging-face-inference-endpoints-update-endpoint-request-structure
- name: Hugging Face Inference Error Structure
  property_count: 2
  slug: hugging-face-inference-error-structure
- name: Hugging Face Inference Feature Extraction Request Structure
  property_count: 1
  slug: hugging-face-inference-feature-extraction-request-structure
- name: Hugging Face Inference Fill Mask Request Structure
  property_count: 1
  slug: hugging-face-inference-fill-mask-request-structure
- name: Hugging Face Inference Fill Mask Response Structure
  property_count: 4
  slug: hugging-face-inference-fill-mask-response-structure
- name: Hugging Face Inference Inference Request Structure
  property_count: 3
  slug: hugging-face-inference-inference-request-structure
- name: Hugging Face Inference Inference Response Structure
  property_count: 0
  slug: hugging-face-inference-inference-response-structure
- name: Hugging Face Inference Model Loading Response Structure
  property_count: 2
  slug: hugging-face-inference-model-loading-response-structure
- name: Hugging Face Inference Object Detection Result Structure
  property_count: 3
  slug: hugging-face-inference-object-detection-result-structure
- name: Hugging Face Inference Providers Chat Completion Request Structure
  property_count: 18
  slug: hugging-face-inference-providers-chat-completion-request-structure
- name: Hugging Face Inference Providers Chat Completion Response Structure
  property_count: 6
  slug: hugging-face-inference-providers-chat-completion-response-structure
- name: Hugging Face Inference Providers Chat Completion Stream Response Structure
  property_count: 6
  slug: hugging-face-inference-providers-chat-completion-stream-response-structure
- name: Hugging Face Inference Providers Completion Request Structure
  property_count: 8
  slug: hugging-face-inference-providers-completion-request-structure
- name: Hugging Face Inference Providers Completion Response Structure
  property_count: 5
  slug: hugging-face-inference-providers-completion-response-structure
- name: Hugging Face Inference Providers Completion Stream Response Structure
  property_count: 5
  slug: hugging-face-inference-providers-completion-stream-response-structure
- name: Hugging Face Inference Providers Embedding Request Structure
  property_count: 3
  slug: hugging-face-inference-providers-embedding-request-structure
- name: Hugging Face Inference Providers Embedding Response Structure
  property_count: 4
  slug: hugging-face-inference-providers-embedding-response-structure
- name: Hugging Face Inference Providers Error Structure
  property_count: 1
  slug: hugging-face-inference-providers-error-structure
- name: Hugging Face Inference Providers Image Generation Request Structure
  property_count: 8
  slug: hugging-face-inference-providers-image-generation-request-structure
- name: Hugging Face Inference Providers Image Generation Response Structure
  property_count: 2
  slug: hugging-face-inference-providers-image-generation-response-structure
- name: Hugging Face Inference Providers Usage Structure
  property_count: 3
  slug: hugging-face-inference-providers-usage-structure
- name: Hugging Face Inference Question Answering Request Structure
  property_count: 1
  slug: hugging-face-inference-question-answering-request-structure
- name: Hugging Face Inference Question Answering Response Structure
  property_count: 4
  slug: hugging-face-inference-question-answering-response-structure
- name: Hugging Face Inference Sentence Similarity Request Structure
  property_count: 1
  slug: hugging-face-inference-sentence-similarity-request-structure
- name: Hugging Face Inference Speech Recognition Response Structure
  property_count: 1
  slug: hugging-face-inference-speech-recognition-response-structure
- name: Hugging Face Inference Summarization Request Structure
  property_count: 2
  slug: hugging-face-inference-summarization-request-structure
- name: Hugging Face Inference Summarization Response Structure
  property_count: 1
  slug: hugging-face-inference-summarization-response-structure
- name: Hugging Face Inference Text Classification Request Structure
  property_count: 1
  slug: hugging-face-inference-text-classification-request-structure
- name: Hugging Face Inference Text Generation Request Structure
  property_count: 3
  slug: hugging-face-inference-text-generation-request-structure
- name: Hugging Face Inference Text Generation Response Structure
  property_count: 1
  slug: hugging-face-inference-text-generation-response-structure
- name: Hugging Face Inference Text To Image Request Structure
  property_count: 2
  slug: hugging-face-inference-text-to-image-request-structure
- name: Hugging Face Inference Translation Request Structure
  property_count: 1
  slug: hugging-face-inference-translation-request-structure
- name: Hugging Face Inference Translation Response Structure
  property_count: 1
  slug: hugging-face-inference-translation-response-structure
- name: Hugging Face Inference Zero Shot Classification Request Structure
  property_count: 2
  slug: hugging-face-inference-zero-shot-classification-request-structure
- name: Hugging Face Inference Zero Shot Classification Response Structure
  property_count: 3
  slug: hugging-face-inference-zero-shot-classification-response-structure
- name: Hugging Face Structure
  property_count: 0
  slug: hugging-face-structure
- name: Hugging Face Text Generation Inference Chat Completion Request Structure
  property_count: 17
  slug: hugging-face-text-generation-inference-chat-completion-request-structure
- name: Hugging Face Text Generation Inference Chat Completion Response Structure
  property_count: 6
  slug: hugging-face-text-generation-inference-chat-completion-response-structure
- name: Hugging Face Text Generation Inference Chat Completion Stream Response Structure
  property_count: 6
  slug: hugging-face-text-generation-inference-chat-completion-stream-response-structure
- name: Hugging Face Text Generation Inference Completion Request Structure
  property_count: 9
  slug: hugging-face-text-generation-inference-completion-request-structure
- name: Hugging Face Text Generation Inference Completion Response Structure
  property_count: 5
  slug: hugging-face-text-generation-inference-completion-response-structure
- name: Hugging Face Text Generation Inference Completion Stream Response Structure
  property_count: 5
  slug: hugging-face-text-generation-inference-completion-stream-response-structure
- name: Hugging Face Text Generation Inference Error Response Structure
  property_count: 2
  slug: hugging-face-text-generation-inference-error-response-structure
- name: Hugging Face Text Generation Inference Generate Request Structure
  property_count: 2
  slug: hugging-face-text-generation-inference-generate-request-structure
- name: Hugging Face Text Generation Inference Generate Response Structure
  property_count: 2
  slug: hugging-face-text-generation-inference-generate-response-structure
- name: Hugging Face Text Generation Inference Info Structure
  property_count: 18
  slug: hugging-face-text-generation-inference-info-structure
- name: Hugging Face Text Generation Inference Stream Response Structure
  property_count: 3
  slug: hugging-face-text-generation-inference-stream-response-structure
- name: Hugging Face Text Generation Inference Usage Structure
  property_count: 3
  slug: hugging-face-text-generation-inference-usage-structure
jsonld:
- class_count: 4
  name: Hugging Face Context
  property_count: 15
  slug: hugging-face-context
- class_count: 0
  name: Hugging Face Dataset Viewer Context
  property_count: 0
  slug: hugging-face-dataset-viewer-context
- class_count: 0
  name: Hugging Face Hub Context
  property_count: 0
  slug: hugging-face-hub-context
- class_count: 0
  name: Hugging Face Inference Context
  property_count: 0
  slug: hugging-face-inference-context
- class_count: 0
  name: Hugging Face Inference Endpoints Context
  property_count: 0
  slug: hugging-face-inference-endpoints-context
- class_count: 0
  name: Hugging Face Inference Providers Context
  property_count: 0
  slug: hugging-face-inference-providers-context
- class_count: 0
  name: Hugging Face Text Generation Inference Context
  property_count: 0
  slug: hugging-face-text-generation-inference-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Hugging Face
nav: Providers
network: true
overview: 'Hugging Face publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Chat API, Chat Completions API, and 18 more.


  The Hugging Face catalog on APIs.io includes 7 JSON-LD contexts and 2 Spectral governance rulesets.


  Hugging Face''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, changelog, and 49 more developer resources.'
plans:
- name: Hugging Face Plans Pricing
  plan_count: 8
  slug: hugging-face-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Hugging Face Rate Limits
  slug: hugging-face-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Hugging Face API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: hugging-face-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Hugging Face API Rules
  rule_count: 16
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 9
  slug: hugging-face-spectral-rules
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 66.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 4.3
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 13.6
    contract_quality: 68.4
    developer_ergonomics: 85.7
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: false
    note: provider carries no tags; regime could not be determined
    undetermined: true
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hugging-face/refs/heads/main/screenshots/hugging-face-2026-06-20T182926.png
security:
- kind: authentication
  name: Hugging Face Authentication
  slug: hugging-face-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Hugging Face Domain Security
  slug: hugging-face-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hugging Face Vulnerability Disclosure
  slug: hugging-face-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 16
skills:
- name: hf-cli
  slug: hf-cli
- name: hf-mcp
  slug: hf-mcp
- name: huggingface-best
  slug: huggingface-best
- name: huggingface-community-evals
  slug: huggingface-community-evals
- name: huggingface-datasets
  slug: huggingface-datasets
- name: huggingface-gradio
  slug: huggingface-gradio
- name: huggingface-llm-trainer
  slug: huggingface-llm-trainer
- name: huggingface-local-models
  slug: huggingface-local-models
- name: huggingface-paper-publisher
  slug: huggingface-paper-publisher
- name: huggingface-papers
  slug: huggingface-papers
- name: huggingface-tool-builder
  slug: huggingface-tool-builder
- name: huggingface-trackio
  slug: huggingface-trackio
- name: huggingface-vision-trainer
  slug: huggingface-vision-trainer
- name: huggingface-zerogpu
  slug: huggingface-zerogpu
- name: train-sentence-transformers
  slug: train-sentence-transformers
- name: transformers-js
  slug: transformers-js
slug: hugging-face
use_cases:
- description: Rapidly prototype AI applications by running inference on pre-trained models without infrastructure setup.
  name: ML Model Prototyping
- description: Deploy and scale ML models for production workloads with dedicated endpoints and autoscaling.
  name: Production ML Deployment
- description: Explore, validate, and curate ML datasets programmatically for training pipeline automation.
  name: Dataset Curation
- description: Build AI-powered applications using unified inference APIs with multi-provider routing.
  name: AI Application Development
- description: Compare model performance across providers and hardware configurations for optimization.
  name: Model Benchmarking
website: https://huggingface.co
---
