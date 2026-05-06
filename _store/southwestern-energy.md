---
aid: southwestern-energy
name: Southwestern Energy
description: Southwestern Energy Company (SWN) is one of the largest producers of natural gas in the United States, with exploration and production operations focused primarily on the Marcellus and Haynesville shales. In October 2024, Southwestern Energy completed a merger with Expand Energy Corporation (formerly Chesapeake Energy), though the SWN brand and investor relations infrastructure continues to operate under swn.com. As a Fortune 500 energy company, SWN focuses on responsible development of natural gas resources in the Appalachian Basin and Gulf Coast regions.
url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Fortune 500
  - Natural Gas
  - Energy
  - Oil And Gas
apis:
  - aid: southwestern-energy:southwestern-energy-investor-relations-api
    name: Southwestern Energy Investor Relations API
    description: The Southwestern Energy investor relations portal provides financial data, shareholder information, earnings summaries, SEC filings, and corporate governance information. The investor relations infrastructure continues to operate at ir.swn.com following the merger with Expand Energy Corporation.
    humanURL: https://ir.swn.com/
    tags:
      - Investor Relations
      - Financial Data
      - Natural Gas
    properties:
      - type: Website
        url: https://ir.swn.com/CorporateProfile/default.aspx
      - type: Investor FAQ
        url: https://ir.swn.com/resources/investor-faq/default.aspx
      - type: Shareholder Information
        url: https://www.swn.com/investors/shareholder-information/
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/json-schema/southwestern-energy-production-schema.json
  - aid: southwestern-energy:expand-energy-investor-api
    name: Expand Energy Investor Relations API
    description: Following the merger, Expand Energy Corporation's investor relations portal provides access to combined company financial data, earnings releases, SEC filings, and investor presentations for the merged natural gas production company.
    humanURL: https://investors.expandenergy.com/
    tags:
      - Investor Relations
      - Financial Data
      - Natural Gas
      - Energy
    properties:
      - type: Website
        url: https://investors.expandenergy.com/
      - type: Annual Report
        url: https://investors.expandenergy.com/static-files/e946a7e5-4ef1-4e8b-ba7b-f51506895db0
common:
  - type: Website
    url: https://www.swn.com
  - type: Investor Relations
    url: https://ir.swn.com/
  - type: Expand Energy
    url: https://www.expandenergy.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/southwestern-energy
  - type: X
    url: https://twitter.com/SWNenergy
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/json-ld/southwestern-energy-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/southwestern-energy/refs/heads/main/vocabulary/southwestern-energy-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
