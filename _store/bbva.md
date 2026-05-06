---
aid: bbva
url: https://raw.githubusercontent.com/api-evangelist/bbva/refs/heads/main/apis.yml
name: BBVA
description: BBVA is a multinational Spanish financial services group operating in over 30 countries. The BBVA API Market provides a comprehensive catalog of banking APIs covering accounts, payments, collections, financing, identity, and open data across Spain, Mexico, Latin America, and other global markets. BBVA is a recognized open banking leader offering PSD2-compliant APIs, treasury management solutions, and digital ecosystem integrations.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Banking
  - Financial Services
  - Open Banking
  - PSD2
  - Spain
  - Mexico
access: 3rd-Party
created: '2025-02-08'
modified: '2026-04-21'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: bbva:accounts-psd2
    name: BBVA Accounts PSD2 API
    description: PSD2-compliant account information service (AIS) API for Spain. Allows authorized third parties to access customer payment account information including account lists, balances, transaction history, and account holder details. Requires a PSD2 AIS license and registration through the Redsys platform.
    humanURL: https://www.bbvaapimarket.com/en/banking-apis/es-account-information-psd2/
    tags:
      - Banking
      - Accounts
      - PSD2
      - Spain
      - Open Banking
    properties:
      - type: Documentation
        url: https://www.bbvaapimarket.com/en/banking-apis/es-account-information-psd2/
  - aid: bbva:payments-psd2
    name: BBVA Payments PSD2 API
    description: PSD2-compliant payment initiation service (PIS) API for Spain. Allows authorized third parties to initiate payments on behalf of customers including SEPA transfers, immediate payments, Bank of Spain FMO payments, and international transfers. Requires a PSD2 PIS license and registration through the Redsys platform.
    humanURL: https://www.bbvaapimarket.com/en/banking-apis/es-payments-psd2/
    tags:
      - Banking
      - Payments
      - PSD2
      - Spain
      - Open Banking
    properties:
      - type: Documentation
        url: https://www.bbvaapimarket.com/en/banking-apis/es-payments-psd2/
  - aid: bbva:mexico-business-payments
    name: BBVA Mexico Business Payments API
    description: Business payment processing API for Mexico enabling bulk payments, payroll disbursements, and supplier payments through BBVA Mexico's banking infrastructure. Supports SPEI transfers and other Mexican payment systems.
    humanURL: https://www.bbvaapimarket.com/en/banking-apis/
    tags:
      - Banking
      - Payments
      - Mexico
      - Business Banking
    properties:
      - type: Documentation
        url: https://www.bbvaapimarket.com/en/banking-apis/
  - aid: bbva:locations
    name: BBVA Locations API
    description: Open data API providing access to BBVA branch and ATM location data. Available for Spain and Mexico, this API returns geolocation data, operating hours, services available, and accessibility information for all BBVA branches and ATMs.
    humanURL: https://www.bbvaapimarket.com/en/banking-apis/
    tags:
      - Banking
      - Open Data
      - Locations
    properties:
      - type: Documentation
        url: https://www.bbvaapimarket.com/en/banking-apis/
common:
  - type: Portal
    url: https://www.bbvaapimarket.com/en/
  - type: Website
    url: https://www.bbva.com/
  - type: Documentation
    url: https://www.bbvaapimarket.com/en/api-developers/
  - type: GettingStarted
    url: https://www.bbvaapimarket.com/en/api-developers/
  - type: Sandbox
    url: https://www.bbvaapimarket.com/en/api-developers/
  - type: TermsOfService
    url: https://www.bbva.com/en/legal-notice/
  - type: PrivacyPolicy
    url: https://www.bbva.com/en/privacy-policy/
  - type: Blog
    url: https://www.bbvaapimarket.com/en/api-world/
  - type: SpectralRules
    url: rules/bbva-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bbva-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/open-banking.yaml
  - type: JSON-LD
    url: json-ld/bbva-context.jsonld
  - type: Features
    data:
      - name: PSD2 Compliance
        description: All European banking APIs are fully compliant with the PSD2 Payment Services Directive, including AIS and PIS services.
      - name: Multi-Country Coverage
        description: APIs available across 15+ countries including Spain, Mexico, Peru, Colombia, Argentina, Belgium, France, UK, Turkey, and USA.
      - name: Treasury Management
        description: Multi-country treasury APIs for global enterprises to manage payments, collections, and cash positions.
      - name: Digital Ecosystems
        description: APIs enabling businesses to embed BBVA banking services into their own digital platforms and applications.
      - name: Sandbox Environment
        description: Developer sandbox environment for testing and validating API integrations before production deployment.
      - name: Open Data APIs
        description: Publicly accessible location and branch data APIs available without authentication for branch/ATM locators.
  - type: UseCases
    data:
      - name: Account Aggregation
        description: Build personal finance and wealth management apps that aggregate BBVA account data across accounts.
      - name: Payment Initiation
        description: Enable one-click checkout and payment initiation from customer bank accounts in Spain and other PSD2 markets.
      - name: Treasury Automation
        description: Automate corporate treasury operations including bulk payments, collections, and cash management across BBVA markets.
      - name: Financial Data Analytics
        description: Access transaction and account data to power credit scoring, risk analysis, and financial advisory services.
      - name: Branch Locator
        description: Integrate BBVA branch and ATM location data into customer-facing applications using the open locations API.
  - type: Integrations
    data:
      - name: Redsys
        description: Spanish payment gateway and PSD2 infrastructure through which BBVA PSD2 APIs are registered and deployed.
      - name: SEPA
        description: Single Euro Payments Area integration for European payment transfers in Spain and EU markets.
      - name: SPEI
        description: Mexican interbank payment system integration for Mexico business payment APIs.
      - name: SAP
        description: ERP integration for treasury management customers connecting SAP financial systems with BBVA APIs.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
