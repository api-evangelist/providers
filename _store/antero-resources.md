---
name: Antero Resources
description: Antero Resources is an independent oil and natural gas company engaged in the exploration, development, and production of natural gas, NGLs, and oil properties in the Appalachian Basin (West Virginia and Ohio). It is one of the largest natural gas producers in the United States, with operations focused on the Marcellus and Utica Shale formations.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/antero-resources/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.16'
tags:
  - Energy
  - Natural Gas
  - NGL
  - Oil And Gas
  - Upstream
apis:
  - name: Antero Resources SEC EDGAR Filings
    description: 'Antero Resources Corporation (NYSE: AR) files annual reports (10-K), quarterly reports (10-Q), current reports (8-K), proxy statements, and other regulatory disclosures with the U.S. Securities and Exchange Commission. These filings are accessible via the SEC EDGAR full-text search API and the EDGAR data APIs for machine-readable financial data.'
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001433270&type=&dateb=&owner=include&count=40
    baseURL: https://data.sec.gov/submissions/CIK0001433270.json
    tags:
      - Energy
      - Financial Data
      - Natural Gas
      - Oil And Gas
      - SEC Filings
    properties:
      - type: Documentation
        url: https://efts.sec.gov/LATEST/search-index?q=%22antero+resources%22&dateRange=custom&startdt=2020-01-01&enddt=2026-04-19&forms=10-K
      - type: APIReference
        url: https://data.sec.gov/submissions/CIK0001433270.json
    contact:
      - FN: SEC EDGAR Support
        url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001433270
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
    X: apievangelist
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://www.anteroresources.com
  - type: TermsOfService
    url: https://www.anteroresources.com/legal/terms-and-conditions
  - type: PrivacyPolicy
    url: https://www.anteroresources.com/legal/privacy-policy
---
