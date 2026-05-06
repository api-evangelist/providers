---
aid: nutanix
name: Nutanix
description: Nutanix is a hyper-converged infrastructure solution that integrates compute, virtualization, storage, networking, and security to power enterprise applications. Nutanix provides public APIs for managing and automating infrastructure including Prism Central, Prism Element, Karbon Kubernetes, Nutanix Database Service (NDB), Cloud Clusters (NC2), NCM Self-Service, and the GA v4 API platform.
type: Index
position: Producer
access: 1st-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Management
  - Hyperconverged
  - Infrastructure
  - Virtualization
  - Kubernetes
  - Database
url: https://raw.githubusercontent.com/api-evangelist/nutanix/refs/heads/main/apis.yml
created: '2025-03-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: nutanix:prism-central-v3
    name: Nutanix Prism Central API V3
    description: RESTful API for managing Nutanix clusters, VMs, storage, networking, and other infrastructure components through Prism Central. The v3 API uses an intent-based model where resources are defined by their desired state.
    humanURL: https://www.nutanix.dev/api_references/prism-central-v3/
    baseURL: https://{{prism-central-ip}}:9440/api/nutanix/v3
    tags:
      - Cloud Management
      - Infrastructure
      - Virtualization
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_references/prism-central-v3/
      - type: Authentication
        url: https://www.nutanix.dev/api_references/prism-central-v3/#authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nutanix/refs/heads/main/openapi/nutanix-prism-central-v3-openapi.yml
  - aid: nutanix:prism-central-v4
    name: Nutanix Prism Central API V4
    description: The next-generation v4 API for managing the Nutanix Cloud Platform through Prism Central with GA SDKs for Python, Java, Go, and JavaScript. The v4 API is now the recommended version for production environments.
    humanURL: https://www.nutanix.dev/api-reference-v4/
    baseURL: https://{{prism-central-ip}}:9440/api
    tags:
      - Cloud Management
      - Infrastructure
      - SDK
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api-reference-v4/
      - type: Getting Started
        url: https://www.nutanix.dev/nutanix-api-user-guide/
      - type: SDKs
        url: https://www.nutanix.dev/sdk_reference/
      - type: Change Log
        url: https://www.nutanix.dev/api-versions/
      - type: Developer Portal
        url: https://developers.nutanix.com/
  - aid: nutanix:prism-element-v2
    name: Nutanix Prism Element API V2
    description: Cluster-local API for managing individual Nutanix clusters through Prism Element, including storage containers, hosts, virtual machines, and cluster operations.
    humanURL: https://www.nutanix.dev/api_references/prism-element/
    baseURL: https://{{cluster-ip}}:9440/PrismGateway/services/rest/v2.0
    tags:
      - Cluster Management
      - Infrastructure
      - Storage
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_references/prism-element/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/nutanix/refs/heads/main/openapi/nutanix-prism-element-v2-openapi.yml
  - aid: nutanix:karbon
    name: Nutanix Karbon API
    description: API for managing Kubernetes clusters through Nutanix Karbon, including cluster lifecycle, upgrades, and configuration.
    humanURL: https://www.nutanix.dev/api_references/karbon/
    tags:
      - Container Management
      - Kubernetes
      - Orchestration
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_references/karbon/
  - aid: nutanix:ndb
    name: Nutanix Database Service API
    description: REST API for Nutanix Database Service (NDB) providing database-as-a-service capabilities for PostgreSQL, MySQL, SQL Server, Oracle, and MongoDB.
    humanURL: https://www.nutanix.dev/api_reference/apis/ndb0.9.html
    tags:
      - Database
      - DBaaS
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_reference/apis/ndb0.9.html
  - aid: nutanix:nc2
    name: Nutanix Cloud Clusters API
    description: REST API for Nutanix Cloud Clusters (NC2), enabling creation and management of Nutanix clusters on AWS and Azure public clouds.
    humanURL: https://www.nutanix.dev/api_reference/apis/nc2.html
    baseURL: https://api.nutanix.com
    tags:
      - AWS
      - Azure
      - Hybrid Cloud
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_reference/apis/nc2.html
  - aid: nutanix:ncm-self-service
    name: Nutanix NCM Self-Service API
    description: API for Nutanix Cloud Manager Self-Service (formerly Calm), enabling automation of application deployment and lifecycle management through blueprints and runbooks.
    humanURL: https://www.nutanix.dev/api_references/ncm-self-service/
    tags:
      - Automation
      - Application Management
      - Orchestration
      - DevOps
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_references/ncm-self-service/
  - aid: nutanix:foundation
    name: Nutanix Foundation API
    description: API for Foundation and Foundation Central, enabling automated cluster deployment and remote node imaging.
    humanURL: https://www.nutanix.dev/api_references/foundation/
    tags:
      - Cluster Deployment
      - Automation
    properties:
      - type: Documentation
        url: https://www.nutanix.dev/api_references/foundation/
common:
  - type: Website
    url: https://www.nutanix.com
  - type: Documentation
    url: https://www.nutanix.dev/
  - type: Getting Started
    url: https://www.nutanix.dev/nutanix-api-user-guide/
  - type: SDKs
    url: https://www.nutanix.dev/sdk_reference/
  - type: Reference
    url: https://www.nutanix.dev/api_references/
  - type: Code Samples
    url: https://www.nutanix.dev/code_samples/
  - type: Change Log
    url: https://www.nutanix.dev/api-versions/
  - type: Blog
    url: https://www.nutanix.dev/blog/
  - type: Community
    url: https://next.nutanix.com/
  - type: Support
    url: https://www.nutanix.com/support-services/product-support
  - type: Status
    url: https://status.nutanix.com/
  - type: Login
    url: https://my.nutanix.com/
  - type: Sign Up
    url: https://my.nutanix.com/page/signup
  - type: GitHub Organization
    url: https://github.com/nutanix
  - type: Developer Portal
    url: https://developers.nutanix.com/
  - type: Terms of Service
    url: https://www.nutanix.com/legal/terms-of-use
  - type: Privacy Policy
    url: https://www.nutanix.com/legal/privacy-notice
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
