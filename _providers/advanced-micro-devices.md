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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Advanced Micro Devices Agentic Access
  operation_count: 13
  slug: advanced-micro-devices-agentic-access
  summary_line: 13 operations · 3 acting · 1 human-in-the-loop
api_count: 8
apis:
- description: ROCm system configuration
  name: Advanced Micro Devices Configuration API
  slug: advanced-micro-devices-configuration-api
- description: Cloud credit balance and usage
  name: Advanced Micro Devices Credits API
  slug: advanced-micro-devices-credits-api
- description: GPU device enumeration and information
  name: Advanced Micro Devices Devices API
  slug: advanced-micro-devices-devices-api
- description: GPU health and diagnostic status
  name: Advanced Micro Devices Health API
  slug: advanced-micro-devices-health-api
- description: GPU compute instance management
  name: Advanced Micro Devices Instances API
  slug: advanced-micro-devices-instances-api
- description: AI model deployment and management
  name: Advanced Micro Devices Models API
  slug: advanced-micro-devices-models-api
- description: GPU utilization and performance monitoring
  name: Advanced Micro Devices Monitoring API
  slug: advanced-micro-devices-monitoring-api
- description: Performance counters and profiling data
  name: Advanced Micro Devices Performance API
  slug: advanced-micro-devices-performance-api
artifact_total: 92
collections:
- collection_type: postman
  name: AMD Developer Cloud Configuration API
  slug: postman-advanced-micro-devices-configuration-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Credits API
  slug: postman-advanced-micro-devices-credits-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Devices API
  slug: postman-advanced-micro-devices-devices-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Health API
  slug: postman-advanced-micro-devices-health-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Instances API
  slug: postman-advanced-micro-devices-instances-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Models API
  slug: postman-advanced-micro-devices-models-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Monitoring API
  slug: postman-advanced-micro-devices-monitoring-api
- collection_type: postman
  name: AMD Developer Cloud Configuration Performance API
  slug: postman-advanced-micro-devices-performance-api
- collection_type: open
  name: AMD Developer Cloud API
  slug: open-amd-developer-cloud-api
- collection_type: open
  name: AMD ROCm Management API
  slug: open-amd-rocm-management-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/advanced-micro-devices/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/advanced-micro-devices-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advanced-micro-devices-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/advanced-micro-devices-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amd
- group: company
  title: ''
  type: Website
  url: https://www.amd.com
- group: start
  title: ''
  type: Portal
  url: https://developer.amd.com
- group: docs
  title: ''
  type: Documentation
  url: https://rocm.docs.amd.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amd.com/resources/rocm-resources/
- group: operate
  title: ''
  type: Support
  url: https://developer.amd.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.amd.com/en/corporate/blog.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amd.com/en/legal/terms-and-conditions.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amd.com/en/legal/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ROCm
- group: learn
  title: ''
  type: Academy
  url: https://academy.amd.com
- group: start
  title: ''
  type: Signup
  url: https://developer.amd.com/amd-developer-cloud/
created: '2024-01-01'
description: Advanced Micro Devices (AMD) is a global semiconductor company that develops high-performance computing, graphics, and visualization technologies for data centers, gaming, and embedded markets. AMD provides the ROCm open software platform for GPU computing, HIP programming interface, and the AMD Developer Cloud for AI workloads using AMD Instinct GPUs.
examples:
- key_count: 5
  name: Cloud Api Credits Example
  slug: cloud-api-credits-example
- key_count: 8
  name: Cloud Api Instance Example
  slug: cloud-api-instance-example
- key_count: 5
  name: Cloud Api Instanceinput Example
  slug: cloud-api-instanceinput-example
- key_count: 2
  name: Cloud Api Instancelist Example
  slug: cloud-api-instancelist-example
- key_count: 6
  name: Cloud Api Instancemetrics Example
  slug: cloud-api-instancemetrics-example
- key_count: 5
  name: Cloud Api Model Example
  slug: cloud-api-model-example
- key_count: 5
  name: Cloud Api Modelinput Example
  slug: cloud-api-modelinput-example
- key_count: 1
  name: Cloud Api Modellist Example
  slug: cloud-api-modellist-example
- key_count: 8
  name: Rocm Api Device Example
  slug: rocm-api-device-example
- key_count: 6
  name: Rocm Api Devicehealth Example
  slug: rocm-api-devicehealth-example
