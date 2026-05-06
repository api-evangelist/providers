---
aid: kubeflow-pipelines
name: Kubeflow Pipelines
description: Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers. It provides a way to orchestrate complex ML workflows with dependencies, enabling data scientists and ML engineers to deploy production-ready ML systems on Kubernetes.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Science
  - Kubernetes
  - Machine Learning
  - MLOps
  - Orchestration
  - Pipelines
  - Workflows
url: https://raw.githubusercontent.com/api-evangelist/kubeflow-pipelines/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kubeflow-pipelines:rest-api
    name: Kubeflow Pipelines REST API
    description: REST API for managing ML pipelines, experiments, runs, and artifacts. Provides programmatic access to create, execute, and monitor ML workflows on a Kubeflow Pipelines deployment.
    humanURL: https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/
    baseURL: https://your-kubeflow-host/pipeline
    tags:
      - Experiments
      - Pipelines
      - REST API
      - Runs
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/pipelines/reference/api/kubeflow-pipeline-api-spec/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kubeflow/pipelines/master/backend/api/v2beta1/swagger/pipeline.swagger.json
  - aid: kubeflow-pipelines:python-sdk
    name: Kubeflow Pipelines Python SDK
    description: Python SDK for building, compiling, and submitting ML pipelines. Provides decorators and utilities to define pipeline components and workflows using Python.
    humanURL: https://kubeflow-pipelines.readthedocs.io/
    baseURL: https://pypi.org/project/kfp/
    tags:
      - Client Library
      - DSL
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://kubeflow-pipelines.readthedocs.io/
      - type: GitHubRepository
        url: https://github.com/kubeflow/pipelines/tree/master/sdk/python
      - type: Examples
        url: https://github.com/kubeflow/pipelines/tree/master/samples
  - aid: kubeflow-pipelines:go-client
    name: Kubeflow Pipelines Go Client
    description: Go client library for interacting with the Kubeflow Pipelines API programmatically from Go applications.
    humanURL: https://github.com/kubeflow/pipelines/tree/master/backend/api/go_client
    tags:
      - Client Library
      - Go
      - SDK
    properties:
      - type: Documentation
        url: https://pkg.go.dev/github.com/kubeflow/pipelines/backend/api/go_client
      - type: GitHubRepository
        url: https://github.com/kubeflow/pipelines/tree/master/backend/api/go_client
  - aid: kubeflow-pipelines:metadata-api
    name: Kubeflow Pipelines Metadata API
    description: API for tracking and managing metadata about ML artifacts, executions, and lineage information throughout the ML pipeline lifecycle, backed by ML Metadata (MLMD).
    humanURL: https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/
    tags:
      - Artifacts
      - Lineage
      - Metadata
      - ML Metadata
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/
      - type: GitHubRepository
        url: https://github.com/google/ml-metadata
common:
  - type: Website
    url: https://www.kubeflow.org/docs/components/pipelines/
  - type: Documentation
    url: https://www.kubeflow.org/docs/components/pipelines/
  - type: Getting Started
    url: https://www.kubeflow.org/docs/components/pipelines/getting-started/
  - type: GitHubOrg
    url: https://github.com/kubeflow
  - type: GitHubRepository
    url: https://github.com/kubeflow/pipelines
  - type: Blog
    url: https://blog.kubeflow.org/
  - type: Community
    url: https://www.kubeflow.org/docs/about/community/
  - type: Change Log
    url: https://github.com/kubeflow/pipelines/releases
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
