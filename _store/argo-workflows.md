---
aid: argo-workflows
name: Argo Workflows
description: Argo Workflows is an open-source, container-native workflow engine for orchestrating parallel jobs on Kubernetes. It is a CNCF graduated project that allows you to define workflows where each step is a container, model multi-step workflows as sequences of tasks or DAGs, and run compute-intensive jobs for machine learning, data processing, and CI/CD pipelines natively on Kubernetes. Governed by the Linux Foundation and the CNCF.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNCF
  - Containers
  - Data Processing
  - Kubernetes
  - Machine Learning
  - Open Source
  - Workflow Engine
url: https://raw.githubusercontent.com/api-evangelist/argo-workflows/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: argo-workflows:argo-workflows
    name: Argo Workflows API
    description: The Argo Workflows REST API provides programmatic access to workflow lifecycle management, workflow templates, cron scheduling, archived workflow history, events, and cluster workflow templates. Authentication uses JWT bearer tokens from service account secrets.
    humanURL: https://argo-workflows.readthedocs.io/en/latest/swagger/
    tags:
      - Kubernetes
      - REST API
      - Workflow Engine
    properties:
      - type: Documentation
        url: https://argo-workflows.readthedocs.io/en/latest/
      - type: OpenAPI
        url: openapi/argo-workflows-openapi.json
      - type: GettingStarted
        url: https://argo-workflows.readthedocs.io/en/latest/quick-start/
      - type: APIReference
        url: https://argo-workflows.readthedocs.io/en/latest/swagger/
      - type: Authentication
        url: https://argo-workflows.readthedocs.io/en/latest/access-token/
common:
  - type: Website
    url: https://argoproj.github.io/workflows/
  - type: Documentation
    url: https://argo-workflows.readthedocs.io/en/latest/
  - type: GettingStarted
    url: https://argo-workflows.readthedocs.io/en/latest/quick-start/
  - type: GitHubOrganization
    url: https://github.com/argoproj
  - type: GitHubRepository
    url: https://github.com/argoproj/argo-workflows
  - type: ReleaseNotes
    url: https://github.com/argoproj/argo-workflows/releases
  - type: ChangeLog
    url: https://argo-workflows.readthedocs.io/en/latest/new-features/
  - type: CLI
    url: https://argo-workflows.readthedocs.io/en/latest/cli/
  - type: SDK
    url: https://hera.readthedocs.io/en/stable/
  - type: Support
    url: https://github.com/argoproj/argo-workflows/issues
  - type: SpectralRules
    url: rules/argo-workflows-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/workflow-orchestration.yaml
  - type: Vocabulary
    url: vocabulary/argo-workflows-vocabulary.yaml
  - type: Features
    data:
      - name: Container-Native Workflows
        description: Every workflow step runs as a Kubernetes container, providing complete isolation and reproducibility.
      - name: DAG and Step-Based Orchestration
        description: Define multi-step workflows as sequential steps or directed acyclic graphs (DAGs) with dependencies.
      - name: Parallel Execution
        description: Run multiple workflow steps in parallel to maximize compute utilization and reduce execution time.
      - name: Workflow Templates
        description: Store and reuse workflow definitions as templates across the cluster.
      - name: Cron Workflows
        description: Schedule workflows to run on cron schedules directly on Kubernetes.
      - name: Artifact Support
        description: Pass artifacts between workflow steps via S3, GCS, Azure Blob, Artifactory, and more.
      - name: Workflow Archive
        description: Persist workflow history to a database for long-term retention and querying.
      - name: Web UI
        description: Monitor and manage workflows through a rich graphical interface.
      - name: Multi-Tenancy
        description: Namespace-based isolation with RBAC for multi-team environments.
      - name: Event-Driven Triggers
        description: Trigger workflows from Kubernetes events, webhooks, and custom event sources.
      - name: Python SDK (Hera)
        description: Define workflows in Python using the Hera SDK, the official Python SDK.
      - name: Plugin Architecture
        description: Extend with custom executor plugins and artifact driver plugins.
  - type: UseCases
    data:
      - name: Machine Learning Pipelines
        description: Orchestrate data preparation, model training, evaluation, and deployment as containerized steps.
      - name: Data Processing and ETL
        description: Run parallel data transformation and ETL jobs at scale on Kubernetes.
      - name: CI/CD on Kubernetes
        description: Run CI/CD pipelines natively on Kubernetes without external CI tools.
      - name: Batch Processing
        description: Process large datasets in parallel with automatic resource management.
      - name: Infrastructure Automation
        description: Automate infrastructure provisioning, testing, and validation workflows.
      - name: Scientific Computing
        description: Orchestrate complex scientific computation and simulation jobs with dependencies.
  - type: Integrations
    data:
      - name: Python Hera SDK
        description: Official Python SDK for defining and submitting workflows programmatically.
      - name: Argo CD
        description: Use Argo CD to deploy and manage Argo Workflows resources via GitOps.
      - name: Prometheus
        description: Expose workflow metrics for Prometheus monitoring and alerting.
      - name: Grafana
        description: Visualize workflow performance metrics in Grafana dashboards.
      - name: HashiCorp Vault
        description: Inject secrets into workflow containers securely via Vault integration.
      - name: Amazon S3
        description: Use S3 as artifact storage for passing data between workflow steps.
      - name: Google GCS
        description: Use Google Cloud Storage as artifact backend.
      - name: Azure Blob Storage
        description: Use Azure Blob Storage for artifact persistence.
      - name: Kubeflow
        description: Run Kubeflow ML pipelines using Argo Workflows as the underlying engine.
      - name: Apache Spark
        description: Orchestrate Apache Spark jobs as Argo Workflow steps.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
