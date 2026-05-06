---
aid: azure-test-labs
name: Azure DevTest Labs
description: Azure DevTest Labs enables developers to efficiently self-manage virtual machines and PaaS resources without waiting for approvals. DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates for development and testing purposes.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Development
  - Infrastructure
  - Labs
  - Testing
  - Virtual Machines
url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: azure-test-labs:azure-devtest-labs-api
    name: Azure DevTest Labs API
    description: The DevTest Labs Client enables you to manage virtual machines, environments, artifacts, formulas, and custom images for development and testing purposes.
    humanURL: https://azure.microsoft.com/en-us/services/devtest-lab/
    baseURL: https://management.azure.com
    tags:
      - Artifacts
      - Environments
      - Labs
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/devtest-labs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/Azure/azure-rest-api-specs/main/specification/devtestlabs/resource-manager/Microsoft.DevTestLab/stable/2018-09-15/DevTestLabs.json
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://docs.microsoft.com/en-us/azure/devtest-labs/
  - type: Getting Started
    url: https://azure.microsoft.com/en-us/get-started/
  - type: Status
    url: https://status.azure.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/rules/azure-test-labs-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/vocabulary/azure-test-labs-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/json-ld/azure-test-labs-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/capabilities/azure-test-labs-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/capabilities/shared/azure-test-labs.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
