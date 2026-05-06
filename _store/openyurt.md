---
aid: openyurt
name: OpenYurt
description: OpenYurt is a CNCF incubating project that extends Kubernetes for edge and cloud-edge collaboration scenarios. It provides node autonomy for edge nodes to continue operating during cloud-edge network disconnections, seamless node conversion between cloud and edge modes, and unified management of edge resources through NodePool and YurtAppSet abstractions.
url: https://openyurt.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Cloud-Edge
  - Edge Computing
  - Incubating
  - IoT
  - Kubernetes
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: openyurt:openyurt-api
    name: OpenYurt Edge Management API
    description: OpenYurt extends Kubernetes with CRDs for edge computing including NodePool for grouping edge nodes, YurtAppSet for deploying applications across node pools, YurtAppDaemon for pool-scoped daemon workloads, and Raven for cross-edge-cloud networking. The YurtHub component provides local caching and autonomy when edge nodes lose cloud connectivity.
    humanURL: https://openyurt.io/docs/
    properties:
      - type: Documentation
        url: https://openyurt.io/docs/
    tags:
      - Autonomy
      - Edge Management
      - Node Pools
common:
  - type: Documentation
    name: OpenYurt Documentation
    description: Official OpenYurt documentation.
    url: https://openyurt.io/docs/
  - type: GitHubOrg
    name: OpenYurt GitHub
    description: Source code repository.
    url: https://github.com/openyurtio/openyurt
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
