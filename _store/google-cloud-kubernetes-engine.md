---
aid: google-cloud-kubernetes-engine
name: Google Cloud Kubernetes Engine
description: Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling containerized applications using Google infrastructure. GKE runs on Kubernetes, providing automated cluster management, auto-scaling, auto-repair, and integrated logging and monitoring for container workloads.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-search/google-cloud-kubernetes-engine/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Compute
  - Containers
  - GKE
  - Google Cloud
  - Kubernetes
  - Orchestration
apis:
  - name: Google Kubernetes Engine API
    description: The GKE API enables programmatic management of Kubernetes clusters, including creating and deleting clusters, managing node pools, configuring cluster networking, and performing cluster upgrades.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cloud.google.com/kubernetes-engine/docs/reference/rest
    baseURL: https://container.googleapis.com
    tags:
      - Clusters
      - Containers
      - Kubernetes
      - Node Pools
      - Operations
    properties:
      - type: Documentation
        url: https://cloud.google.com/kubernetes-engine/docs/reference/rest
      - type: OpenAPI
        url: openapi/gke-openapi.yml
      - type: Authentication
        url: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication
      - type: Getting Started
        url: https://cloud.google.com/kubernetes-engine/docs/quickstart
      - type: JSONSchema
        url: json-schema/gke-cluster.json
common:
  - type: Portal
    url: https://cloud.google.com/kubernetes-engine
  - type: Getting Started
    url: https://cloud.google.com/kubernetes-engine/docs/quickstart
  - type: Documentation
    url: https://cloud.google.com/kubernetes-engine/docs
  - type: Authentication
    url: https://cloud.google.com/kubernetes-engine/docs/how-to/api-server-authentication
  - type: Pricing
    url: https://cloud.google.com/kubernetes-engine/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com/
  - type: Support
    url: https://cloud.google.com/kubernetes-engine/docs/support
  - type: JSON-LD
    url: json-ld/gke-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
