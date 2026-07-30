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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Nvidia Nim Agentic Access
  operation_count: 16
  slug: nvidia-nim-agentic-access
  summary_line: 16 operations · 11 acting
api_count: 11
apis:
- description: Legacy OpenAI-compatible text completion endpoint (/v1/completions) for non-chat foundation models served by NIM. Accepts a raw prompt and returns generated text with the same streaming, sampling, and
  name: NVIDIA NIM Completions API
  slug: nvidia-nim-completions-api
- description: 'OpenAI-compatible embeddings endpoint (/v1/embeddings) backed by NVIDIA NeMo Retriever text embedding models including NV-Embed, NV-EmbedQA-E5, llama-3.2-nv-embedqa-1b, and BAAI BGE-M3. Returns dense '
  name: NVIDIA NIM Embeddings API
  slug: nvidia-nim-embeddings-api
- description: NeMo Retriever cross-encoder reranking endpoint (/v1/ranking) for scoring candidate passages against a query. Improves retrieval relevance on RAG pipelines and supports the llama-3.2-nv-rerankqa-1b an
  name: NVIDIA NIM Reranking API
  slug: nvidia-nim-reranking-api
- description: 'OpenAI-compatible model catalog endpoint (/v1/models) returning the list of models served by the NIM endpoint or container. Each entry includes id, owned_by, and created timestamp. Used by clients to '
  name: NVIDIA NIM Models API
  slug: nvidia-nim-models-api
- description: Vision-language model inference through the standard /v1/chat/completions surface with image inputs (base64 or URL) in the messages payload. Supports NVIDIA NeVA, microsoft/kosmos-2, Phi-3-vision, lla
  name: NVIDIA NIM Vision Language Models API
  slug: nvidia-nim-vision-api
- description: Liveness, readiness, and startup probes exposed by self-hosted NIM containers (/v1/health/live, /v1/health/ready) and a Prometheus /v1/metrics scrape endpoint for GPU utilization, request latency, and
  name: NVIDIA NIM Health API
  slug: nvidia-nim-health-api
- description: BioNeMo NIMs for protein structure prediction (AlphaFold2, ESMFold, OpenFold), protein generation (ProtGPT2, RFDiffusion), molecular property prediction (MolMIM), small molecule generation, and molecu
  name: NVIDIA NIM Biology (BioNeMo) API
  slug: nvidia-nim-biology-api
- description: Automatic speech recognition (speech-to-text)
  name: NVIDIA NIM ASR API
  slug: nvidia-nim-asr-api
- description: OpenAI-compatible chat completion operations
  name: NVIDIA NIM Chat API
  slug: nvidia-nim-chat-api
- description: Text-to-image and image-to-image generation
  name: NVIDIA NIM Images API
  slug: nvidia-nim-images-api
- description: Text-to-speech synthesis
  name: NVIDIA NIM TTS API
  slug: nvidia-nim-tts-api
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
artifact_total: 93
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
  name: NVIDIA NIM Biology (BioNeMo) API
  slug: open-nvidia-nim-biology-api
- collection_type: open
  name: NVIDIA NIM Chat Completions API
  slug: open-nvidia-nim-chat-completions-api
- collection_type: open
  name: NVIDIA NIM Completions API
  slug: open-nvidia-nim-completions-api
- collection_type: open
  name: NVIDIA NIM Embeddings API
  slug: open-nvidia-nim-embeddings-api
- collection_type: open
  name: NVIDIA NIM Health API
  slug: open-nvidia-nim-health-api
- collection_type: open
  name: NVIDIA NIM Image Generation API
  slug: open-nvidia-nim-image-generation-api
- collection_type: open
  name: NVIDIA NIM Models API
  slug: open-nvidia-nim-models-api
- collection_type: open
  name: NVIDIA NIM Reranking API
  slug: open-nvidia-nim-reranking-api
- collection_type: open
  name: NVIDIA NIM Speech API
  slug: open-nvidia-nim-speech-api
- collection_type: open
  name: NVIDIA NIM Vision Language Models API
  slug: open-nvidia-nim-vision-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nvidia-nim-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nvidia-nim-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nvidia-nim-domain-security.yml
- group: auth
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
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-bionemo-drug-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-discover-and-chat-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-generate-image-and-caption-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-health-gated-completion-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-rag-rerank-answer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nvidia-nim-vision-describe-and-summarize-workflow.yml
- group: design
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
  title: ''
  type: Plans
  url: plans/nvidia-nim-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nvidia-nim-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nvidia-nim-finops.yml
- group: build
  title: ''
  type: Packages
  url: packages/nvidia-nim-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nvidia-nim-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nvidia-nim-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nvidia-nim-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nvidia-nim-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nvidia-nim-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nvidia-nim-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nvidia-nim-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nvidia-nim-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/nvidia-nim-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nvidia-nim-data-model.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_asr.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_tts.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_nmt.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_audio.proto
- group: other
  title: ''
  type: Protobuf
  url: grpc/nvidia-nim-riva_common.proto
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-chat-completions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-completions-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-embeddings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-reranking-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-models-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-vision-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-image-generation-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-speech-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nvidia-nim-biology-overlay.yaml
- group: other
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
- name: Nvidia Nim Finops
  service_category: ''
  slug: nvidia-nim-finops
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
- description: ''
  name: nvidia-nim-mcp.yml
  slug: nvidia-nim-mcpyml
modified: '2026-06-20'
name: NVIDIA NIM
nav: Providers
network: true
overview: 'NVIDIA NIM publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Completions API, Embeddings API, Reranking API, and 8 more. Tagged areas include AI, Artificial Intelligence, Inference, Microservices, and LLM.


  The NVIDIA NIM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NVIDIA NIM''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, sandbox, pricing, and 68 more developer resources.'
plans:
- name: Nvidia Nim Plans Pricing
  plan_count: 3
  slug: nvidia-nim-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Nvidia Nim Rate Limits
  slug: nvidia-nim-rate-limits
rules:
- name: NVIDIA NIM API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: nvidia-nim-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 71.0
  delta: -2.4
  facets:
    commercial_clarity: 78.9
    contract_quality: 74.0
    developer_ergonomics: 76.1
    discoverability: 83.3
    governance: 69.8
    operational_transparency: 36.8
  previous_composite: 73.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nvidia-nim/refs/heads/main/screenshots/nvidia-nim-2026-06-20T190540.png
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
  summary_line: disclosure policy published
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
- AI
- Artificial Intelligence
- Inference
- Microservices
- LLM
- Foundation Models
- GPU
- Kubernetes
- NVIDIA
- OpenAI Compatible
website: https://build.nvidia.com
---
