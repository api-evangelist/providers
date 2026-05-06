---
aid: lambda
name: Lambda
description: Lambda gives your team instant access to the compute you need to build and deploy Artificial Intelligence. Lambda Cloud provides on-demand GPU instances powered by NVIDIA A100, H100, and other high-performance GPUs for deep learning training and inference workloads.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Cloud Computing
  - Compute
  - Deep Learning
  - GPU
  - Machine Learning
created: '2025-01-07'
modified: '2026-04-18'
url: https://raw.githubusercontent.com/api-evangelist/lambda/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: lambda:cloud-api
    name: Lambda Cloud API
    description: The Lambda Cloud API allows you to manage GPU cloud instances programmatically. You can launch, list, restart, and terminate instances, manage SSH keys, list available instance types and images, and manage persistent storage file systems through a RESTful interface.
    humanURL: https://docs.lambda.ai/public-cloud/cloud-api/
    baseURL: https://cloud.lambdalabs.com/api/v1
    tags:
      - Cloud
      - Compute
      - File Systems
      - GPU
      - Instances
      - SSH Keys
    properties:
      - type: Documentation
        url: https://docs.lambda.ai/public-cloud/cloud-api/
      - type: OpenAPI
        url: openapi/lambda-cloud-api-openapi.yml
      - type: APIReference
        url: https://cloud.lambdalabs.com/api/v1/docs
    contact:
      - type: Support
        url: https://support.lambdalabs.com/hc/en-us
common:
  - type: Portal
    url: https://lambda.ai/cloud
  - type: Documentation
    url: https://docs.lambda.ai/
  - type: GettingStarted
    url: https://docs.lambda.ai/public-cloud/on-demand/getting-started/
  - type: Authentication
    url: https://cloud.lambdalabs.com/api/v1/docs
  - type: Pricing
    url: https://lambda.ai/pricing
  - type: Blog
    url: https://lambda.ai/blog
  - type: StatusPage
    url: https://status.lambda.ai
  - type: Support
    url: https://support.lambdalabs.com/hc/en-us
  - type: SignUp
    url: https://cloud.lambdalabs.com/sign-up
  - type: SDK
    url: https://pypi.org/project/lambda-cloud-client/
  - type: GitHubOrganization
    url: https://github.com/LambdaLabsML
  - type: Features
    data:
      - On-demand GPU cloud instances (A100, H100)
      - Persistent storage file systems
      - SSH key management
      - Jupyter notebook integration
      - RESTful API with API key authentication
      - Multiple region availability
      - Pre-installed deep learning frameworks
  - type: UseCases
    data:
      - Training large language models and deep learning models
      - Running GPU-accelerated inference workloads
      - Provisioning ephemeral compute for ML experiments
      - Managing persistent datasets across training runs
      - Automating GPU infrastructure with CI/CD pipelines
  - type: Integrations
    data:
      - PyTorch
      - TensorFlow
      - JAX
      - Hugging Face
      - Jupyter Notebooks
      - NVIDIA CUDA
      - Docker
  - type: JSONSchema
    url: json-schema/lambda-cloud-api-schema.json
  - type: JSONLD
    url: json-ld/lambda-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
