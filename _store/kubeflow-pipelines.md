---
aid: kubeflow-pipelines
url: https://raw.githubusercontent.com/api-evangelist/kubeflow-pipelines/refs/heads/main/apis.yml
apis:
- aid: kubeflow-pipelines:rest-api
  name: Kubeflow Pipelines REST API
  description: REST API for managing ML pipelines, experiments, runs, and artifacts. Provides programmatic access to create, execute, and monitor ML workflows.
  humanURL: https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/
  baseURL: https://your-kubeflow-host/pipeline
  tags:
  - Experiments
  - Pipelines
  - REST API
  properties:
  - type: Documentation
    url: https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/kubeflow/pipelines/master/backend/api/v2beta1/swagger/pipeline_spec.swagger.json
- aid: kubeflow-pipelines:python-sdk
  name: Kubeflow Pipelines Python SDK
  description: Python SDK for building, compiling, and submitting ML pipelines.
  humanURL: https://kubeflow-pipelines.readthedocs.io/
  baseURL: https://pypi.org/project/kfp/
  tags:
  - Python
  - SDK
  properties:
  - type: Documentation
    url: https://kubeflow-pipelines.readthedocs.io/
name: Kubeflow Pipelines
tags:
- Data Science
- Kubernetes
- Machine Learning
- MLOps
- Orchestration
- Pipelines
- Workflows
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers. It provides a way to orchestrate complex ML workflows with dependencies, enabling data scientists and ML engineers to deploy production-ready ML systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

