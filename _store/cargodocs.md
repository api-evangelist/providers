---
aid: cargodocs
url: https://raw.githubusercontent.com/api-evangelist/cargodocs/refs/heads/main/apis.yml
apis:
- aid: cargodocs:partner-api
  name: CargoDocs Partner API
  tags:
  - Bills of Lading
  - Shipping
  - Trade
  humanURL: https://cargodocs-partner.readme.io/
  properties:
  - url: https://cargodocs-partner.readme.io/
    type: Documentation
  - url: https://cargodocs-partner.readme.io/docs/api-environments
    type: GettingStarted
  - url: openapi/cargodocs-partner-openapi.yml
    type: OpenAPI
  - url: json-schema/cargodocs-customer.json
    type: JSONSchema
  - url: json-schema/cargodocs-counterparty.json
    type: JSONSchema
  description: The CargoDocs Partner API enables partners and platform providers to embed CargoDocs DocEx functionality into their trade or trade finance platforms, handling original electronic bills of lading (eBoL) and warehouse warrants (eWW). The Partner Exchange API retrieves customer and partner data to perform specific actions, with endpoints to retrieve data based on conditions and filters and Action endpoints to action over transactions.
- aid: cargodocs:issuer-api
  name: CargoDocs Issuer API
  tags:
  - Bills of Lading
  - Issuance
  - Shipping
  humanURL: https://cargodocs-issuer.readme.io/
  properties:
  - url: https://cargodocs-issuer.readme.io/
    type: Documentation
  - url: https://cargodocs-issuer.readme.io/docs/first-api-call
    type: GettingStarted
  - url: openapi/cargodocs-issuer-openapi.yml
    type: OpenAPI
  - url: json-schema/cargodocs-bill-of-lading.json
    type: JSONSchema
  description: The CargoDocs Issuer API enables container lines or NVOCCs to manage relevant tasks relating to electronic straight and negotiable bills of lading at Origin or Destination from within their TMS. The API supports sharing draft eBoL/SWB for shipper approval, signing and issuing original eBoL/SWB, receiving surrendered original electronic bills of lading, and managing Amendment Requests or Splits of an eBoL.
- aid: cargodocs:customer-api
  name: CargoDocs Customer Data/Docs API
  tags:
  - Documents
  - Shipping
  - Trade
  humanURL: https://cargodocs-customer.readme.io/
  properties:
  - url: https://cargodocs-customer.readme.io/
    type: Documentation
  - url: openapi/cargodocs-customer-openapi.yml
    type: OpenAPI
  - url: json-schema/cargodocs-transaction.json
    type: JSONSchema
  - url: json-schema/cargodocs-document.json
    type: JSONSchema
  description: The CargoDocs Customer Data/Docs API enables exporters to draft trade and shipping documents, including tanker, bulker, or barge bills of lading from data imported from an ERP system, CTRM, TMS, WMS, etc. It also enables any party using CargoDocs to download copy docs and data to automate various back-office steps.
name: CargoDocs
tags:
- Documentation
- Shipping
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: CargoDocs is a digital platform that streamlines and automates the documentation process for global trade transactions. By digitizing and centralizing all shipping documents, such as bills of lading, certificates of origin, and invoices, CargoDocs eliminates the need for manual paperwork and reduces the risk of errors and delays.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