- key_count: 1
  name: Rocm Api Devicelist Example
  slug: rocm-api-devicelist-example
- key_count: 5
  name: Rocm Api Deviceperformance Example
  slug: rocm-api-deviceperformance-example
- key_count: 2
  name: Rocm Api Errorresponse Example
  slug: rocm-api-errorresponse-example
- key_count: 4
  name: Rocm Api Rocmversion Example
  slug: rocm-api-rocmversion-example
features:
- description: On-demand access to MI300X, MI250, and MI210 GPU instances for AI training, inference, and HPC workloads.
  name: AMD Instinct GPU Instances
- description: Open-source GPU compute platform with HIP programming model, math libraries, and deep learning framework support.
  name: ROCm Software Platform
- description: CUDA-compatible GPU programming interface enabling portable code across AMD and NVIDIA hardware.
  name: HIP Programming Interface
- description: Deploy and serve large language models using vLLM, TGI, and other inference engines on AMD Instinct GPUs.
  name: AI Model Serving
- description: Optimized libraries including rocBLAS, rocFFT, rocRAND, and rocSPARSE for scientific computing and deep learning.
  name: ROCm Math Libraries
- description: RCCL (ROCm Communication Collectives Library) for efficient multi-GPU and multi-node collective operations.
  name: Multi-GPU Communication
- description: Free GPU cloud credits for qualifying researchers, startups, and developers through the AMD AI Developer Program.
  name: AI Developer Cloud Credits
- description: Full compatibility with PyTorch, TensorFlow, JAX, and other ML frameworks via ROCm backend support.
  name: Framework Compatibility
finops:
- name: Advanced Micro Devices Finops
  service_category: Compute / Semiconductors
  slug: advanced-micro-devices-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/advanced-micro-devices.png
integrations:
- description: Full ROCm support for PyTorch including autograd, distributed training, and all major model architectures.
  name: PyTorch
- description: TensorFlow-ROCm integration enabling GPU-accelerated training and inference on AMD hardware.
  name: TensorFlow
- description: AMD Instinct Day-0 support in vLLM for high-performance LLM inference serving.
  name: vLLM
- description: Transformers and Diffusers library compatibility with ROCm for loading and running models from Hugging Face Hub.
  name: Hugging Face
- description: AMD GPU operator for Kubernetes enabling GPU-accelerated containerized workloads on AMD hardware.
  name: Kubernetes
- description: Official ROCm Docker images for containerized GPU computing environments.
  name: Docker
- description: ONNX Runtime ROCm execution provider for cross-framework model deployment on AMD GPUs.
  name: ONNX Runtime
json_schemas:
- name: Credits
  property_count: 5
  slug: cloud-api-credits
- name: InstanceInput
  property_count: 5
  slug: cloud-api-instance-input
- name: InstanceList
  property_count: 2
  slug: cloud-api-instance-list
- name: InstanceMetrics
  property_count: 6
  slug: cloud-api-instance-metrics
- name: Instance
  property_count: 8
  slug: cloud-api-instance
- name: ModelInput
  property_count: 5
  slug: cloud-api-model-input
- name: ModelList
  property_count: 1
  slug: cloud-api-model-list
- name: Model
  property_count: 5
  slug: cloud-api-model
- name: DeviceHealth
  property_count: 6
  slug: rocm-api-device-health
- name: DeviceList
  property_count: 1
  slug: rocm-api-device-list
- name: DevicePerformance
  property_count: 5
  slug: rocm-api-device-performance
- name: Device
  property_count: 8
  slug: rocm-api-device
- name: ErrorResponse
  property_count: 2
  slug: rocm-api-error-response
- name: RocmVersion
  property_count: 4
  slug: rocm-api-rocm-version
json_structures:
- name: Cloud Api Credits Structure
  property_count: 5
  slug: cloud-api-credits-structure
- name: Cloud Api Instance Input Structure
  property_count: 5
  slug: cloud-api-instance-input-structure
- name: Cloud Api Instance List Structure
  property_count: 2
  slug: cloud-api-instance-list-structure
- name: Cloud Api Instance Metrics Structure
  property_count: 6
  slug: cloud-api-instance-metrics-structure
- name: Cloud Api Instance Structure
  property_count: 8
  slug: cloud-api-instance-structure
- name: Cloud Api Model Input Structure
  property_count: 5
  slug: cloud-api-model-input-structure
- name: Cloud Api Model List Structure
  property_count: 1
  slug: cloud-api-model-list-structure
