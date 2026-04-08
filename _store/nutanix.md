---
aid: nutanix
url: https://raw.githubusercontent.com/api-evangelist/nutanix/refs/heads/main/apis.yml
apis:
- aid: nutanix:prism-central-v3
  name: Nutanix Prism Central API V3
  description: RESTful API for managing Nutanix clusters, VMs, storage, networking, and other infrastructure components through Prism Central.
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
- aid: nutanix:prism-central-v4
  name: Nutanix Prism Central API V4
  description: The next-generation v4 API for managing the Nutanix Cloud Platform through Prism Central with GA SDKs for Python, Java, Go, and JavaScript.
  humanURL: https://www.nutanix.dev/api-reference-v4/
  baseURL: https://{{prism-central-ip}}:9440/api
  tags:
  - Cloud Management
  - Infrastructure
  properties:
  - type: Documentation
    url: https://www.nutanix.dev/api-reference-v4/
  - type: Getting Started
    url: https://www.nutanix.dev/nutanix-api-user-guide/
  - type: SDKs
    url: https://www.nutanix.dev/sdk_reference/
  - type: Change Log
    url: https://www.nutanix.dev/api-versions/
- aid: nutanix:prism-element-v2
  name: Nutanix Prism Element API V2
  description: API for managing individual Nutanix clusters through Prism Element, including storage containers, hosts, and cluster operations.
  humanURL: https://www.nutanix.dev/api_references/prism-element/
  tags:
  - Cluster Management
  - Infrastructure
  properties:
  - type: Documentation
    url: https://www.nutanix.dev/api_references/prism-element/
- aid: nutanix:karbon
  name: Nutanix Karbon API
  description: API for managing Kubernetes clusters through Nutanix Karbon.
  humanURL: https://www.nutanix.dev/api_references/karbon/
  tags:
  - Container Management
  - Kubernetes
  properties:
  - type: Documentation
    url: https://www.nutanix.dev/api_references/karbon/
- aid: nutanix:ndb
  name: Nutanix Database Service API
  description: REST API for Nutanix Database Service providing database-as-a-service capabilities for PostgreSQL, MySQL, SQL Server, Oracle, and MongoDB.
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
name: Nutanix
tags:
- Cloud Management
- Hyperconverged
- Infrastructure
- Virtualization
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Nutanix is a hyper-converged infrastructure solution that integrates compute, virtualization, storage, networking, and security to power enterprise applications. Nutanix provides public APIs for managing and automating infrastructure including Prism Central, Karbon Kubernetes, Database Service, and Cloud Manager.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

