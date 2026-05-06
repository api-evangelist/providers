---
aid: workday-business-processes
name: Workday Business Processes
description: APIs for managing and executing business processes within Workday, including initiating, monitoring, and completing various workflow processes.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: Workday Business Process API
    description: API for initiating, managing, and monitoring business processes in Workday, including approvals, onboarding, and other workflow operations.
    image: https://www.workday.com/content/dam/web/images/logos/workday-logo.svg
    humanURL: https://www.workday.com/en-us/products/financial-management/business-process.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Approvals
      - Business Processes
      - Finance
      - HCM
      - Workflows
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Business_Process_Service/v41.1/Business_Process_Service.yaml
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wws-overview/wws-authentication.html
      - type: SDKs
        url: https://github.com/Workday
      - type: Rate Limits
        url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wws-overview/wws-rate-limits.html
      - type: Webhooks
        url: https://doc.workday.com/admin-guide/en-us/workday-integrations/integration-concepts/workday-webhooks.html
      - type: Changelog
        url: https://community.workday.com/api-release-notes
      - type: Status
        url: https://status.workday.com
      - type: Support
        url: https://community.workday.com
      - type: OpenAPI
        url: openapi/workday-business-processes-openapi.yml
      - type: JSONSchema
        url: json-schema/workday-business-processes-business-process-definition-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-process-instance-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-initiate-process-request-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-process-step-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-inbox-item-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-approval-request-schema.json
      - type: JSONSchema
        url: json-schema/workday-business-processes-denial-request-schema.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-business-process-definition-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-process-instance-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-initiate-process-request-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-process-step-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-inbox-item-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-approval-request-structure.json
      - type: JSONStructure
        url: json-structure/workday-business-processes-denial-request-structure.json
      - type: JSONLd
        url: json-ld/workday-business-processes-context.jsonld
      - type: SpectralRules
        url: rules/workday-business-processes-spectral-rules.yml
      - type: NaftikoCapability - Workflow Management
        url: capabilities/workflow-management.yaml
      - type: NaftikoCapability - Business Processes (Shared)
        url: capabilities/shared/business-processes.yaml
      - type: Vocabulary
        url: vocabulary/workday-business-processes-vocabulary.yml
    contact:
      - type: Support
        url: https://www.workday.com/en-us/company/customer-support.html
common:
  - type: Portal
    url: https://community.workday.com
  - type: Getting Started
    url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wws-overview/getting-started-with-workday-web-services.html
  - type: API Standards
    url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-overview.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Terms of Service
    url: https://www.workday.com/en-us/terms-of-service.html
  - type: Security
    url: https://www.workday.com/en-us/why-workday/our-technology/security.html
  - type: JSON-LD
    url: json-ld/workday-business-processes-context.jsonld
  - type: SpectralRules
    url: rules/workday-business-processes-spectral-rules.yml
  - type: NaftikoCapability - Workflow Management
    url: capabilities/workflow-management.yaml
  - type: NaftikoCapability - Business Processes (Shared)
    url: capabilities/shared/business-processes.yaml
  - type: Vocabulary
    url: vocabulary/workday-business-processes-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
