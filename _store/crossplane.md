---
aid: crossplane
name: Crossplane
x-type: opensource
description: Crossplane is a graduated CNCF open-source Kubernetes add-on that transforms a cluster into a universal control plane for cloud infrastructure, services, and applications. Crossplane introduces custom resources including CompositeResourceDefinitions (XRDs), Compositions, Claims, Providers, ProviderConfigs, Configurations, Functions, and EnvironmentConfigs, allowing platform teams to author self-service platform APIs that compose managed resources across AWS, GCP, Azure, and other providers using Kubernetes-style declarative configuration.
url: https://raw.githubusercontent.com/api-evangelist/crossplane/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache 2.0
  - CNCF
  - Cloud Native
  - Composition
  - Control Plane
  - Custom Resource Definitions
  - Graduated
  - Infrastructure as Code
  - Kubernetes
  - Multi-Cloud
  - Open Source
  - Platform Engineering
  - Providers
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
type: Index
access: Public
position: Provider
apis:
  - aid: crossplane:crossplane-kubernetes-api
    name: Crossplane Kubernetes API
    description: 'The Crossplane Kubernetes API extends the Kubernetes API server with custom resources for managing cloud infrastructure declaratively. Resources are organized into two main API groups: apiextensions.crossplane.io for composition primitives (Compositions, CompositeResourceDefinitions, EnvironmentConfigs, DeploymentRuntimeConfigs) and pkg.crossplane.io for package management (Providers, Functions, Configurations and their revisions). All operations use standard Kubernetes REST conventions and are authenticated through the Kubernetes API server''s authentication mechanisms.'
    humanURL: https://docs.crossplane.io/latest/api/
    baseURL: https://kubernetes.default.svc
    properties:
      - type: Documentation
        url: https://docs.crossplane.io/latest/
      - type: Reference
        url: https://docs.crossplane.io/latest/api/
      - type: GettingStarted
        url: https://docs.crossplane.io/latest/get-started/get-started-with-composition/
      - type: OpenAPI
        url: openapi/crossplane-kubernetes-api-openapi.yml
      - type: Rules
        url: rules/crossplane-kubernetes-api-rules.yml
      - type: Capabilities
        url: capabilities/crossplane-kubernetes-api-capabilities.yml
      - type: JSONSchema
        url: json-schema/crossplane-composition-schema.json
      - type: JSONSchema
        url: json-schema/crossplane-xrd-schema.json
      - type: JSONSchema
        url: json-schema/crossplane-provider-schema.json
      - type: JSONLD
        url: json-ld/crossplane-context.jsonld
      - type: ChangeLog
        url: https://github.com/crossplane/crossplane/releases
    tags:
      - Composition
      - Control Plane
      - Custom Resources
      - Infrastructure as Code
      - Kubernetes
      - Multi-Cloud
      - Platform Engineering
common:
  - type: JSONSchema
    url: json-schema/crossplane-composition-schema.json
  - type: JSONSchema
    url: json-schema/crossplane-xrd-schema.json
  - type: JSONSchema
    url: json-schema/crossplane-provider-schema.json
  - type: JSONLD
    url: json-ld/crossplane-context.jsonld
  - type: Vocabulary
    url: vocabulary/crossplane-vocabulary.yml
  - type: Website
    url: https://www.crossplane.io/
  - type: Documentation
    url: https://docs.crossplane.io/latest/
  - type: GettingStarted
    url: https://docs.crossplane.io/latest/get-started/get-started-with-composition/
  - type: Reference
    url: https://docs.crossplane.io/latest/api/
  - type: Blog
    url: https://blog.crossplane.io/
  - type: GitHubOrganization
    url: https://github.com/crossplane
  - type: GitHubRepository
    url: https://github.com/crossplane/crossplane
  - type: ChangeLog
    url: https://github.com/crossplane/crossplane/releases
  - type: Community
    url: https://docs.crossplane.io/latest/learn/
  - type: Contributing
    url: https://docs.crossplane.io/contribute/contribute/
  - type: License
    url: https://github.com/crossplane/crossplane/blob/main/LICENSE
  - type: CNCF
    url: https://www.cncf.io/projects/crossplane/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
