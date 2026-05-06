---
aid: openkruise
name: OpenKruise
description: OpenKruise is a CNCF incubating project providing advanced workload management and deployment automation for Kubernetes. It extends Kubernetes with enhanced controllers including CloneSet for efficient stateless updates, Advanced StatefulSet with in-place updates, Advanced DaemonSet, SidecarSet for sidecar container management, BroadcastJob for node-level tasks, and ImagePullJob for pre-pulling container images.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/openkruise/refs/heads/main/apis.yml
tags:
  - Cloud Native
  - Controllers
  - Deployment
  - Incubating
  - Kubernetes
  - Workload Management
  - CRDs
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: openkruise:openkruise-api
    name: OpenKruise Workload API
    description: OpenKruise provides Kubernetes Custom Resource Definitions (CRDs) for advanced workload management. CloneSet offers efficient rolling updates with partition control, Advanced StatefulSet supports in-place container updates, Advanced DaemonSet provides surge and partitioned updates, SidecarSet manages sidecar containers across pods, BroadcastJob runs tasks on all nodes, and ImagePullJob pre-pulls images. Each controller extends standard Kubernetes capabilities with fine-grained deployment control through the apps.kruise.io/v1alpha1 and v1beta1 API groups.
    humanURL: https://openkruise.io/docs/
    baseURL: https://kubernetes.example.com/apis/apps.kruise.io/v1beta1
    tags:
      - Deployment
      - In-Place Updates
      - Workload Controllers
      - Kubernetes CRDs
    properties:
      - type: Documentation
        url: https://openkruise.io/docs/
      - type: APIReference
        url: https://openkruise.io/docs/reference/cloneset-api
      - type: GitHubRepository
        url: https://github.com/openkruise/kruise
common:
  - type: Documentation
    name: OpenKruise Documentation
    description: Official OpenKruise documentation.
    url: https://openkruise.io/docs/
  - type: Website
    name: OpenKruise Website
    url: https://openkruise.io/
  - type: GitHubOrg
    name: OpenKruise GitHub
    description: Source code repository.
    url: https://github.com/openkruise
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
