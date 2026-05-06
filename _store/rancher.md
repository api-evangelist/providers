---
aid: rancher
name: Rancher
description: Rancher is an open source container management platform built by SUSE that provides a complete software stack for teams adopting containers. It simplifies Kubernetes cluster deployment and management across any infrastructure, providing unified security, policy, and user management across all clusters. The Rancher Management API exposes these capabilities as Kubernetes-style REST resources for automation and platform engineering.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cluster Management
  - Containers
  - Kubernetes
  - Multi-Cluster
  - Open Source
  - SUSE
  - Platform Engineering
url: https://raw.githubusercontent.com/api-evangelist/rancher/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rancher:rancher-management-api
    name: Rancher Management API
    description: The Rancher Management API exposes Rancher's multi-cluster Kubernetes management capabilities as Kubernetes-style REST resources. It supports automation of cluster lifecycle, project and namespace management, user and access control, catalog and app management, and integration of Rancher into CI/CD and platform engineering workflows. Authentication is via bearer tokens generated from the Rancher UI or via the login endpoint, and the API is reached through the Rancher server URL.
    humanURL: https://ranchermanager.docs.rancher.com/api/quickstart
    baseURL: https://{rancher_host}/v3
    tags:
      - Cluster Management
      - Containers
      - Kubernetes
      - Multi-Cluster
      - Open Source
      - SUSE
    properties:
      - type: Documentation
        url: https://ranchermanager.docs.rancher.com/
      - type: Getting Started
        url: https://ranchermanager.docs.rancher.com/getting-started/overview
      - type: API Quick Start
        url: https://ranchermanager.docs.rancher.com/api/quickstart
      - type: OpenAPI
        url: openapi/rancher-management-api-openapi.yml
      - type: JSONSchema
        url: json-schema/rancher-cluster.json
      - type: JSONSchema
        url: json-schema/rancher-project.json
      - type: JSONSchema
        url: json-schema/rancher-node.json
      - type: JSONLD
        url: json-ld/rancher-context.jsonld
      - type: JSONStructure
        url: json-structure/rancher-cluster-structure.json
      - type: JSONStructure
        url: json-structure/rancher-project-structure.json
      - type: JSONStructure
        url: json-structure/rancher-node-structure.json
      - type: Example
        url: examples/rancher-list-clusters-example.json
      - type: Example
        url: examples/rancher-create-cluster-example.json
      - type: Example
        url: examples/rancher-list-projects-example.json
      - type: SpectralRules
        url: rules/rancher-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/cluster-lifecycle.yaml
      - type: NaftikoCapabilities
        url: capabilities/access-control.yaml
common:
  - type: Website
    url: https://www.rancher.com/
  - type: Documentation
    url: https://ranchermanager.docs.rancher.com/
  - type: GitHub Organization
    url: https://github.com/rancher
  - type: GitHub Repository
    url: https://github.com/rancher/rancher
  - type: Blog
    url: https://www.suse.com/c/rancher/
  - type: Pricing
    url: https://www.rancher.com/pricing
  - type: Sign Up
    url: https://www.rancher.com/quick-start
  - type: Support
    url: https://www.rancher.com/support-maintenance-terms
  - type: Vocabulary
    url: vocabulary/rancher-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
