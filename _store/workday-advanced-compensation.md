---
aid: workday-advanced-compensation
name: Workday Advanced Compensation
description: API for managing compensation plans, budgets, allocations, and related processes in Workday.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - name: Workday Advanced Compensation API
    description: RESTful and SOAP APIs for managing compensation plans, merit increases, bonuses, stock awards, and compensation budgets.
    image: https://www.workday.com/content/dam/web/images/logo.png
    humanUrl: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation/v41.1/index.html
    baseUrl: https://wd2-impl-services1.workday.com/ccx/service
    tags:
      - Bonuses
      - Compensation
      - HR
      - Merit
      - Payroll
      - Salary Planning
      - Stock Awards
    properties:
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation/v41.1/index.html
      - type: OpenAPI
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Compensation/v41.1/Compensation.yaml
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/integration-security/securing-workday-web-services/authentication-types.html
      - type: Versioning
        url: https://doc.workday.com/r/Workday_Web_Services/Workday_Web_Services_Directory/About_Workday_Web_Services_Versioning
      - type: OpenAPI
        url: openapi/workday-advanced-compensation-openapi.yml
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-compensation-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-compensation-grade-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-merit-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-bonus-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-stock-plan-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-compensation-budget-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-compensation-review-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-employee-compensation-schema.json
      - type: JSONSchema
        url: json-schema/workday-advanced-compensation-compensation-change-request-schema.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-compensation-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-compensation-grade-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-merit-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-bonus-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-stock-plan-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-compensation-budget-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-compensation-review-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-employee-compensation-structure.json
      - type: JSONStructure
        url: json-structure/workday-advanced-compensation-compensation-change-request-structure.json
      - type: JSONLd
        url: json-ld/workday-advanced-compensation-context.jsonld
      - type: SpectralRules
        url: rules/workday-advanced-compensation-spectral-rules.yml
      - type: NaftikoCapability - Compensation Management
        url: capabilities/compensation-management.yaml
      - type: NaftikoCapability - Advanced Compensation (Shared)
        url: capabilities/shared/advanced-compensation.yaml
      - type: Vocabulary
        url: vocabulary/workday-advanced-compensation-vocabulary.yml
    contact:
      - type: Support
        url: https://www.workday.com/en-us/customer-experience/support.html
      - type: Community
        url: https://community.workday.com/
    operations:
      - name: Get Compensation Plans
        description: Retrieve compensation plan details including eligibility rules and budget pools
        method: GET
        path: /Compensation_Plan
      - name: Submit Compensation Changes
        description: Submit compensation change requests for employees
        method: POST
        path: /Submit_Compensation_Change_Request
      - name: Get Compensation Budgets
        description: Retrieve compensation budget information and allocations
        method: GET
        path: /Compensation_Budget
      - name: Get Merit Plans
        description: Retrieve merit increase plan configurations
        method: GET
        path: /Merit_Plan
      - name: Get Bonus Plans
        description: Retrieve bonus plan details and award criteria
        method: GET
        path: /Bonus_Plan
      - name: Get Stock Plans
        description: Retrieve stock and equity compensation plan information
        method: GET
        path: /Stock_Plan
      - name: Get Compensation Grades
        description: Retrieve compensation grade profiles and ranges
        method: GET
        path: /Compensation_Grade_Profile
      - name: Get Salary Survey Data
        description: Retrieve market survey data and benchmarking information
        method: GET
        path: /Salary_Survey_Data
      - name: Get Compensation Review Process
        description: Retrieve compensation review process status and workflow
        method: GET
        path: /Compensation_Review_Process
      - name: Update Compensation Package
        description: Update employee compensation package details
        method: PUT
        path: /Compensation_Package
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include:
  - name: Workday Human Capital Management
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Human_Resources/index.html
  - name: Workday Payroll
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/Payroll/index.html
common:
  - type: Developer Portal
    url: https://developer.workday.com/
  - type: API Status
    url: https://status.workday.com/
  - type: Terms of Service
    url: https://www.workday.com/en-us/legal.html
  - type: Privacy Policy
    url: https://www.workday.com/en-us/privacy.html
  - type: Security
    url: https://www.workday.com/en-us/why-workday/security-trust.html
  - type: Rate Limits
    url: https://doc.workday.com/r/Workday_Web_Services/Workday_Web_Services_Directory/Web_Service_Rate_Limiting
  - type: Sandbox Environment
    url: https://doc.workday.com/r/en-us/workday-studio/workday-studio-user-guide/sandboxes
  - type: SDKs
    url: https://github.com/Workday
  - type: JSON-LD
    url: json-ld/workday-advanced-compensation-context.jsonld
  - type: SpectralRules
    url: rules/workday-advanced-compensation-spectral-rules.yml
  - type: NaftikoCapability - Compensation Management
    url: capabilities/compensation-management.yaml
  - type: NaftikoCapability - Advanced Compensation (Shared)
    url: capabilities/shared/advanced-compensation.yaml
  - type: Vocabulary
    url: vocabulary/workday-advanced-compensation-vocabulary.yml
---
