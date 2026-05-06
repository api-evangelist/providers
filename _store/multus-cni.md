---
aid: multus-cni
name: Multus CNI
description: Multus CNI is a container network interface plugin for Kubernetes that enables attaching multiple network interfaces to pods. It acts as a meta-plugin that can call multiple other CNI plugins, allowing pods to have connectivity to multiple networks simultaneously.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNI
  - Containers
  - Kubernetes
  - Multi-Network
  - Networking
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/multus-cni/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
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
common:
  - type: Website
    url: https://github.com/k8snetworkplumbingwg/multus-cni
  - type: Documentation
    url: https://github.com/k8snetworkplumbingwg/multus-cni/tree/master/docs
  - type: Getting Started
    url: https://github.com/k8snetworkplumbingwg/multus-cni/blob/master/docs/quickstart.md
  - type: GitHub Organization
    url: https://github.com/k8snetworkplumbingwg
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
