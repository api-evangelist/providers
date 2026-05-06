---
aid: operator-framework
name: Operator Framework
description: The Operator Framework is a CNCF incubating toolkit for building and managing Kubernetes Operators. It includes the Operator SDK for scaffolding and building operators using Go, Ansible, or Helm, the Operator Lifecycle Manager (OLM) for installing and managing operators on clusters, and OperatorHub for discovering and sharing operators. The framework codifies operational knowledge into software.
url: https://operatorframework.io
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Cloud Native
  - Incubating
  - Kubernetes
  - Lifecycle Management
  - Operators
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
apis:
  - aid: operator-framework:olm-api
    name: Operator Lifecycle Manager API
    description: OLM extends Kubernetes with CRDs for operator lifecycle management including ClusterServiceVersion for describing operator capabilities and requirements, Subscription for tracking update channels, InstallPlan for managing operator installation, CatalogSource for defining operator repositories, and OperatorGroup for multi-tenant operator deployment scoping.
    humanURL: https://olm.operatorframework.io/docs/
    properties:
      - type: Documentation
        url: https://olm.operatorframework.io/docs/
    tags:
      - Installation
      - Lifecycle Management
      - Updates
  - aid: operator-framework:operator-sdk
    name: Operator SDK
    description: The Operator SDK provides tools for building Kubernetes operators. It includes scaffolding commands, code generation for CRD types and controllers, integration testing harness, scorecard for validating operator quality, and bundle commands for packaging operators for distribution through OLM catalogs.
    humanURL: https://sdk.operatorframework.io/docs/
    properties:
      - type: Documentation
        url: https://sdk.operatorframework.io/docs/
    tags:
      - Code Generation
      - Scaffolding
      - SDK
common:
  - type: Documentation
    name: Operator Framework Documentation
    description: Official Operator Framework documentation.
    url: https://operatorframework.io/
  - type: GitHubOrg
    name: Operator Framework GitHub
    description: Source code repositories.
    url: https://github.com/operator-framework
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
