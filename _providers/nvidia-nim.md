---
access_model:
  confidence: low
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Nvidia Nim Agentic Access
  operation_count: 16
  slug: nvidia-nim-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 3
apis:
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: Legacy OpenAI-compatible text completion endpoint (/v1/completions) for non-chat foundation models served by NIM. Accepts a raw prompt and returns generated text with the same streaming, sampling, and
  name: NVIDIA NIM Completions API
  phrasing_intents:
  - id: createCompletion
    intent: Complete a raw text prompt
    question: Can I send a plain prompt string, not chat messages, and get a raw text continuation back?
  phrasing_ops: 1
  slug: nvidia-nim-completions-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: 'OpenAI-compatible embeddings endpoint (/v1/embeddings) backed by NVIDIA NeMo Retriever text embedding models including NV-Embed, NV-EmbedQA-E5, llama-3.2-nv-embedqa-1b, and BAAI BGE-M3. Returns dense '
  name: NVIDIA NIM Embeddings API
  phrasing_intents:
  - id: createEmbedding
    intent: Create embedding vectors for text
    question: Can I turn a batch of text strings into embedding vectors for semantic search?
  phrasing_ops: 1
  slug: nvidia-nim-embeddings-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: NeMo Retriever cross-encoder reranking endpoint (/v1/ranking) for scoring candidate passages against a query. Improves retrieval relevance on RAG pipelines and supports the llama-3.2-nv-rerankqa-1b an
  name: NVIDIA NIM Reranking API
  phrasing_intents:
  - id: rankPassages
    intent: Rerank passages by relevance to a query
    question: Can I reorder a set of retrieved passages by how relevant they are to a search query?
  phrasing_ops: 1
  slug: nvidia-nim-reranking-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: 'OpenAI-compatible model catalog endpoint (/v1/models) returning the list of models served by the NIM endpoint or container. Each entry includes id, owned_by, and created timestamp. Used by clients to '
  name: NVIDIA NIM Models API
  phrasing_intents:
  - id: listModels
    intent: List the models this NIM endpoint serves
    question: Which models are available on this NIM endpoint or container?
  - id: getModel
    intent: Get details for one model
    question: What metadata is available for one specific model id on the NIM endpoint?
  phrasing_ops: 2
  slug: nvidia-nim-models-api
- baseURL: https://integrate.api.nvidia.com
  baseurl_source: spec
  description: Liveness, readiness, and startup probes exposed by self-hosted NIM containers (/v1/health/live, /v1/health/ready) and a Prometheus /v1/metrics scrape endpoint for GPU utilization, request latency, and
  name: NVIDIA NIM Health API
  phrasing_intents:
  - id: getLiveness
    intent: Check that the NIM container process is alive
    question: Is my NIM container process still running, for a Kubernetes liveness probe?
  - id: getReadiness
    intent: Check that the model is loaded and ready
    question: Has the model engine finished loading so the NIM can start accepting traffic?
  - id: getMetrics
    intent: Get Prometheus metrics for a NIM container
    question: Where can I scrape GPU utilization and request latency metrics for my NIM deployment?
  phrasing_ops: 3
  slug: nvidia-nim-health-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: BioNeMo NIMs for protein structure prediction (AlphaFold2, ESMFold, OpenFold), protein generation (ProtGPT2, RFDiffusion), molecular property prediction (MolMIM), small molecule generation, and molecu
  name: NVIDIA NIM Biology (BioNeMo) API
  phrasing_intents:
  - id: predictProteinStructure
    intent: Predict a protein's 3D structure from its sequence
    question: Can I get a predicted 3D structure for a protein from just its amino acid sequence using AlphaFold2?
  - id: dockLigand
    intent: Dock a small-molecule ligand to a protein
    question: Can I predict where and how a drug-like molecule binds to my protein with DiffDock?
  - id: generateMolecules
    intent: Generate small molecules around a seed SMILES
    question: Can I generate new drug-like molecules similar to a seed SMILES string with MolMIM?
  phrasing_ops: 3
  slug: nvidia-nim-biology-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: Automatic speech recognition (speech-to-text)
  name: NVIDIA NIM ASR API
  phrasing_intents:
  - id: createTranscription
    intent: Transcribe an audio clip to text
    question: Can I turn a WAV, FLAC or MP3 recording into text with a Parakeet or Canary speech model?
  phrasing_ops: 1
  slug: nvidia-nim-asr-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: Text-to-image and image-to-image generation
  name: NVIDIA NIM Images API
  phrasing_intents:
  - id: generateImage
    intent: Generate or edit an image from a prompt
    question: Can I create an image from a text prompt with FLUX.1, SDXL or Edify image models?
  phrasing_ops: 1
  slug: nvidia-nim-images-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: Text-to-speech synthesis
  name: NVIDIA NIM TTS API
  phrasing_intents:
  - id: createSpeech
    intent: Synthesize speech audio from text
    question: Can I convert a paragraph of text into a spoken WAV or MP3 file with Magpie-TTS or FastPitch?
  phrasing_ops: 1
  slug: nvidia-nim-tts-api
