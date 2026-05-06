---
aid: argo
name: Argo
description: Argo is a collection of open-source Kubernetes-native tools for workflows, events, CI/CD, and progressive delivery. The project includes Argo Workflows (container-native workflow engine), Argo CD (declarative GitOps continuous delivery), Argo Events (event-driven automation framework), and Argo Rollouts (progressive delivery with canary and blue-green strategies). Argo is a CNCF graduated project governed by the Linux Foundation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNCF
  - CI/CD
  - GitOps
  - Kubernetes
  - Open Source
  - Progressive Delivery
  - Workflow Engine
url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: argo:argo-workflows-api
    name: Argo Workflows API
    description: REST API for managing Argo Workflows, workflow templates, cron workflows, archived workflow records, events, and sensors on Kubernetes clusters. Authentication uses JWT bearer tokens from Kubernetes service accounts.
    humanURL: https://argo-workflows.readthedocs.io/en/latest/rest-api/
    baseURL: https://localhost:2746/api/v1
    tags:
      - Automation
      - Kubernetes
      - Workflow Engine
    properties:
      - type: Documentation
        url: https://argo-workflows.readthedocs.io/en/latest/
      - type: APIReference
        url: https://argo-workflows.readthedocs.io/en/latest/rest-api/
      - type: OpenAPI
        url: openapi/argo-workflows-openapi.yml
      - type: GettingStarted
        url: https://argo-workflows.readthedocs.io/en/latest/quick-start/
  - aid: argo:argo-cd-api
    name: Argo CD API
    description: REST API for managing Argo CD GitOps applications, projects, repositories, clusters, and sync operations for Kubernetes declarative continuous delivery. Authentication uses JWT bearer tokens.
    humanURL: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
    baseURL: https://localhost/api/v1
    tags:
      - Continuous Delivery
      - GitOps
      - Kubernetes
    properties:
      - type: Documentation
        url: https://argo-cd.readthedocs.io/en/stable/
      - type: APIReference
        url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
      - type: OpenAPI
        url: openapi/argo-cd-openapi.yml
  - aid: argo:argo-events-api
    name: Argo Events API
    description: Kubernetes-native API for the Argo Events event-driven automation framework. Exposes CRD-based resources including EventSource, EventBus, and Sensor for triggering Argo Workflows and Kubernetes actions in response to over 20 event types including webhooks, S3, cron, and messaging queues.
    humanURL: https://argoproj.github.io/argo-events/APIs/
    tags:
      - Automation
      - Event-Driven
      - Events
      - Kubernetes
    properties:
      - type: Documentation
        url: https://argoproj.github.io/argo-events/
      - type: APIReference
        url: https://argoproj.github.io/argo-events/APIs/
      - type: GitHubRepository
        url: https://github.com/argoproj/argo-events
      - type: AsyncAPI
        url: asyncapi/argo-events-asyncapi.yml
  - aid: argo:argo-rollouts-api
    name: Argo Rollouts API
    description: Kubernetes CRD-based API for Argo Rollouts progressive delivery controller. Provides Rollout and AnalysisTemplate resources for managing canary and blue-green deployment strategies with automated analysis, traffic splitting, and rollback capabilities.
    humanURL: https://argo-rollouts.readthedocs.io/en/stable/
    tags:
      - Blue-Green
      - Canary
      - Deployments
      - Kubernetes
      - Progressive Delivery
    properties:
      - type: Documentation
        url: https://argo-rollouts.readthedocs.io/en/stable/
      - type: GitHubRepository
        url: https://github.com/argoproj/argo-rollouts
      - type: APIReference
        url: https://argo-rollouts.readthedocs.io/en/stable/features/kubectl-plugin/
common:
  - type: Website
    url: https://argoproj.github.io/
  - type: Documentation
    url: https://argoproj.github.io/
  - type: GitHubOrganization
    url: https://github.com/argoproj
  - type: GitHubRepository
    url: https://github.com/argoproj/argoproj
  - type: Blog
    url: https://blog.argoproj.io/
  - type: Support
    url: https://github.com/argoproj/argo-workflows/issues
  - type: JSONLD
    url: json-ld/argo-context.jsonld
  - type: SpectralRules
    url: rules/argo-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/argo-platform.yaml
  - type: Vocabulary
    url: vocabulary/argo-vocabulary.yaml
  - type: Features
    data:
      - name: Argo Workflows
        description: Container-native workflow engine for orchestrating parallel jobs and ML pipelines on Kubernetes.
      - name: Argo CD
        description: Declarative GitOps continuous delivery tool that syncs Kubernetes application state from Git.
      - name: Argo Events
        description: Event-driven automation framework supporting 20+ event sources to trigger Kubernetes workflows.
      - name: Argo Rollouts
        description: Progressive delivery controller with canary, blue-green, and experiment strategies for Kubernetes.
      - name: CNCF Graduated
        description: All four Argo projects are CNCF graduated, ensuring production-quality governance and stability.
      - name: Kubernetes-Native
        description: All tools are implemented as Kubernetes CRDs and controllers, integrating natively with the platform.
  - type: UseCases
    data:
      - name: GitOps Platform
        description: Combine Argo CD and Argo Workflows for a complete Git-driven DevOps platform on Kubernetes.
      - name: Machine Learning Pipelines
        description: Use Argo Workflows to orchestrate multi-step ML training, evaluation, and deployment pipelines.
      - name: Event-Driven Automation
        description: Use Argo Events to trigger workflows based on webhooks, schedules, messaging, and cloud events.
      - name: Progressive Delivery
        description: Use Argo Rollouts for safe canary and blue-green deployments with automated analysis and rollback.
      - name: CI/CD on Kubernetes
        description: Build complete CI/CD pipelines natively on Kubernetes using Argo Workflows and Argo CD together.
  - type: Integrations
    data:
      - name: Helm
        description: Argo CD natively renders Helm charts; Argo Workflows can execute Helm operations as steps.
      - name: Kustomize
        description: Argo CD supports Kustomize overlays for environment-specific application configuration.
      - name: Prometheus
        description: All Argo tools expose Prometheus metrics for monitoring workflow and deployment health.
      - name: Slack
        description: Argo CD and Argo Workflows support Slack notifications for deployment and workflow events.
      - name: GitHub
        description: Deep integration with GitHub webhooks for triggering workflows and CD syncs.
      - name: Amazon S3
        description: Argo Workflows uses S3 as an artifact repository for passing data between workflow steps.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
