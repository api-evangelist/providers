---
aid: bureau-of-engraving-and-printing
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-engraving-and-printing/refs/heads/main/apis.yml
name: Bureau of Engraving and Printing
tags:
  - Currency
  - Engraving
  - Federal Government
  - Money
  - Printing
  - Security Printing
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-25'
modified: '2026-04-21'
position: Consumer
description: The Bureau of Engraving and Printing (BEP) is an agency of the U.S. Department of the Treasury that designs and produces U.S. currency (Federal Reserve Notes), postage stamps, and other official U.S. government security documents. BEP offers a U.S. Currency Reader Program for the visually impaired and provides a mutilated currency redemption service.
apis:
  - aid: bureau-of-engraving-and-printing:bep-currency-reader-program
    name: BEP U.S. Currency Reader Program
    tags:
      - Accessibility
      - Currency
      - Federal Government
    humanURL: https://www.bep.gov/currency/current-currency-features/uscurrency-reader-program
    properties:
      - url: https://www.bep.gov/currency/current-currency-features/uscurrency-reader-program
        type: Documentation
    description: The BEP U.S. Currency Reader Program provides free currency readers to blind and visually impaired individuals in the United States, enabling them to identify Federal Reserve Note denominations using accessible technology.
  - aid: bureau-of-engraving-and-printing:bep-mutilated-currency-redemption
    name: BEP Mutilated Currency Redemption
    tags:
      - Currency
      - Federal Government
      - Redemption
    humanURL: https://www.bep.gov/services/mutilated-currency-redemption
    properties:
      - url: https://www.bep.gov/services/mutilated-currency-redemption
        type: Documentation
    description: The BEP redeems severely damaged or mutilated Federal Reserve Notes as a free public service. Citizens can submit damaged currency for examination and potential redemption.
  - aid: bureau-of-engraving-and-printing:bep-data-catalog
    name: BEP Data and Publications
    tags:
      - Currency
      - Federal Government
      - Publications
      - Statistics
    humanURL: https://www.bep.gov/currency
    properties:
      - url: https://catalog.data.gov/dataset?organization=bep-gov
        type: DataAPI
      - url: https://www.bep.gov/currency
        type: Documentation
    description: BEP publishes currency production figures, annual reports, and historical data about Federal Reserve Note printing. Data is available via data.gov for programmatic access.
common:
  - type: Website
    url: https://www.bep.gov/
  - type: Privacy Policy
    url: https://www.bep.gov/privacy-policy
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=bep-gov
  - type: Currency Features
    url: https://www.bep.gov/currency/current-currency-features
  - type: About
    url: https://www.bep.gov/about
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
