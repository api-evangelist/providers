---
aid: argo
url: https://raw.githubusercontent.com/api-evangelist/argo/refs/heads/main/apis.yml
apis:
- aid: argo:argo-workflows-api
  name: Argo Workflows API
  description: REST API for managing Argo Workflows, workflow templates, cron workflows, and archived workflow records on Kubernetes clusters.
  humanURL: https://argo-workflows.readthedocs.io/en/latest/rest-api/
  baseURL: https://localhost:2746/api/v1
  tags:
  - Automation
  - Kubernetes
  - Workflows
  properties:
  - type: Documentation
    url: https://argo-workflows.readthedocs.io/en/latest/
  - type: Reference
    url: https://argo-workflows.readthedocs.io/en/latest/rest-api/
  - type: OpenAPI
    url: openapi/argo-workflows-openapi.yml
  - type: JSONSchema
    url: json-schema/argo-workflow-schema.json
- aid: argo:argo-cd-api
  name: Argo CD API
  description: API for managing Argo CD GitOps applications, projects, repositories, clusters, and sync operations for Kubernetes declarative continuous delivery.
  humanURL: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
  baseURL: https://localhost/api/v1
  tags:
  - Continuous Delivery
  - GitOps
  - Kubernetes
  properties:
  - type: Documentation
    url: https://argo-cd.readthedocs.io/en/stable/
  - type: Reference
    url: https://argo-cd.readthedocs.io/en/stable/developer-guide/api-docs/
  - type: OpenAPI
    url: openapi/argo-cd-openapi.yml
  - type: JSONSchema
    url: json-schema/argo-application-schema.json
- aid: argo:argo-events-api
  name: Argo Events API
  description: Kubernetes-native API for the Argo Events event-driven automation framework. Exposes CRD-based resources including EventSource, EventBus, and Sensor that enable triggering Argo Workflows and other Kubernetes actions in response to over 20 event types such as webhooks, S3, cron schedules, and messaging queues.
  humanURL: https://argoproj.github.io/argo-events/APIs/
  tags:
  - Automation
  - Event-Driven
  - Events
  - Kubernetes
  properties:
  - type: Documentation
    url: https://argoproj.github.io/argo-events/
  - type: Reference
    url: https://argoproj.github.io/argo-events/APIs/
  - type: GitHubRepository
    url: https://github.com/argoproj/argo-events
  - type: AsyncAPI
    url: asyncapi/argo-events-asyncapi.yml
- aid: argo:argo-rollouts-api
  name: Argo Rollouts API
  description: Kubernetes CRD-based API for the Argo Rollouts progressive delivery controller. Provides Rollout and AnalysisTemplate resources for managing canary and blue-green deployment strategies with automated analysis, traffic splitting, and rollback capabilities on Kubernetes.
  humanURL: https://argo-rollouts.readthedocs.io/en/stable/
  tags:
  - Canary
  - Deployments
  - Kubernetes
  - Progressive Delivery
  properties:
  - type: Documentation
    url: https://argo-rollouts.readthedocs.io/en/stable/
  - type: GitHubRepository
    url: https://github.com/argoproj/argo-rollouts
  - type: JSONSchema
    url: json-schema/argo-rollout-schema.json
name: Argo
tags:
- CI/CD
- GitOps
- Kubernetes
- Workflows
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Argo is a collection of open source tools for Kubernetes-native workflows, events, CI/CD, and progressive delivery. It includes Argo Workflows for orchestrating parallel jobs, Argo CD for GitOps continuous delivery, Argo Events for event-driven automation, and Argo Rollouts for progressive delivery strategies.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

