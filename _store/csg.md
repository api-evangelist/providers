---
aid: csg
url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/apis.yml
apis:
- aid: csg:csg-forte-rest-api
  name: CSG Forte REST API
  tags:
  - ACH
  - Billing
  - Credit Card
  - Payments
  - PCI
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
  humanURL: https://developers.forte.net/
  baseURL: https://api.forte.net
  properties:
  - url: https://developers.forte.net/introduction-rest-api/
    type: Documentation
  - url: https://restdocs.forte.net/
    type: Reference
  - url: https://developers.forte.net/getting-started/
    type: GettingStarted
  - url: https://www.forte.net/test-account-setup/
    type: Sandbox
  - url: https://releases.forte.net/
    type: ChangeLog
  - url: https://status.forte.net/
    type: Status
  - url: https://support.forte.net/
    type: Support
  - url: https://training.forte.net/
    type: Training
  - url: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/openapi/csg-forte-rest-openapi.yml
    type: OpenAPI
  description: CSG Forte provides full-stack REST APIs for payment processing within a PCI-compliant architecture. The API enables merchants and partners to create and update credit card, echeck, and scheduled transactions, securely manage customer and payment data, and query settlement information. Authentication uses standard HTTP credential headers.
- aid: csg:csg-forte-js
  name: CSG Forte.js
  tags:
  - JavaScript
  - Payments
  - SDK
  - Web
  image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
  humanURL: https://developers.forte.net/forte-js/
  baseURL: https://api.forte.net
  properties:
  - url: https://developers.forte.net/forte-js/
    type: Documentation
  description: Forte.js is a JavaScript library for secure browser-based payment tokenization. It enables web applications to collect and tokenize payment card data client-side before submitting to Forte's payment API, reducing PCI scope.
- aid: csg:csg-forte-react-native-sdk
  name: CSG Forte React Native SDK
  tags:
  - Mobile
  - Payments
  - React Native
  - SDK
  image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
  humanURL: https://developers.forte.net/forte-react-native/
  baseURL: https://api.forte.net
  properties:
  - url: https://developers.forte.net/forte-react-native/
    type: Documentation
  - url: https://developers.forte.net/forte-react-native/
    type: SDKs
  description: The Forte React Native SDK enables mobile application developers to integrate payment processing capabilities into iOS and Android apps built with React Native.
- aid: csg:csg-singleview-api
  name: CSG Singleview Billing API
  tags:
  - Billing
  - BSS
  - Revenue Management
  - SOAP
  - Telecom
  image: https://raw.githubusercontent.com/api-evangelist/csg/refs/heads/main/image.png
  humanURL: https://www.csgi.com/
  baseURL: https://api.csgi.com
  properties:
  - url: https://www.csgi.com/
    type: Documentation
  description: CSG Singleview is a comprehensive, convergent billing and revenue management platform designed for communication service providers. APIs enable subscriber billing, usage rating, invoice generation, and payment processing across converged 5G and IoT services.
name: Csg
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: CSG is a global provider of customer engagement, revenue management, and payments solutions enabling communications, media, and entertainment companies to monetize and digitally enable customer experiences.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

