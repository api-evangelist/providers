---
aid: operator-framework
url: https://raw.githubusercontent.com/api-evangelist/operator-framework/refs/heads/main/apis.yml
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
name: Operator Framework
tags:
- Automation
- Cloud Native
- Incubating
- Kubernetes
- Lifecycle Management
- Operators
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Operator Framework is a CNCF incubating toolkit for building and managing Kubernetes Operators. It includes the Operator SDK for scaffolding and building operators using Go, Ansible, or Helm, the Operator Lifecycle Manager (OLM) for installing and managing operators on clusters, and OperatorHub for discovering and sharing operators. The framework codifies operational knowledge into software.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

