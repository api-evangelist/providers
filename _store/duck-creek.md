---
aid: duck-creek
url: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/apis.yml
apis:
- aid: duck-creek:duck-creek-anywhere-api
  name: Duck Creek Anywhere REST API
  tags:
  - Billing
  - Claims
  - Insurance
  - Policy
  - REST
  - SaaS
  image: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/image.png
  humanURL: https://www.duckcreek.com/product/anywhere-integration/
  baseURL: https://api.duckcreek.com
  properties:
  - url: https://www.duckcreek.com/product/anywhere-integration/
    type: Documentation
  - url: http://duckcreek.dev/
    type: Portal
  - url: https://solutioncenter.duckcreek.com/
    type: Reference
  - url: https://www.duckcreek.com/content-exchange/anywhere_api_extension_sdk/
    type: SDKs
  - url: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/openapi/duck-creek-policy-openapi.yml
    type: OpenAPI
  description: Duck Creek Anywhere provides a RESTful API enabling non-Duck Creek systems to query product definitions, configurations, and content to drive processing within third-party systems. The platform exposes 2,600+ APIs across all Duck Creek applications using open standards. The Anywhere API Extension SDK allows developers to create custom REST API extensions to the Duck Creek Anywhere REST infrastructure.
- aid: duck-creek:duck-creek-policy-api
  name: Duck Creek Policy Administration API
  tags:
  - Insurance
  - P&C Insurance
  - Policy
  - Premium Calculation
  - Product Configuration
  image: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/image.png
  humanURL: https://www.duckcreek.com/product/policy-management-software/
  baseURL: https://api.duckcreek.com
  properties:
  - url: https://www.duckcreek.com/product/policy-management-software/
    type: Documentation
  description: Duck Creek Policy Administration API enables product configuration, premium calculation, policy lifecycle management, and policy issuance for P&C and specialty insurance carriers. Supports end-to-end policy management from quoting through renewal.
- aid: duck-creek:duck-creek-billing-api
  name: Duck Creek Billing API
  tags:
  - Billing
  - Insurance
  - P&C Insurance
  - Payments
  image: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/image.png
  humanURL: https://www.duckcreek.com/product/duck-creek-platform/
  baseURL: https://api.duckcreek.com
  properties:
  - url: https://www.duckcreek.com/product/duck-creek-platform/
    type: Documentation
  description: Duck Creek Billing API provides billing operations for insurance carriers including invoice generation, payment processing, installment plans, and billing account management.
- aid: duck-creek:duck-creek-claims-api
  name: Duck Creek Claims API
  tags:
  - Claims
  - Claims Management
  - Insurance
  - P&C Insurance
  image: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/image.png
  humanURL: https://www.duckcreek.com/product/duck-creek-platform/
  baseURL: https://api.duckcreek.com
  properties:
  - url: https://www.duckcreek.com/product/duck-creek-platform/
    type: Documentation
  description: Duck Creek Claims API supports claims intake, adjudication workflow, reserve management, and payment processing for P&C insurance carriers. Enables integration with third-party claims services and data providers.
- aid: duck-creek:duck-creek-payments-api
  name: Duck Creek Payments Orchestrator API
  tags:
  - Insurance
  - P&C Insurance
  - Payment Processing
  - Payments
  image: https://raw.githubusercontent.com/api-evangelist/duck-creek/refs/heads/main/image.png
  humanURL: https://developers.imbursepayments.com/
  baseURL: https://api.imbursepayments.com
  properties:
  - url: https://developers.imbursepayments.com/
    type: Documentation
  - url: https://developers.imbursepayments.com/
    type: Portal
  description: Duck Creek Payments Orchestrator API enables insurance carriers to orchestrate payment workflows including premium collection and claims disbursements. Provides reference documentation and how-to guides via the dedicated payments developer portal at developers.imbursepayments.com.
name: Duck Creek
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The path forward to competing today and in the future requires an open platform designed to sit at the center of your P&C solutions – and seamlessly.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

