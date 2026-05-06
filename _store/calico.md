---
aid: calico
name: Calico
description: Calico is an open source networking and network security solution for containers, virtual machines, and native host-based workloads. Created and maintained by Tigera, it is the most widely adopted solution for container networking and security, powering over 8 million nodes daily across 166 countries.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CNI
  - Containers
  - eBPF
  - Kubernetes
  - Network Policy
  - Network Security
  - Networking
  - Open Source
  - Service Mesh
url: https://raw.githubusercontent.com/api-evangelist/calico/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: calico:calico-client-api
    name: Calico Client API
    description: The Calico Client Library provides programmatic access to manage Calico resources such as network policies, IP pools, BGP configuration, host and workload endpoints, and IPAM settings. It is the core programmatic interface consumed by calicoctl and other Calico components for managing container networking and security resources.
    humanURL: https://docs.tigera.io/calico/latest/reference/
    tags:
      - Client Library
      - CNI
      - Network Policy
      - Networking
    properties:
      - type: Documentation
        url: https://docs.tigera.io/calico/latest/reference/
      - type: GitHub
        url: https://github.com/projectcalico/calico
  - aid: calico:calicoctl-cli
    name: calicoctl CLI
    description: calicoctl is the command-line tool that enables operators and automation systems to create, read, update, and delete Calico resources such as policies, IP pools, BGP peers, host endpoints, and workload endpoints. It also supports datastore migration, IPAM management, node diagnostics, and cluster status operations.
    humanURL: https://docs.tigera.io/calico/latest/reference/calicoctl/
    tags:
      - CLI
      - IPAM
      - Network Policy
      - Operations
    properties:
      - type: Documentation
        url: https://docs.tigera.io/calico/latest/reference/calicoctl/
      - type: GitHub
        url: https://github.com/projectcalico/calicoctl
  - aid: calico:calico-kubernetes-crds
    name: Calico Kubernetes CRDs
    description: Calico exposes its networking and security primitives through Kubernetes Custom Resource Definitions (CRDs) including NetworkPolicy, GlobalNetworkPolicy, IPPool, BGPConfiguration, BGPPeer, HostEndpoint, WorkloadEndpoint, FelixConfiguration, and others. These CRDs allow declarative management of container networking and security via the Kubernetes API.
    humanURL: https://docs.tigera.io/calico/latest/reference/resources/
    tags:
      - CRDs
      - Kubernetes
      - Network Policy
      - Security
    properties:
      - type: Documentation
        url: https://docs.tigera.io/calico/latest/reference/resources/
      - type: GitHub
        url: https://github.com/projectcalico/calico
common:
  - type: Website
    url: https://www.tigera.io/project-calico/
  - type: Documentation
    url: https://docs.tigera.io/
  - type: Getting Started
    url: https://docs.tigera.io/calico/latest/getting-started/kubernetes/quickstart
  - type: GitHub Organization
    url: https://github.com/projectcalico
  - type: GitHub Repository
    url: https://github.com/projectcalico/calico
  - type: Blog
    url: https://www.tigera.io/blog/
  - type: Pricing
    url: https://www.tigera.io/tigera-products/calico/
  - type: Slack
    url: https://slack.projectcalico.org/
  - type: Training
    url: https://www.tigera.io/interactive-training/
  - type: Certification
    url: https://www.tigera.io/lp/calico-certification/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
