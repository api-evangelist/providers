---
aid: chaos-mesh
url: https://raw.githubusercontent.com/api-evangelist/chaos-mesh/refs/heads/main/apis.yml
name: Chaos Mesh
x-type: opensource
tags:
  - Chaos Engineering
  - Cloud Native
  - CNCF
  - Fault Injection
  - Kubernetes
  - Observability
  - Open Source
  - Reliability
  - Resilience
  - Testing
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Open Source
created: '2025-01-01'
modified: '2026-04-23'
position: Consumer
description: Chaos Mesh is a CNCF graduated cloud-native chaos engineering platform that orchestrates chaos experiments on Kubernetes to test system resilience and reliability. It exposes Kubernetes Custom Resource Definitions (CRDs) for a wide range of chaos kinds (network, pod, IO, stress, DNS, time, kernel, JVM, HTTP), along with a Chaos Dashboard web UI backed by a REST API for creating, managing, and monitoring chaos experiments and workflows. Chaos Mesh integrates with Kubernetes, Argo Workflows, Prometheus, Grafana, and CI/CD pipelines to run experiments safely in staging and production environments.
apis:
  - aid: chaos-mesh:chaos-mesh-api
    name: Chaos Mesh API
    tags:
      - Chaos Engineering
      - CRDs
      - Dashboard
      - Experiments
      - Fault Injection
      - Kubernetes
      - Workflows
    humanURL: https://chaos-mesh.org/docs/
    properties:
      - url: https://chaos-mesh.org/docs/
        type: Documentation
      - type: Getting Started
        url: https://chaos-mesh.org/docs/quick-start/
      - type: GitHubRepository
        url: https://github.com/chaos-mesh/chaos-mesh
      - type: OpenAPI
        url: openapi/chaos-mesh-dashboard-api-openapi.yml
      - type: JSONSchema
        url: json-schema/chaos-mesh-experiment-schema.json
      - type: JSONLD
        url: json-ld/chaos-mesh-context.jsonld
    description: Chaos Mesh provides Kubernetes Custom Resources and a REST API for orchestrating chaos experiments including network faults, pod failures, IO chaos, stress testing, kernel chaos, DNS chaos, time chaos, JVM chaos, and HTTP request injection. The Chaos Dashboard exposes a REST API for creating, running, scheduling, and observing experiments and multi-step workflows, with RBAC and event auditing.
common:
  - type: Website
    url: https://chaos-mesh.org/
  - type: Documentation
    url: https://chaos-mesh.org/docs/
  - type: GettingStarted
    url: https://chaos-mesh.org/docs/quick-start/
  - type: Blog
    url: https://chaos-mesh.org/blog/
  - type: ChangeLog
    url: https://github.com/chaos-mesh/chaos-mesh/blob/master/CHANGELOG.md
  - type: GitHub
    url: https://github.com/chaos-mesh
  - type: GitHubRepository
    url: https://github.com/chaos-mesh/chaos-mesh
  - type: Community
    url: https://chaos-mesh.org/community/
  - type: License
    url: https://github.com/chaos-mesh/chaos-mesh/blob/master/LICENSE
  - type: CNCF
    url: https://www.cncf.io/projects/chaos-mesh/
  - type: Slack
    url: https://slack.cncf.io/
  - type: X
    url: https://x.com/chaos_mesh
  - type: JSONLD
    url: json-ld/chaos-mesh-context.jsonld
    name: Chaos Mesh JSON-LD Context
    description: Linked data context mapping Chaos Mesh resources to standard vocabularies.
  - type: JSONSchema
    url: json-schema/chaos-mesh-experiment-schema.json
    name: Chaos Mesh Experiment JSON Schema
    description: JSON Schema for Chaos Mesh experiment custom resources covering all supported chaos kinds.
  - name: Features
    type: Features
    data:
      - name: Pod Chaos
      - name: Network Chaos
      - name: IO Chaos
      - name: Stress Chaos
      - name: Kernel Chaos
      - name: Time Chaos
      - name: DNS Chaos
      - name: JVM Chaos
      - name: HTTP Chaos
      - name: AWS Chaos
      - name: GCP Chaos
      - name: Azure Chaos
      - name: Block Chaos
      - name: Physical Machine Chaos
      - name: Workflows
      - name: Schedules
      - name: Chaos Dashboard
      - name: Kubernetes CRDs
      - name: REST API
      - name: RBAC
      - name: Audit Events
      - name: Safe Mode
      - name: Status Monitoring
  - name: UseCases
    type: UseCases
    data:
      - name: Resilience Testing
      - name: Disaster Recovery Drills
      - name: SRE Game Days
      - name: Canary Validation
      - name: Production Reliability Testing
      - name: Multi-Region Failover Testing
      - name: Performance Bottleneck Discovery
      - name: Observability Validation
      - name: Continuous Chaos in CI/CD
      - name: Microservices Dependency Testing
      - name: Database Fault Tolerance Testing
  - name: Integrations
    type: Integrations
    data:
      - name: Kubernetes
      - name: EKS
      - name: GKE
      - name: AKS
      - name: OpenShift
      - name: Rancher
      - name: Argo Workflows
      - name: Argo CD
      - name: Prometheus
      - name: Grafana
      - name: OpenTelemetry
      - name: Jaeger
      - name: Datadog
      - name: Litmus
      - name: GitHub Actions
      - name: GitLab CI
      - name: Jenkins
      - name: Tekton
      - name: Helm
      - name: AWS
      - name: Google Cloud
      - name: Azure
  - name: ChaosKinds
    type: ChaosKinds
    data:
      - name: PodChaos
      - name: NetworkChaos
      - name: IOChaos
      - name: TimeChaos
      - name: KernelChaos
      - name: StressChaos
      - name: DNSChaos
      - name: HTTPChaos
      - name: JVMChaos
      - name: AWSChaos
      - name: GCPChaos
      - name: AzureChaos
      - name: BlockChaos
      - name: PhysicalMachineChaos
      - name: Schedule
      - name: Workflow
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
