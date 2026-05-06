---
aid: densify
name: Densify
description: Densify (now Kubex) provides a machine learning powered cloud and container optimization platform that continuously right-sizes resources to reduce cost and improve performance across Kubernetes, public cloud, and virtualized environments. The Densify REST API exposes optimization analysis, recommendations, account and cluster inventory, and systems data so that optimization can be embedded into CI/CD pipelines, infrastructure as code templates, and FinOps workflows.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Cost
  - Container Optimization
  - FinOps
  - Kubernetes
  - Machine Learning
  - Recommendations
  - Right-Sizing
url: https://raw.githubusercontent.com/api-evangelist/densify/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Producer
access: 3rd-Party
apis:
  - aid: densify:public-cloud-api
    name: Densify Public Cloud API
    description: The Densify Public Cloud REST API exposes optimization analysis, recommendations, account and instance inventory, and systems data for AWS, Azure, and Google Cloud environments. The API uses JSON over HTTPS, follows a resource-oriented design under the /api/v2/ path, and authenticates with JWT bearer tokens obtained from the /authorize endpoint. Common use cases include integrating right-sizing recommendations into Terraform, CloudFormation, and CI/CD pipelines.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.densify.com/docs-api/WebHelp_Densify_API_Cloud/Content/API_Guide/Introduction.htm
    baseURL: https://api.densify.com/api/v2
    tags:
      - Cloud
      - FinOps
      - Optimization
      - Recommendations
      - Right-Sizing
    properties:
      - type: Documentation
        url: https://www.densify.com/docs-api/WebHelp_Densify_API_Cloud/Content/API_Guide/Introduction.htm
      - type: Reference
        url: https://www.densify.com/docs/WebHelp_Densify_Cloud/Content/Resources/PDFs/Densify-API-Reference-Guide.pdf
      - type: Postman
        url: https://www.densify.com/dev
    contact:
      - FN: Densify Support
        email: support@densify.com
        url: https://www.densify.com/contact
  - aid: densify:container-api
    name: Densify Container Optimization API
    description: The Densify Container Optimization REST API provides programmatic access to container right-sizing recommendations across Amazon EKS, AKS, GKE, OpenShift, and self-managed Kubernetes footprints. It exposes endpoints for clusters, namespaces, controllers, container groups, and recommended requests/limits for CPU and memory based on machine learned utilization patterns.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.densify.com/docs-api/WebHelp_Densify_API/Content/Densify_API.htm
    baseURL: https://api.densify.com/api/v2
    tags:
      - Containers
      - Kubernetes
      - Optimization
      - Recommendations
      - Right-Sizing
    properties:
      - type: Documentation
        url: https://www.densify.com/docs-api/WebHelp_Densify_API/Content/Densify_API.htm
      - type: Developer Resources
        url: https://www.densify.com/dev
    contact:
      - FN: Densify Support
        email: support@densify.com
        url: https://www.densify.com/contact
common:
  - type: Website
    url: https://www.densify.com
  - type: Portal
    url: https://portal.densify.com/
  - type: Documentation
    url: https://docs.densify.com
  - type: Developer Resources
    url: https://www.densify.com/dev
  - type: Documentation Landing
    url: https://portal.densify.com/docs-landing/
  - type: Resources
    url: https://www.densify.com/resources
  - type: Blog
    url: https://www.densify.com/blog
  - type: Pricing
    url: https://www.densify.com/pricing
  - type: Free Trial
    url: https://www.densify.com/free-trial
  - type: Support
    url: https://www.densify.com/support
  - type: GitHub Organization
    url: https://github.com/densify-dev
  - type: Terms of Service
    url: https://www.densify.com/legal
  - type: Privacy Policy
    url: https://www.densify.com/privacy-policy
  - type: Contact
    url: https://www.densify.com/contact
  - type: JSON-LD
    url: json-ld/densify-context.jsonld
  - type: Vocabulary
    url: vocabulary/densify-vocabulary.yml
  - type: Capabilities
    url: capabilities/densify-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
