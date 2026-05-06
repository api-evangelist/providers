---
aid: determined-ai
name: Determined AI
description: Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. Determined allows deep learning engineers to focus on building and training models at scale, without needing to worry about DevOps or writing custom code for common tasks like fault tolerance or experiment tracking. It bridges the gap between tools like TensorFlow and PyTorch for single researchers to the challenges that arise when doing deep learning at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Artificial Intelligence
  - Deep Learning
  - Machine Learning
  - MLOps
url: https://raw.githubusercontent.com/api-evangelist/determined-ai/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: determined-ai:determined-ai-api
    name: Determined AI REST API
    description: Determined helps deep learning teams train models more quickly, easily share GPU resources, and effectively collaborate. The REST API provides programmatic access to manage experiments, models, checkpoints, templates, users, tokens, and cluster resources.
    humanURL: https://docs.determined.ai/latest/rest-api/index.html
    tags:
      - Artificial Intelligence
      - Deep Learning
      - Machine Learning
      - MLOps
    properties:
      - type: Documentation
        url: https://docs.determined.ai/latest/rest-api/index.html
      - type: Getting Started
        url: https://docs.determined.ai/latest/get-started/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/determined-ai/refs/heads/main/openapi/determined-ai-openapi.yml
      - type: Source Code
        url: https://github.com/determined-ai/determined
common:
  - type: Website
    url: https://www.determined.ai/
  - type: Documentation
    url: https://docs.determined.ai/
  - type: GitHub Organization
    url: https://github.com/determined-ai
  - type: License
    url: https://github.com/determined-ai/determined/blob/main/LICENSE
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
