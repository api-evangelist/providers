---
aid: kserve
name: KServe
description: KServe is a standard model inference platform on Kubernetes, built for highly scalable use cases. It provides performant, standardized inference protocol across ML frameworks including TensorFlow, PyTorch, scikit-learn, XGBoost, and more.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Inference
  - Kubernetes
  - Machine Learning
  - MLOps
  - Model Serving
url: https://raw.githubusercontent.com/api-evangelist/kserve/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kserve:inference-api
    name: KServe Inference API
    description: KServe's standardized model inference protocol for serving predictions across multiple ML frameworks on Kubernetes.
    humanURL: https://kserve.github.io/website/
    tags:
      - Inference
      - Model Serving
    properties:
      - type: Documentation
        url: https://kserve.github.io/website/latest/get_started/
      - type: Reference
        url: https://kserve.github.io/website/latest/reference/api/
common:
  - type: Website
    url: https://kserve.github.io/website/
  - type: Documentation
    url: https://kserve.github.io/website/latest/
  - type: Getting Started
    url: https://kserve.github.io/website/latest/get_started/
  - type: GitHub Organization
    url: https://github.com/kserve/kserve
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
