---
aid: fis
url: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/apis.yml
apis:
- aid: fis:fis-core-banking-api
  name: FIS Core Banking API
  tags:
  - Banking
  - Core Banking
  - Financial Services
  - Mainframe
  - SOAP
  image: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/image.png
  humanURL: https://codeconnect.fisglobal.com/
  baseURL: https://api.fisglobal.com
  properties:
  - url: https://codeconnect.fisglobal.com/
    type: Portal
  - url: https://codeconnect.fisglobal.com/
    type: Documentation
  description: FIS (Fidelity National Information Services) provides core banking platforms including the Systematics suite. APIs bridge mainframe-based account processing, transaction management, and loan servicing systems to modern integration layers via SOAP and REST interfaces.
- aid: fis:fis-payments-api
  name: FIS Payments API
  tags:
  - Banking
  - Financial Services
  - Payments
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/image.png
  humanURL: https://codeconnect.fisglobal.com/
  baseURL: https://api.fisglobal.com
  properties:
  - url: https://codeconnect.fisglobal.com/
    type: Portal
  - url: https://codeconnect.fisglobal.com/
    type: Documentation
  - url: openapi/fis-payments-openapi.yml
    type: OpenAPI
  description: FIS provides payment processing APIs through the CodeConnect marketplace, enabling integration with card processing, ACH, wire transfers, and real-time payment networks for financial institutions and fintech developers.
- aid: fis:fis-wealth-management-api
  name: FIS Wealth Management API
  tags:
  - Banking
  - Financial Services
  - REST
  - Wealth Management
  image: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/image.png
  humanURL: https://codeconnect.fisglobal.com/
  baseURL: https://api.fisglobal.com
  properties:
  - url: https://codeconnect.fisglobal.com/
    type: Portal
  - url: https://codeconnect.fisglobal.com/
    type: Documentation
  description: FIS wealth management APIs enable integration with portfolio management, account aggregation, trading, and advisory systems for wealth management platforms and financial advisors.
name: Fis
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: FIS (Fidelity National Information Services) is a global provider of financial services technology with solutions in retail and institutional banking, payments, asset and wealth management, risk and compliance, and outsourcing.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

