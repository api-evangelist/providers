---
aid: bankruptcywatch
url: https://raw.githubusercontent.com/api-evangelist/bankruptcywatch/refs/heads/main/apis.yml
name: BankruptcyWatch
tags:
  - Bankruptcy
  - Compliance
  - Court Data
  - Legal
  - Lending
  - PACER
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-25'
modified: '2026-04-21'
position: Consumer
description: BankruptcyWatch is the proven creditor bankruptcy platform built with machine learning and intelligent automation to elevate every bankruptcy interaction. The PACER API provides access to US bankruptcy court data enabling creditors, lenders, and legal teams to search for cases, retrieve dockets, manage claims, file Proof of Claim documents, and automate bankruptcy monitoring across all federal bankruptcy court districts.
apis:
  - aid: bankruptcywatch:pacer-api
    name: BankruptcyWatch PACER API
    tags:
      - Bankruptcy
      - Claims
      - Court Filings
      - PACER
      - Monitoring
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.bankruptcywatch.com/v1
    humanURL: https://www.bankruptcywatch.com/products/pacer-api
    properties:
      - url: https://www.bankruptcywatch.com/products/pacer-api
        type: Documentation
      - url: https://www.bankruptcywatch.com/api-kickoff
        type: GettingStarted
      - url: https://documenter.getpostman.com/view/13540419/TVmLAxnr
        type: PostmanCollection
      - url: openapi/bankruptcywatch-pacer-api-openapi.yml
        type: OpenAPI
    description: The BankruptcyWatch PACER API provides a comprehensive collection of services for interacting with US bankruptcy court data. Search cases across all districts, retrieve dockets and claims registers, file Proof of Claim documents, and set up automated monitoring alerts for bankruptcy filings.
common:
  - type: Website
    url: https://www.bankruptcywatch.com/
    name: BankruptcyWatch
  - type: Documentation
    url: https://www.bankruptcywatch.com/api-kickoff
    name: API Kickoff Guide
  - type: TermsOfService
    url: https://www.bankruptcywatch.com/terms
    name: Terms of Service
  - type: SpectralRules
    url: rules/bankruptcywatch-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/bankruptcywatch-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/bankruptcy-monitoring.yaml
  - type: JSON-LD
    url: json-ld/bankruptcywatch-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Case Search
        description: Search for bankruptcy cases across all US federal bankruptcy court districts.
      - name: Docket Retrieval
        description: Retrieve case docket entries and court filings via PACER.
      - name: Claims Register
        description: Access the full claims register for any bankruptcy case.
      - name: Proof of Claim Filing
        description: Programmatically file Proof of Claim documents with bankruptcy courts.
      - name: Bankruptcy Monitoring
        description: Automated alerts when monitored debtors or entities file for bankruptcy.
      - name: Machine Learning
        description: ML-powered document parsing and case classification.
      - name: No-Code Integrations
        description: Native integrations with Zapier, Salesforce, and Google Sheets.
      - name: Webhooks
        description: Real-time webhook notifications for bankruptcy events.
  - name: Use Cases
    type: UseCases
    data:
      - name: Creditor Bankruptcy Management
        description: Automate detection, research, and response to customer bankruptcy filings.
      - name: Loan Portfolio Monitoring
        description: Monitor loan portfolios for borrower bankruptcy filings in real time.
      - name: Proof of Claim Automation
        description: Automatically file Proof of Claim documents when debtors file bankruptcy.
      - name: Legal Case Management
        description: Manage multiple client creditor representations in bankruptcy proceedings.
      - name: Debt Portfolio Acquisition
        description: Research and evaluate bankruptcy debt for acquisition or restructuring.
      - name: Compliance Reporting
        description: Automated bankruptcy event detection for regulatory compliance.
  - name: Integrations
    type: Integrations
    data:
      - name: Zapier
      - name: Salesforce
      - name: Google Sheets
      - name: PACER (US Federal Courts)
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
