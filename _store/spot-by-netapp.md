---
aid: spot-by-netapp
name: Spot by NetApp
description: Spot by NetApp (formerly Spot by Flexera, originally Spotinst) is a cloud infrastructure optimization platform providing automated cost optimization, scaling, and intelligent management for cloud workloads across AWS, Azure, and GCP. The Spot platform includes Elastigroup for intelligent auto-scaling using Spot instances, Ocean for Kubernetes and container cost optimization, Stateful Nodes for stateful workloads, EMR Scaler for Hadoop workloads, and Ocean CD for progressive delivery. The platform delivers FinOps capabilities including rightsizing recommendations, cost analysis, and cloud spend visibility.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Optimization
  - FinOps
  - Kubernetes
  - AWS
  - Azure
  - GCP
  - Cost Optimization
  - Auto Scaling
created: '2026-03-27'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/spot-by-netapp/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: spot-by-netapp:spot-by-netapp
    name: Spot by NetApp API
    description: The Spot by NetApp REST API enables programmatic management of cloud infrastructure optimization resources. Manage Elastigroup auto-scaling groups across AWS, Azure, and GCP; create and configure Ocean clusters for Kubernetes cost optimization; set up Stateful Nodes for persistent workloads; retrieve cost analysis and savings reports; access rightsizing recommendations; and manage account configuration, API tokens, audit logs, and notification subscriptions. Bearer token authentication required.
    humanURL: https://spot.io/
    baseURL: https://api.spotinst.io
    tags:
      - Cloud Optimization
      - FinOps
      - Kubernetes
      - AWS
      - Azure
      - GCP
      - Auto Scaling
      - Spot Instances
      - Cost Management
      - DevOps
    properties:
      - type: Documentation
        url: https://docs.spot.io/
      - type: Reference
        url: https://docs.spot.io/api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/spot-by-netapp/refs/heads/main/openapi/spot-by-netapp-openapi.yml
      - type: Getting Started
        url: https://docs.spot.io/
      - type: GitHub
        url: https://github.com/spotinst/openapi
common:
  - type: Website
    url: https://spot.io/
  - type: Portal
    url: https://docs.spot.io/
  - type: Documentation
    url: https://docs.spot.io/
  - type: Reference
    url: https://docs.spot.io/api/
  - type: GitHub
    url: https://github.com/spotinst
  - type: SDK
    url: https://github.com/spotinst/spotinst-sdk-go
  - type: SDK
    url: https://github.com/spotinst/spotinst-sdk-java
  - type: SDK
    url: https://github.com/spotinst/spotinst-sdk-nodejs
  - type: SDK
    url: https://github.com/spotinst/spotinst-sdk-python
  - type: Terraform
    url: https://github.com/spotinst/terraform-provider-spotinst
  - type: Helm
    url: https://github.com/spotinst/spotinst-kubernetes-helm-charts
  - type: CLI
    url: https://github.com/spotinst/spotctl
  - type: Console
    url: https://console.spotinst.com/
  - type: Login
    url: https://console.spotinst.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
