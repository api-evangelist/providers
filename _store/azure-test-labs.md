---
aid: azure-test-labs
url: https://raw.githubusercontent.com/api-evangelist/azure-test-labs/refs/heads/main/apis.yml
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
name: Azure DevTest Labs
tags:
- Development
- Infrastructure
- Labs
- Testing
- Virtual Machines
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Azure DevTest Labs enables developers to efficiently self-manage virtual machines and PaaS resources without waiting for approvals. DevTest Labs creates labs consisting of pre-configured bases or Azure Resource Manager templates for development and testing purposes.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

