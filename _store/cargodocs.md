---
aid: cargodocs
url: https://raw.githubusercontent.com/api-evangelist/cargodocs/refs/heads/main/apis.yml
name: CargoDocs
description: CargoDocs, operated by EssDocs, is a digital trade documentation platform that eliminates paper-based shipping documents by letting carriers, shippers, banks, and partner platforms issue, sign, transfer, and surrender original electronic bills of lading (eBoL), sea waybills (SWB), warehouse warrants (eWW), and supporting trade documents. CargoDocs DocEx is used by container lines, NVOCCs, bulk/tanker carriers, commodity shippers, and trade finance banks to move documents in minutes rather than days while retaining negotiability and legal effect. Developers interact with CargoDocs through three OpenAPI-described REST APIs hosted on ReadMe - the Partner API (embed DocEx in third-party platforms), the Issuer API (carrier/NVOCC issuance and amendments), and the Customer Data/Docs API (exporter drafting and back-office integration).
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bills of Lading
  - Documentation
  - eBoL
  - EssDocs
  - MLETR
  - Shipping
  - Supply Chain
  - Trade
  - Trade Finance
  - Warehouse Warrants
created: '2025-01-08'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: cargodocs:partner-api
    name: CargoDocs Partner API
    description: The CargoDocs Partner API enables platform providers and trade finance/trade management platforms to embed CargoDocs DocEx functionality, including original electronic bills of lading (eBoL) and warehouse warrants (eWW). The API exposes Partner Exchange endpoints to retrieve customer, counterparty, document, and transaction data using conditions and filters, and Action endpoints to perform operations over transactions such as signing, transferring, and surrendering documents.
    humanURL: https://cargodocs-partner.readme.io/
    baseURL: https://api.essdocs.com
    tags:
      - Bills of Lading
      - Shipping
      - Trade
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
    x-features:
      - Retrieve customer, counterparty, and transaction data with filters
      - Perform signing, transferring, and surrendering actions
      - Embed DocEx workflows in partner platforms
      - Sandbox and production API environments
      - JSON document retrieval plus PDF rendering
      - Partner-scoped authentication and audit trail
    x-use-cases:
      - Trade finance platforms embedding eBoL workflows
      - TMS/CTRM providers offering native digital docs
      - Freight forwarder portals with integrated surrender flows
      - Bank-held eBoL custody during letter-of-credit settlement
  - aid: cargodocs:issuer-api
    name: CargoDocs Issuer API
    description: The CargoDocs Issuer API enables container lines, NVOCCs, and bulk/tanker carriers to manage electronic straight and negotiable bills of lading and sea waybills at origin or destination from within their TMS. It supports sharing draft eBoL/SWB for shipper approval, signing and issuing original eBoL/SWB, receiving surrendered original electronic bills of lading, and managing amendment requests or splits of an eBoL.
    humanURL: https://cargodocs-issuer.readme.io/
    baseURL: https://api.essdocs.com
    tags:
      - Bills of Lading
      - Issuance
      - Shipping
    properties:
      - url: https://cargodocs-issuer.readme.io/
        type: Documentation
      - url: https://cargodocs-issuer.readme.io/docs/first-api-call
        type: GettingStarted
      - url: openapi/cargodocs-issuer-openapi.yml
        type: OpenAPI
      - url: json-schema/cargodocs-bill-of-lading.json
        type: JSONSchema
    x-features:
      - Draft, sign, and issue original eBoL / SWB
      - Shipper approval workflow for drafts
      - Receive surrendered original eBoL at destination
      - Amendment requests and eBoL split handling
      - Straight and negotiable bill of lading support
      - Carrier-side legal audit trail
    x-use-cases:
      - Container line TMS integration
      - NVOCC issuance automation
      - Bulk/tanker carrier documentation
      - Origin/destination eBoL surrender workflows
  - aid: cargodocs:customer-api
    name: CargoDocs Customer Data/Docs API
    description: The CargoDocs Customer Data/Docs API enables exporters and commodity shippers to draft trade and shipping documents, including tanker, bulker, or barge bills of lading, from data imported out of ERP, CTRM, TMS, or WMS systems. It also enables any party using CargoDocs to download copy documents and structured transaction data to automate back-office steps such as invoicing, reconciliation, and reporting.
    humanURL: https://cargodocs-customer.readme.io/
    baseURL: https://api.essdocs.com
    tags:
      - Documents
      - Shipping
      - Trade
    properties:
      - url: https://cargodocs-customer.readme.io/
        type: Documentation
      - url: openapi/cargodocs-customer-openapi.yml
        type: OpenAPI
      - url: json-schema/cargodocs-transaction.json
        type: JSONSchema
      - url: json-schema/cargodocs-document.json
        type: JSONSchema
    x-features:
      - Drafting of tanker, bulker, and barge bills of lading
      - ERP/CTRM/TMS/WMS data import
      - Copy document and structured data download
      - Transaction metadata for back-office automation
      - Exporter-friendly document templates
    x-use-cases:
      - Commodity shipper documentation automation
      - ERP-driven eBoL drafting
      - Back-office reconciliation of shipping documents
      - Data feeds into trade finance and invoicing systems
common:
  - type: Website
    url: https://www.essdocs.com/
  - type: Product
    url: https://www.essdocs.com/cargodocs
  - url: json-ld/cargodocs-context.jsonld
    name: CargoDocs JSON-LD Context
    type: JSONLDContext
    description: JSON-LD context document for CargoDocs domain entities.
  - type: Partner Docs
    url: https://cargodocs-partner.readme.io/
  - type: Issuer Docs
    url: https://cargodocs-issuer.readme.io/
  - type: Customer Docs
    url: https://cargodocs-customer.readme.io/
  - type: Blog
    url: https://www.essdocs.com/blog
  - type: Contact
    url: https://www.essdocs.com/contact
  - type: Terms of Service
    url: https://www.essdocs.com/terms
  - type: Privacy Policy
    url: https://www.essdocs.com/privacy
  - type: LinkedIn
    url: https://www.linkedin.com/company/essdocs
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
