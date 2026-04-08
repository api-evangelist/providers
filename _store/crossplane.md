---
aid: crossplane
url: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/apis.yml
apis:
- aid: crossplane:crossplane-kubernetes-api
  name: Crossplane Kubernetes API
  description: The Crossplane Kubernetes API extends the Kubernetes API with custom resources including Compositions, CompositeResourceDefinitions (XRDs), Providers, ProviderConfigs, and Claims. These resources allow declarative management of cloud infrastructure and services through standard Kubernetes manifests and the kubectl CLI.
  humanURL: https://docs.crossplane.io/latest/api/
  baseURL: https://kubernetes.default.svc
  tags:
  - Control Plane
  - Infrastructure as Code
  - Kubernetes
  properties:
  - type: Documentation
    url: https://docs.crossplane.io/latest/
  - type: Reference
    url: https://docs.crossplane.io/latest/api/
  - type: Getting Started
    url: https://docs.crossplane.io/latest/get-started/get-started-with-composition/
  - type: OpenAPI
    url: openapi/crossplane-kubernetes-api-openapi.yml
  - type: JSONSchema
    url: json-schema/crossplane-composition-schema.json
  - type: JSONSchema
    url: json-schema/crossplane-xrd-schema.json
  - type: JSONSchema
    url: json-schema/crossplane-provider-schema.json
  - type: JSON-LD
    url: json-ld/crossplane-context.jsonld
  - type: Change Log
    url: https://github.com/crossplane/crossplane/releases
name: Crossplane
tags:
- Cloud Native
- Control Plane
- Infrastructure as Code
- Kubernetes
- Multi-Cloud
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Open source Kubernetes add-on that transforms your cluster into a universal control plane, enabling you to manage cloud infrastructure, services, and applications using Kubernetes-style declarative configuration. Crossplane is a graduated Cloud Native Computing Foundation project.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

