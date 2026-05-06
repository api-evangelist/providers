---
aid: dollar-tree
name: Dollar Tree
description: Dollar Tree is a leading operator of discount variety stores in North America, operating more than 16,000 stores under the Dollar Tree and Family Dollar banners. Vendor and supplier integration is primarily handled through EDI, SAP, and ERP systems via the Dollar Tree Vendor Portal. No public REST API is currently available.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Retail
  - Discount Retail
  - EDI
  - Vendor Management
  - Fortune 500
url: https://raw.githubusercontent.com/api-evangelist/dollar-tree/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
access: 3rd-Party
position: Consuming
apis:
  - aid: dollar-tree:vendor-portal
    name: Dollar Tree Vendor Portal
    description: Dollar Tree provides a vendor portal for supplier partners to manage orders and product information. Integration with Dollar Tree is handled via EDI, SAP, and ERP systems. No public REST API is exposed.
    humanURL: https://www.dollartree.com/company-faq-vendor-partners
    baseURL: https://cvp.dollartree.com
    tags:
      - Discount Retail
      - EDI
      - Retail
      - Vendor Management
    properties:
      - type: Website
        url: https://www.dollartree.com/company-faq-vendor-partners
      - type: VendorPortal
        url: https://cvp.dollartree.com
common:
  - type: Website
    url: https://www.dollartree.com
  - type: Family Dollar
    url: https://www.familydollar.com
  - type: Vendor Portal
    url: https://cvp.dollartree.com
  - type: Careers
    url: https://careers.dollartree.com
  - type: Investor Relations
    url: https://www.dollartreeinfo.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
