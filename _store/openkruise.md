---
aid: openkruise
url: https://raw.githubusercontent.com/api-evangelist/openkruise/refs/heads/main/apis.yml
apis:
- aid: openkruise:openkruise-api
  name: OpenKruise Workload API
  description: OpenKruise provides Kubernetes CRDs for advanced workload management. CloneSet offers efficient rolling updates with partition control, Advanced StatefulSet supports in-place container updates, SidecarSet manages sidecar containers across pods, BroadcastJob runs tasks on all nodes, and ImagePullJob pre-pulls images. Each controller extends standard Kubernetes capabilities with fine-grained deployment control.
  humanURL: https://openkruise.io/docs/
  properties:
  - type: Documentation
    url: https://openkruise.io/docs/
  tags:
  - Deployment
  - In-Place Updates
  - Workload Controllers
name: OpenKruise
tags:
- Cloud Native
- Controllers
- Deployment
- Incubating
- Kubernetes
- Workload Management
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OpenKruise is a CNCF incubating project providing advanced workload management and deployment automation for Kubernetes. It extends Kubernetes with enhanced controllers including CloneSet for efficient stateless updates, Advanced StatefulSet with in-place updates, SidecarSet for sidecar container management, BroadcastJob for node-level tasks, and ImagePullJob for pre-pulling container images.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