- baseURL: https://integrate.api.nvidia.com/v1
  baseurl_source: declared
  description: OpenAI-compatible chat completion operations
  name: NVIDIA NIM Chat Completions API
  slug: nvidia-nim-chat-completions-api
arazzos:
- description: Fold a protein from sequence, dock a ligand into the predicted structure, then generate optimized analog molecules.
  name: NVIDIA NIM BioNeMo Drug Discovery
  slug: nvidia-nim-bionemo-drug-discovery-workflow
- description: List the served models, confirm a target model's metadata, then run a chat completion against it.
  name: NVIDIA NIM Discover And Chat
  slug: nvidia-nim-discover-and-chat-workflow
- description: Generate an image from a text prompt, then caption the generated image with a vision-language model.
  name: NVIDIA NIM Generate Image And Caption
  slug: nvidia-nim-generate-image-and-caption-workflow
- description: Check a self-hosted NIM container's readiness, and only run a text completion once the engine reports ready.
  name: NVIDIA NIM Health Gated Completion
  slug: nvidia-nim-health-gated-completion-workflow
- description: Embed a query, rerank candidate passages against it, then answer the question grounded in the top passage.
  name: NVIDIA NIM RAG Rerank And Answer
  slug: nvidia-nim-rag-rerank-answer-workflow
- description: Describe an image with a vision-language model, then condense the description into a short caption with an LLM.
  name: NVIDIA NIM Vision Describe And Summarize
  slug: nvidia-nim-vision-describe-and-summarize-workflow
- description: Transcribe an audio clip with Riva ASR, answer the transcript with an LLM, then synthesize the reply with Riva TTS.
  name: NVIDIA NIM Voice Assistant Loop
  slug: nvidia-nim-voice-assistant-loop-workflow
artifact_total: 96
collections:
- collection_type: postman
  name: NVIDIA NIM Biology (BioNeMo) API
  slug: postman-nvidia-nim-biology-api
- collection_type: postman
  name: NVIDIA NIM Chat Completions API
  slug: postman-nvidia-nim-chat-completions-api
- collection_type: postman
  name: NVIDIA NIM Completions API
  slug: postman-nvidia-nim-completions-api
- collection_type: postman
  name: NVIDIA NIM Embeddings API
  slug: postman-nvidia-nim-embeddings-api
- collection_type: postman
  name: NVIDIA NIM Health API
  slug: postman-nvidia-nim-health-api
- collection_type: postman
  name: NVIDIA NIM Image Generation API
  slug: postman-nvidia-nim-image-generation-api
- collection_type: postman
  name: NVIDIA NIM Models API
  slug: postman-nvidia-nim-models-api
- collection_type: postman
  name: NVIDIA NIM Reranking API
  slug: postman-nvidia-nim-reranking-api
- collection_type: postman
  name: NVIDIA NIM Speech API
  slug: postman-nvidia-nim-speech-api
- collection_type: postman
  name: NVIDIA NIM Vision Language Models API
  slug: postman-nvidia-nim-vision-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR API
  slug: open-nvidia-nim-asr-api
- collection_type: open
  name: NVIDIA NIM (BioNeMo) ASR Biology API
  slug: open-nvidia-nim-biology-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Chat API
  slug: open-nvidia-nim-chat-api
- collection_type: open
  name: NVIDIA NIM Chat Completions API
  slug: open-nvidia-nim-chat-completions-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Completions API
  slug: open-nvidia-nim-completions-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Embeddings API
  slug: open-nvidia-nim-embeddings-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Health API
  slug: open-nvidia-nim-health-api
- collection_type: open
  name: NVIDIA NIM Image Generation API
  slug: open-nvidia-nim-image-generation-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Images API
  slug: open-nvidia-nim-images-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Models API
  slug: open-nvidia-nim-models-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Reranking API
  slug: open-nvidia-nim-reranking-api
