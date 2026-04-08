---
aid: kubeflow
url: https://raw.githubusercontent.com/api-evangelist/kubeflow/refs/heads/main/apis.yml
apis:
- aid: kubeflow:pipelines-api
  name: Kubeflow Pipelines API
  description: REST API for creating, managing, and executing machine learning pipelines on Kubernetes.
  humanURL: https://www.kubeflow.org/docs/components/pipelines/
  baseURL: https://your-kubeflow-instance/pipeline
  tags:
  - Machine Learning
  - Pipelines
  - Workflows
  properties:
  - type: Documentation
    url: https://www.kubeflow.org/docs/components/pipelines/v2/reference/api/kubeflow-pipeline-api-spec/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/kubeflow/pipelines/master/backend/api/v2beta1/swagger/pipeline.swagger.json
- aid: kubeflow:notebooks-api
  name: Kubeflow Notebooks API
  description: API for managing Jupyter notebook instances in Kubeflow.
  humanURL: https://www.kubeflow.org/docs/components/notebooks/
  tags:
  - Jupyter
  - Notebooks
  properties:
  - type: Documentation
    url: https://www.kubeflow.org/docs/components/notebooks/
name: Kubeflow
tags:
- AI
- Deep Learning
- Kubernetes
- Machine Learning
- MLOps
- Model Serving
- Model Training
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kubeflow is an open-source machine learning platform for Kubernetes, designed to make deployments of ML workflows on Kubernetes simple, portable, and scalable. It provides tools for training, serving, and managing ML models.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

