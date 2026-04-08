---
aid: hmrc
url: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/apis.yml
apis:
- aid: hmrc:hmrc-vat-mtd-api
  name: HMRC VAT (Making Tax Digital) API
  tags:
  - Government
  - Making Tax Digital
  - REST
  - Tax
  - UK
  - VAT
  image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
  humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0
  baseURL: https://api.service.hmrc.gov.uk
  properties:
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0
    type: Documentation
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api/service/vat-api/1.0/oas/page
    type: Reference
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
    type: Authentication
  - url: openapi/hmrc-vat-mtd-openapi.yml
    type: OpenAPI
  description: The HMRC VAT (Making Tax Digital) API enables software to submit VAT returns, retrieve VAT obligations, liabilities, payments, penalties, and customer details in compliance with UK Making Tax Digital requirements. Uses OAuth 2.0 authentication with fraud prevention headers required.
- aid: hmrc:hmrc-self-assessment-api
  name: HMRC Self Assessment API
  tags:
  - Government
  - Income Tax
  - REST
  - Self Assessment
  - Tax
  - UK
  image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
  humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
  baseURL: https://api.service.hmrc.gov.uk
  properties:
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    type: Documentation
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
    type: Authentication
  description: The HMRC Self Assessment APIs enable software to submit and manage self assessment tax returns, income sources, and tax calculations for individuals and sole traders under Making Tax Digital for Income Tax.
- aid: hmrc:hmrc-paye-api
  name: HMRC PAYE (Pay As You Earn) API
  tags:
  - Government
  - PAYE
  - Payroll
  - REST
  - Tax
  - UK
  image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
  humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
  baseURL: https://api.service.hmrc.gov.uk
  properties:
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    type: Documentation
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
    type: Authentication
  description: The HMRC PAYE APIs enable payroll software to submit employer payroll data, retrieve tax codes and employee records, and manage PAYE submissions for Real Time Information (RTI) reporting.
- aid: hmrc:hmrc-customs-declarations-api
  name: HMRC Customs Declarations API
  tags:
  - Customs
  - Excise
  - Government
  - REST
  - Tax
  - UK
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
  humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
  baseURL: https://api.service.hmrc.gov.uk
  properties:
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    type: Documentation
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
    type: Authentication
  description: The HMRC Customs Declarations APIs enable customs software to submit import and export declarations, manage authorizations, and integrate with the UK Customs Declaration Service (CDS) for trade compliance.
- aid: hmrc:hmrc-corporation-tax-api
  name: HMRC Corporation Tax API
  tags:
  - Business
  - Corporation Tax
  - Government
  - REST
  - Tax
  - UK
  image: https://raw.githubusercontent.com/api-evangelist/hmrc/refs/heads/main/image.png
  humanURL: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
  baseURL: https://api.service.hmrc.gov.uk
  properties:
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/api
    type: Documentation
  - url: https://developer.service.hmrc.gov.uk/api-documentation/docs/authorisation
    type: Authentication
  description: The HMRC Corporation Tax APIs enable accounting software to submit corporation tax returns, retrieve liabilities, manage payments, and access tax calculation data for UK businesses.
name: Hmrc
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Your feedback (opens in new tab) will help us to improve this service.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

