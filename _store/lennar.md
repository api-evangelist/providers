---
aid: lennar
name: Lennar
description: Lennar Corporation is a Fortune 500 company and one of the leading homebuilders of new homes for sale in the United States. Lennar operates an internal Azure-hosted API Management developer portal where Lennar developers and partners discover and consume Lennar Corporation APIs. Public OpenAPI artifacts have not been observed; access generally requires sign-in and partner approval.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Partner
tags:
  - Homebuilder
  - Real Estate
  - Fortune 500
  - Mortgage
url: https://raw.githubusercontent.com/api-evangelist/lennar/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: lennar:lennar-corporation-developer-portal
    name: Lennar Corporation Developer Portal
    description: Azure API Management developer portal for Lennar Corporation. Allows developers to discover Lennar APIs, sign up for an API key, read the auto-generated reference, and exercise endpoints from the API console. No public OpenAPI spec is exposed without authentication.
    humanURL: https://azu-lndscapmu01e.portal.azure-api.net/
    tags:
      - Developer Portal
      - Azure API Management
    properties:
      - url: https://azu-lndscapmu01e.portal.azure-api.net/
        type: DeveloperPortal
  - aid: lennar:lennar-mortgage-fannie-mae
    name: Lennar Mortgage Fannie Mae Integration
    description: Lennar Mortgage, LLC is listed as a Fannie Mae technology integration partner using Fannie Mae's lending APIs. The technical contract is owned by Fannie Mae; Lennar Mortgage is the consumer.
    humanURL: https://singlefamily.fanniemae.com/applications-programming-interfaces-apis/lennar-mortgage-llc
    tags:
      - Mortgage
      - Lending
      - Partner Integration
    properties:
      - url: https://singlefamily.fanniemae.com/applications-programming-interfaces-apis/lennar-mortgage-llc
        type: Documentation
common:
  - url: https://www.lennar.com
    type: Website
  - url: https://azu-lndscapmu01e.portal.azure-api.net/
    type: DeveloperPortal
  - url: https://investor-marketplace.lennar.com/
    type: InvestorRelations
  - url: https://www.lennar.com/privacypolicy
    type: PrivacyPolicy
  - url: https://www.lennar.com/contact/business-inquiry
    type: BusinessInquiries
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
