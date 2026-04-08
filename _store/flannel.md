---
aid: flannel
url: https://raw.githubusercontent.com/api-evangelist/flannel/refs/heads/main/apis.yml
apis:
- aid: flannel:flannel
  name: Flannel
  description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It allocates subnet leases to each host and provides a layer 3 IPv4 network between multiple nodes in a cluster.
  humanURL: https://github.com/flannel-io/flannel
  tags:
  - CNI
  - Containers
  - Kubernetes
  - Networking
  - Overlay Network
  properties:
  - type: Documentation
    url: https://github.com/flannel-io/flannel/blob/master/Documentation/kubernetes.md
  - type: Getting Started
    url: https://github.com/flannel-io/flannel/blob/master/Documentation/running.md
name: Flannel
tags:
- CNI
- Containers
- Kubernetes
- Networking
- Open Source
- Overlay Network
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It runs a small single binary agent called flanneld on each host and is responsible for allocating a subnet lease to each host out of a larger preconfigured address space.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

