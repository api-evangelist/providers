---
name: Tax Templates
description: Pre-designed templates for organizing and filing tax documents and returns. Financial institutions and enterprises use these templates to streamline tax operations and manage fiscal responsibilities. Covers tax document collection, structured data formats for financial disclosures, corporate tax returns, and regulatory compliance frameworks across jurisdictions.
url: https://raw.githubusercontent.com/api-evangelist/tax-templates/refs/heads/main/apis.yml
tags:
  - Documentation
  - Finance
  - Tax
  - Templates
  - Compliance
created: '2025'
modified: '2026-05-03'
apis:
  - aid: tax-templates:turbotax-api
    name: TurboTax API
    tags:
      - Finance
      - Tax
      - Tax Preparation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.intuit.com
    humanURL: https://developer.intuit.com/
    properties:
      - url: https://developer.intuit.com/
        type: Documentation
    description: Intuit TurboTax API enables integration with TurboTax for consumer and business tax preparation workflows, including data import, tax calculation, and e-filing.
  - aid: tax-templates:h-r-block-api
    name: H&R Block API
    tags:
      - Finance
      - Tax
      - Tax Preparation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.hrblock.com/tax-center/filing/e-file/
    properties:
      - url: https://www.hrblock.com/tax-center/filing/e-file/
        type: Documentation
    description: H&R Block provides tax preparation templates and tools for individual and small business returns, including document import and guided filing workflows.
  - aid: tax-templates:xero-tax-api
    name: Xero Tax API
    tags:
      - Accounting
      - Finance
      - Tax
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.xero.com
    humanURL: https://developer.xero.com/documentation/xero-app-store/app-partner-guides/tax/
    properties:
      - url: https://developer.xero.com/documentation/xero-app-store/app-partner-guides/tax/
        type: Documentation
    description: Xero's Tax API enables accounting software and tax providers to connect to Xero for seamless tax return preparation using real-time financial data.
  - aid: tax-templates:quickbooks-tax-api
    name: QuickBooks Tax API
    tags:
      - Accounting
      - Finance
      - Tax
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://sandbox-quickbooks.api.intuit.com/v3
    humanURL: https://developer.intuit.com/app/developer/qbo/docs/develop
    properties:
      - url: https://developer.intuit.com/app/developer/qbo/docs/develop
        type: Documentation
    description: QuickBooks Online API provides access to tax-related financial data including income, expenses, and payroll for generating tax templates and returns.
  - aid: tax-templates:fatca-crs-reporting
    name: FATCA/CRS Reporting Templates
    tags:
      - Banking
      - Compliance
      - FATCA
      - Finance
      - International Tax
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.irs.gov/businesses/corporations/foreign-account-tax-compliance-act-fatca
    properties:
      - url: https://www.irs.gov/businesses/corporations/foreign-account-tax-compliance-act-fatca
        type: Documentation
    description: FATCA (Foreign Account Tax Compliance Act) and CRS (Common Reporting Standard) templates for financial institutions reporting foreign account holders to the IRS and international tax authorities.
common:
  - type: Website
    url: https://www.irs.gov/
  - type: JSON Schema
    url: json-schema/tax-document-schema.json
  - type: JSON Structure
    url: json-structure/tax-document-structure.json
  - type: JSON-LD
    url: json-ld/tax-templates-context.jsonld
  - type: Vocabulary
    url: vocabulary/tax-templates-vocabulary.yml
---
