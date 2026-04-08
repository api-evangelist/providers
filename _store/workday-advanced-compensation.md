---
aid: workday-advanced-compensation
url: https://raw.githubusercontent.com/api-evangelist/workday-advanced-compensation/refs/heads/main/apis.yml
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
name: Workday Advanced Compensation
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for managing compensation plans, budgets, allocations, and related processes in Workday.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

