---
aid: cheniere-energy
name: Cheniere Energy
x-type: company
description: Cheniere Energy, Inc. is an international energy company headquartered in Houston, Texas, and is the leading producer and exporter of liquefied natural gas (LNG) in the United States. Cheniere operates the Sabine Pass LNG terminal in Louisiana and the Corpus Christi LNG terminal in Texas, providing full-service LNG solutions including liquefaction, vessel loading, and regasification to customers worldwide. Cheniere does not currently expose a public developer API; supplier and contractor integration is handled through a dedicated portal, and investors and customers are served through corporate, sustainability, and IR channels.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cheniere-energy/refs/heads/main/apis.yml
tags:
  - Corpus Christi
  - Energy
  - Export
  - Houston
  - LNG
  - Liquefaction
  - Natural Gas
  - Regasification
  - Sabine Pass
  - Texas
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: cheniere-energy:website
    name: Cheniere Energy Website
    description: Cheniere Energy is a leading producer and exporter of liquefied natural gas (LNG) in the United States. The company does not currently offer a public developer API. Supplier and contractor integration is handled through a dedicated portal.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cheniere.com
    baseURL: https://www.cheniere.com
    tags:
      - Energy
      - Export
      - LNG
      - Natural Gas
    properties:
      - type: Website
        url: https://www.cheniere.com
      - type: SupplierPortal
        url: https://www.cheniere.com/about/resources/suppliers-and-contractors
      - type: OpenAPI
        url: openapi/cheniere.yml
common:
  - type: Website
    url: https://www.cheniere.com
  - type: SupplierPortal
    url: https://www.cheniere.com/about/resources/suppliers-and-contractors
  - type: InvestorRelations
    url: https://www.cheniere.com/investors
  - type: Sustainability
    url: https://www.cheniere.com/sustainability
  - type: Newsroom
    url: https://www.cheniere.com/news-events
  - type: Careers
    url: https://www.cheniere.com/careers
  - type: Operations
    url: https://www.cheniere.com/operations
  - type: ContactUs
    url: https://www.cheniere.com/contact-us
  - name: Operations
    type: Operations
    data:
      - name: Sabine Pass LNG Terminal
      - name: Corpus Christi LNG Terminal
      - name: Cheniere Marketing
      - name: Creole Trail Pipeline
      - name: Corpus Christi Pipeline
  - name: Services
    type: Services
    data:
      - name: LNG Liquefaction
      - name: LNG Vessel Loading
      - name: Regasification
      - name: Natural Gas Marketing
      - name: Long-Term LNG Sales and Purchase Agreements
  - name: UseCases
    type: UseCases
    data:
      - name: International LNG Export
      - name: Long-Term LNG Supply Contracts
      - name: Spot LNG Cargo Sales
      - name: Energy Security
      - name: Natural Gas Liquefaction Services
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
