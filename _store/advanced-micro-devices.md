---
aid: advanced-micro-devices
url: https://raw.githubusercontent.com/api-evangelist/advanced-micro-devices/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - name: AMD Developer Cloud API
    description: The AMD Developer Cloud API provides access to AMD Instinct GPU instances for AI inference, training, and HPC workloads. Supports managing compute instances, deploying AI models, monitoring GPU utilization, and integrating with ROCm-compatible frameworks including PyTorch, TensorFlow, and vLLM.
    humanURL: https://developer.amd.com
    baseURL: https://api.developer.amd.com/v1
    tags:
      - AI
      - Cloud Computing
      - GPU
      - HPC
      - Instinct
    properties:
      - type: Documentation
        url: https://developer.amd.com
      - type: OpenAPI
        url: openapi/amd-developer-cloud-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/amd-developer-cloud-api-context.jsonld
      - type: SpectralRules
        url: rules/amd-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/developer-cloud-api.yaml
      - type: Vocabulary
        url: vocabulary/advanced-micro-devices-vocabulary.yaml
  - name: AMD ROCm API
    description: The AMD ROCm (Radeon Open Compute) platform provides the runtime and library APIs for GPU-accelerated computing on AMD hardware. Includes HIP (Heterogeneous-compute Interface for Portability), math libraries (rocBLAS, rocFFT, rocRAND), and communication libraries (RCCL) for high-performance computing and AI workloads.
    humanURL: https://rocm.docs.amd.com
    baseURL: https://rocm.docs.amd.com/en/latest
    tags:
      - GPU
      - HPC
      - Machine Learning
      - ROCm
      - SDK
    properties:
      - type: Documentation
        url: https://rocm.docs.amd.com
      - type: OpenAPI
        url: openapi/amd-rocm-management-api-openapi.yml
      - type: JSONSchema
        url: json-schema/
      - type: JSONStructure
        url: json-structure/
      - type: JSONLD
        url: json-ld/amd-rocm-management-api-context.jsonld
      - type: SpectralRules
        url: rules/amd-spectral-rules.yml
      - type: NaftikoCapability
        url: capabilities/ai-gpu-computing.yaml
      - type: Vocabulary
        url: vocabulary/advanced-micro-devices-vocabulary.yaml
common:
  - type: Website
    url: https://www.amd.com
  - type: Portal
    url: https://developer.amd.com
  - type: Documentation
    url: https://rocm.docs.amd.com
  - type: GettingStarted
    url: https://developer.amd.com/resources/rocm-resources/
  - type: Support
    url: https://developer.amd.com/support/
  - type: Blog
    url: https://www.amd.com/en/corporate/blog.html
  - type: TermsOfService
    url: https://www.amd.com/en/legal/terms-and-conditions.html
  - type: PrivacyPolicy
    url: https://www.amd.com/en/legal/privacy.html
  - type: GitHubOrganization
    url: https://github.com/ROCm
  - type: Academy
    url: https://academy.amd.com
  - type: SignUp
    url: https://developer.amd.com/amd-developer-cloud/
  - type: Features
    data:
      - name: AMD Instinct GPU Instances
        description: On-demand access to MI300X, MI250, and MI210 GPU instances for AI training, inference, and HPC workloads.
      - name: ROCm Software Platform
        description: Open-source GPU compute platform with HIP programming model, math libraries, and deep learning framework support.
      - name: HIP Programming Interface
        description: CUDA-compatible GPU programming interface enabling portable code across AMD and NVIDIA hardware.
      - name: AI Model Serving
        description: Deploy and serve large language models using vLLM, TGI, and other inference engines on AMD Instinct GPUs.
      - name: ROCm Math Libraries
        description: Optimized libraries including rocBLAS, rocFFT, rocRAND, and rocSPARSE for scientific computing and deep learning.
      - name: Multi-GPU Communication
        description: RCCL (ROCm Communication Collectives Library) for efficient multi-GPU and multi-node collective operations.
      - name: AI Developer Cloud Credits
        description: Free GPU cloud credits for qualifying researchers, startups, and developers through the AMD AI Developer Program.
      - name: Framework Compatibility
        description: Full compatibility with PyTorch, TensorFlow, JAX, and other ML frameworks via ROCm backend support.
  - type: UseCases
    data:
      - name: Large Language Model Training
        description: Train and fine-tune large language models on AMD Instinct GPU clusters with ROCm-optimized PyTorch.
      - name: AI Inference Serving
        description: Deploy LLM inference endpoints using vLLM on AMD Instinct GPUs for high-throughput token generation.
      - name: Scientific Computing
        description: Run HPC simulations, molecular dynamics, and fluid dynamics workloads on AMD GPU clusters with ROCm.
      - name: Computer Vision
        description: Train and deploy image classification, object detection, and segmentation models using AMD GPU acceleration.
      - name: Data Analytics
        description: Accelerate data processing and analytics workloads using GPU-accelerated computing with ROCm.
      - name: Generative AI Development
        description: Develop and iterate on generative AI applications using AMD Developer Cloud free GPU credits.
  - type: Integrations
    data:
      - name: PyTorch
        description: Full ROCm support for PyTorch including autograd, distributed training, and all major model architectures.
      - name: TensorFlow
        description: TensorFlow-ROCm integration enabling GPU-accelerated training and inference on AMD hardware.
      - name: vLLM
        description: AMD Instinct Day-0 support in vLLM for high-performance LLM inference serving.
      - name: Hugging Face
        description: Transformers and Diffusers library compatibility with ROCm for loading and running models from Hugging Face Hub.
      - name: Kubernetes
        description: AMD GPU operator for Kubernetes enabling GPU-accelerated containerized workloads on AMD hardware.
      - name: Docker
        description: Official ROCm Docker images for containerized GPU computing environments.
      - name: ONNX Runtime
        description: ONNX Runtime ROCm execution provider for cross-framework model deployment on AMD GPUs.
description: Advanced Micro Devices (AMD) is a global semiconductor company that develops high-performance computing, graphics, and visualization technologies for data centers, gaming, and embedded markets. AMD provides the ROCm open software platform for GPU computing, HIP programming interface, and the AMD Developer Cloud for AI workloads using AMD Instinct GPUs.
name: Advanced Micro Devices
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
created: '2024-01-01'
specificationVersion: '0.19'
tags:
  - AI
  - Cloud Computing
  - GPU
  - HPC
  - Machine Learning
  - Semiconductor
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
