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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 18
  human_in_the_loop: 2
  name: Qubrid Ai Agentic Access
  operation_count: 33
  slug: qubrid-ai-agentic-access
  summary_line: 33 operations · 18 acting · 2 human-in-the-loop
api_count: 13
apis:
- description: Generate chat-based completions using open-source large language models hosted on NVIDIA GPU infrastructure. Compatible with the OpenAI chat completions request and response format.
  name: Qubrid AI Chat Completions API
  slug: qubrid-ai-chat-completions-api
- description: Upload and manage CSV training datasets used for fine-tuning models. Datasets must be in CSV format with columns appropriate for the selected task type (QA or non-QA).
  name: Qubrid AI Datasets API
  slug: qubrid-ai-datasets-api
- description: Upload, list, and manage documents within a knowledge base. Supported formats include PDF, text, CSV, and other common document types. Documents are automatically processed, chunked, and embedded upon
  name: Qubrid AI Documents API
  slug: qubrid-ai-documents-api
- description: Generate vector embeddings from text input using embedding models hosted on the Qubrid AI platform, suitable for semantic search, clustering, and retrieval-augmented generation workflows.
  name: Qubrid AI Embeddings API
  slug: qubrid-ai-embeddings-api
- description: List and manage fine-tuned model artifacts produced by completed fine-tuning jobs. Fine-tuned models can be deployed for inference on the Qubrid AI platform.
  name: Qubrid AI Fine-Tuned Models API
  slug: qubrid-ai-fine-tuned-models-api
- description: Create, monitor, and manage fine-tuning jobs that customize pre-deployed text generation and code generation models using uploaded training datasets on GPU infrastructure.
  name: Qubrid AI Fine-Tuning Jobs API
  slug: qubrid-ai-fine-tuning-jobs-api
- description: Browse available GPU types, configurations, and pricing tiers including on-demand, weekly, monthly, and reserved options for NVIDIA, AMD, and Intel accelerators.
  name: Qubrid AI GPU Catalog API
  slug: qubrid-ai-gpu-catalog-api
- description: Provision, manage, start, stop, and terminate GPU compute instances on the Qubrid AI platform. Instances include NVIDIA H100, H200, and B200 accelerators with configurable memory, storage, and network
  name: Qubrid AI Instances API
  slug: qubrid-ai-instances-api
- description: Create and manage knowledge bases that store enterprise and departmental data for retrieval-augmented generation. Each knowledge base contains ingested documents that are chunked, embedded, and stored
  name: Qubrid AI Knowledge Bases API
  slug: qubrid-ai-knowledge-bases-api
- description: List and retrieve details about the open-source AI models available for inference on the Qubrid AI platform, including text generation, code generation, vision-language, and image generation models.
  name: Qubrid AI Models API
  slug: qubrid-ai-models-api
- description: 'Query a knowledge base using natural language with retrieval-augmented generation. The API retrieves relevant document chunks from the knowledge base and uses them as context for generating accurate, '
  name: Qubrid AI RAG Queries API
  slug: qubrid-ai-rag-queries-api
- description: Manage SSH keys for secure access to GPU compute instances. Users get full root access to their instances for installing custom libraries, running scripts, and managing workloads.
  name: Qubrid AI SSH Keys API
  slug: qubrid-ai-ssh-keys-api
- description: List and deploy pre-configured AI and ML environment templates including PyTorch, TensorFlow, ComfyUI, n8n, and Langflow, all optimized to run on Qubrid GPU instances.
  name: Qubrid AI Templates API
  slug: qubrid-ai-templates-api
artifact_total: 29
collections:
- collection_type: open
  name: Qubrid AI Compute API
  slug: open-qubrid-ai-compute
- collection_type: open
  name: Qubrid AI Fine-Tuning API
  slug: open-qubrid-ai-fine-tuning
- collection_type: open
  name: Qubrid AI Inference API
  slug: open-qubrid-ai-inference
- collection_type: open
  name: Qubrid AI RAG API
  slug: open-qubrid-ai-rag
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qubrid-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qubrid-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qubrid-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QubridAI-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qubrid
- group: start
  title: ''
  type: Portal
  url: https://platform.qubrid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.platform.qubrid.com
- group: company
  title: ''
  type: Website
  url: https://qubrid.com
- group: start
  title: ''
  type: Login
  url: https://platform.qubrid.com/login
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/json-ld/qubrid-ai-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.platform.qubrid.com/llms.txt
created: '2026-03-24'
description: Qubrid AI is a cloud platform that provides GPU-accelerated infrastructure and AI services for enterprise developers. Their developer platform offers OpenAI-compatible inference endpoints, GPU compute provisioning, model fine-tuning, and retrieval-augmented generation capabilities, all running on NVIDIA GPU infrastructure.
finops:
- name: Qubrid Ai Finops
  service_category: AI Infrastructure
  slug: qubrid-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qubrid-ai.png
json_schemas:
- name: Qubrid AI Compute Entities
  property_count: 0
  slug: qubrid-ai-compute
- name: Qubrid AI Fine-Tuning Entities
  property_count: 0
  slug: qubrid-ai-fine-tuning
- name: Qubrid AI Inference Entities
  property_count: 0
  slug: qubrid-ai-inference
- name: Qubrid AI RAG Entities
  property_count: 0
  slug: qubrid-ai-rag
jsonld:
- class_count: 0
  name: Qubrid Ai Context
  property_count: 8
  slug: qubrid-ai-context
layout: provider
modified: '2026-05-19'
name: Qubrid AI
nav: Providers
network: true
overview: 'Qubrid AI publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Chat Completions API, Datasets API, Documents API, and 10 more. Tagged areas include Artificial Intelligence, Cloud Computing, GPU, Inference, and Large Language Models.


  The Qubrid AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Qubrid AI''s developer surface includes authentication, developer portal, documentation, and 8 more developer resources.'
plans:
- name: Qubrid Ai Plans Pricing
  plan_count: 4
  slug: qubrid-ai-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Qubrid Ai Rate Limits
  slug: qubrid-ai-rate-limits
rules:
- name: Qubrid AI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: qubrid-ai-jsonschema-spectral-rules
score:
  band: developing
  composite: 52.7
  delta: -4.2
  facets:
    commercial_clarity: 52.6
    contract_quality: 74.6
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 56.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qubrid-ai/refs/heads/main/screenshots/qubrid-ai-2026-06-20T192419.png
security:
- kind: authentication
  name: Qubrid Ai Authentication
  slug: qubrid-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Qubrid Ai Domain Security
  slug: qubrid-ai-domain-security
  summary_line: TLSv1.2 · DMARC
slug: qubrid-ai
tags:
- Artificial Intelligence
- Cloud Computing
- GPU
- Inference
- Large Language Models
- Machine Learning
- NVIDIA
- Serverless
website: https://qubrid.com
---
