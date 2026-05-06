---
aid: carlisle
url: https://raw.githubusercontent.com/api-evangelist/carlisle/refs/heads/main/apis.yml
name: Carlisle Companies
description: 'Carlisle Companies Incorporated (NYSE: CSL) is a global diversified manufacturer of highly engineered building envelope products and solutions, serving commercial and residential construction, insulation, roofing, waterproofing, and specialty markets. Carlisle''s primary operating segment is Carlisle Construction Materials (CCM), which includes brands such as Carlisle SynTec Systems, Hunter Panels, Henry Company, MB Technology, and WIP Industrial. Carlisle does not publish a public developer API; distributors and direct contractors transact through the Carlisle Customer Success Portal, and commercial trading partners integrate with Carlisle using standard X12 EDI transactions (850, 855, 856, 810) over AS2/SFTP.'
type: Index
x-type: company
position: Consumer
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Building Envelope
  - Building Products
  - Construction
  - Contractor Portal
  - Distributors
  - EDI
  - Insulation
  - Manufacturing
  - Roofing
  - Waterproofing
created: '2026-03-23'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: carlisle:customer-success-portal
    name: Carlisle Customer Success Portal
    description: The Carlisle Customer Success Portal is the primary digital channel for Carlisle Construction Materials distributors and direct contractor customers across the continental United States and Canada. It covers all commercial roofing brands under CCM and exposes web-based access to SKU-level product information, net pricing, order status, invoices, confirmations, shipping notices, and packing lists. The portal is accessed at customersuccesslogin.com or through individual brand sites and is gated by contractor or distributor credentials.
    humanURL: https://customersuccesslogin.com
    tags:
      - Building Envelope
      - Contractor Portal
      - Distributors
      - Roofing
    properties:
      - url: https://customersuccesslogin.com
        type: Portal
      - url: https://www.carlisleconstructionmaterials.com/
        type: Documentation
    x-features:
      - SKU catalog with descriptions, images, and UOM
      - Customer-specific net pricing
      - Real-time open-order tracking and ship dates
      - Order history across CCM brands
      - Invoice, order confirmation, ASN, and packing list retrieval
      - Covers all CCM commercial roofing brands
      - Available in the continental US and Canada
    x-use-cases:
      - Distributor self-service order management
      - Direct contractor pricing and order tracking
      - Accounting team invoice retrieval and reconciliation
      - Project-level material status for roofing contractors
  - aid: carlisle:edi-trading-partner
    name: Carlisle EDI Trading Partner Integration
    description: Carlisle Construction Materials and Carlisle's other operating segments exchange purchase orders, acknowledgments, advance ship notices, and invoices with distributors, retailers, and large contractors via X12 EDI. Typical transaction set usage includes 850 Purchase Order, 855 PO Acknowledgment, 856 Advance Ship Notice, and 810 Invoice over AS2 or SFTP, provisioned through Carlisle trading partner onboarding.
    humanURL: https://www.carlisle.com/our-businesses/default.aspx
    tags:
      - EDI
      - Manufacturing
      - Supply Chain
    properties:
      - url: https://www.carlisle.com/contact-us/default.aspx
        type: Contact
    x-features:
      - X12 EDI 850, 855, 856, 810 transactions
      - AS2 and SFTP connectivity
      - Distributor, retailer, and national account onboarding
      - Trading-partner-specific mapping and conformance testing
    x-use-cases:
      - Distributor replenishment automation
      - National retailer purchase order flow
      - Advance ship notice to WMS systems
      - Invoice ingestion into AP automation platforms
common:
  - type: Website
    url: https://www.carlisle.com/
  - type: Businesses
    url: https://www.carlisle.com/our-businesses/default.aspx
  - type: Construction Materials
    url: https://www.carlisleconstructionmaterials.com/
  - type: SynTec Systems
    url: https://www.carlislesyntec.com/
  - type: Investor Relations
    url: https://ir.carlisle.com/
  - type: Careers
    url: https://careers.carlisle.com/
  - type: Contact
    url: https://www.carlisle.com/contact-us/default.aspx
  - type: Privacy Policy
    url: https://www.carlisle.com/privacy-policy/default.aspx
  - type: Terms of Service
    url: https://www.carlisle.com/terms-of-use/default.aspx
  - type: LinkedIn
    url: https://www.linkedin.com/company/carlisle-companies-incorporated/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
