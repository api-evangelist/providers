---
aid: vantiv
url: https://raw.githubusercontent.com/api-evangelist/vantiv/refs/heads/main/apis.yml
name: Vantiv
tags:
  - Payments
  - Payment Processing
  - eCommerce
  - Finance
  - FinTech
type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-03'
modified: '2026-05-03'
description: Vantiv was a leading American payment processing and technology provider that merged with Worldpay in 2018, forming Worldpay from FIS. Vantiv provided integrated payment processing solutions for merchants, financial institutions, and businesses across eCommerce, in-store, and omni-channel payment scenarios. Their cnpAPI (formerly litleAPI) supported credit card authorizations, captures, sales, refunds, voids, tokenization, chargebacks, and recurring billing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
apis:
  - aid: vantiv:cnp-api
    name: Vantiv CNP API
    tags:
      - Payments
      - Payment Processing
      - eCommerce
      - Finance
      - Card-Not-Present
    humanURL: https://developer.vantiv.com/community/ecommerce
    baseURL: https://payments.vantivprelive.com/vap/communicator/online
    properties:
      - url: https://developer.vantiv.com/community/ecommerce/pages/sdks
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/vantiv/refs/heads/main/openapi/vantiv-cnp-openapi.yml
        type: OpenAPI
    description: The Vantiv Card Not Present (CNP) API, formerly known as the Litle eCommerce API, enables online and mobile payment processing. Supports authorizations, sales, captures, credits, voids, tokenization, chargebacks, and recurring billing through XML-based HTTPS POST requests.
  - aid: vantiv:express-api
    name: Vantiv Express API
    tags:
      - Payments
      - Payment Processing
      - Point Of Sale
      - Finance
    humanURL: https://developer.vantiv.com/community/point-of-sale/pages/documentation
    baseURL: https://api.vantivintegrationtest.com/express/v1
    properties:
      - url: https://developer.vantiv.com/community/point-of-sale/pages/documentation
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/vantiv/refs/heads/main/openapi/vantiv-express-openapi.yml
        type: OpenAPI
    description: The Vantiv Integrated Payments Express API provides a REST/XML interface for point-of-sale and in-person payment processing. Supports credit, debit, EBT, gift card, and check transactions with EMV chip support.
  - aid: vantiv:chargeback-api
    name: Vantiv Chargeback API
    tags:
      - Payments
      - Chargebacks
      - Finance
      - Dispute Management
    humanURL: https://developer.vantiv.com/community/ecommerce
    baseURL: https://services.vantivprelive.com/services/chargebacks
    properties:
      - url: https://raw.githubusercontent.com/api-evangelist/vantiv/refs/heads/main/openapi/vantiv-chargeback-openapi.yml
        type: OpenAPI
    description: The Vantiv Chargeback API provides programmatic access to chargeback and dispute management, allowing merchants to retrieve chargeback details, upload evidence, and respond to disputes.
common:
  - name: Developer Community
    url: https://developer.vantiv.com/community/ecommerce
    type: Portal
  - name: eCommerce SDKs
    url: https://developer.vantiv.com/community/ecommerce/pages/sdks
    type: SDK
  - name: Sandbox Documentation
    url: https://developer.vantiv.com/docs/DOC-1347
    type: Sandbox
  - name: GitHub Organization
    url: https://github.com/Vantiv
    type: SDK
  - name: Java SDK
    url: https://github.com/Vantiv/cnp-sdk-for-java
    type: SDK
  - name: Python SDK
    url: https://github.com/Vantiv/vantiv-sdk-for-python
    type: SDK
  - name: PHP SDK
    url: https://github.com/Vantiv/cnp-sdk-for-php
    type: SDK
  - name: .NET SDK
    url: https://github.com/Vantiv/cnp-sdk-for-dotnet
    type: SDK
  - name: Ruby SDK
    url: https://github.com/Vantiv/cnp-sdk-for-ruby
    type: SDK
  - name: Chargeback SDK Java
    url: https://github.com/Vantiv/cnp-chargeback-sdk-java
    type: SDK
  - name: Worldpay Developer Hub
    url: https://developer.worldpay.com
    type: Documentation
  - name: Website
    url: https://www.vantiv.com
    type: Website
---
