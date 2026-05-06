---
aid: hmrc
name: HMRC UK Tax Authority
description: HM Revenue and Customs (HMRC) provides over 115 APIs through the HMRC Developer Hub for UK tax compliance including Making Tax Digital for VAT and Income Tax, PAYE, customs declarations, corporation tax, and construction industry scheme. APIs use OAuth 2.0 and support both REST and XML protocols with a sandbox testing environment.
url: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/apis.yml
type: Index
image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
tags:
  - Government
  - Making Tax Digital
  - Regulatory
  - Tax
  - UK
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hmrc:hmrc-vat-mtd-api
    name: HMRC VAT (Making Tax Digital) API
    description: The HMRC VAT (Making Tax Digital) API enables software to submit VAT returns, retrieve VAT obligations, liabilities, payments, penalties, and customer details in compliance with UK Making Tax Digital requirements. Uses OAuth 2.0 authentication with fraud prevention headers required.
    humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0
    baseURL: https://api.service.hmrc.gov.uk
    image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
    tags:
      - Government
      - Making Tax Digital
      - REST
      - Tax
      - UK
      - VAT
    properties:
      - type: Documentation
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0
      - type: Reference
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0/oas/page
      - type: Authentication
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
      - type: OpenAPI
        url: openapi/hmrc-vat-mtd-openapi.yml
  - aid: hmrc:hmrc-self-assessment-api
    name: HMRC Self Assessment API
    description: The HMRC Self Assessment APIs enable software to submit and manage self assessment tax returns, income sources, and tax calculations for individuals and sole traders under Making Tax Digital for Income Tax.
    humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    baseURL: https://api.service.hmrc.gov.uk
    image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
    tags:
      - Government
      - Income Tax
      - REST
      - Self Assessment
      - Tax
      - UK
    properties:
      - type: Documentation
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
      - type: Authentication
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
  - aid: hmrc:hmrc-paye-api
    name: HMRC PAYE (Pay As You Earn) API
    description: The HMRC PAYE APIs enable payroll software to submit employer payroll data, retrieve tax codes and employee records, and manage PAYE submissions for Real Time Information (RTI) reporting.
    humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    baseURL: https://api.service.hmrc.gov.uk
    image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
    tags:
      - Government
      - PAYE
      - Payroll
      - REST
      - Tax
      - UK
    properties:
      - type: Documentation
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
      - type: Authentication
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
  - aid: hmrc:hmrc-customs-declarations-api
    name: HMRC Customs Declarations API
    description: The HMRC Customs Declarations APIs enable customs software to submit import and export declarations, manage authorizations, and integrate with the UK Customs Declaration Service (CDS) for trade compliance.
    humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    baseURL: https://api.service.hmrc.gov.uk
    image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
    tags:
      - Customs
      - Excise
      - Government
      - REST
      - Tax
      - UK
      - XML
    properties:
      - type: Documentation
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
      - type: Authentication
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
  - aid: hmrc:hmrc-corporation-tax-api
    name: HMRC Corporation Tax API
    description: The HMRC Corporation Tax APIs enable accounting software to submit corporation tax returns, retrieve liabilities, manage payments, and access tax calculation data for UK businesses.
    humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    baseURL: https://api.service.hmrc.gov.uk
    image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
    tags:
      - Business
      - Corporation Tax
      - Government
      - REST
      - Tax
      - UK
    properties:
      - type: Documentation
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
      - type: Authentication
        url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
common:
  - type: Portal
    url: https://developer.service.hmrc.gov.uk/
  - type: Documentation
    url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
  - type: Authentication
    url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
  - type: Getting Started
    url: https://developer.service.hmrc.gov.uk/api-documentation/docs/using-the-hub
  - type: Terms of Service
    url: https://www.gov.uk/api-documentation/docs/terms-of-use
  - type: Status
    url: https://api-platform-status.production.tax.service.gov.uk/
  - type: Support
    url: https://developer.service.hmrc.gov.uk/
  - type: Website
    url: https://www.gov.uk/government/organisations/hm-revenue-customs
  - type: OpenAPI
    url: openapi/hmrc-vat-mtd-openapi.yml
  - type: JSONSchema
    url: json-schema/hmrc-vat-return-schema.json
  - type: JSONLDContext
    url: json-ld/hmrc-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
