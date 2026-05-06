---
aid: zions-bancorp
name: Zions Bancorporation
description: Zions Bancorporation is one of the nation's premier financial services companies, operating under local management teams and distinct brands in 11 western U.S. states. The company offers a comprehensive suite of banking, treasury management, lending, and wealth management services for individuals, businesses, and public sector clients. Zions provides ERP-to-bank integration capabilities, ACH payment origination, wire transfers, and cash management tools for corporate treasury operations. The company does not currently publish a public REST API developer portal; integrations are delivered via Treasury Internet Banking import/export, NACHA-compliant ACH files, and direct file-transfer arrangements with corporate customers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Financial Services
  - Treasury Management
  - Payments
url: https://raw.githubusercontent.com/api-evangelist/zions-bancorp/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: zions-bancorp:treasury-internet-banking
    name: Zions Treasury Internet Banking
    description: Zions Treasury Internet Banking provides businesses with a secure online platform for managing treasury operations including ACH payments, domestic and international wire transfers, account transfers, positive pay, and real-time cash position visibility. Supports ERP integration via import and export of standard file formats for automated payment origination and reconciliation.
    humanURL: https://www.zionsbank.com/business/treasury/treasury-internet-banking/
    tags:
      - Treasury Management
      - ACH
      - Wire Transfers
      - Cash Management
      - Banking
    properties:
      - type: Documentation
        url: https://www.zionsbank.com/business/treasury/
      - type: Login
        url: https://treasurygateway.zionsbank.com/
  - aid: zions-bancorp:ach-payments
    name: Zions ACH Payments
    description: Zions ACH Payments is a payment disbursement solution enabling businesses to pay employees, suppliers, vendors, and tax agencies via ACH. Supports import and export file formats for integration with accounting and ERP software, making cash flow management more efficient, predictable, and cost effective.
    humanURL: https://www.zionsbank.com/business/treasury/treasury-management-select/ach-payments/
    tags:
      - ACH
      - Payments
      - Treasury Management
      - Banking
    properties:
      - type: Documentation
        url: https://www.zionsbank.com/business/treasury/treasury-management-select/ach-payments/
  - aid: zions-bancorp:wire-transfers
    name: Zions Wire Transfer Services
    description: Zions Wire Transfer Services enables businesses to send domestic and international wire transfers efficiently. Supports foreign currency transfers to more than 60 countries worldwide. Available through Treasury Internet Banking for streamlined origination and status tracking.
    humanURL: https://www.zionsbank.com/business/treasury/disbursements/wire-transfers/
    tags:
      - Wire Transfers
      - International Payments
      - Banking
      - Treasury Management
    properties:
      - type: Documentation
        url: https://www.zionsbank.com/business/treasury/disbursements/wire-transfers/
common:
  - type: Website
    url: https://www.zionsbank.com
  - type: Portal
    url: https://treasurygateway.zionsbank.com/
  - type: Documentation
    url: https://www.zionsbank.com/business/treasury/
  - type: Login
    url: https://www.zionsbank.com/personal/sign-in/
  - type: Support
    url: https://www.zionsbank.com/personal/customer-service/
  - type: TermsOfService
    url: https://www.zionsbank.com/disclosure-documents/
  - type: PrivacyPolicy
    url: https://www.zionsbank.com/about/privacy/
  - data:
      - name: Treasury Internet Banking
        description: Online treasury management platform with payment origination and reporting.
      - name: ACH Origination
        description: NACHA-compliant ACH payment file origination for payroll, vendor, and tax payments.
      - name: Wire Transfers
        description: Domestic and international wire transfers including foreign currency.
      - name: Positive Pay
        description: Check fraud prevention with issued-check matching and exception review.
      - name: ERP Integration
        description: File import/export integration with accounting and ERP systems.
      - name: Account Reporting
        description: Real-time visibility into account balances, transactions, and check images.
    name: Features
    type: Features
  - data:
      - name: Corporate Treasury Operations
        description: Cash management and payment origination for corporate treasurers.
      - name: Public Sector Banking
        description: Treasury and payment services for state, county, and municipal governments.
      - name: Small Business Banking
        description: Banking and payment services for small and mid-sized businesses.
      - name: Wealth Management
        description: Trust, investment, and wealth advisory services.
    name: UseCases
    type: UseCases
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
