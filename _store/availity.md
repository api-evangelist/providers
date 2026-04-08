---
aid: availity
url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/apis.yml
apis:
- aid: availity:availity-eligibility-benefits-api
  name: Availity Eligibility & Benefits API
  tags:
  - Benefits
  - EDI
  - Eligibility
  - Healthcare
  - X12 270/271
  image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
  humanURL: https://developer.availity.com/
  baseURL: https://api.availity.com
  properties:
  - url: https://developer.availity.com/partner/documentation
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  - url: https://developer.availity.com/blog/2025/3/4/ebvalue-add-api
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/openapi/availity-eligibility-openapi.yml
    type: OpenAPI
  description: The Availity Eligibility & Benefits API supports the ASC X12N 270 and 271 transactions, enabling real-time verification of member coverage, co-pays, deductibles, and benefits information. REST APIs connect provider systems to every major health plan nationwide for eligibility checks.
- aid: availity:availity-claims-status-api
  name: Availity Claim Status API
  tags:
  - Claims
  - Clearinghouse
  - EDI
  - Healthcare
  - X12 276/277
  image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
  humanURL: https://developer.availity.com/
  baseURL: https://api.availity.com
  properties:
  - url: https://developer.availity.com/partner/documentation
    type: Documentation
  - url: https://developer.availity.com/blog/2025/3/25/enhanced-claim-status
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  description: The Availity Claim Status API enables the standard ASC X12N 276 and 277 transactions, allowing providers to find, create, and manage claim status inquiries against payer systems. REST APIs bridge provider billing systems and payers through the Availity clearinghouse network.
- aid: availity:availity-claim-attachments-api
  name: Availity Claim Attachments API
  tags:
  - Attachments
  - Claims
  - Clearinghouse
  - EDI
  - Healthcare
  image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
  humanURL: https://developer.availity.com/
  baseURL: https://api.availity.com
  properties:
  - url: https://developer.availity.com/blog/2025/2/28/claim-attachment-api
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  description: The Availity Claim Attachments API enables electronic submission of supporting documentation alongside healthcare claims. REST APIs support structured and unstructured attachment types for additional clinical information required by payers during claims adjudication.
- aid: availity:availity-service-reviews-api
  name: Availity Service Reviews (Prior Authorization) API
  tags:
  - EDI
  - Healthcare
  - Prior Authorization
  - Service Reviews
  - X12 278
  image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
  humanURL: https://developer.availity.com/
  baseURL: https://api.availity.com
  properties:
  - url: https://developer.availity.com/blog/2025/3/4/service-reviews
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  description: The Availity Service Reviews API enables the ASC X12N 278 transaction for prior authorization and healthcare service review. REST APIs allow providers to find, create, and manage authorization requests and responses with health plan payers through the Availity clearinghouse.
- aid: availity:availity-hipaa-transactions-api
  name: Availity Healthcare HIPAA Transactions API
  tags:
  - Clearinghouse
  - EDI
  - Healthcare
  - HIPAA
  image: https://raw.githubusercontent.com/api-evangelist/availity/refs/heads/main/image.png
  humanURL: https://developer.availity.com/portal/catalogue-products/healthcare-hipaa-transactions-1
  baseURL: https://api.availity.com
  properties:
  - url: https://developer.availity.com/portal/catalogue-products/healthcare-hipaa-transactions-1
    type: Documentation
  - url: https://developer.availity.com/blog/2025/3/25/hipaa-transactions
    type: Documentation
  - url: https://developer.availity.com/partner/gettingstarted
    type: GettingStarted
  description: The Availity Healthcare HIPAA Transactions API provides a unified interface for standard HIPAA EDI transactions. REST APIs enable healthcare providers and vendors to submit and receive X12 EDI transactions across payers including eligibility, claims, remittance, authorizations, and referrals.
name: Availity
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Create your application and subscribe to a plan to make use of our APIs.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

