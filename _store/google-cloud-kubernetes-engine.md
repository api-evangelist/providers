---
aid: google-cloud-kubernetes-engine
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-kubernetes-engine/refs/heads/main/apis.yml
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
name: Google Cloud Kubernetes Engine
tags:
- Compute
- Containers
- GKE
- Google Cloud
- Kubernetes
- Orchestration
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Kubernetes Engine (GKE) provides a managed environment for deploying, managing, and scaling containerized applications using Google infrastructure. GKE runs on Kubernetes, providing automated cluster management, auto-scaling, auto-repair, and integrated logging and monitoring for container workloads.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

