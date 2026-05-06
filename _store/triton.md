---
name: Triton Inference Server
description: NVIDIA Triton Inference Server provides a cloud and edge inferencing solution optimized for both CPUs and GPUs. Triton supports an HTTP/REST and gRPC protocol that allows remote clients to request inferencing for any model being managed by the server. Open source and part of the broader NVIDIA AI ecosystem, Triton implements the KServe V2 inference protocol supporting TensorRT, TensorFlow, PyTorch, ONNX Runtime, Python, and more backends.
image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
tags:
  - AI
  - Deep Learning
  - Inference
  - Machine Learning
  - Model Serving
  - NVIDIA
  - Open Source
created: '2024-01-15'
modified: '2026-05-03'
url: https://github.com/triton-inference-server/server
specificationVersion: '0.18'
apis:
  - name: Triton HTTP/REST API
    description: RESTful API implementing the KServe V2 inference protocol for model inference, health checks, metadata queries, model repository management, statistics, tracing, and logging.
    image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
    humanURL: https://github.com/triton-inference-server/server/blob/main/docs/protocol/extension_binary_data.md
    baseURL: http://localhost:8000
    tags:
      - HTTP
      - Inference
      - Model Management
      - REST
      - KServe
    properties:
      - type: Documentation
        url: https://github.com/triton-inference-server/server/blob/main/docs/protocol/extension_binary_data.md
      - type: OpenAPI
        url: https://github.com/triton-inference-server/server/blob/main/docs/protocol/rest_api.yaml
      - type: Postman Collection
        url: https://www.postman.com/nvidia-triton
      - type: OpenAPI
        url: openapi/triton-http-rest-openapi.yml
    contact:
      - FN: NVIDIA Triton Team
        email: triton@nvidia.com
  - name: Triton GRPC API
    description: High-performance gRPC API for model inference with support for streaming and binary tensor data.
    image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
    humanURL: https://github.com/triton-inference-server/server/blob/main/docs/protocol/README.md
    baseURL: grpc://localhost:8001
    tags:
      - GRPC
      - High Performance
      - Inference
      - Streaming
    properties:
      - type: Documentation
        url: https://github.com/triton-inference-server/server/blob/main/docs/protocol/README.md
      - type: Protocol Buffers
        url: https://github.com/triton-inference-server/common/blob/main/protobuf/grpc_service.proto
      - type: Examples
        url: https://github.com/triton-inference-server/client/tree/main/src/python/examples
    contact:
      - FN: NVIDIA Triton Team
        email: triton@nvidia.com
  - name: Triton Metrics API
    description: Prometheus-compatible metrics API for monitoring server and model performance including inference request counts, latencies, GPU utilization, and memory usage.
    image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
    humanURL: https://github.com/triton-inference-server/server/blob/main/docs/user_guide/metrics.md
    baseURL: http://localhost:8002/metrics
    tags:
      - Metrics
      - Monitoring
      - Observability
      - Prometheus
    properties:
      - type: Documentation
        url: https://github.com/triton-inference-server/server/blob/main/docs/user_guide/metrics.md
      - type: Metrics Format
        url: https://prometheus.io/docs/instrumenting/exposition_formats/
      - type: OpenAPI
        url: openapi/triton-metrics-openapi.yml
    contact:
      - FN: NVIDIA Triton Team
        email: triton@nvidia.com
common:
  - type: GitHub Repository
    url: https://github.com/triton-inference-server/server
  - type: Documentation
    url: https://docs.nvidia.com/deeplearning/triton-inference-server/
  - type: Getting Started
    url: https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md
  - type: Client Libraries
    url: https://github.com/triton-inference-server/client
  - type: Model Repository
    url: https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md
  - type: Supported Backends
    url: https://github.com/triton-inference-server/backend
  - type: Docker Images
    url: https://catalog.ngc.nvidia.com/orgs/nvidia/containers/tritonserver
  - type: Community Forum
    url: https://github.com/triton-inference-server/server/discussions
  - type: Release Notes
    url: https://github.com/triton-inference-server/server/releases
  - type: PyTriton
    url: https://github.com/triton-inference-server/pytriton
  - type: Model Analyzer
    url: https://github.com/triton-inference-server/model_analyzer
  - type: Triton CLI
    url: https://github.com/triton-inference-server/triton_cli
  - type: OpenAPI
    url: openapi/triton-http-rest-openapi.yml
  - type: OpenAPI
    url: openapi/triton-metrics-openapi.yml
  - type: JSON-LD
    url: json-ld/triton-context.jsonld
  - type: JSONSchema
    url: json-schema/triton-model-schema.json
  - type: JSONSchema
    url: json-schema/triton-inference-request-schema.json
  - type: JSONSchema
    url: json-schema/triton-inference-response-schema.json
  - type: JSON Structure
    url: json-structure/triton-model-structure.json
  - type: Spectral Rules
    url: rules/triton-rules.yml
  - type: Naftiko Capability
    url: capabilities/model-inference.yaml
  - type: Vocabulary
    url: vocabulary/triton-vocabulary.yml
  - type: x-profiled
    url: 2026-05
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
