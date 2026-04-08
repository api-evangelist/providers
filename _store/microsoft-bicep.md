---
aid: microsoft-bicep
url: https://raw.githubusercontent.com/api-evangelist/microsoft-bicep/refs/heads/main/apis.yml
apis:
- name: Bicep CLI
  description: Command-line interface for compiling and deploying Bicep files.
  image: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/media/bicep-logo.png
  baseURL: https://github.com/Azure/bicep
  humanURL: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/
  properties:
  - type: Documentation
    url: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/
  - type: GitHub Repository
    url: https://github.com/Azure/bicep
  - type: Installation Guide
    url: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/install
  - type: Bicep Playground
    url: https://bicepdemo.z22.web.core.windows.net/
  contact:
  - type: GitHub Issues
    url: https://github.com/Azure/bicep/issues
  - type: Twitter
    url: https://twitter.com/Azure
- name: Bicep Language Server
  description: Language server implementation for Bicep providing IntelliSense and validation.
  baseURL: https://github.com/Azure/bicep
  humanURL: https://github.com/Azure/bicep/tree/main/src/Bicep.LangServer
  properties:
  - type: Documentation
    url: https://github.com/Azure/bicep/blob/main/docs/contributing/language-server.md
  - type: GitHub Repository
    url: https://github.com/Azure/bicep/tree/main/src/Bicep.LangServer
  - type: VS Code Extension
    url: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-bicep
- name: Bicep Deployments REST API
  description: Azure Resource Manager Deployments REST API used by Microsoft Bicep to deploy infrastructure as code templates. Provides operations for creating, validating, and managing ARM/Bicep template deployments at resource group, subscription, management group, and tenant scopes.
  baseURL: https://management.azure.com
  humanURL: https://learn.microsoft.com/en-us/rest/api/resources/deployments
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/resources/deployments
  - type: OpenAPI
    url: openapi/microsoft-bicep-deployments-openapi.yml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/authenticate-multi-tenant
- name: Bicep Template Specs REST API
  description: Azure Resource Manager Template Specs REST API used by Microsoft Bicep for publishing and managing reusable infrastructure templates. Template Specs allow you to store ARM/Bicep templates as Azure resources for versioning, sharing, and access control across your organization.
  baseURL: https://management.azure.com
  humanURL: https://learn.microsoft.com/en-us/rest/api/resources/template-specs
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/resources/template-specs
  - type: OpenAPI
    url: openapi/microsoft-bicep-template-specs-openapi.yml
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/authenticate-multi-tenant
name: Microsoft Bicep
tags:
- ARM Templates
- Azure
- Cloud
- Deployment
- DevOps
- Infrastructure as Code
type: Contract
image: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/media/bicep-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Microsoft Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources. It provides a transparent abstraction over ARM templates and offers a more concise syntax, improved type safety, and better support for modularity and code reuse.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

