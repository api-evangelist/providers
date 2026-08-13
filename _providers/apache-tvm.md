---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: The TVM Python API provides a comprehensive interface for model compilation, optimization, and deployment. Key modules include tvm.relay for defining and optimizing computational graphs, tvm.auto_sche
  name: Apache TVM Python API
  slug: apache-tvm-python-api
- description: The TVM RPC (Remote Procedure Call) system enables remote compilation, deployment, and profiling of optimized models on target devices. It provides server/client APIs for uploading and executing compi
  name: Apache TVM RPC API
  slug: apache-tvm-rpc-api
artifact_total: 22
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/tvm/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/tvm/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-tvm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-tvm-domain-security.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/tvm
- group: docs
  title: ''
  type: Documentation
  url: https://tvm.apache.org/docs/
- group: start
  title: ''
  type: Portal
  url: https://tvm.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://tvm.apache.org/docs/get_started/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/apache/tvm/releases
- group: operate
  title: ''
  type: Support
  url: https://discuss.tvm.apache.org/
- group: company
  title: ''
  type: Blog
  url: https://tvm.apache.org/rss.xml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2026-03-16'
description: Apache TVM is an open-source compiler framework for deep learning that provides performance portability across diverse hardware backends including CPUs, GPUs, FPGAs, and specialized accelerators (ARM, NVIDIA, AMD, Qualcomm). It automatically optimizes deep learning models from frameworks like TensorFlow, PyTorch, ONNX, MXNet, and Keras for deployment on edge and cloud targets. TVM is an Apache Software Foundation top-level project.
features:
- description: Import models from TensorFlow, PyTorch, ONNX, MXNet, Keras, and other frameworks.
  name: Multi-Framework Support
- description: Automatic operator scheduling and kernel fusion for CPUs, GPUs, and custom accelerators.
  name: Hardware-Specific Optimization
- description: AutoTVM and AutoScheduler for automated hyperparameter optimization of compute kernels.
  name: Auto-Tuning
- description: Deploy optimized models on microcontrollers and bare-metal devices without an OS.
  name: MicroTVM
- description: Bring Your Own Codegen framework for integrating custom hardware accelerators.
  name: BYOC Framework
- description: High-level intermediate representation for end-to-end model optimization.
  name: Relay IR
finops:
- name: Apache Tvm Finops
  service_category: API
  slug: apache-tvm-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-tvm.png
integrations:
- description: Import and optimize ONNX models from any ONNX-compatible ML framework.
  name: ONNX
- description: TorchScript to TVM compilation for PyTorch model optimization.
  name: PyTorch
- description: TensorFlow and TFLite model import and optimization.
  name: TensorFlow
- description: CUDA/cuDNN backend for NVIDIA GPU kernel generation and optimization.
  name: NVIDIA CUDA
- description: ARM CPU (Cortex-A, Cortex-M) and ARM Mali GPU backend support.
  name: ARM
layout: provider
modified: '2026-04-19'
name: Apache TVM
nav: Providers
network: true
overview: 'Apache TVM publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Compiler, Deep Learning, Edge Computing, and Model Optimization.


  Apache TVM''s developer surface includes documentation, developer portal, getting-started guide, release notes, support, engineering blog, and 7 more developer resources.'
plans:
- name: Apache Tvm Plans Pricing
  plan_count: 3
  slug: apache-tvm-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: Apache Tvm Rate Limits
  slug: apache-tvm-rate-limits
score:
  band: emerging
  composite: 21.2
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 21.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-tvm/refs/heads/main/screenshots/apache-tvm-2026-06-20T172156.png
security:
- kind: domain-security
  name: Apache Tvm Domain Security
  slug: apache-tvm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Tvm Vulnerability Disclosure
  slug: apache-tvm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-tvm
tags:
- AI
- Compiler
- Deep Learning
- Edge Computing
- Model Optimization
- Open Source
use_cases:
- description: Deploy optimized deep learning models on edge devices and microcontrollers.
  name: Edge AI Deployment
- description: Optimize inference performance for cloud GPU/CPU model serving.
  name: Model Serving Optimization
- description: Compile a single model for multiple hardware targets from one codebase.
  name: Cross-Platform Deployment
- description: Integrate custom AI accelerators using TVM's BYOC framework.
  name: Custom Accelerator Integration
website: https://tvm.apache.org/
---
