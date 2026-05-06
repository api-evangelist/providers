---
aid: cf-industries-holdings
url: https://raw.githubusercontent.com/api-evangelist/cf-industries-holdings/refs/heads/main/apis.yml
name: CF Industries Holdings
tags:
  - Agriculture
  - Ammonia
  - Chemicals
  - Clean Energy
  - Fertilizer
  - Fortune 500
  - Hydrogen
  - Investor Relations
  - Low-Carbon
  - Manufacturing
  - Nitrogen
  - Supply Chain
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: CF Industries Holdings is a Fortune 500 American manufacturer and distributor of nitrogen-based fertilizers (ammonia, urea, ammonium nitrate, UAN) and clean-energy products serving agricultural and industrial customers worldwide. CF operates one of the largest global ammonia production networks and is scaling clean (blue and green) ammonia for low-carbon energy. CF does not publish a public developer API program; programmatic data access is limited to investor-relations SEC filings feeds, press/news RSS, and partner EDI/B2B integrations with agricultural distributors, rail, terminal, and industrial customers.
apis:
  - aid: cf-industries-holdings:cf-investor-relations
    name: CF Industries Investor Relations Data
    tags:
      - EDGAR
      - Earnings
      - Financial
      - Investor
      - SEC
    humanURL: https://www.cfindustries.com/investors
    properties:
      - url: https://www.cfindustries.com/investors
        type: Website
      - url: https://www.cfindustries.com/newsroom/press-releases
        type: PressReleases
      - url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001324404
        type: SECEDGAR
    description: CF Industries publishes financial disclosures, press releases, and investor presentations that are accessible programmatically through SEC EDGAR filings feeds and the corporate newsroom RSS.
  - aid: cf-industries-holdings:cf-edi-b2b
    name: CF Industries EDI / B2B Supply Chain
    tags:
      - B2B
      - EDI
      - Rail
      - Supply Chain
    humanURL: https://www.cfindustries.com/what-we-do
    properties:
      - url: https://www.cfindustries.com/what-we-do
        type: Website
      - url: https://www.cfindustries.com/products
        type: Products
    description: CF Industries exchanges orders, shipments, and invoices with distributors, rail carriers, and industrial customers through traditional EDI transactions and private B2B integrations rather than public REST APIs. These connections support the company's global terminal and distribution network across North America, the United Kingdom, and export markets.
common:
  - type: Website
    url: https://www.cfindustries.com/
  - type: About
    url: https://www.cfindustries.com/about-us
  - type: WhatWeDo
    url: https://www.cfindustries.com/what-we-do
  - type: Products
    url: https://www.cfindustries.com/products
  - type: Investors
    url: https://www.cfindustries.com/investors
  - type: Newsroom
    url: https://www.cfindustries.com/newsroom
  - type: Sustainability
    url: https://www.cfindustries.com/sustainability
  - type: Wikipedia
    url: https://en.wikipedia.org/wiki/CF_Industries
  - type: Privacy Policy
    url: https://www.cfindustries.com/privacy-policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
