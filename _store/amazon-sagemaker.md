---
name: Amazon SageMaker
description: Amazon SageMaker is a fully managed machine learning platform that enables developers and data scientists to build, train, and deploy machine learning models at scale. SageMaker removes the heavy lifting from each step of the machine learning process, providing built-in algorithms, managed Jupyter notebooks, distributed training, automatic model tuning, and one-click deployment to production endpoints with auto-scaling.
url: https://aws.amazon.com/sagemaker/
baseURL: https://api.sagemaker.amazonaws.com
x-type: company
created: '2024-01-01'
modified: '2026-04-19'
tags:
  - AI
  - AWS
  - Inference
  - Machine Learning
  - MLOps
  - Training
apis:
  - name: Amazon SageMaker API
    description: The Amazon SageMaker control plane API for creating and managing SageMaker resources including notebook instances, training jobs, models, endpoints, pipelines, experiments, feature groups, and monitoring schedules.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html
    baseURL: https://api.sagemaker.{region}.amazonaws.com
    tags:
      - Machine Learning
      - AI
      - Training
      - Inference
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/Welcome.html
      - type: OpenAPI
        url: openapi/amazon-sagemaker-openapi.yml
      - type: JSONSchema
        url: json-schema/amazon-sagemaker-notebook-instance-schema.json
      - type: JSONSchema
        url: json-schema/amazon-sagemaker-training-job-schema.json
      - type: JSONSchema
        url: json-schema/amazon-sagemaker-model-schema.json
      - type: JSONSchema
        url: json-schema/amazon-sagemaker-endpoint-schema.json
      - type: SDK
        url: https://pypi.org/project/sagemaker/
        title: Python SDK
      - type: CodeExamples
        url: https://github.com/aws/amazon-sagemaker-examples
        title: Jupyter Notebook Examples
  - name: Amazon SageMaker Runtime API
    description: The Amazon SageMaker AI runtime API for invoking deployed model endpoints to get real-time inference predictions.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/dg/API_runtime_InvokeEndpoint.html
    baseURL: https://runtime.sagemaker.{region}.amazonaws.com
    tags:
      - Inference
      - Runtime
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/dg/API_runtime_InvokeEndpoint.html
  - name: Amazon SageMaker Feature Store Runtime API
    description: Data plane API operations for the Amazon SageMaker Feature Store supporting put, delete, and retrieve operations for ML features.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Feature_Store_Runtime.html
    baseURL: https://featurestore-runtime.sagemaker.{region}.amazonaws.com
    tags:
      - Feature Store
      - Machine Learning
      - Data
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Feature_Store_Runtime.html
  - name: Amazon SageMaker Metrics Service API
    description: Data plane API operations for Amazon SageMaker Metrics for putting and retrieving metrics related to training runs.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Metrics_Service.html
    baseURL: https://metrics.sagemaker.{region}.amazonaws.com
    tags:
      - Metrics
      - Training
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_Metrics_Service.html
  - name: Amazon SageMaker Geospatial API
    description: APIs for creating and managing Amazon SageMaker geospatial capabilities including earth observation jobs and vector enrichment jobs.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_geospatial_capabilities.html
    baseURL: https://sagemaker-geospatial.{region}.amazonaws.com
    tags:
      - Geospatial
      - Machine Learning
      - AWS
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_SageMaker_geospatial_capabilities.html
  - name: Amazon SageMaker Edge Manager API
    description: SageMaker Edge Manager dataplane service for communicating with active edge agents running ML models on edge devices.
    humanURL: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_Sagemaker_Edge.html
    baseURL: https://edge.sagemaker.{region}.amazonaws.com
    tags:
      - Edge
      - IoT
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_Operations_Amazon_Sagemaker_Edge.html
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: GettingStarted
    url: https://aws.amazon.com/sagemaker/getting-started/
  - type: Documentation
    url: https://docs.aws.amazon.com/sagemaker/latest/dg/
  - type: APIReference
    url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/
  - type: Console
    url: https://console.aws.amazon.com/sagemaker/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Pricing
    url: https://aws.amazon.com/sagemaker/pricing/
  - type: FAQ
    url: https://aws.amazon.com/sagemaker/faqs/
  - type: Blog
    url: https://aws.amazon.com/blogs/machine-learning/
  - type: StatusPage
    url: https://status.aws.amazon.com/
  - type: Support
    url: https://aws.amazon.com/support/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Security
    url: https://docs.aws.amazon.com/sagemaker/latest/dg/security.html
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/amazon-sagemaker
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: CLI
    url: https://docs.aws.amazon.com/cli/latest/reference/sagemaker/
  - type: CLI
    url: https://github.com/aws/sagemaker-hyperpod-cli
    title: SageMaker HyperPod CLI
  - type: SDK
    url: https://github.com/aws/sagemaker-python-sdk
    title: Python SDK (GitHub)
  - type: GitHubRepository
    url: https://github.com/aws/sagemaker-core
  - type: GitHubRepository
    url: https://github.com/aws/sagemaker-distribution
  - type: SpectralRules
    url: rules/amazon-sagemaker-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-sagemaker-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/ml-lifecycle-management.yaml
  - type: Training
    url: https://aws.amazon.com/training/
  - type: Features
    data:
      - name: SageMaker Studio
        description: Fully integrated development environment for ML work with notebooks, debugging, and experiment tracking.
      - name: SageMaker HyperPod
        description: Purpose-built infrastructure for distributed training that reduces foundation model training time by up to 40%.
      - name: SageMaker JumpStart
        description: Hub providing access to foundation models, pre-built algorithms, and one-click deployment.
      - name: SageMaker Autopilot
        description: Automated model creation with complete visibility and transparency.
      - name: SageMaker Canvas
        description: No-code visual interface for creating ML models without writing code.
      - name: SageMaker Feature Store
        description: Store, share, and manage features for machine learning models.
      - name: SageMaker Data Wrangler
        description: Data preparation tool that reduces transformation workflow time significantly.
      - name: SageMaker Ground Truth
        description: Incorporates human feedback throughout the ML lifecycle for data labeling.
      - name: SageMaker Pipelines
        description: Purpose-built CI/CD service for machine learning workflows.
      - name: SageMaker Model Monitor
        description: Automatically detects concept drift and data quality issues in deployed models.
      - name: SageMaker Clarify
        description: Provides machine learning explainability and bias detection.
      - name: SageMaker Experiments
        description: Streamlines tracking and management of ML experiments.
      - name: ML Governance
        description: Access controls and transparency across the full ML lifecycle with audit trails.
  - type: UseCases
    data:
      - name: Generative AI Applications
        description: Build custom generative AI applications using proprietary data with foundation model fine-tuning.
      - name: ML Model Development
        description: Train and deploy ML models across the entire machine learning lifecycle from exploration to production.
      - name: Data Analytics
        description: Query and analyze data across unified sources with built-in SQL analytics and data processing.
      - name: Enterprise AI Governance
        description: Manage data and AI artifacts with fine-grained security controls and compliance tooling.
      - name: Computer Vision
        description: Build and deploy computer vision models for image classification, object detection, and segmentation.
      - name: Natural Language Processing
        description: Train and deploy NLP models for text classification, entity recognition, and language generation.
      - name: Fraud Detection
        description: Build real-time fraud detection models with low-latency inference endpoints.
      - name: Predictive Maintenance
        description: Deploy ML models on edge devices for predictive maintenance use cases.
  - type: Integrations
    data:
      - name: Amazon S3
        description: Store training data, model artifacts, and inference outputs in Amazon S3 data lakes.
      - name: Amazon Redshift
        description: Zero-ETL integration for near real-time data ingestion from Redshift warehouses.
      - name: Amazon ECR
        description: Store and manage Docker containers for custom training and inference environments.
      - name: AWS Lambda
        description: Trigger ML inference pipelines and post-processing workflows with Lambda functions.
      - name: Amazon EventBridge
        description: Trigger SageMaker pipelines and workflows based on events.
      - name: AWS Step Functions
        description: Orchestrate multi-step ML workflows using Step Functions state machines.
      - name: Apache Iceberg
        description: Lakehouse architecture supporting Apache Iceberg-compatible data tools.
      - name: Amazon DataZone
        description: SageMaker Catalog built on Amazon DataZone for data discovery and governance.
      - name: Amazon Q Developer
        description: Natural language assistance integrated into SageMaker Unified Studio.
      - name: Hugging Face
        description: Deploy Hugging Face models directly via SageMaker JumpStart.
  - type: JSON-LD
    url: json-ld/amazon-sagemaker-context.jsonld
  - type: JSONSchema
    url: json-schema/amazon-sagemaker-tag-schema.json
  - type: JSONStructure
    url: json-structure/amazon-sagemaker-endpoint-structure.json
  - type: JSONStructure
    url: json-structure/amazon-sagemaker-model-structure.json
  - type: JSONStructure
    url: json-structure/amazon-sagemaker-notebook-instance-structure.json
  - type: JSONStructure
    url: json-structure/amazon-sagemaker-tag-structure.json
  - type: JSONStructure
    url: json-structure/amazon-sagemaker-training-job-structure.json
  - type: Example
    url: examples/amazon-sagemaker-endpoint-example.json
  - type: Example
    url: examples/amazon-sagemaker-model-example.json
  - type: Example
    url: examples/amazon-sagemaker-notebook-instance-example.json
  - type: Example
    url: examples/amazon-sagemaker-tag-example.json
  - type: Example
    url: examples/amazon-sagemaker-training-job-example.json
  - type: NaftikoCapability
    url: capabilities/shared/amazon-sagemaker.yaml
maintainer: Kin Lane
---
