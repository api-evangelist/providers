---
aid: karmada
url: https://raw.githubusercontent.com/api-evangelist/karmada/refs/heads/main/apis.yml
apis:
- aid: karmada:karmada-api
  name: Karmada Multi-Cluster API
  description: Karmada extends the Kubernetes API with custom resources for multi-cluster management including PropagationPolicy for distributing resources across clusters, OverridePolicy for cluster-specific customization, and ResourceBinding for tracking resource placement. The Karmada API server provides a unified interface for managing workloads across clusters.
  humanURL: https://karmada.io/docs/
  properties:
  - type: Documentation
    url: https://karmada.io/docs/
  tags:
  - Federation
  - Multi-Cluster
  - Scheduling
name: Karmada
tags:
- Cloud Native
- Federation
- Incubating
- Kubernetes
- Multi-Cluster
- Scheduling
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Karmada is a CNCF incubating Kubernetes management system that enables running applications across multiple Kubernetes clusters and clouds. It provides a unified control plane for multi-cluster scheduling, failover, and traffic management. Karmada uses Kubernetes-native APIs and supports propagation policies, override policies, and federated resource management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

