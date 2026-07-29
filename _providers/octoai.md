---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: OpenAI-compatible chat and text-completion endpoints serving open-source LLMs including Llama 2, Llama 3, Mixtral 8x7B, Mistral 7B, Code Llama, and customer fine-tunes. Supported streaming, function c
  name: OctoAI Text Gen Inference API
  slug: octoai-text-gen-api
- description: Text-to-image and image-to-image inference for SDXL, SDXL-Lightning, Stable Diffusion 1.5, and SSD-1B with ControlNet, LoRA, and adapter support, plus inpainting and asset-management endpoints. The AP
  name: OctoAI Image Gen Inference API
  slug: octoai-image-gen-api
- description: Endpoints for uploading, listing, and managing user assets — checkpoints, LoRAs, textual inversions, ControlNets, and VAE files — used by the image and text inference APIs. The API was reachable under
  name: OctoAI Asset Library API
  slug: octoai-asset-library-api
- description: Container-deployment API ("Compute Service") that let customers build, register, and serve their own custom model containers on OctoAI's managed GPU fleet, with autoscaling and OpenAI-style invocation
  name: OctoAI Compute Service API
  slug: octoai-compute-service-api
- description: OctoStack was OctoAI's self-contained generative-AI production stack for deploying open and customer-trained foundation models inside a customer's VPC or on-premises environment. Announced April 2024,
  name: OctoStack
  slug: octostack
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octoai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octo.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/octoml
- group: other
  title: ''
  type: Acquirer
  url: https://www.nvidia.com
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.geekwire.com/2024/chip-giant-nvidia-acquires-octoai-a-seattle-startup-that-helps-companies-run-ai-models/
- group: other
  title: ''
  type: WindDownNotice
  url: https://www.sunsethq.com/blog/octoai-acquisition
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/octoml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/octoml
- group: build
  title: ''
  type: SDKs
  url: ''
- group: other
  title: ''
  type: SuccessorOrganization
  url: https://www.nvidia.com
created: '2026-05-25'
description: OctoAI (formerly OctoML) was a Seattle-based AI inference platform founded in 2019 as a University of Washington Allen School spin-out of the Apache TVM project. The company originally focused on machine-learning model optimization and compilation across CPUs, GPUs, and accelerators, and in June 2023 launched a generative-AI SaaS inference platform that served open-source foundation models (Llama 2, Mixtral, SDXL, Stable Diffusion, Whisper) behind OpenAI-style REST APIs with Python and TypeScript SDKs. In January 2024 OctoML formally rebranded to OctoAI and in April 2024 unveiled OctoStack, a self-contained generative-AI production stack for deploying models inside customer VPC and on-premises environments across NVIDIA GPUs, AMD GPUs, and AWS Inferentia. NVIDIA acquired OctoAI in September 2024 for a reported $165M (down from a 2021 peak valuation of ~$900M), with CEO Luis Ceze and key staff joining NVIDIA. OctoAI sent customers a "Wind down of OctoAI Services" notice and terminated
  all hosted endpoints, accounts, and SDK access on 31 October 2024. The octo.ai domain now 301-redirects to nvidia.com and no public OctoAI product, API, dashboard, or developer portal remains; the technology has been absorbed into NVIDIA's internal AI inference stack and is not separately purchasable. This catalog entry is a historical record of the former OctoAI developer surface and the GitHub artifacts that remain.
features:
- description: OctoAI's text and image endpoints implemented OpenAI-style request and response shapes so existing OpenAI client code could be repointed by changing the base URL and API key.
  name: OpenAI-Compatible Inference
- description: A shared catalog hosted Llama 2/3, Mixtral, Mistral, Code Llama, SDXL, SSD-1B, Stable Diffusion 1.5, and Whisper behind per-token and per-image pricing without GPU provisioning.
  name: Open-Source Model Catalog
- description: Customers could package their own model containers and have OctoAI autoscale them on a managed GPU fleet, billed by GPU-second.
  name: Custom Model Compute Service
- description: Upload and manage LoRAs, checkpoints, textual inversions, VAEs, and ControlNets and apply them at request time to image and text-generation endpoints.
  name: Asset Library
- description: Self-contained inference stack that ran inside a customer VPC or on-premises across NVIDIA, AMD, and AWS Inferentia hardware with fine-tuning, batching, and asset management built in.
  name: OctoStack Private Deployment
- description: OctoAI's optimization pipeline descended from Apache TVM (created by founder Tianqi Chen) and used ML-guided compilation to improve throughput and latency across heterogeneous accelerators.
  name: TVM-Based Model Optimization
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octoai.png
integrations:
- description: Acquired OctoAI in September 2024 for a reported $165M; OctoAI team and technology absorbed into NVIDIA's AI inference stack and all OctoAI hosted services terminated on 31 October 2024.
  name: NVIDIA
- description: OctoAI's optimization stack originated from Apache TVM, the deep-learning compiler founded by OctoAI co-founder Tianqi Chen at the University of Washington.
  name: Apache TVM
- description: OctoAI was an AWS Partner; OctoStack ran on AWS GPU instances and AWS Inferentia accelerators, with sagemaker-examples published in the GitHub org.
  name: AWS
- description: OctoAI ran a DockerCon 2023 generative-AI workshop and published the dockercon23-octoai workshop repo.
  name: Docker
- description: OctoAI's LLM endpoints shipped with documented LangChain and LlamaIndex providers, demonstrated in the octoml-llm-qa sample repo.
  name: LangChain & LlamaIndex
layout: provider
modified: '2026-05-25'
name: OctoAI
nav: Providers
network: true
overview: OctoAI publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Defunct, AI Inference, Generative AI, and LLM.
random_paper: 7
score:
  band: minimal
  composite: 8.5
  delta: -2.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octoai/refs/heads/main/screenshots/octoai-2026-06-20T190611.png
security:
- kind: domain-security
  name: Octoai Domain Security
  slug: octoai-domain-security
  summary_line: TLSv1.2 · DMARC
slug: octoai
tags:
- Acquired
- Defunct
- AI Inference
- Generative AI
- LLM
- Foundation Models
- Model Optimization
- Apache TVM
- GPU
- Private AI
- NVIDIA
use_cases:
- description: Teams used the OpenAI-compatible endpoints to swap GPT-3.5/4 calls for Llama 2 / Mixtral at lower cost without rewriting client code.
  name: Repointing OpenAI Workloads to Open Models
- description: Product, marketing, and creative teams ran SDXL-based image generation with custom LoRAs and ControlNets for branded asset production.
  name: Generative Image Pipelines
- description: Healthcare, financial-services, and government customers deployed OctoStack in-VPC or on-premises to keep prompts, completions, and model weights inside their security boundary.
  name: Private Generative AI in Regulated Industries
- description: Teams fine-tuned open-weights models and served the resulting adapters and full-weight checkpoints behind OctoAI inference endpoints without managing GPU infrastructure.
  name: Custom Fine-Tune Hosting
website: https://octo.ai
---
