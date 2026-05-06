---
aid: vmware-tanzu
name: VMware Tanzu
description: VMware Tanzu (now part of Broadcom) is a portfolio of products for modernizing applications and infrastructure with a common approach to building, running, and managing Kubernetes across multi-cloud environments. Key APIs include the Tanzu Service Mesh REST API for cluster and global namespace management, Kubernetes CRD-based APIs for VM Operator, Projects Operator, and NSX Operator, and the Tanzu CLI plugin runtime.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Containers
  - Enterprise
  - Kubernetes
  - Multi-Cloud
  - Service Mesh
  - VMware
url: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vmware-tanzu:tanzu-service-mesh-api
    name: VMware Tanzu Service Mesh API
    description: The Tanzu Service Mesh REST API provides programmatic access to manage clusters, global namespaces, resource groups, and service mesh policies. Authentication uses a CSP API token exchanged for a short-lived Bearer token. The API version is embedded in the URL path (e.g. /v1alpha1/).
    humanURL: https://docs.vmware.com/en/VMware-Tanzu-Service-Mesh/index.html
    tags:
      - Clusters
      - Global Namespaces
      - Kubernetes
      - Resource Groups
      - Service Mesh
    properties:
      - type: Documentation
        url: https://docs.vmware.com/en/VMware-Tanzu-Service-Mesh/services/api-programming-guide/GUID-6C5044B8-6950-42A6-87A5-3D88BEAE09DB.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/openapi/vmware-tanzu-service-mesh-openapi.yml
  - aid: vmware-tanzu:tanzu-kubernetes-grid-api
    name: VMware Tanzu Kubernetes Grid API
    description: Kubernetes-native API for provisioning and managing Tanzu Kubernetes clusters using the TanzuKubernetesCluster CRD (v1alpha1/v1alpha2). Runs on vSphere Supervisor clusters via the Tanzu Kubernetes Grid Service.
    humanURL: https://docs.vmware.com/en/VMware-vSphere/index.html
    tags:
      - Cluster Provisioning
      - Kubernetes
      - TKG
      - vSphere
    properties:
      - type: Documentation
        url: https://docs.vmware.com/en/VMware-vSphere/7.0/vmware-vsphere-with-tanzu/GUID-31BF8166-5FC8-4D43-933D-5797F3BE4A36.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/openapi/vmware-tanzu-kubernetes-grid-openapi.yml
      - type: KubernetesCRD
        url: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/crd/tanzukubernetescluster-crd.yaml
common:
  - type: Website
    url: https://tanzu.vmware.com/
  - type: Documentation
    url: https://docs.vmware.com/en/VMware-Tanzu/index.html
  - type: GitHub Organization
    url: https://github.com/vmware-tanzu
  - type: Blog
    url: https://tanzu.vmware.com/content/blog
  - type: Pricing
    url: https://tanzu.vmware.com/pricing
  - type: Sign Up
    url: https://tanzu.vmware.com/try
  - type: Broadcom TechDocs
    url: https://techdocs.broadcom.com/us/en/vmware-tanzu.html
  - type: CLI
    url: https://github.com/vmware-tanzu/tanzu-cli
  - type: Velero
    url: https://github.com/vmware-tanzu/velero
  - type: Sonobuoy
    url: https://github.com/vmware-tanzu/sonobuoy
  - type: Cartographer
    url: https://github.com/vmware-tanzu/cartographer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
