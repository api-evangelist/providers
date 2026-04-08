---
aid: google-anthos
url: https://raw.githubusercontent.com/api-evangelist/google-anthos/refs/heads/main/apis.yml
apis:
- aid: google-anthos:gke-on-prem-api
  name: GKE On-Prem API
  description: The GKE On-Prem API provides programmatic access to manage the lifecycle of on-premises Kubernetes clusters running on VMware or bare metal infrastructure as part of Google Distributed Cloud. Developers can use the API to create, update, delete, and monitor on-premises clusters, manage node pools, and handle cluster enrollment and upgrades through the Google Cloud control plane.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/anthos/clusters/docs/on-prem-api/overview
  baseURL: https://gkeonprem.googleapis.com
  tags:
  - Bare Metal
  - Clusters
  - Kubernetes
  - On-Premises
  - VMware
  properties:
  - type: Documentation
    url: https://cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest
  - type: OpenAPI
    url: openapi/gke-on-prem-api-openapi.yml
  - type: JSONSchema
    url: json-schema/google-anthos-cluster-schema.json
- aid: google-anthos:anthos-multicloud-api
  name: Anthos Multicloud API
  description: The Anthos Multicloud API provides programmatic access to manage Anthos clusters running on other public clouds such as AWS and Azure. Developers can use the API to create, update, and delete attached clusters and manage node pools on external cloud providers while maintaining centralized management through Google Cloud.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/anthos/clusters/docs/multi-cloud
  baseURL: https://gkemulticloud.googleapis.com
  tags:
  - AWS
  - Azure
  - Clusters
  - Multi-Cloud
  properties:
  - type: Documentation
    url: https://cloud.google.com/anthos/clusters/docs/multi-cloud
name: Google Anthos
tags:
- Container Platform
- Hybrid Cloud
- Kubernetes
- Multi-Cloud
- On-Premises
- Service Mesh
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Anthos is a managed application platform that extends Google Cloud services and engineering practices to hybrid and multi-cloud environments. Built on Kubernetes, Anthos enables consistent development and operations across on-premises data centers, Google Cloud, and other public clouds like AWS and Azure, with centralized management, policy enforcement, and service mesh capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

