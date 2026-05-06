---
aid: kubernetes-operators
name: Kubernetes Operators
description: Kubernetes Operators are a method of packaging, deploying, and managing Kubernetes applications that extend the Kubernetes API to create, configure, and manage instances of complex applications on behalf of a Kubernetes user.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Cloud Native
  - DevOps
  - Infrastructure
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/kubernetes-operators/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: kubernetes-operators:kubernetes-operators
    name: Kubernetes Operators
    description: Kubernetes Operators extend the Kubernetes API for managing complex stateful applications using custom resources and controllers. An Operator encodes the operational knowledge of a domain expert into software that automates the deployment, scaling, and management of Kubernetes applications.
    humanURL: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
    tags:
      - Automation
      - Cloud Native
      - Custom Resources
      - Kubernetes
    properties:
      - type: Documentation
        url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
      - type: Reference
        url: https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/
      - type: AsyncAPI
        url: asyncapi/kubernetes-operators-watch-asyncapi.yml
  - aid: kubernetes-operators:custom-resource-definitions
    name: Kubernetes Custom Resource Definitions
    description: The CustomResourceDefinition (CRD) API lets you extend the Kubernetes API by defining new resource types with custom schemas. When a CRD is created, the Kubernetes API server automatically serves and handles storage for the new custom resource, enabling operators and other controllers to manage domain-specific objects.
    humanURL: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
    tags:
      - API Extension
      - Cloud Native
      - Custom Resources
      - Kubernetes
    properties:
      - type: Documentation
        url: https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/
      - type: Reference
        url: https://kubernetes.io/docs/reference/kubernetes-api/extend-resources/custom-resource-definition-v1/
      - type: Getting Started
        url: https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/
      - type: OpenAPI
        url: openapi/kubernetes-crd-openapi.yml
      - type: JSONSchema
        url: json-schema/kubernetes-operator-schema.json
  - aid: kubernetes-operators:operator-sdk
    name: Operator SDK
    description: The Operator SDK is a framework for building Kubernetes Operators in Go, Ansible, or Helm. It provides high-level APIs, abstractions, scaffolding tools, and CLI commands that simplify writing operator logic and integrating with the Operator Lifecycle Manager (OLM) for packaging and distribution.
    humanURL: https://sdk.operatorframework.io/
    tags:
      - Go
      - Kubernetes
      - Operators
      - SDK
    properties:
      - type: Documentation
        url: https://sdk.operatorframework.io/docs/overview/
      - type: Getting Started
        url: https://sdk.operatorframework.io/docs/building-operators/golang/tutorial/
      - type: GitHubRepository
        url: https://github.com/operator-framework/operator-sdk
  - aid: kubernetes-operators:operator-lifecycle-manager
    name: Operator Lifecycle Manager
    description: The Operator Lifecycle Manager (OLM) extends Kubernetes with a declarative API for installing, upgrading, and managing the lifecycle of Operators and their dependencies in a cluster. OLM provides cluster administrators with fine-grained control over what operators are available and which namespaces they can operate in.
    humanURL: https://olm.operatorframework.io/
    tags:
      - Cloud Native
      - Kubernetes
      - Lifecycle Management
      - Operators
    properties:
      - type: Documentation
        url: https://olm.operatorframework.io/docs/
      - type: GitHubRepository
        url: https://github.com/operator-framework/operator-lifecycle-manager
      - type: Change Log
        url: https://github.com/operator-framework/operator-lifecycle-manager/releases
      - type: OpenAPI
        url: openapi/kubernetes-olm-openapi.yml
  - aid: kubernetes-operators:operatorhub
    name: OperatorHub
    description: OperatorHub.io is a community registry of Kubernetes Operators that can be discovered and installed via the Operator Lifecycle Manager. It provides a catalog of operators across categories including databases, monitoring, security, and networking for use in Kubernetes clusters.
    humanURL: https://operatorhub.io/
    tags:
      - Community
      - Kubernetes
      - Operators
      - Registry
    properties:
      - type: Documentation
        url: https://operatorhub.io/
  - aid: kubernetes-operators:controller-runtime
    name: Controller-Runtime
    description: controller-runtime is a set of Go libraries for building Kubernetes controllers and operators. It is used by both Kubebuilder and Operator SDK and provides core abstractions including Manager, Client, Cache, and Reconciler interfaces for building controllers that interact with the Kubernetes API.
    humanURL: https://github.com/kubernetes-sigs/controller-runtime
    tags:
      - Controllers
      - Go
      - Kubernetes
      - SDK
    properties:
      - type: Documentation
        url: https://pkg.go.dev/sigs.k8s.io/controller-runtime
      - type: GitHubRepository
        url: https://github.com/kubernetes-sigs/controller-runtime
common:
  - type: Website
    url: https://kubernetes.io
  - type: Documentation
    url: https://kubernetes.io/docs/concepts/extend-kubernetes/
  - type: Getting Started
    url: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
  - type: GitHub Organization
    url: https://github.com/operator-framework
  - type: GitHubRepository
    url: https://github.com/operator-framework/operator-sdk
  - type: Blog
    url: https://kubernetes.io/blog/
  - type: Community
    url: https://kubernetes.io/community/
  - type: Change Log
    url: https://kubernetes.io/releases/
  - type: JSONSchema
    url: json-schema/kubernetes-operator-schema.json
  - type: JSON-LD
    url: json-ld/kubernetes-operators-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
