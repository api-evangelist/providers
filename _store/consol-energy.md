---
aid: consol-energy
name: CONSOL Energy
description: CONSOL Energy was a Pittsburgh-based coal mining company that produced high-quality bituminous coal from underground mines for sale to electric utilities, steelmakers, and industrial customers. In 2025 CONSOL Energy merged with Arch Resources to form Core Natural Resources, and the consolenergy.com domain now redirects to corenaturalresources.com. The combined company does not publish public developer APIs; its external digital surface is organized around an investor relations site, a suppliers page (with downloadable terms, conditions, and a Supplier Code of Conduct), and corporate sustainability/safety disclosures.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/consol-energy/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Bituminous Coal
  - Coal Mining
  - Core Natural Resources
  - Energy
  - Investor Relations
  - Mining
  - Suppliers
  - Sustainability
apis:
  - aid: consol-energy:supplier-relations
    name: Core Natural Resources Supplier Relations
    description: The successor company to CONSOL Energy publishes a suppliers page with a downloadable Terms and Conditions document and a Supplier Code of Conduct PDF. There is no online supplier portal, online registration, or public API; suppliers contact the company directly for onboarding.
    humanURL: https://corenaturalresources.com/suppliers/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Procurement
      - Supplier
    properties:
      - type: Documentation
        url: https://corenaturalresources.com/suppliers/
    x-features:
      - Supplier Terms and Conditions
      - Supplier Code of Conduct
    x-use-cases:
      - Review supplier obligations before contracting
      - Download Code of Conduct for compliance review
  - aid: consol-energy:investor-relations
    name: Core Natural Resources Investor Relations
    description: The investor-facing digital channel for the post-merger Core Natural Resources company. It hosts SEC filings, earnings releases, investor presentations, and corporate governance documents. Data is published as PDFs and HTML rather than as a public investor API.
    humanURL: https://corenaturalresources.com/investors/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Filings
      - Investor Relations
    properties:
      - type: Documentation
        url: https://corenaturalresources.com/investors/
    x-features:
      - SEC Filings
      - Earnings Releases
      - Investor Presentations
      - Governance Documents
    x-use-cases:
      - Track CEIX/Core Natural Resources financial reporting
      - Download earnings materials for analyst models
common:
  - type: Website
    url: https://corenaturalresources.com/
  - type: Legacy Website
    url: https://www.consol-energy.com
  - type: Suppliers
    url: https://corenaturalresources.com/suppliers/
  - type: Investors
    url: https://corenaturalresources.com/investors/
  - type: News
    url: https://corenaturalresources.com/news/
  - type: Sustainability
    url: https://corenaturalresources.com/sustainability/
  - type: Careers
    url: https://corenaturalresources.com/careers/
  - type: Contact
    url: https://corenaturalresources.com/contact/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
