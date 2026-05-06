---
aid: workday-payroll
name: Workday Payroll
description: Workday Payroll provides comprehensive APIs for managing payroll operations, employee compensation, tax calculations, and payment processing within the Workday platform.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/workday-payroll/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-03'
specificationVersion: '0.19'
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
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: openapi/workday-payroll-payroll-openapi.yml
      - type: Authentication
        url: https://doc.workday.com/admin-guide/en-us/authentication/authentication.html
      - type: APIConsole
        url: https://community.workday.com/api-console
      - type: RateLimits
        url: https://doc.workday.com/admin-guide/en-us/api-reference/api-rate-limiting.html
      - type: JSON-LD
        url: json-ld/workday-payroll-payroll-context.jsonld
      - type: JSONSchema
        url: json-schema/payroll-calculation-status-schema.json
      - type: JSONSchema
        url: json-schema/payroll-create-pay-run-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-deduction-code-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-deduction-code-ref-schema.json
      - type: JSONSchema
        url: json-schema/payroll-deduction-code-schema.json
      - type: JSONSchema
        url: json-schema/payroll-deduction-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-deduction-schema.json
      - type: JSONSchema
        url: json-schema/payroll-earning-code-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-earning-code-ref-schema.json
      - type: JSONSchema
        url: json-schema/payroll-earning-code-schema.json
      - type: JSONSchema
        url: json-schema/payroll-earning-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-earning-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-group-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-group-ref-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-group-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-period-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-run-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-pay-run-schema.json
      - type: JSONSchema
        url: json-schema/payroll-update-pay-run-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-worker-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-worker-payroll-details-schema.json
      - type: JSONSchema
        url: json-schema/payroll-worker-ref-schema.json
      - type: JSONStructure
        url: json-structure/payroll-calculation-status-structure.json
      - type: JSONStructure
        url: json-structure/payroll-create-pay-run-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-deduction-code-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-deduction-code-ref-structure.json
      - type: JSONStructure
        url: json-structure/payroll-deduction-code-structure.json
      - type: JSONStructure
        url: json-structure/payroll-deduction-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-deduction-structure.json
      - type: JSONStructure
        url: json-structure/payroll-earning-code-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-earning-code-ref-structure.json
      - type: JSONStructure
        url: json-structure/payroll-earning-code-structure.json
      - type: JSONStructure
        url: json-structure/payroll-earning-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-earning-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-group-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-group-ref-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-group-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-period-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-run-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-pay-run-structure.json
      - type: JSONStructure
        url: json-structure/payroll-update-pay-run-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-worker-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-worker-payroll-details-structure.json
      - type: JSONStructure
        url: json-structure/payroll-worker-ref-structure.json
      - type: Example
        url: examples/payroll-calculation-status-example.json
      - type: Example
        url: examples/payroll-create-pay-run-request-example.json
      - type: Example
        url: examples/payroll-deduction-code-collection-example.json
      - type: Example
        url: examples/payroll-deduction-code-example.json
      - type: Example
        url: examples/payroll-deduction-code-ref-example.json
      - type: Example
        url: examples/payroll-deduction-collection-example.json
      - type: Example
        url: examples/payroll-deduction-example.json
      - type: Example
        url: examples/payroll-earning-code-collection-example.json
      - type: Example
        url: examples/payroll-earning-code-example.json
      - type: Example
        url: examples/payroll-earning-code-ref-example.json
      - type: Example
        url: examples/payroll-earning-collection-example.json
      - type: Example
        url: examples/payroll-earning-example.json
      - type: Example
        url: examples/payroll-pay-group-collection-example.json
      - type: Example
        url: examples/payroll-pay-group-example.json
      - type: Example
        url: examples/payroll-pay-group-ref-example.json
      - type: Example
        url: examples/payroll-pay-period-example.json
      - type: Example
        url: examples/payroll-pay-run-collection-example.json
      - type: Example
        url: examples/payroll-pay-run-example.json
      - type: Example
        url: examples/payroll-update-pay-run-request-example.json
      - type: Example
        url: examples/payroll-worker-collection-example.json
      - type: Example
        url: examples/payroll-worker-payroll-details-example.json
      - type: Example
        url: examples/payroll-worker-ref-example.json
      - type: Example
        url: examples/workday-payroll-list-pay-runs-example.json
      - type: NaftikoCapability
        url: capabilities/shared/payroll.yaml
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
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: openapi/workday-payroll-payroll-results-openapi.yml
      - type: JSON-LD
        url: json-ld/workday-payroll-payroll-results-context.jsonld
      - type: JSONSchema
        url: json-schema/payroll-results-pay-period-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-pay-run-result-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payment-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payment-election-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payment-election-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payment-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payslip-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payslip-deduction-line-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payslip-earning-line-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payslip-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-payslip-tax-line-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-worker-ref-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-worker-result-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-results-worker-result-schema.json
      - type: JSONStructure
        url: json-structure/payroll-results-pay-period-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-pay-run-result-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payment-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payment-election-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payment-election-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payment-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payslip-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payslip-deduction-line-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payslip-earning-line-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payslip-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-payslip-tax-line-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-worker-ref-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-worker-result-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-results-worker-result-structure.json
      - type: Example
        url: examples/payroll-results-pay-period-example.json
      - type: Example
        url: examples/payroll-results-pay-run-result-example.json
      - type: Example
        url: examples/payroll-results-payment-collection-example.json
      - type: Example
        url: examples/payroll-results-payment-election-collection-example.json
      - type: Example
        url: examples/payroll-results-payment-election-example.json
      - type: Example
        url: examples/payroll-results-payment-example.json
      - type: Example
        url: examples/payroll-results-payslip-collection-example.json
      - type: Example
        url: examples/payroll-results-payslip-deduction-line-example.json
      - type: Example
        url: examples/payroll-results-payslip-earning-line-example.json
      - type: Example
        url: examples/payroll-results-payslip-example.json
      - type: Example
        url: examples/payroll-results-payslip-tax-line-example.json
      - type: Example
        url: examples/payroll-results-worker-ref-example.json
      - type: Example
        url: examples/payroll-results-worker-result-collection-example.json
      - type: Example
        url: examples/payroll-results-worker-result-example.json
      - type: Example
        url: examples/workday-payroll-get-worker-payslip-example.json
      - type: NaftikoCapability
        url: capabilities/shared/payroll-results.yaml
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
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: openapi/workday-payroll-payroll-input-openapi.yml
      - type: JSON-LD
        url: json-ld/workday-payroll-payroll-input-context.jsonld
      - type: JSONSchema
        url: json-schema/payroll-input-adjustment-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-adjustment-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-create-adjustment-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-create-input-batch-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-create-one-time-payment-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-create-supplemental-earning-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-create-time-off-input-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-input-batch-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-input-batch-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-input-record-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-one-time-payment-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-one-time-payment-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-supplemental-earning-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-supplemental-earning-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-time-off-input-collection-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-time-off-input-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-update-one-time-payment-request-schema.json
      - type: JSONSchema
        url: json-schema/payroll-input-worker-ref-schema.json
      - type: JSONStructure
        url: json-structure/payroll-input-adjustment-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-adjustment-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-create-adjustment-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-create-input-batch-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-create-one-time-payment-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-create-supplemental-earning-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-create-time-off-input-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-input-batch-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-input-batch-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-input-record-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-one-time-payment-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-one-time-payment-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-supplemental-earning-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-supplemental-earning-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-time-off-input-collection-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-time-off-input-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-update-one-time-payment-request-structure.json
      - type: JSONStructure
        url: json-structure/payroll-input-worker-ref-structure.json
      - type: Example
        url: examples/payroll-input-adjustment-collection-example.json
      - type: Example
        url: examples/payroll-input-adjustment-example.json
      - type: Example
        url: examples/payroll-input-create-adjustment-request-example.json
      - type: Example
        url: examples/payroll-input-create-input-batch-request-example.json
      - type: Example
        url: examples/payroll-input-create-one-time-payment-request-example.json
      - type: Example
        url: examples/payroll-input-create-supplemental-earning-request-example.json
      - type: Example
        url: examples/payroll-input-create-time-off-input-request-example.json
      - type: Example
        url: examples/payroll-input-input-batch-collection-example.json
      - type: Example
        url: examples/payroll-input-input-batch-example.json
      - type: Example
        url: examples/payroll-input-input-record-example.json
      - type: Example
        url: examples/payroll-input-one-time-payment-collection-example.json
      - type: Example
        url: examples/payroll-input-one-time-payment-example.json
      - type: Example
        url: examples/payroll-input-supplemental-earning-collection-example.json
      - type: Example
        url: examples/payroll-input-supplemental-earning-example.json
      - type: Example
        url: examples/payroll-input-time-off-input-collection-example.json
      - type: Example
        url: examples/payroll-input-time-off-input-example.json
      - type: Example
        url: examples/payroll-input-update-one-time-payment-request-example.json
      - type: Example
        url: examples/payroll-input-worker-ref-example.json
      - type: Example
        url: examples/workday-payroll-create-one-time-payment-example.json
      - type: NaftikoCapability
        url: capabilities/shared/payroll-input.yaml
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
      - type: Documentation
        url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
      - type: OpenAPI
        url: openapi/workday-payroll-tax-openapi.yml
      - type: JSON-LD
        url: json-ld/workday-payroll-tax-context.jsonld
      - type: JSONSchema
        url: json-schema/tax-create-tax-election-request-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-election-collection-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-election-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-filing-collection-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-filing-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-jurisdiction-collection-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-jurisdiction-ref-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-jurisdiction-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-result-collection-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-result-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-withholding-collection-schema.json
      - type: JSONSchema
        url: json-schema/tax-tax-withholding-schema.json
      - type: JSONSchema
        url: json-schema/tax-update-tax-withholding-request-schema.json
      - type: JSONSchema
        url: json-schema/tax-worker-ref-schema.json
      - type: JSONSchema
        url: json-schema/tax-worker-tax-summary-schema.json
      - type: JSONStructure
        url: json-structure/tax-create-tax-election-request-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-election-collection-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-election-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-filing-collection-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-filing-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-jurisdiction-collection-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-jurisdiction-ref-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-jurisdiction-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-result-collection-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-result-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-withholding-collection-structure.json
      - type: JSONStructure
        url: json-structure/tax-tax-withholding-structure.json
      - type: JSONStructure
        url: json-structure/tax-update-tax-withholding-request-structure.json
      - type: JSONStructure
        url: json-structure/tax-worker-ref-structure.json
      - type: JSONStructure
        url: json-structure/tax-worker-tax-summary-structure.json
      - type: Example
        url: examples/tax-create-tax-election-request-example.json
      - type: Example
        url: examples/tax-tax-election-collection-example.json
      - type: Example
        url: examples/tax-tax-election-example.json
      - type: Example
        url: examples/tax-tax-filing-collection-example.json
      - type: Example
        url: examples/tax-tax-filing-example.json
      - type: Example
        url: examples/tax-tax-jurisdiction-collection-example.json
      - type: Example
        url: examples/tax-tax-jurisdiction-example.json
      - type: Example
        url: examples/tax-tax-jurisdiction-ref-example.json
      - type: Example
        url: examples/tax-tax-result-collection-example.json
      - type: Example
        url: examples/tax-tax-result-example.json
      - type: Example
        url: examples/tax-tax-withholding-collection-example.json
      - type: Example
        url: examples/tax-tax-withholding-example.json
      - type: Example
        url: examples/tax-update-tax-withholding-request-example.json
      - type: Example
        url: examples/tax-worker-ref-example.json
      - type: Example
        url: examples/tax-worker-tax-summary-example.json
      - type: NaftikoCapability
        url: capabilities/shared/payroll-tax.yaml
