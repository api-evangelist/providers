---
aid: wasmcloud
name: wasmCloud
description: wasmCloud is a CNCF incubating platform for building, managing, and scaling distributed applications using WebAssembly components. It provides a runtime that manages the lifecycle of WebAssembly actors and capability providers, enabling developers to write portable business logic that connects to infrastructure capabilities like HTTP servers, messaging, key-value stores, and databases through a declarative linking model based on WebAssembly Interface Types (WIT).
url: https://wasmcloud.com
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - CNCF
  - Distributed Systems
  - Incubating
  - Runtime
  - Wasm
  - WebAssembly
  - WIT
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: wasmcloud:wasmcloud-control-api
    name: wasmCloud Control Interface API
    description: The wasmCloud control interface provides a NATS-based API for managing the wasmCloud lattice. It supports operations for starting and stopping actors and providers, establishing links between components, querying host inventories, and managing application deployments. The wash CLI and wasmCloud dashboard interact with hosts through this interface.
    humanURL: https://wasmcloud.com/docs/hosts/lattice-protocols/control-interface/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmcloud.com/docs/hosts/lattice-protocols/control-interface/
      - type: Reference
        url: https://wasmcloud.com/docs/concepts/
      - type: AsyncAPI
        url: asyncapi/wasmcloud-control-asyncapi.yml
      - type: AsyncAPI
        url: asyncapi/wasmcloud-lattice-events-asyncapi.yml
    tags:
      - Control API
      - Lattice Management
      - NATS
  - aid: wasmcloud:wasmcloud-wadm-api
    name: wasmCloud Application Deployment Manager (wadm) API
    description: wadm provides a declarative application deployment API for wasmCloud. Applications are defined as YAML manifests specifying components, capability providers, and their links. wadm manages the desired state of applications across the lattice, handling scaling, updates, and self-healing through reconciliation loops using the Open Application Model format.
    humanURL: https://wasmcloud.com/docs/ecosystem/wadm/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmcloud.com/docs/ecosystem/wadm/
      - type: Reference
        url: https://wasmcloud.com/docs/ecosystem/wadm/api/
      - type: GitHubRepository
        url: https://github.com/wasmCloud/wadm
      - type: JSONSchema
        url: json-schema/wasmcloud-manifest-schema.json
      - type: AsyncAPI
        url: asyncapi/wasmcloud-wadm-asyncapi.yml
      - type: JSONSchema
        url: json-schema/wasmcloud-oam-manifest-schema.json
    tags:
      - Application Management
      - Declarative
      - Deployment
      - OAM
  - aid: wasmcloud:wasmcloud-wash-cli
    name: wasmCloud wash CLI
    description: wash (WAsmcloud SHell) is the comprehensive command-line tool for developing, building, deploying, and managing wasmCloud applications and WebAssembly components. It bundles a wasmCloud host, NATS server, and wadm for local development, and supports publishing components to OCI registries and managing remote lattices.
    humanURL: https://wasmcloud.com/docs/cli/wash/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmcloud.com/docs/cli/wash/
      - type: Getting Started
        url: https://wasmcloud.com/docs/getting-started/
      - type: GitHubRepository
        url: https://github.com/wasmCloud/wash
      - type: Change Log
        url: https://github.com/wasmCloud/wash/releases
    tags:
      - CLI
      - Developer Tools
      - WebAssembly
  - aid: wasmcloud:wasmcloud-interfaces
    name: wasmCloud WIT Interfaces
    description: wasmCloud interfaces are defined using WebAssembly Interface Type (WIT), the open standard interface description language maintained as part of the W3C WebAssembly Component Model. wasmCloud supports WASI 0.2 interfaces as well as wasmCloud-specific interfaces for capability providers covering HTTP, messaging, key-value, blobstore, and other infrastructure concerns.
    humanURL: https://wasmcloud.com/docs/concepts/interfaces/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmcloud.com/docs/concepts/interfaces/
      - type: Reference
        url: https://wasmcloud.com/docs/reference/wasi/support/
      - type: GitHubRepository
        url: https://github.com/wasmCloud/wasmCloud
    tags:
      - Interfaces
      - WASI
      - WebAssembly
      - WIT
  - aid: wasmcloud:wasmcloud-kubernetes-operator
    name: wasmCloud Kubernetes Operator
    description: The wasmCloud Kubernetes Operator enables running wasmCloud infrastructure natively on Kubernetes clusters. It deploys wasmCloud hosts as Kubernetes workloads and bridges the Kubernetes control plane with the wasmCloud lattice, enabling seamless integration with existing Kubernetes tooling and GitOps workflows. Defines CRDs for Hosts, Artifacts, Workloads, WorkloadDeploments, and WorkloadReplicaSets under the runtime.wasmcloud.dev group.
    humanURL: https://wasmcloud.com/docs/deployment/k8s/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://wasmcloud.com/docs/deployment/k8s/
      - type: GitHubRepository
        url: https://github.com/wasmCloud/wasmcloud-operator
      - type: KubernetesCRD
        url: crd/runtime.wasmcloud.dev_hosts.yaml
      - type: KubernetesCRD
        url: crd/runtime.wasmcloud.dev_artifacts.yaml
      - type: KubernetesCRD
        url: crd/runtime.wasmcloud.dev_workloads.yaml
      - type: KubernetesCRD
        url: crd/runtime.wasmcloud.dev_workloaddeployments.yaml
      - type: KubernetesCRD
        url: crd/runtime.wasmcloud.dev_workloadreplicasets.yaml
    tags:
      - Kubernetes
      - Operator
      - Deployment
common:
  - type: Website
    url: https://wasmcloud.com
  - type: Documentation
    url: https://wasmcloud.com/docs/
  - type: Getting Started
    url: https://wasmcloud.com/docs/getting-started/
  - type: Blog
    url: https://wasmcloud.com/blog/
  - type: Community
    url: https://wasmcloud.com/community/
  - type: GitHubOrganization
    url: https://github.com/wasmCloud
  - type: GitHubRepository
    url: https://github.com/wasmCloud/wasmCloud
  - type: Change Log
    url: https://github.com/wasmcloud/wasmcloud/releases
  - type: Slack
    url: https://slack.wasmcloud.com/
  - type: AsyncAPI
    url: asyncapi/wasmcloud-control-asyncapi.yml
  - type: AsyncAPI
    url: asyncapi/wasmcloud-wadm-asyncapi.yml
  - type: AsyncAPI
    url: asyncapi/wasmcloud-lattice-events-asyncapi.yml
  - type: JSONSchema
    url: json-schema/wasmcloud-manifest-schema.json
  - type: JSONSchema
    url: json-schema/wasmcloud-oam-manifest-schema.json
  - type: JSON-LD
    url: json-ld/wasmcloud-context.jsonld
  - type: JSONStructure
    url: json-structure/wasmcloud-oam-manifest-structure.json
  - type: Vocabulary
    url: vocabulary/wasmcloud-vocabulary.yml
  - type: KubernetesCRD
    url: crd/runtime.wasmcloud.dev_hosts.yaml
  - type: KubernetesCRD
    url: crd/runtime.wasmcloud.dev_artifacts.yaml
  - type: KubernetesCRD
    url: crd/runtime.wasmcloud.dev_workloads.yaml
  - type: KubernetesCRD
    url: crd/runtime.wasmcloud.dev_workloaddeployments.yaml
  - type: KubernetesCRD
    url: crd/runtime.wasmcloud.dev_workloadreplicasets.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