- name: Cloud Api Model Structure
  property_count: 5
  slug: cloud-api-model-structure
- name: Rocm Api Device Health Structure
  property_count: 6
  slug: rocm-api-device-health-structure
- name: Rocm Api Device List Structure
  property_count: 1
  slug: rocm-api-device-list-structure
- name: Rocm Api Device Performance Structure
  property_count: 5
  slug: rocm-api-device-performance-structure
- name: Rocm Api Device Structure
  property_count: 8
  slug: rocm-api-device-structure
- name: Rocm Api Error Response Structure
  property_count: 2
  slug: rocm-api-error-response-structure
- name: Rocm Api Rocm Version Structure
  property_count: 4
  slug: rocm-api-rocm-version-structure
jsonld:
- class_count: 33
  name: Amd Developer Cloud Api Context
  property_count: 2
  slug: amd-developer-cloud-api-context
- class_count: 30
  name: Amd Rocm Management Api Context
  property_count: 0
  slug: amd-rocm-management-api-context
layout: provider
modified: '2026-04-19'
name: Advanced Micro Devices
nav: Providers
network: true
overview: 'Advanced Micro Devices publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Configuration API, Credits API, Devices API, and 5 more. Tagged areas include AI, Cloud Computing, GPU, HPC, and Machine Learning.


  The Advanced Micro Devices catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Advanced Micro Devices'' developer surface includes authentication, developer portal, documentation, getting-started guide, support, engineering blog, academy / training, and 9 more developer resources.'
plans:
- name: Advanced Micro Devices Plans Pricing
  plan_count: 3
  slug: advanced-micro-devices-plans-pricing
press:
- date: '2026-05-25'
  title: AMD and Meta Announce Expanded Strategic Partnership ...
  url: https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus
- date: '2026-05-25'
  title: Press Release dated July 30, 2024
  url: https://www.sec.gov/Archives/edgar/data/2488/000000248824000121/q22024991.htm
- date: '2026-05-25'
  title: AMD Announces “Advancing AI 2025”
  url: https://ir.amd.com/news-events/press-releases/detail/1243/amd-announces-advancing-ai-2025
- date: '2026-05-25'
  title: Advanced Micro Devices has secured massive AI ...
  url: https://www.facebook.com/Neewtoop/posts/advanced-micro-devices-has-secured-massive-ai-infrastructure-deals-with-meta-and/998984876042705/
- date: '2026-05-25'
  title: Advanced Micro Devices, Inc. (AMD) Stock Price, News ...
  url: https://finance.yahoo.com/quote/AMD/
random_paper: 101
rate_limits:
- limit_count: 1
  name: Advanced Micro Devices Rate Limits
  slug: advanced-micro-devices-rate-limits
rules:
- name: Advanced Micro Devices API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: advanced-micro-devices-jsonschema-spectral-rules
- name: Advanced Micro Devices API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: advanced-micro-devices-spectral-rules
- name: Advanced Micro Devices API Rules
  rule_count: 31
  severity_counts:
    error: 16
    hint: 0
    info: 4
    warn: 11
  slug: amd-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.6
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 10.5
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/advanced-micro-devices/refs/heads/main/screenshots/advanced-micro-devices-2026-06-20T165331.png
security:
- kind: authentication
  name: Advanced Micro Devices Authentication
  slug: advanced-micro-devices-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Advanced Micro Devices Domain Security
  slug: advanced-micro-devices-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: advanced-micro-devices
tags:
- AI
- Cloud Computing
- GPU
- HPC
- Machine Learning
- Semiconductor
- Fortune 500
use_cases:
- description: Train and fine-tune large language models on AMD Instinct GPU clusters with ROCm-optimized PyTorch.
  name: Large Language Model Training
- description: Deploy LLM inference endpoints using vLLM on AMD Instinct GPUs for high-throughput token generation.
  name: AI Inference Serving
- description: Run HPC simulations, molecular dynamics, and fluid dynamics workloads on AMD GPU clusters with ROCm.
  name: Scientific Computing
- description: Train and deploy image classification, object detection, and segmentation models using AMD GPU acceleration.
  name: Computer Vision
- description: Accelerate data processing and analytics workloads using GPU-accelerated computing with ROCm.
  name: Data Analytics
- description: Develop and iterate on generative AI applications using AMD Developer Cloud free GPU credits.
  name: Generative AI Development
website: https://www.amd.com
---
