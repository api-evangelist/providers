---
aid: swift-transportation
name: Swift Transportation
description: Swift Transportation, now operating as Knight-Swift Transportation Holdings (KNX), is the largest full truckload motor carrier in North America. The company provides truckload, LTL, logistics, and intermodal transportation services across the US, Mexico, and Canada. Technology integration is primarily through EDI for freight tendering, shipment status, and invoicing workflows with trading partners and shippers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - EDI
  - Freight
  - Logistics
  - Transportation
  - Truckload
url: https://raw.githubusercontent.com/api-evangelist/swift-transportation/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: swift-transportation:knight-swift-edi
    name: Knight-Swift EDI Integration
    description: Knight-Swift Transportation supports EDI integration for freight tendering, shipment tracking, and invoicing. Trading partners can submit load tenders (EDI 204), receive responses (EDI 990), get shipment status updates (EDI 214), and process freight invoices (EDI 210) via standard ANSI X12 EDI transactions.
    humanURL: https://www.knighttrans.com/
    tags:
      - EDI
      - Freight Tendering
      - Invoicing
      - Logistics
      - Shipment Tracking
      - Transportation
    properties:
      - type: Website
        url: https://www.knighttrans.com/
      - type: EDIDocumentation
        url: https://edixtb2b.com/partners/logistics/knight-swift-transportation
      - type: Integration
        url: https://www.cleo.com/trading-partner-network/knight-swift-transportation-holdings
common:
  - type: Website
    url: https://knight-swift.com
  - type: Website
    url: https://www.knighttrans.com
  - type: InvestorRelations
    url: https://investor.knight-swift.com/overview/default.aspx
  - type: Careers
    url: https://www.knighttrans.com/careers/
  - type: CustomerPortal
    url: https://www.knighttrans.com/shipping/
  - type: LoadBoard
    url: https://www.swifttrans.com/services/swift-logistics
  - type: DriverPortal
    url: https://www.knighttrans.com/driving/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
