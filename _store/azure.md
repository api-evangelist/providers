---
aid: azure
url: https://raw.githubusercontent.com/api-evangelist/azure/refs/heads/main/apis.yml
apis:
- aid: azure:azure-compute-api
  name: Azure Compute API
  description: Manage virtual machines, containers, and serverless computing resources.
  humanURL: https://azure.microsoft.com/en-us/products/category/compute
  baseURL: https://management.azure.com
  tags:
  - Containers
  - Functions
  - Kubernetes
  - Virtual Machines
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/compute/
- aid: azure:azure-storage-api
  name: Azure Storage API
  description: Scalable cloud storage for data objects, files, messages, and more.
  humanURL: https://azure.microsoft.com/en-us/products/category/storage
  baseURL: https://management.azure.com
  tags:
  - Blob Storage
  - File Storage
  - Queue Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/storageservices/
- aid: azure:azure-cognitive-services-api
  name: Azure Cognitive Services API
  description: Add AI capabilities including vision, speech, language, and decision-making.
  humanURL: https://azure.microsoft.com/en-us/products/cognitive-services
  baseURL: https://{region}.api.cognitive.microsoft.com
  tags:
  - Artificial Intelligence
  - Computer Vision
  - Natural Language
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/cognitive-services/
name: Microsoft Azure
tags:
- Cloud Computing
- Databases
- Infrastructure
- Machine Learning
- Networking
- Platform as a Service
- Storage
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Azure is a comprehensive cloud computing platform offering IaaS, PaaS, and SaaS solutions for building, deploying, and managing applications through Microsoft's global network of datacenters.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

