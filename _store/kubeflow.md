---
aid: kubeflow
name: Kubeflow
description: Kubeflow is an open-source machine learning platform for Kubernetes, designed to make deployments of ML workflows on Kubernetes simple, portable, and scalable. It provides tools for training, serving, tuning, and managing ML models across the full lifecycle.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Deep Learning
  - Kubernetes
  - Machine Learning
  - MLOps
  - Model Serving
  - Model Training
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/kubeflow/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kubeflow:pipelines-api
    name: Kubeflow Pipelines API
    description: REST API for creating, managing, and executing machine learning pipelines on Kubernetes, including experiments, runs, and artifacts.
    humanURL: https://www.kubeflow.org/docs/components/pipelines/
    baseURL: https://your-kubeflow-instance/pipeline
    tags:
      - Machine Learning
      - MLOps
      - Pipelines
      - Workflows
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/pipelines/v2/reference/api/kubeflow-pipeline-api-spec/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kubeflow/pipelines/master/backend/api/v2beta1/swagger/pipeline.swagger.json
      - type: GitHubRepository
        url: https://github.com/kubeflow/pipelines
  - aid: kubeflow:metadata-api
    name: Kubeflow Metadata API
    description: API for tracking and managing metadata, artifacts, and lineage for ML workflows running on Kubeflow.
    humanURL: https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/
    tags:
      - Artifacts
      - Metadata
      - ML Tracking
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/
      - type: GitHubRepository
        url: https://github.com/google/ml-metadata
  - aid: kubeflow:kserve-api
    name: KServe Inference API
    description: KServe (formerly KFServing) provides a serverless model inference API on Kubernetes, supporting standardized prediction protocols, autoscaling, and multi-framework model serving.
    humanURL: https://kserve.github.io/website/
    tags:
      - Inference
      - Model Serving
      - Predictions
      - Serverless
    properties:
      - type: Documentation
        url: https://kserve.github.io/website/modelserving/v1beta1/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/kserve/kserve/master/docs/predict-api/v2/rest_predict_v2.yaml
      - type: GitHubRepository
        url: https://github.com/kserve/kserve
  - aid: kubeflow:katib-api
    name: Katib API
    description: Katib is the Kubeflow component for hyperparameter tuning, neural architecture search, and AutoML, exposing a Kubernetes-native API for defining and running tuning experiments.
    humanURL: https://www.kubeflow.org/docs/components/katib/
    tags:
      - AutoML
      - Hyperparameter Tuning
      - Neural Architecture Search
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/katib/reference/
      - type: GitHubRepository
        url: https://github.com/kubeflow/katib
  - aid: kubeflow:notebooks-api
    name: Kubeflow Notebooks API
    description: API for managing Jupyter notebook server instances within a Kubeflow cluster, providing isolated, browser-based development environments.
    humanURL: https://www.kubeflow.org/docs/components/notebooks/
    tags:
      - Development Environment
      - Jupyter
      - Notebooks
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/notebooks/
      - type: GitHubRepository
        url: https://github.com/kubeflow/kubeflow/tree/master/components/notebook-controller
  - aid: kubeflow:central-dashboard
    name: Kubeflow Central Dashboard API
    description: API supporting the Kubeflow central dashboard and UI components, which provide a unified interface to all installed Kubeflow components.
    humanURL: https://www.kubeflow.org/docs/components/central-dash/
    tags:
      - Dashboard
      - Management
      - UI
    properties:
      - type: Documentation
        url: https://www.kubeflow.org/docs/components/central-dash/
      - type: GitHubRepository
        url: https://github.com/kubeflow/kubeflow/tree/master/components/centraldashboard
common:
  - type: Website
    url: https://www.kubeflow.org
  - type: Documentation
    url: https://www.kubeflow.org/docs/
  - type: Getting Started
    url: https://www.kubeflow.org/docs/started/
  - type: Blog
    url: https://blog.kubeflow.org/
  - type: GitHubOrg
    url: https://github.com/kubeflow
  - type: Community
    url: https://www.kubeflow.org/docs/about/community/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
