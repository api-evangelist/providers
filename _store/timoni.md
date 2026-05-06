---
aid: timoni
name: Timoni
description: Timoni is a package manager for Kubernetes powered by CUE that provides a type-safe alternative to Helm charts. It enables software vendors to define complex application deployments packaged as Modules using CUE definitions, distributed as OCI artifacts in container registries with semantic versioning and cryptographic signing.
type: Index
position: Consumer
access: Open Source
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Kubernetes
  - Package Manager
  - CUE
created: '2026-03-26'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: timoni:timoni
    name: Timoni Module Registry API
    description: Timoni modules are distributed as OCI artifacts in container registries. The registry API provides operations for listing module tags, retrieving OCI manifests, and downloading module blobs containing CUE definitions and Kubernetes configurations.
    humanURL: https://timoni.sh/
    baseURL: https://ghcr.io
    tags:
      - Containers
      - Kubernetes
      - Package Manager
      - OCI Registry
    properties:
      - type: Documentation
        url: https://timoni.sh/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/openapi/timoni-openapi.yml
      - type: GitHub Repository
        url: https://github.com/stefanprodan/timoni
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-schema/timoni-module-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-structure/timoni-module-structure.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-ld/timoni-context.jsonld
features:
  - Type-safe Kubernetes configuration via CUE
  - OCI artifact distribution and signing
  - Semantic versioning for modules
  - Bundle-based multi-instance management
  - Kubernetes CRD lifecycle management
  - Drift detection and correction
  - Bundle Runtime API for dynamic configuration
  - Cryptographic signing and verification
useCases:
  - Kubernetes application packaging and distribution
  - Type-safe alternative to Helm charts
  - Multi-service deployment orchestration
  - GitOps-compatible application delivery
  - Kubernetes module versioning and rollback
integrations:
  - GitHub Container Registry (ghcr.io)
  - Docker Hub
  - Any OCI-compatible container registry
  - Kubernetes clusters
  - Flux CD
solutions:
  - Cloud-native application delivery
  - Kubernetes package management
  - Infrastructure as code
  - CUE-based configuration management
common:
  - type: Website
    url: https://timoni.sh/
  - type: Documentation
    url: https://timoni.sh/
  - type: GitHub Organization
    url: https://github.com/stefanprodan/timoni
  - type: Getting Started
    url: https://timoni.sh/quickstart/
  - type: Concepts
    url: https://timoni.sh/concepts/
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/openapi/timoni-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-schema/timoni-module-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/json-ld/timoni-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/timoni/refs/heads/main/vocabulary/timoni-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
