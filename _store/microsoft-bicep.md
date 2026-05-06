---
name: Microsoft Bicep
description: Microsoft Bicep is a domain-specific language (DSL) that uses declarative syntax to deploy Azure resources. It provides a transparent abstraction over ARM templates and offers a more concise syntax, improved type safety, and better support for modularity and code reuse.
image: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/media/bicep-logo.png
url: https://github.com/Azure/bicep
created: '2024-01-15'
modified: '2026-04-28'
specificationVersion: '0.18'
tags:
  - ARM Templates
  - Azure
  - Cloud
  - Deployment
  - DevOps
  - Infrastructure as Code
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: GitHub Organization
    url: https://github.com/Azure
  - type: Blog
    url: https://devblogs.microsoft.com/azure-sdk/
  - type: Support
    url: https://docs.microsoft.com/en-us/answers/topics/azure-bicep.html
  - type: Learning Resources
    url: https://docs.microsoft.com/en-us/azure/azure-resource-manager/bicep/learn-bicep
  - type: Bicep Examples
    url: https://github.com/Azure/bicep/tree/main/docs/examples
  - type: Release Notes
    url: https://github.com/Azure/bicep/releases
  - type: Contributing Guide
    url: https://github.com/Azure/bicep/blob/main/CONTRIBUTING.md
  - type: License
    url: https://github.com/Azure/bicep/blob/main/LICENSE
  - type: JSON-LD
    url: json-ld/microsoft-bicep-context.jsonld
  - type: JSONSchema
    url: json-schema/microsoft-bicep-deployment-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-bicep-template-spec-schema.json
include:
  - name: Azure Resource Manager APIs
    url: https://management.azure.com
  - name: Azure Template Specs
    url: https://docs.microsoft.com/en-us/azure/azure-resource-manager/templates/template-specs
  - name: Azure Container Registry (for Bicep modules)
    url: https://azure.microsoft.com/en-us/services/container-registry/
---
