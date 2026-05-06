---
aid: internal-revenue-service
name: Internal Revenue Service
description: The Internal Revenue Service (IRS) is the United States federal tax collection agency and a bureau of the Department of the Treasury. The IRS publishes developer resources for tax software providers and transmitters including the Modernized e-File (MeF) system for electronic tax return submission, the e-Services suite for authorized e-file providers, and Publication 4164 (the MeF Guide for Software Developers and Transmitters) which documents the XML schemas and transmission protocols required for integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Finance
  - IRS
  - Tax
  - Tax Filing
url: https://raw.githubusercontent.com/api-evangelist/internal-revenue-service/refs/heads/main/apis.yml
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: internal-revenue-service:modernized-e-file
    name: IRS Modernized e-File (MeF)
    description: The IRS Modernized e-File (MeF) system is the web-based electronic filing platform supporting individual, business, and tax-exempt return submission via XML-based schemas. Software developers and transmitters integrate with MeF to submit returns and receive acknowledgements.
    humanURL: https://www.irs.gov/e-file-providers/modernized-e-file-mef-internet-filing
    tags:
      - Federal Government
      - Tax Filing
    properties:
      - type: Documentation
        url: https://www.irs.gov/e-file-providers/modernized-e-file-mef-internet-filing
      - type: Schemas
        url: https://www.irs.gov/e-file-providers/modernized-e-file-mef-schemas-and-business-rules
      - type: Guide
        url: https://www.irs.gov/pub/irs-pdf/p4164.pdf
  - aid: internal-revenue-service:e-services
    name: IRS e-Services
    description: IRS e-Services is a suite of web-based products for tax professionals, reporting agents, and authorized e-file providers offering Transcript Delivery, TIN Matching, e-file application management, and secure messaging for electronic interactions with the IRS.
    humanURL: https://www.irs.gov/tax-professionals/e-services
    tags:
      - Federal Government
      - Tax Professionals
    properties:
      - type: Documentation
        url: https://www.irs.gov/tax-professionals/e-services
common:
  - type: Website
    url: https://www.irs.gov/
  - type: Developer
    url: https://www.irs.gov/e-file-providers/software-developers
  - type: Support
    url: https://www.irs.gov/help
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
