---
name: Hugging Face
description: The AI community building the future with open-source machine learning models, datasets, and applications.
image: https://huggingface.co/front/assets/huggingface_logo.svg
url: https://huggingface.co
created: '2024'
modified: '2026-04-18'
specificationVersion: '0.18'
apis:
  - name: Hugging Face Inference API
    description: Run inference on 200,000+ machine learning models with a simple HTTP request.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/api-inference/index
    baseURL: https://api-inference.huggingface.co
    tags:
      - AI
      - Inference
      - Machine Learning
      - Models
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/api-inference/index
      - type: OpenAPI
        url: https://huggingface.co/api-inference/openapi.json
      - type: OpenAPI
        url: openapi/hugging-face-inference-api.yml
      - type: Authentication
        url: https://huggingface.co/docs/api-inference/quicktour#authentication
      - type: GettingStarted
        url: https://huggingface.co/docs/api-inference/quicktour
      - type: RateLimits
        url: https://huggingface.co/docs/api-inference/en/rate-limits
      - type: FAQ
        url: https://huggingface.co/docs/api-inference/faq
    contact:
      - type: Support
        url: https://huggingface.co/support
  - name: Hugging Face Hub API
    description: Programmatically interact with the Hugging Face Hub - manage models, datasets, and spaces.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/hub/api
    baseURL: https://huggingface.co/api
    tags:
      - Datasets
      - Hub
      - Models
      - Repository Management
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/hub/api
      - type: OpenAPI
        url: https://huggingface.co/.well-known/openapi.json
      - type: OpenAPI
        url: openapi/hugging-face-hub-api.yml
      - type: SDK
        url: https://huggingface.co/docs/huggingface_hub/index
      - type: SDK
        url: https://huggingface.co/docs/huggingface.js/hub/README
      - type: Authentication
        url: https://huggingface.co/docs/hub/security-tokens
      - type: RateLimits
        url: https://huggingface.co/docs/hub/en/rate-limits
    contact:
      - type: Support
        url: https://huggingface.co/support
  - name: Hugging Face Inference Endpoints API
    description: Deploy and scale machine learning models with dedicated, secure infrastructure.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/inference-endpoints/index
    baseURL: https://api.endpoints.huggingface.cloud
    tags:
      - Deployment
      - Enterprise
      - Inference
      - Managed Service
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/inference-endpoints/api_reference
      - type: OpenAPI
        url: openapi/hugging-face-inference-endpoints-api.yml
      - type: GettingStarted
        url: https://huggingface.co/docs/inference-endpoints/index
      - type: Pricing
        url: https://huggingface.co/pricing#inference-endpoints
      - type: Authentication
        url: https://huggingface.co/docs/hub/security-tokens
    contact:
      - type: Support
        url: https://huggingface.co/support
  - name: Hugging Face Inference Providers API
    description: Unified proxy layer providing access to 15+ inference partners through a single OpenAI-compatible endpoint.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/inference-providers/en/index
    baseURL: https://router.huggingface.co/v1
    tags:
      - AI
      - Inference
      - OpenAI Compatible
      - Providers
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/inference-providers/en/index
      - type: OpenAPI
        url: openapi/hugging-face-inference-providers-api.yml
      - type: APIReference
        url: https://huggingface.co/docs/inference-providers/en/tasks/index
      - type: GettingStarted
        url: https://huggingface.co/docs/inference-providers/en/guides/first-api-call
      - type: Pricing
        url: https://huggingface.co/docs/inference-providers/pricing
      - type: Models
        url: https://huggingface.co/inference/models
    contact:
      - type: Support
        url: https://huggingface.co/support
  - name: Hugging Face Dataset Viewer API
    description: Query and visualize datasets stored on the Hugging Face Hub through a lightweight REST API.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/dataset-viewer/index
    baseURL: https://datasets-server.huggingface.co
    tags:
      - Data
      - Datasets
      - Viewer
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/dataset-viewer/index
      - type: OpenAPI
        url: https://datasets-server.huggingface.co/openapi.json
      - type: OpenAPI
        url: openapi/hugging-face-dataset-viewer-api.yml
      - type: GettingStarted
        url: https://huggingface.co/docs/dataset-viewer/en/quick_start
      - type: GitHubRepository
        url: https://github.com/huggingface/dataset-viewer
    contact:
      - type: Support
        url: https://huggingface.co/support
  - name: Hugging Face Text Generation Inference API
    description: High-performance toolkit for deploying and serving large language models with optimized inference.
    image: https://huggingface.co/front/assets/huggingface_logo.svg
    humanURL: https://huggingface.co/docs/text-generation-inference/en/index
    baseURL: https://api-inference.huggingface.co
    tags:
      - AI
      - Inference
      - LLM
      - Text Generation
    properties:
      - type: Documentation
        url: https://huggingface.co/docs/text-generation-inference/en/index
      - type: OpenAPI
        url: openapi/hugging-face-text-generation-inference-api.yml
      - type: APIReference
        url: https://huggingface.co/docs/text-generation-inference/en/reference/api_reference
      - type: GettingStarted
        url: https://huggingface.co/docs/text-generation-inference/quicktour
      - type: Documentation
        url: https://huggingface.co/docs/text-generation-inference/en/messages_api
      - type: GitHubRepository
        url: https://github.com/huggingface/text-generation-inference
    contact:
      - type: Support
        url: https://huggingface.co/support