- collection_type: open
  name: NVIDIA NIM Speech API
  slug: open-nvidia-nim-speech-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR TTS API
  slug: open-nvidia-nim-tts-api
- collection_type: open
  name: NVIDIA NIM Biology (BioNeMo) ASR Vision API
  slug: open-nvidia-nim-vision-api
common:
- group: other
  href: https://artifacts.apis.io/nvidia-nim/capabilities/nvidia-nim-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/nvidia-nim-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.nvidia.com/
- group: agent
  href: https://artifacts.apis.io/nvidia-nim/agentic-access/nvidia-nim-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nvidia-nim-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/nvidia-nim/security/nvidia-nim-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/nvidia-nim-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/nvidia-nim/security/nvidia-nim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nvidia-nim-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/nvidia-nim/authentication/nvidia-nim-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nvidia-nim-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/NVIDIA/skills
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/nvidia-nim/overview
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-bionemo-drug-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-bionemo-drug-discovery-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-discover-and-chat-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-discover-and-chat-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-generate-image-and-caption-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-generate-image-and-caption-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-health-gated-completion-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-health-gated-completion-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-rag-rerank-answer-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-rag-rerank-answer-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-vision-describe-and-summarize-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-vision-describe-and-summarize-workflow.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/arazzo/nvidia-nim-voice-assistant-loop-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-voice-assistant-loop-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://build.nvidia.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nvidia.com/nim/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.nvidia.com/nim/reference/llm-apis
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nvidia.com/nim
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nvidia.com/nim/large-language-models/latest/getting-started.html
- group: start
  title: ''
  type: Signup
  url: https://build.nvidia.com/explore/discover
- group: start
  title: ''
  type: Sandbox
  url: https://build.nvidia.com/explore/discover
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nvidia.com/en-us/data-center/products/ai-enterprise/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NVIDIA
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NVIDIA-NIM-Agent-Blueprints
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nvidia.com
- group: company
  title: ''
  type: Blog
  url: https://developer.nvidia.com/blog/category/generative-ai/
- group: company
  title: ''
  type: Blog
  url: https://blogs.nvidia.com/blog/category/generative-ai/
- group: operate
  title: ''
  type: Forums
  url: https://forums.developer.nvidia.com/c/ai-data-science/nemo-llm-service/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.nvidia.com/en-us/about-nvidia/legal-info/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nvidia.com/en-us/about-nvidia/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nvidia.com/en-us/about-nvidia/privacy-policy/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nvidia.com/nim-operator/latest/index.html
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/nim-deploy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/k8s-nim-operator
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/GenerativeAIExamples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/NeMo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/NeMo-Guardrails
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NVIDIA/TensorRT-LLM
- group: build
  title: ''
  type: SDKs
  url: https://github.com/triton-inference-server/server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/langchain-ai/langchain-nvidia
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/openai/
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NVIDIA/GenerativeAIExamples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NVIDIA-AI-Blueprints
- group: other
  title: ''
  type: Models
  url: https://build.nvidia.com/explore/discover
- group: other
  title: ''
  type: KubernetesCRD
  url: https://github.com/NVIDIA/k8s-nim-operator/tree/main/api
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.api.nvidia.com/nim/reference/limits
- group: design
  title: ''
  type: Versioning
  url: https://docs.nvidia.com/nim/large-language-models/latest/release-notes.html
- group: commercial
  href: https://artifacts.apis.io/nvidia-nim/plans/nvidia-nim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nvidia-nim-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/nvidia-nim/rate-limits/nvidia-nim-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/nvidia-nim-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/nvidia-nim/finops/nvidia-nim-finops.yml
  title: ''
  type: FinOps
  url: finops/nvidia-nim-finops.yml
- group: build
  href: https://artifacts.apis.io/nvidia-nim/packages/nvidia-nim-packages.yml
  title: ''
  type: Packages
  url: packages/nvidia-nim-packages.yml
- group: agent
  href: https://artifacts.apis.io/nvidia-nim/well-known/nvidia-nim-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nvidia-nim-well-known.yml
- group: agent
  href: https://artifacts.apis.io/nvidia-nim/mcp/nvidia-nim-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nvidia-nim-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nvidia-nim/llms/nvidia-nim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nvidia-nim-llms.txt
