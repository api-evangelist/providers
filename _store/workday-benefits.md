---
aid: workday-benefits
name: Workday Benefits
description: APIs for managing employee benefits, enrollments, and benefits administration in Workday.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-benefits/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: Workday Benefits API
    description: Comprehensive API for managing employee benefits including health insurance, retirement plans, time off, and other benefit programs.
    image: https://www.workday.com/content/dam/web/images/logo.png
    humanURL: https://www.workday.com/en-us/products/human-capital-management/benefits.html
    baseURL: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Benefits
      - Employee Benefits
      - Enrollments
      - Health Insurance
      - Human Resources
      - Retirement
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits/v40.2/Get_Benefits.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Benefits/v40.2/Benefits.json
      - type: Authentication
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/bRN0dJVT1fKqLxCRjJCx6w
      - type: Postman Collection
        url: https://www.postman.com/workday/workspace/workday-rest-api
      - type: Rate Limits
        url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/VNmXGO5eT8oGWtOQRPd46w
      - type: Change Log
        url: https://community.workday.com/api-versions
      - type: Status Page
        url: https://status.workday.com
      - type: Terms of Service
        url: https://www.workday.com/en-us/legal.html
      - type: Support
        url: https://community.workday.com/
      - type: OpenAPI
        url: openapi/workday-benefits-openapi.yml
      - type: JSONSchema
        url: json-schema/workday-benefits-benefit-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-benefit-enrollment-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-benefit-enrollment-request-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-dependent-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-benefit-event-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-time-off-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-benefits-employee-benefits-schema.json
      - type: JSONStructure
        url: json-structure/workday-benefits-benefit-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-benefit-enrollment-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-benefit-enrollment-request-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-dependent-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-benefit-event-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-time-off-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-benefits-employee-benefits-structure.json
      - type: JSONLd
        url: json-ld/workday-benefits-context.jsonld
      - type: SpectralRules
        url: rules/workday-benefits-spectral-rules.yml
      - type: NaftikoCapability - Benefits Administration
        url: capabilities/benefits-administration.yaml
      - type: NaftikoCapability - Benefits (Shared)
        url: capabilities/shared/benefits.yaml
      - type: Vocabulary
        url: vocabulary/workday-benefits-vocabulary.yml
    contact:
      - type: Support
        url: https://community.workday.com/support
common:
  - type: Getting Started
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/_wTPrHlQFO6kuhPPQvXUdg
  - type: Developer Portal
    url: https://developer.workday.com
  - type: Authentication Guide
    url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/bRN0dJVT1fKqLxCRjJCx6w
  - type: SDKs
    url: https://github.com/Workday
  - type: Blog
    url: https://blog.workday.com/en-us/technology.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: JSON-LD
    url: json-ld/workday-benefits-context.jsonld
  - type: SpectralRules
    url: rules/workday-benefits-spectral-rules.yml
  - type: NaftikoCapability - Benefits Administration
    url: capabilities/benefits-administration.yaml
  - type: NaftikoCapability - Benefits (Shared)
    url: capabilities/shared/benefits.yaml
  - type: Vocabulary
    url: vocabulary/workday-benefits-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
