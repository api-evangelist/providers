---
aid: delek-us-holdings
name: Delek US Holdings
description: 'Delek US Holdings, Inc. (NYSE: DK) is a diversified downstream energy company headquartered in Brentwood, Tennessee with assets in petroleum refining, logistics, asphalt operations, renewable fuels, and convenience store retailing. Delek operates four refineries in Tyler and Big Spring (Texas), El Dorado (Arkansas), and Krotz Springs (Louisiana) with combined crude throughput capacity of roughly 302,000 barrels per day. Logistics assets are operated through Delek Logistics Partners (NYSE: DKL). The company provides investor relations and ESG reporting on its public website but does not publish a developer API; partner integrations occur through industry-standard EDI, terminal automation, and ticketing systems.'
url: https://raw.githubusercontent.com/api-evangelist/delek-us-holdings/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: company
access: 3rd-Party
position: Consuming
tags:
  - Asphalt
  - Convenience Stores
  - Downstream
  - Energy
  - Logistics
  - Petroleum
  - Refining
  - Renewable Fuels
  - Retail
created: '2026-03-24'
modified: '2026-04-28'
apis:
  - aid: delek-us-holdings:delek-us-holdings-website
    name: Delek US Holdings Website
    description: Public-facing corporate website for Delek US Holdings, Inc. providing company information, business segments, sustainability reports, and investor relations material. The site does not expose a developer API.
    humanURL: https://www.delekus.com
    tags:
      - Corporate
      - Website
    properties:
      - type: Documentation
        url: https://www.delekus.com
  - aid: delek-us-holdings:delek-us-holdings-investor-relations
    name: Delek US Holdings Investor Relations
    description: Investor relations site that publishes SEC filings, earnings releases, presentations, and event webcasts for Delek US Holdings. Programmatic access is available through EDGAR and third-party financial data providers rather than a Delek API.
    humanURL: https://ir.delekus.com
    tags:
      - Earnings
      - Investor Relations
      - SEC Filings
    properties:
      - type: Documentation
        url: https://ir.delekus.com
  - aid: delek-us-holdings:delek-us-holdings-logistics
    name: Delek Logistics Partners
    description: 'Delek Logistics Partners, LP (NYSE: DKL) owns and operates crude oil and refined products pipelines, gathering systems, and terminal assets serving Delek US Holdings refineries and third-party customers. DKL maintains its own corporate website with operational and investor information.'
    humanURL: https://www.deleklogistics.com
    tags:
      - Logistics
      - Midstream
      - Pipelines
      - Terminals
    properties:
      - type: Documentation
        url: https://www.deleklogistics.com
common:
  - type: Website
    url: https://www.delekus.com
  - type: InvestorRelations
    url: https://ir.delekus.com
  - type: News
    url: https://www.delekus.com/news
  - type: ContactUs
    url: https://www.delekus.com/contact
  - type: PrivacyPolicy
    url: https://www.delekus.com/privacy-policy
  - type: TermsOfService
    url: https://www.delekus.com/terms-of-use
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
