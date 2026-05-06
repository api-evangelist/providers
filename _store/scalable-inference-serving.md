---
name: Scalable Inference Serving
description: A collection of APIs, frameworks, and platforms for scalable machine learning model inference serving, deployment, and management. This includes the KServe Open Inference Protocol (the CNCF standard for model serving on Kubernetes), BentoML (developer packaging and serving), vLLM (high-throughput LLM inference), NVIDIA Triton Inference Server, and supporting observability and registry tools. KServe recently joined CNCF as an incubating project (November 2025).
image: https://kserve.github.io/website/images/KServe.png
url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - AI
  - CNCF
  - Deployment
  - Inference
  - Kubernetes
  - LLM
  - Machine Learning
  - Model Serving
  - MLOps
  - Scalability
apis:
  - name: KServe Open Inference Protocol API
    description: KServe implements the Open Inference Protocol (OIP), also known as the KServe V2 Inference Protocol, which provides a standardized REST and gRPC interface for model inference across frameworks. KServe is a standardized distributed generative and predictive AI inference platform for scalable, multi-framework deployment on Kubernetes. CNCF incubating project since November 2025. Supports TensorFlow, PyTorch, scikit-learn, XGBoost, ONNX, vLLM, and HuggingFace.
    image: https://kserve.github.io/website/images/KServe.png
    humanUrl: https://kserve.github.io/website/
    baseUrl: https://inference.kserve.example.com
    tags:
      - CNCF
      - Inference
      - Kubernetes
      - Model Serving
      - Open Inference Protocol
      - Open Source
    properties:
      - type: Documentation
        url: https://kserve.github.io/website/docs/intro
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/openapi/kserve-open-inference-protocol-openapi.yml
      - type: GitHub
        url: https://github.com/kserve/kserve
      - type: Changelog
        url: https://github.com/kserve/kserve/releases
      - type: Getting Started
        url: https://kserve.github.io/website/docs/get_started/
      - type: SwaggerUI
        url: https://kserve.github.io/website/latest/reference/swagger-ui/
    contact:
      - type: Slack
        url: https://kubernetes.slack.com/archives/CH6E58LNP
      - type: GitHub Issues
        url: https://github.com/kserve/kserve/issues
  - name: BentoML REST API
    description: BentoML is an open-source unified inference platform for deploying and scaling AI models. It auto-generates RESTful APIs from Python service definitions, provides built-in OpenAPI/Swagger documentation, supports adaptive batching, and integrates with KServe for Kubernetes deployment. BentoML 1.0 introduced the Runner abstraction for parallelizing inference workloads with adaptive batching and independent scaling of pre/post-processing from model inference.
    image: https://www.bentoml.com/favicon.ico
    humanUrl: https://www.bentoml.com/
    baseUrl: https://api.bentoml.example.com
    tags:
      - Batching
      - Inference
      - Model Serving
      - Open Source
      - Python
      - REST API
    properties:
      - type: Documentation
        url: https://docs.bentoml.com/en/latest/
      - type: GitHub
        url: https://github.com/bentoml/BentoML
      - type: Getting Started
        url: https://docs.bentoml.com/en/latest/get-started/quickstart.html
      - type: Pricing
        url: https://www.bentoml.com/pricing
      - type: API Reference
        url: https://docs.bentoml.com/en/latest/reference/index.html
    contact:
      - type: Community
        url: https://l.bentoml.com/join-slack
      - type: GitHub Issues
        url: https://github.com/bentoml/BentoML/issues
  - name: vLLM OpenAI-Compatible API
    description: vLLM is a high-throughput and memory-efficient inference engine for LLMs, implementing PagedAttention for efficient KV cache management. vLLM exposes an OpenAI-compatible REST API allowing seamless migration from OpenAI endpoints. In 2026, vLLM integrates with KServe via LLMInferenceService and llm-d for production-grade distributed LLM inference. Powers major LLM deployments at scale.
    image: https://docs.vllm.ai/en/stable/_static/logo/vllm-logo-text-light.png
    humanUrl: https://docs.vllm.ai/
    baseUrl: https://vllm.example.com/v1
    tags:
      - GPU
      - Inference
      - KV Cache
      - LLM
      - Model Serving
      - Open Source
      - OpenAI-Compatible
    properties:
      - type: Documentation
        url: https://docs.vllm.ai/en/stable/
      - type: GitHub
        url: https://github.com/vllm-project/vllm
      - type: API Reference
        url: https://docs.vllm.ai/en/stable/serving/openai_compatible_server.html
      - type: Changelog
        url: https://github.com/vllm-project/vllm/releases
    contact:
      - type: GitHub Issues
        url: https://github.com/vllm-project/vllm/issues
      - type: Slack
        url: https://vllm-dev.slack.com/
  - name: NVIDIA Triton Inference Server HTTP API
    description: NVIDIA Triton Inference Server is an open-source inference serving software that implements the KServe Open Inference Protocol (V2). Supports TensorRT, ONNX, TensorFlow, PyTorch, and Python backends. Provides dynamic batching, model ensembles, model analyzers, and GPU/CPU inference. Used extensively in production ML pipelines requiring maximum throughput.
    image: https://developer.nvidia.com/favicon.ico
    humanUrl: https://developer.nvidia.com/triton-inference-server
    baseUrl: https://triton.example.com
    tags:
      - GPU
      - Inference
      - Model Serving
      - NVIDIA
      - Open Source
      - TensorRT
      - Triton
    properties:
      - type: Documentation
        url: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/
      - type: GitHub
        url: https://github.com/triton-inference-server/server
      - type: Getting Started
        url: https://github.com/triton-inference-server/tutorials
      - type: API Reference
        url: https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/customization_guide/inference_protocols.html
    contact:
      - type: GitHub Issues
        url: https://github.com/triton-inference-server/server/issues
      - type: Forums
        url: https://forums.developer.nvidia.com/c/ai-data-science/deep-learning/triton-inference-server/
  - name: MLflow Model Registry REST API
    description: MLflow is an open source platform for managing the ML lifecycle, including experiment tracking, reproducibility, and deployment. The MLflow REST API manages experiments, runs, metrics, parameters, artifacts, and the Model Registry for versioning and staging model deployments. CNCF-adjacent; used with KServe for model lifecycle management.
    image: https://mlflow.org/favicon.ico
    humanUrl: https://mlflow.org/
    baseUrl: https://mlflow.example.com/api/2.0
    tags:
      - Experiment Tracking
      - Machine Learning
      - Model Registry
      - MLOps
      - Open Source
      - Versioning
    properties:
      - type: Documentation
        url: https://mlflow.org/docs/latest/rest-api.html
      - type: GitHub
        url: https://github.com/mlflow/mlflow
      - type: Getting Started
        url: https://mlflow.org/docs/latest/getting-started/intro-quickstart/
      - type: API Reference
        url: https://mlflow.org/docs/latest/rest-api.html
    contact:
      - type: Community
        url: https://github.com/mlflow/mlflow/discussions
      - type: GitHub Issues
        url: https://github.com/mlflow/mlflow/issues
  - name: Ray Serve REST API
    description: Ray Serve is a scalable model serving library built on Ray, designed for building online inference APIs. Supports composable deployments, autoscaling, HTTP ingress, gRPC, WebSockets, and request batching. Integrates with any ML framework. The Ray Serve dashboard and REST API manage deployments, replicas, routes, and application status.
    image: https://www.ray.io/favicon.ico
    humanUrl: https://docs.ray.io/en/latest/serve/index.html
    baseUrl: https://ray-serve.example.com
    tags:
      - Autoscaling
      - Inference
      - Machine Learning
      - Model Serving
      - Open Source
      - Python
      - Ray
    properties:
      - type: Documentation
        url: https://docs.ray.io/en/latest/serve/index.html
      - type: GitHub
        url: https://github.com/ray-project/ray
      - type: Getting Started
        url: https://docs.ray.io/en/latest/serve/getting_started.html
      - type: API Reference
        url: https://docs.ray.io/en/latest/serve/api/index.html
    contact:
      - type: Community
        url: https://discuss.ray.io/
      - type: GitHub Issues
        url: https://github.com/ray-project/ray/issues
common:
  - type: Authentication
    url: https://kserve.github.io/website/docs/intro
  - type: Getting Started
    url: https://kserve.github.io/website/docs/get_started/
  - type: GitHub Organization
    url: https://github.com/kserve
  - type: CNCF Landscape
    url: https://landscape.cncf.io/card-mode?project=incubating
  - type: Blog
    url: https://kserve.github.io/website/blog/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/openapi/kserve-open-inference-protocol-openapi.yml
  - type: SpectralRuleset
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/rules/kserve-open-inference-protocol-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/capabilities/model-inference-operations.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/json-schema/kserve-inference-request-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/json-schema/kserve-model-metadata-schema.json
  - type: JSONLd
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/json-ld/scalable-inference-serving-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scalable-inference-serving/main/vocabulary/scalable-inference-serving-vocabulary.yml
maintainers:
  - name: API Evangelist
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