- group: design
  href: https://artifacts.apis.io/nvidia-nim/conformance/nvidia-nim-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nvidia-nim-conformance.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/errors/nvidia-nim-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nvidia-nim-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/lifecycle/nvidia-nim-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nvidia-nim-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/conventions/nvidia-nim-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nvidia-nim-conventions.yml
- group: operate
  href: https://artifacts.apis.io/nvidia-nim/changelog/nvidia-nim-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/nvidia-nim-changelog.yml
- group: build
  href: https://artifacts.apis.io/nvidia-nim/cli/nvidia-nim-cli.yml
  title: ''
  type: CLI
  url: cli/nvidia-nim-cli.yml
- group: design
  href: https://artifacts.apis.io/nvidia-nim/data-model/nvidia-nim-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nvidia-nim-data-model.yml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/grpc/nvidia-nim-riva_asr.proto
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_asr.proto
- group: other
  href: https://artifacts.apis.io/nvidia-nim/grpc/nvidia-nim-riva_tts.proto
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_tts.proto
- group: other
  href: https://artifacts.apis.io/nvidia-nim/grpc/nvidia-nim-riva_nmt.proto
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_nmt.proto
- group: other
  href: https://artifacts.apis.io/nvidia-nim/grpc/nvidia-nim-riva_audio.proto
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_audio.proto
- group: other
  href: https://artifacts.apis.io/nvidia-nim/grpc/nvidia-nim-riva_common.proto
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_common.proto
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-chat-completions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-chat-completions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-completions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-completions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-embeddings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-embeddings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-reranking-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-reranking-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-models-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-models-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-vision-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-vision-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-image-generation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-image-generation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-speech-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-speech-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-biology-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-biology-overlay.yaml
- group: other
  href: https://artifacts.apis.io/nvidia-nim/overlays/nvidia-nim-health-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-health-overlay.yaml
created: '2026-05-25'
description: NVIDIA NIM (NVIDIA Inference Microservices) is a catalog of GPU-accelerated, containerized AI inference microservices that package optimized model engines (TensorRT-LLM, vLLM, SGLang, Triton) behind industry-standard OpenAI-compatible REST APIs. NIM covers large language models, embeddings and reranking, vision-language models, speech (Riva), visual generative AI, and biology (BioNeMo) — exposed identically whether consumed from the hosted endpoint at integrate.api.nvidia.com or self-hosted via Docker containers and the Kubernetes-native NIM Operator. NIM ships with NVIDIA AI Enterprise for commercial deployment and is the inference layer underneath NVIDIA AI Blueprints, NeMo Retriever, NeMo Guardrails, and the broader NVIDIA developer stack.
features:
- OpenAI-compatible REST surface — /v1/chat/completions, /v1/completions, /v1/embeddings, /v1/models, /v1/ranking
- 100+ foundation models exposed through a single API contract — Llama 3.1/3.2/3.3, Mistral, Mixtral, NVIDIA Nemotron, DeepSeek-R1, Qwen 2.5, Microsoft Phi, Google Gemma, IBM Granite, and Falcon
- Free hosted inference at build.nvidia.com on DGX Cloud — 1,000 credits on signup, 40 RPM rate limit
- Self-hosted deployment via Docker containers shipping TensorRT-LLM, vLLM, or SGLang inference engines
- Kubernetes-native deployment via the NIM Operator with NIMService, NIMCache, NIMPipeline CRDs
- GPU-aware autoscaling, persistent model caches, and rolling upgrades managed by the operator
- Multi-tenant licensing through NVIDIA AI Enterprise (commercial production use)
- NeMo Retriever NIMs for embeddings, reranking, OCR, and PDF-to-Markdown extraction in RAG pipelines
- Vision Language Model NIMs reusing the chat-completions surface for multimodal inputs
- NVIDIA Riva speech NIMs (Parakeet ASR, Canary translation, Magpie TTS) with HTTP and gRPC adapters
- BioNeMo NIMs for AlphaFold2, ESMFold, ProtGPT2, MolMIM, DiffDock, RFDiffusion
- Visual generative AI NIMs — FLUX.1, SDXL, Shutterstock Edify Image, Edify 3D
- NeMo Guardrails for input/output safety and topic policy enforcement
- Function calling, JSON mode, tool use, and structured outputs across compatible LLMs
- Streaming via Server-Sent Events on chat/completions
- Prometheus /v1/metrics scrape endpoint and /v1/health/{live,ready} probes for Kubernetes
- LangChain, LlamaIndex, Haystack, OpenAI SDK, and direct REST client compatibility
- NVIDIA AI Blueprints — full reference RAG, multimodal search, drug discovery, and digital human stacks
- Available on DGX Cloud, AWS, Azure, Google Cloud, Oracle Cloud, GKE, EKS, AKS, OpenShift, and on-prem
finops:
- has_sources: true
  method: derived
  name: Nvidia Nim Finops
  primary_unit: ''
  service_category: ''
  slug: nvidia-nim-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nvidia-nim.png
