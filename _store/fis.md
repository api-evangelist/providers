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
common:
  aid: fis
  name: FIS Global
  description: FIS (Fidelity National Information Services) is a global leader in financial technology providing APIs for core banking, payments, wealth management, and capital markets through the CodeConnect API marketplace. APIs connect financial institutions, fintechs, and enterprises to FIS banking and payment infrastructure.
  image: https://raw.githubusercontent.com/api-evangelist/fis/refs/heads/main/image.png
  tags:
    - Banking
    - Core Banking
    - Financial Services
    - Payments
    - Fintech
  properties:
    - url: https://codeconnect.fisglobal.com/
      type: Portal
    - url: https://codeconnect.fisglobal.com/
      type: Documentation
    - url: https://www.fisglobal.com/terms-of-use
      type: Terms of Service
    - url: https://www.fisglobal.com/privacy
      type: Privacy Policy
    - url: https://www.fisglobal.com/
      type: Website
    - url: https://www.fisglobal.com/blog
      type: Blog
    - url: openapi/fis-payments-openapi.yml
      type: OpenAPI
    - url: json-schema/fis-payment-schema.json
      type: JSONSchema
    - url: json-ld/fis-context.jsonld
      type: JSONLDContext
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: FIS (Fidelity National Information Services) is a global provider of financial services technology with solutions in retail and institutional banking, payments, asset and wealth management, risk and compliance, and outsourcing.
---
