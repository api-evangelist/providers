---
aid: international-trade-commission
name: International Trade Commission
description: The United States International Trade Commission (USITC) is an independent, nonpartisan, quasi-judicial federal agency that fulfills a range of trade-related mandates. The USITC provides high-quality analysis of international trade issues to the President and the Congress, and serves as the primary forum for the adjudication of intellectual property and trade disputes. The agency exposes U.S. trade and tariff statistics through the USITC DataWeb interactive data service.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Government Data
  - Intellectual Property
  - Trade
  - Tariffs
url: https://raw.githubusercontent.com/api-evangelist/international-trade-commission/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: international-trade-commission:usitc-dataweb
    name: USITC DataWeb
    description: The USITC DataWeb provides interactive access to U.S. international trade statistics and U.S. tariff data, including imports, exports, and production by commodity and country.
    humanURL: https://dataweb.usitc.gov/
    baseURL: https://dataweb.usitc.gov/
    tags:
      - Trade Data
      - Tariffs
      - Statistics
    properties:
      - type: Documentation
        url: https://dataweb.usitc.gov/
      - type: SignUp
        url: https://dataweb.usitc.gov/user/register
common:
  - type: Website
    url: https://www.usitc.gov/
  - type: Data
    url: https://www.usitc.gov/data/index.htm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
