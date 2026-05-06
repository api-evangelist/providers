---
aid: global-payments
name: Global Payments
description: Global Payments is a leading worldwide provider of payment technology and software solutions delivering innovative services to customers globally. The company operates developer portals at developer.globalpayments.com and developer.globalpaymentsintegrated.com, offering a unified cloud-powered REST API for payment facilitation, card issuing, and multi-currency processing, along with integrated payment solutions for ISVs and software partners.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - eCommerce
  - Payment Processing
  - Payment Technology
  - Payments
  - POS
created: '2026-03-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/global-payments/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: global-payments:payments-api
    name: Global Payments Unified Payments API
    tags:
      - eCommerce
      - Payment Processing
      - Payment Technology
      - Payments
      - POS
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://apis.globalpay.com
    humanURL: https://developer.globalpayments.com/
    properties:
      - url: https://developer.globalpayments.com/
        type: Portal
      - url: https://developer.globalpayments.com/#!/api
        type: Documentation
      - url: openapi/global-payments-unified-payments-api-openapi.yml
        type: OpenAPI
    description: The Global Payments Unified Payments API is a cloud-powered REST API providing partners and developers with a single integration point for payment facilitation, card issuing, and multi-currency payment processing. The API supports sandbox testing, comprehensive SDKs, and OAuth 2.0 authentication for secure payment operations across POS, eCommerce, and in-app channels.
  - aid: global-payments:integrated-api
    name: Global Payments Integrated API
    tags:
      - ISV
      - Payment Integration
      - Payments
      - Software Partners
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.globalpaymentsintegrated.com
    humanURL: https://developer.globalpaymentsintegrated.com/
    properties:
      - url: https://developer.globalpaymentsintegrated.com/
        type: Portal
      - url: https://www.globalpaymentsintegrated.com/en-us/apis-and-sdks/developer-resources
        type: Documentation
    description: The Global Payments Integrated API provides ISVs and software partners with payment integration capabilities including credit card processing, ACH payments, and reporting. The platform supports semi-integrated and fully integrated solutions with developer resources, SDKs, and sandbox environments.
common:
  - type: Portal
    url: https://developer.globalpayments.com/
  - type: Website
    url: https://www.globalpayments.com/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
