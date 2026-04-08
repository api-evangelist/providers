---
aid: workday-payroll
url: https://raw.githubusercontent.com/api-evangelist/workday-payroll/refs/heads/main/apis.yml
apis:
- name: Workday Payroll API
  description: Core API for managing payroll processes including payroll calculations, employee pay data, deductions, earnings, and payroll runs.
  image: https://www.workday.com/content/dam/web/en-us/images/logos/workday-logo.svg
  humanURL: https://www.workday.com/en-us/products/payroll-management.html
  baseURL: https://api.workday.com/payroll/v1
  tags:
  - Compensation
  - Deductions
  - Earnings
  - Pay-Runs
  - Payroll
  properties:
  - type: documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: openapi
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/payroll/v1/openapi.yaml
  - type: authentication
    url: https://doc.workday.com/admin-guide/en-us/authentication/authentication.html
  - type: api-console
    url: https://community.workday.com/api-console
  - type: rate-limits
    url: https://doc.workday.com/admin-guide/en-us/api-reference/api-rate-limiting.html
  - type: OpenAPI
    url: openapi/workday-payroll-payroll-openapi.yml
  contact:
  - type: support
    url: https://www.workday.com/en-us/company/customer-support.html
  - type: email
    url: support@workday.com
- name: Workday Payroll Results API
  description: API for retrieving payroll calculation results, payment details, and historical payroll data.
  humanURL: https://www.workday.com/en-us/products/payroll-management.html
  baseURL: https://api.workday.com/payroll-results/v1
  tags:
  - History
  - Payments
  - Payroll-Results
  - Reporting
  properties:
  - type: documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: openapi
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/payroll-results/v1/openapi.yaml
  - type: OpenAPI
    url: openapi/workday-payroll-payroll-results-openapi.yml
- name: Workday Payroll Input API
  description: API for submitting and managing payroll input data including one-time payments, adjustments, and supplemental earnings.
  humanURL: https://www.workday.com/en-us/products/payroll-management.html
  baseURL: https://api.workday.com/payroll-input/v1
  tags:
  - Adjustments
  - One-Time-Payments
  - Payroll-Input
  - Supplemental-Earnings
  properties:
  - type: documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: openapi
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/payroll-input/v1/openapi.yaml
  - type: OpenAPI
    url: openapi/workday-payroll-payroll-input-openapi.yml
- name: Workday Tax API
  description: API for managing payroll tax calculations, tax withholdings, and tax filing information.
  humanURL: https://www.workday.com/en-us/products/payroll-management.html
  baseURL: https://api.workday.com/tax/v1
  tags:
  - Compliance
  - Tax
  - Tax-Filing
  - Withholdings
  properties:
  - type: documentation
    url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
  - type: OpenAPI
    url: openapi/workday-payroll-tax-openapi.yml
name: Workday Payroll
tags:
- Compensation
- Enterprise
- Human-Resources
- Payroll
- Saas
- Tax
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Workday Payroll provides comprehensive APIs for managing payroll operations, employee compensation, tax calculations, and payment processing within the Workday platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