common:
  - type: DeveloperPortal
    url: https://community.workday.com/
  - type: GettingStarted
    url: https://doc.workday.com/developer/studio/en-us/getting-started.html
  - type: Authentication
    url: https://doc.workday.com/admin-guide/en-us/authentication/authentication.html
  - type: TermsOfService
    url: https://www.workday.com/en-us/legal.html
  - type: PrivacyPolicy
    url: https://www.workday.com/en-us/privacy.html
  - type: StatusPage
    url: https://status.workday.com/
  - type: Security
    url: https://www.workday.com/en-us/why-workday/security.html
  - type: JSON-LD
    url: json-ld/workday-payroll-context.jsonld
  - type: JSONSchema
    url: json-schema/workday-payroll-pay-run-schema.json
  - type: JSONSchema
    url: json-schema/workday-payroll-payslip-schema.json
  - type: JSONStructure
    url: json-structure/workday-payroll-pay-run-structure.json
  - type: JSONStructure
    url: json-structure/workday-payroll-payslip-structure.json
  - type: Example
    url: examples/workday-payroll-pay-run-example.json
  - type: Example
    url: examples/workday-payroll-payslip-example.json
  - type: SpectralRules
    url: rules/workday-payroll-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/payroll-processing.yaml
  - type: Vocabulary
    url: vocabulary/workday-payroll-vocabulary.yml
  - type: Tools
    url: https://github.com/Workday/raas-python
    title: Report-as-a-Service Python Client
  - type: Tools
    url: https://github.com/Workday/everywhere
    title: Workday Everywhere SDK
  - type: Tools
    url: https://github.com/Workday/asor
    title: Agent System of Record API
  - type: Features
    data:
      - name: Global Payroll Engine
        description: Process payroll across multiple countries with configurable calculation logic, pay components, and statutory rules.
      - name: Pay Run Management
        description: Create, schedule, and execute payroll runs with full visibility into calculation status and results.
      - name: Earnings and Deductions
        description: Configure and apply earnings, deductions, accumulations, and balances per worker, organization, or pay group.
      - name: Tax Calculation and Withholding
        description: Automated tax calculations and withholdings with support for federal, state, local, and international jurisdictions.
      - name: Payroll Input Processing
        description: Submit one-time payments, retroactive adjustments, and supplemental earnings outside of scheduled pay runs.
      - name: Payslip Generation
        description: Produce worker-facing payslips and pay statements with detailed breakdowns of earnings, deductions, and taxes.
      - name: Compliance Reporting
        description: Generate statutory and compliance reports including tax filings, year-end forms, and audit trails.
      - name: Worker Self-Service
        description: Surface pay history, payslips, and tax documents to workers via Workday Mobile and the Workday user experience.
  - type: UseCases
    data:
      - name: Multi-Country Payroll Operations
        description: Run payroll for a global workforce across regions while standardizing on a single platform and data model.
      - name: Payroll Cycle Automation
        description: Schedule, execute, and audit recurring payroll runs end-to-end with minimal manual intervention.
      - name: One-Time Payments and Adjustments
        description: Submit bonuses, retroactive pay, and corrections programmatically through the Payroll Input API.
      - name: Tax Filing and Compliance
        description: Calculate withholdings and produce data feeds for statutory tax filings and year-end reporting.
      - name: Pay Data Integration
        description: Sync payroll results into general ledger, banking, benefits, and analytics systems downstream of payroll runs.
      - name: Worker Pay Transparency
        description: Provide workers with secure programmatic access to payslips, year-to-date totals, and tax forms.
  - type: Integrations
    data:
      - name: Workday Human Capital Management
        description: Integrated source of worker, organization, compensation, and time tracking data feeding payroll calculations.
      - name: Workday Financial Management
        description: Posts payroll journal entries and accruals into the Workday general ledger.
      - name: Workday Time Tracking
        description: Feeds approved time and absence data into payroll calculations.
      - name: Workday Benefits
        description: Provides benefit elections and deductions consumed by payroll.
      - name: Workday Studio
        description: Visual integration tool for building inbound and outbound payroll integrations.
      - name: Workday Cloud Connect for Third-Party Payroll
        description: Pre-built integrations to third-party payroll providers and tax filing services.
      - name: Banking and Payment Networks
        description: Generates ACH and international payment files for direct deposit and payroll disbursements.
  - type: Solutions
    data:
      - name: Workday Payroll for the U.S.
        description: Full-service payroll solution for U.S. employers including federal, state, and local tax calculation and filing support.
      - name: Workday Payroll for Canada
        description: Payroll solution covering Canadian federal and provincial requirements.
      - name: Workday Payroll for the U.K.
        description: U.K. payroll with HMRC reporting and statutory pay support.
      - name: Workday Payroll for France
        description: French payroll covering DSN reporting and statutory rules.
      - name: Workday Cloud Connect for Third-Party Payroll
        description: Connectors and data feeds for customers running payroll on a third-party provider while using Workday HCM.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
tags:
  - Compensation
  - Enterprise
  - Human Resources
  - Payroll
  - SaaS
  - Tax
---
