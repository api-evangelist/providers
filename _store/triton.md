---
aid: triton
url: https://raw.githubusercontent.com/api-evangelist/triton/refs/heads/main/apis.yml
apis:
- name: Triton HTTP/REST API
  description: RESTful API for model inference, health checks, metadata queries, and server management.
  image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
  humanURL: https://github.com/triton-inference-server/server/blob/main/docs/protocol/extension_binary_data.md
  baseURL: http://localhost:8000
  tags:
  - HTTP
  - Inference
  - Model Management
  - REST
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
  description: High-performance GRPC API for model inference with support for streaming and binary tensor data.
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
  description: Prometheus-compatible metrics API for monitoring server and model performance.
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
name: Triton Inference Server
tags:
- AI
- Deep Learning
- Inference
- Machine Learning
- Model Serving
type: Contract
image: https://developer.nvidia.com/sites/default/files/akamai/triton-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: NVIDIA Triton Inference Server provides a cloud and edge inferencing solution optimized for both CPUs and GPUs. Triton supports an HTTP/REST and GRPC protocol that allows remote clients to request inferencing for any model being managed by the server.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

