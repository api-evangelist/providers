---
aid: flannel
name: Flannel
description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It runs a small single binary agent called flanneld on each host and is responsible for allocating a subnet lease to each host out of a larger preconfigured address space. Flannel does not expose its own HTTP/REST API; it stores network configuration in either the Kubernetes API or etcd directly and is managed via configuration files, kubectl, and Helm.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNI
  - Cloud Native
  - Containers
  - Kubernetes
  - Networking
  - Open Source
  - Overlay Network
url: https://raw.githubusercontent.com/api-evangelist/flannel/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: flannel:flannel
    name: Flannel
    description: Flannel is a simple overlay network that satisfies the Kubernetes networking requirements. It allocates subnet leases to each host and provides a layer 3 IPv4 network between multiple nodes in a cluster. It is configured via the Kubernetes API or etcd and exposes no REST API of its own.
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
      - type: Configuration
        url: https://github.com/flannel-io/flannel/blob/master/Documentation/configuration.md
common:
  - type: Website
    url: https://github.com/flannel-io/flannel
  - type: Documentation
    url: https://github.com/flannel-io/flannel/blob/master/Documentation/kubernetes.md
  - type: Getting Started
    url: https://github.com/flannel-io/flannel/blob/master/Documentation/running.md
  - type: GitHub Organization
    url: https://github.com/flannel-io
  - type: Helm Chart
    url: https://flannel-io.github.io/flannel/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