json_schemas:
- name: NVIDIA NIM Chat Completion
  property_count: 0
  slug: nvidia-nim-chat-completion
- name: NVIDIA NIM Embedding
  property_count: 0
  slug: nvidia-nim-embedding
jsonld:
- class_count: 40
  name: Nvidia Nim Context
  property_count: 10
  slug: nvidia-nim-context
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP; 15 tools listed. A candidate, not confirmed as published by the provider.
  name: NVIDIA NIM MCP Server
  slug: nvidia-nim
modified: '2026-06-20'
name: NVIDIA NIM
nav: Providers
network: true
overview: 'NVIDIA NIM publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Completions API, Embeddings API, Reranking API, and 7 more. Tagged areas include Artificial Intelligence, Inference, Microservices, LLM, and Foundation Models.


  The NVIDIA NIM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NVIDIA NIM''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, sandbox, pricing, and 70 more developer resources.'
plans:
- name: Nvidia Nim Plans Pricing
  plan_count: 0
  slug: nvidia-nim-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Nvidia Nim Rate Limits
  slug: nvidia-nim-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: NVIDIA NIM — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: nvidia-nim-jsonschema-spectral-rules
score:
  band: strong
  composite: 59.8
  coverage:
    artifact_dirs: 33
    catalog_earned: 59.7
    catalog_earned_first_party: 0.0
    catalog_gap: 55.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 52.6
    contract_governance: 20.5
    contract_quality: 64.0
    developer_ergonomics: 82.6
    discoverability: 69.6
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nvidia-nim/nvidia-nim-2026-06-20T190540.png
security:
- kind: authentication
  name: Nvidia Nim Authentication
  slug: nvidia-nim-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nvidia Nim Domain Security
  slug: nvidia-nim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nvidia Nim Vulnerability Disclosure
  slug: nvidia-nim-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 237
skills:
- name: accelerated-computing-cudf
  slug: accelerated-computing-cudf
- name: aiq-deploy
  slug: aiq-deploy-2
- name: aiq-deploy
  slug: aiq-deploy
- name: aiq-research
  slug: aiq-research-2
- name: aiq-research
  slug: aiq-research
- name: cudaq-guide
  slug: cudaq-guide
- name: cufolio
  slug: cufolio
- name: cuopt-developer
  slug: cuopt-developer
- name: cuopt-install
  slug: cuopt-install
- name: cuopt-numerical-optimization-api-c
  slug: cuopt-numerical-optimization-api-c
- name: cuopt-numerical-optimization-api-cli
  slug: cuopt-numerical-optimization-api-cli
- name: cuopt-numerical-optimization-api-python
  slug: cuopt-numerical-optimization-api-python
- name: cuopt-numerical-optimization-formulation
  slug: cuopt-numerical-optimization-formulation
- name: cuopt-routing-api-python
  slug: cuopt-routing-api-python
- name: cuopt-routing-formulation
  slug: cuopt-routing-formulation
- name: cuopt-server-api-python
  slug: cuopt-server-api-python
- name: cuopt-server-common
  slug: cuopt-server-common
- name: cuopt-skill-evolution
  slug: cuopt-skill-evolution
- name: cuopt-user-rules
  slug: cuopt-user-rules-2
- name: cuopt-user-rules
  slug: cuopt-user-rules
- name: cupynumeric-hdf5
  slug: cupynumeric-hdf5
- name: cupynumeric-install
  slug: cupynumeric-install
- name: cupynumeric-migration-readiness
  slug: cupynumeric-migration-readiness
- name: cupynumeric-parallel-data-load
  slug: cupynumeric-parallel-data-load
slug: nvidia-nim
tags:
- Artificial Intelligence
- Inference
- Microservices
- LLM
- Foundation Models
- GPU
- Kubernetes
- NVIDIA
- OpenAI-Compatible
website: https://www.nvidia.com/
---
