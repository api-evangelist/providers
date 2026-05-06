---
aid: sm-energy
url: https://raw.githubusercontent.com/api-evangelist/sm-energy/refs/heads/main/apis.yml
name: SM Energy
tags:
  - Oil and Gas
  - Energy
  - Exploration
  - Production
  - Permian Basin
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-05-02'
modified: '2026-05-02'
position: Consumer
segments:
  - Energy
  - Oil and Gas
description: 'SM Energy Company (NYSE: SM) is an independent oil and gas exploration and production company headquartered in Denver, Colorado. Founded in 1908 (originally as St. Mary Land & Exploration Company), SM Energy focuses on acquiring, exploring, developing, and producing crude oil, natural gas, and natural gas liquids (NGLs) from top-tier assets across the Permian Basin in West Texas and New Mexico, the Maverick Basin in South Texas, the DJ Basin in Colorado, and the Uinta Basin in northeast Utah. The company is a Fortune 1000 member with approximately 1,241 employees and average daily net production of 206.8 MBoe/d. SM Energy completed a merger with Civitas Resources in early 2026. The company does not offer a public developer API; investor data is accessible through financial data APIs and SEC EDGAR.'
apis:
  - aid: sm-energy:investor-data
    name: SM Energy Investor Data
    tags:
      - Investor Relations
      - Financial Data
      - Oil and Gas
      - Energy
    humanURL: https://www.sm-energy.com/investors
    properties:
      - url: https://www.sm-energy.com/investors
        type: InvestorRelations
      - url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=SM&type=10-K
        type: SECFilings
      - url: https://www.sm-energy.com/about-us/fact-sheet
        type: FactSheet
      - url: json-ld/sm-energy-context.jsonld
        type: JSON-LD
      - url: vocabulary/sm-energy-vocabulary.yml
        type: Vocabulary
    description: 'SM Energy Company (NYSE: SM) financial and operational data is accessible through investor relations resources, SEC EDGAR filings, and third-party financial data providers. The company reports quarterly production volumes, proved reserves, capital expenditures, and hedging positions across its Permian, Maverick, DJ, and Uinta Basin operations.'
common:
  - type: Website
    url: https://www.sm-energy.com
  - type: About
    url: https://www.sm-energy.com/about-us
  - type: FactSheet
    url: https://www.sm-energy.com/about-us/fact-sheet
  - type: InvestorRelations
    url: https://www.sm-energy.com/investors
  - type: PressReleases
    url: https://www.sm-energy.com/investors/news-events/press-releases
  - type: SECFilings
    url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=SM&type=10-K
  - type: OwnerRelations
    url: https://www.sm-energy.com/owner-relations
  - type: Sustainability
    url: https://www.sm-energy.com/esg
  - type: JSON-LD
    url: json-ld/sm-energy-context.jsonld
  - type: Vocabulary
    url: vocabulary/sm-energy-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
