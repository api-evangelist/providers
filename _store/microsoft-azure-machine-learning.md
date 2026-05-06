---
name: Azure Machine Learning
description: Azure Machine Learning is an enterprise-grade cloud service for building, training, deploying, and managing machine learning models. It supports the full ML lifecycle including data preparation, model training, evaluation, deployment, and monitoring with MLOps capabilities.
image: https://azure.microsoft.com/svghandler/machine-learning/
url: https://azure.microsoft.com/en-us/services/machine-learning/
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - AI
  - Azure
  - Machine Learning
  - MLOps
  - Model Deployment
  - Model Training
apis:
  - aid: microsoft-azure-machine-learning:rest-api
    name: Azure Machine Learning REST API
    description: Azure Machine Learning REST API provides management of ML workspaces, compute resources, datasets, experiments, models, and endpoints. It supports the full ML lifecycle including data preparation, model training, evaluation, deployment, and monitoring.
    image: https://azure.microsoft.com/svghandler/machine-learning/
    humanURL: https://learn.microsoft.com/en-us/rest/api/azureml/
    baseURL: https://management.azure.com
    tags:
      - AI
      - Machine Learning
      - MLOps
      - Model Deployment
      - Model Training
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/azure/machine-learning/
      - type: APIReference
        url: https://learn.microsoft.com/en-us/rest/api/azureml/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/rest/api/azure/
      - type: GettingStarted
        url: https://learn.microsoft.com/en-us/azure/machine-learning/quickstart-create-resources
      - type: Pricing
        url: https://azure.microsoft.com/en-us/pricing/details/machine-learning/
      - type: SDK
        url: https://learn.microsoft.com/en-us/python/api/overview/azure/ai-ml-readme
        title: Python SDK v2
      - type: SDK
        url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/resourcemanager.machinelearning-readme
        title: .NET SDK
    contact:
      - type: Support
        url: https://azure.microsoft.com/en-us/support/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/machine-learning/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/machine-learning/
  - type: StatusPage
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: TermsOfService
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: PrivacyPolicy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Features
    data:
      - name: Workspace Management
        description: Create and manage Azure ML workspaces as the top-level resource for ML assets and experiments.
      - name: Compute Resources
        description: Provision and manage compute clusters, compute instances, and Kubernetes-attached compute targets.
      - name: Model Training
        description: Run training jobs at scale with automated ML, distributed training, and hyperparameter tuning.
      - name: Model Deployment
        description: Deploy models as managed online endpoints, batch endpoints, or to Kubernetes for real-time and batch inference.
      - name: MLOps and Pipelines
        description: Build reproducible ML pipelines with versioning, CI/CD integration, and model registry capabilities.
      - name: Responsible AI
        description: Use built-in tools for fairness assessment, interpretability, and model monitoring across the lifecycle.
  - type: UseCases
    data:
      - name: Predictive Analytics
        description: Build and deploy predictive models for forecasting, classification, and regression scenarios.
      - name: Computer Vision
        description: Train and deploy image classification, object detection, and segmentation models.
      - name: Natural Language Processing
        description: Build NLP models for text classification, entity recognition, and sentiment analysis.
      - name: MLOps and Production ML
        description: Operationalize ML models with automated training pipelines, deployment, and monitoring.
  - type: Integrations
    data:
      - name: Azure Storage
        description: Store training data, models, and experiment artifacts in Azure Blob Storage and Data Lake.
      - name: Azure Kubernetes Service
        description: Deploy ML models to AKS for production-grade inference at scale.
      - name: Azure DevOps
        description: Integrate ML pipelines with Azure DevOps for continuous integration and deployment.
      - name: GitHub Actions
        description: Automate ML workflows with GitHub Actions for training and deployment automation.
      - name: Power BI
        description: Consume ML model predictions in Power BI dashboards and reports.
---
