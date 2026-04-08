---
aid: multus-cni
url: https://raw.githubusercontent.com/api-evangelist/multus-cni/refs/heads/main/apis.yml
apis:
- aid: multus-cni:multus-cni
  name: Multus CNI
  description: Multus CNI is a meta-plugin for Kubernetes that enables attaching multiple network interfaces to pods. It supports delegating to other CNI plugins and allows pods to connect to multiple networks for advanced networking use cases.
  humanURL: https://github.com/k8snetworkplumbingwg/multus-cni
  tags:
  - CNI
  - Containers
  - Kubernetes
  - Multi-Network
  - Networking
  properties:
  - type: Documentation
    url: https://github.com/k8snetworkplumbingwg/multus-cni/tree/master/docs
  - type: Getting Started
    url: https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/quickstart.md
name: Multus CNI
tags:
- CNI
- Containers
- Kubernetes
- Multi-Network
- Networking
- Open Source
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Multus CNI is a container network interface plugin for Kubernetes that enables attaching multiple network interfaces to pods. It acts as a meta-plugin that can call multiple other CNI plugins, allowing pods to have connectivity to multiple networks simultaneously.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

