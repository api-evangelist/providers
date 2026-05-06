---
aid: conocophillips
name: ConocoPhillips
description: ConocoPhillips is a leading global exploration and production company, headquartered in Houston, Texas, that is uniquely equipped to deliver reliable, responsibly produced oil and natural gas. The company operates in more than a dozen countries with conventional and unconventional crude oil, natural gas, LNG, and natural gas liquids assets. ConocoPhillips does not publish public developer APIs; its external digital surface is organized around an investor relations portal, a vendor relations portal (powered by third-party platforms such as GEP and Taulia), an LNG technology and licensing program, and a custom sustainability report builder.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/conocophillips/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
x-type: company
tags:
  - Crude Oil
  - Energy
  - Exploration and Production
  - LNG
  - Natural Gas
  - Oil and Gas
  - Sustainability
  - Upstream
  - Vendor Portal
apis:
  - aid: conocophillips:vendor-relations-portal
    name: ConocoPhillips Vendor Relations Portal
    description: The ConocoPhillips vendor relations digital channel where suppliers check invoice status, manage purchase orders via the GEP portal, and collaborate via the Taulia Supplier Portal. ConocoPhillips does not currently publish a public REST API for vendor data; integration is mediated through the underlying GEP and Taulia platforms.
    humanURL: https://vendors.conocophillips.com/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Procurement
      - Supplier Portal
      - Vendor
    properties:
      - type: Documentation
        url: https://vendors.conocophillips.com/
      - type: GEP Portal
        url: https://www.gep.com/
      - type: Taulia
        url: https://www.taulia.com/
    x-features:
      - Invoice Status
      - Purchase Order Acknowledgement
      - ACH/EFT Payment Setup
      - Supplier Communication
    x-use-cases:
      - Look up invoice status as a ConocoPhillips supplier
      - Acknowledge purchase orders via GEP
      - Manage early-payment options through Taulia
  - aid: conocophillips:lng-technology-licensing
    name: ConocoPhillips LNG Technology and Licensing
    description: ConocoPhillips licenses its Optimized Cascade liquefaction process and related LNG technologies to third-party LNG project developers. The licensing program operates as a contracted technical service rather than a public API, with technical documentation and engineering support delivered to licensed partners.
    humanURL: https://www.conocophillips.com/operations/lng-technology-licensing/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Licensing
      - LNG
      - Technology
    properties:
      - type: Documentation
        url: https://www.conocophillips.com/operations/lng-technology-licensing/
    x-features:
      - Optimized Cascade Process
      - LNG Plant Design Support
      - Licensing Agreements
    x-use-cases:
      - License LNG liquefaction technology for new projects
      - Access engineering support for cascade-process plants
  - aid: conocophillips:sustainability-report-builder
    name: ConocoPhillips Custom Sustainability Report Builder
    description: A web-based tool that lets analysts and stakeholders assemble custom sustainability reports from ConocoPhillips's published ESG data (emissions, safety, governance, etc.). Output is a curated PDF/web report rather than a developer API.
    humanURL: https://www.conocophillips.com/sustainability/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - ESG
      - Reporting
      - Sustainability
    properties:
      - type: Documentation
        url: https://www.conocophillips.com/sustainability/
    x-features:
      - Custom Report Builder
      - ESG Data Library
      - Downloadable Reports
    x-use-cases:
      - Build custom ESG reports for investor analysis
      - Compare ConocoPhillips sustainability metrics over time
common:
  - type: Website
    url: https://www.conocophillips.com
  - type: Investor Relations
    url: https://www.conocophillips.com/investors/
  - type: Vendor Portal
    url: https://vendors.conocophillips.com/
  - type: Sustainability
    url: https://www.conocophillips.com/sustainability/
  - type: News
    url: https://www.conocophillips.com/news-media/
  - type: Careers
    url: https://www.conocophillips.com/careers/
  - type: Operations
    url: https://www.conocophillips.com/operations/
  - type: Contact
    url: https://www.conocophillips.com/about-us/contact-us/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