common:
  - type: Portal
    url: https://huggingface.co
  - type: Documentation
    url: https://huggingface.co/docs
  - type: GettingStarted
    url: https://huggingface.co/inference/get-started
  - type: Pricing
    url: https://huggingface.co/pricing
  - type: Blog
    url: https://huggingface.co/blog
  - type: ChangeLog
    url: https://huggingface.co/changelog
  - type: SignUp
    url: https://huggingface.co/signup
  - type: Login
    url: https://huggingface.co/login
  - type: Support
    url: https://huggingface.co/support
  - type: Contact
    url: https://huggingface.co/contact/sales
  - type: Support
    url: https://discuss.huggingface.co
  - type: GitHubOrganization
    url: https://github.com/huggingface
  - type: X
    url: https://twitter.com/huggingface
  - type: LinkedIn
    url: https://www.linkedin.com/company/huggingface
  - type: Support
    url: https://huggingface.co/join/discord
  - type: YouTube
    url: https://www.youtube.com/@HuggingFace
  - type: StatusPage
    url: https://status.huggingface.co
  - type: TermsOfService
    url: https://huggingface.co/terms-of-service
  - type: PrivacyPolicy
    url: https://huggingface.co/privacy
  - type: SDK
    url: https://huggingface.co/docs/huggingface_hub/index
  - type: SDK
    url: https://huggingface.co/docs/huggingface.js/en/index
  - type: Features
    data:
      - name: Model Inference
        description: Run inference on 200,000+ ML models with a simple HTTP request across NLP, vision, audio, and multimodal tasks.
      - name: Hub Repository Management
        description: Programmatically manage models, datasets, and spaces including creation, versioning, and access control.
      - name: Dedicated Endpoints
        description: Deploy models on dedicated infrastructure with autoscaling, custom hardware, and private networking.
      - name: Multi-Provider Routing
        description: Unified OpenAI-compatible API routing to 15+ inference providers with automatic model selection.
      - name: Dataset Exploration
        description: Query, search, filter, and visualize datasets without downloading via the Dataset Viewer API.
      - name: Text Generation Inference
        description: High-performance LLM serving with streaming, tool calling, structured output, and grammar constraints.
      - name: OpenAI Compatibility
        description: Drop-in replacement for OpenAI API with chat completions, embeddings, and image generation endpoints.
  - type: UseCases
    data:
      - name: ML Model Prototyping
        description: Rapidly prototype AI applications by running inference on pre-trained models without infrastructure setup.
      - name: Production ML Deployment
        description: Deploy and scale ML models for production workloads with dedicated endpoints and autoscaling.
      - name: Dataset Curation
        description: Explore, validate, and curate ML datasets programmatically for training pipeline automation.
      - name: AI Application Development
        description: Build AI-powered applications using unified inference APIs with multi-provider routing.
      - name: Model Benchmarking
        description: Compare model performance across providers and hardware configurations for optimization.
  - type: Integrations
    data:
      - name: AWS
        description: Deploy inference endpoints on AWS with SageMaker integration and GPU instances.
      - name: Google Cloud
        description: Route inference to Google Cloud TPUs and GPUs through the providers API.
      - name: Azure
        description: Deploy models on Azure infrastructure with managed endpoint support.
      - name: LangChain
        description: Use Hugging Face models as LangChain LLM and embedding providers.
      - name: Gradio
        description: Build interactive ML demos with Gradio and deploy as Hugging Face Spaces.
  - type: JSONSchema
    url: json-schema/hugging-face-model-schema.json
  - type: JSONSchema
    url: json-schema/hugging-face-dataset-schema.json
  - type: JSONSchema
    url: json-schema/hugging-face-space-schema.json
  - type: JSONSchema
    url: json-schema/hugging-face-inference-endpoint-schema.json
  - type: JSONSchema
    url: json-schema/hugging-face-user-schema.json
  - type: JSONLD
    url: json-ld/hugging-face-context.jsonld
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
