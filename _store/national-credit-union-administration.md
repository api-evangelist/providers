---
aid: national-credit-union-administration
name: National Credit Union Administration
description: Created by the U.S. Congress in 1970, the National Credit Union Administration is an independent federal agency that insures deposits at federally insured credit unions, protects the members who own credit unions, and charters and regulates federal credit unions. NCUA publishes Call Report and Financial Performance data and a Credit Union Locator, but does not currently document a public REST API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-credit-union-administration/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Credit Unions
  - Federal Government
  - Finance
  - Banking
apis:
  - aid: national-credit-union-administration:ncua-data
    name: NCUA Data and Call Reports
    tags:
      - Credit Unions
      - Finance
      - Call Reports
      - Open Data
    humanURL: https://ncua.gov/data
    properties:
      - url: https://ncua.gov/data
        type: Documentation
      - url: https://mapping.ncua.gov/ResearchCreditUnion
        type: ResearchTool
      - url: https://mapping.ncua.gov/
        type: Locator
    description: The NCUA publishes downloadable Call Report data, Financial Performance Reports, and a Research a Credit Union tool. There is no documented public REST API at this time; data is available as downloadable bulk files and through interactive web tools.
common:
  - type: Website
    url: https://www.ncua.gov/
  - type: Portal
    url: https://ncua.gov/data
  - type: Locator
    url: https://mapping.ncua.gov/
  - type: Contact
    url: mailto:BImail@ncua.gov
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
