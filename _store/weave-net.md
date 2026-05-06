---
aid: weave-net
name: Weave Net
description: Weave Net is an open source container networking plugin that creates a virtual network connecting Docker containers and Kubernetes pods across multiple hosts. It provides automatic IP address management (IPAM), DNS resolution via WeaveDNS, network policy enforcement, and optional encryption for container-to-container communication. The Weave Net daemon exposes a local HTTP API on port 6784 for programmatic network management. Weave Net is maintained by Weaveworks and is archived but remains widely used in production environments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Networking
  - Kubernetes
  - Docker
  - IPAM
  - Open Source
  - CNCF
url: https://raw.githubusercontent.com/api-evangelist/weave-net/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: weave-net:weave-net-http-api
    name: Weave Net HTTP API
    description: The Weave Net local HTTP API exposed on port 6784 for managing container networking including IP address allocation (IPAM), peer connections, WeaveDNS registration, and network bridge exposure.
    humanURL: https://github.com/weaveworks/weave
    tags:
      - Containers
      - Networking
      - IPAM
      - DNS
    properties:
      - url: openapi/weave-net-openapi.yml
        type: OpenAPI
      - url: https://github.com/weaveworks/weave
        type: Documentation
      - url: https://github.com/weaveworks/weave/tree/master/api
        type: APIReference
common:
  - url: https://github.com/weaveworks/weave
    type: GitHubRepository
  - url: https://github.com/weaveworks
    type: GitHubOrganization
  - url: https://github.com/weaveworks/weave/blob/master/LICENSE
    type: TermsOfService
  - url: https://github.com/weaveworks/weave/blob/master/SECURITY.md
    type: Security
  - url: https://github.com/weaveworks/weave/blob/master/CHANGELOG.md
    type: ChangeLog
  - url: https://github.com/weaveworks/weave/issues
    type: Support
  - type: SpectralRules
    url: rules/weave-net-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/container-networking.yaml
    title: Container Networking Capability
  - type: Vocabulary
    url: vocabulary/weave-net-vocabulary.yml
  - type: Features
    data:
      - name: Container Overlay Network
        description: Creates a virtual network connecting containers across multiple hosts without requiring any configuration of the physical network.
      - name: Automatic IPAM
        description: Automatically allocates IP addresses to containers from a configurable subnet using distributed consensus.
      - name: WeaveDNS
        description: Built-in DNS resolution for containers by hostname, making services discoverable by name on the Weave network.
      - name: Network Encryption
        description: Optional encryption of all network traffic using NaCl for secure container-to-container communication.
      - name: Kubernetes Integration
        description: Native Kubernetes CNI plugin for pod-to-pod networking across nodes.
      - name: Docker Integration
        description: Docker network plugin for seamless multi-host Docker container networking.
      - name: Fast Datapath
        description: Kernel-level packet forwarding using Open vSwitch for high-performance networking.
  - type: UseCases
    data:
      - name: Multi-Host Docker Networking
        description: Connect Docker containers across multiple physical or virtual machines without complex network configuration.
      - name: Kubernetes Pod Networking
        description: Provide pod-to-pod networking for Kubernetes clusters as a CNI-compliant network plugin.
      - name: Automated IP Management
        description: Automate container IP allocation and release in orchestration workflows.
      - name: Service Discovery
        description: Enable container service discovery by DNS name using WeaveDNS.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
