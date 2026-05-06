---
aid: national-endowment-for-the-humanities
name: National Endowment for the Humanities
description: The National Endowment for the Humanities (NEH) is the nation's largest public funder of the humanities, which include history, philosophy, literature, language, ethics, law, archaeology, political theory, comparative religion, anthropology, sociology, and media and cultural studies. NEH does not publish a fully documented public REST API, but it offers a Funded Project Query Form API and bulk XML datasets covering all grants awarded since 1965, plus evaluator and panelist information from 1988 onward.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-endowment-for-the-humanities/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Humanities
  - Grants
  - Open Data
apis:
  - aid: national-endowment-for-the-humanities:funded-project-query
    name: NEH Funded Project Query API
    description: Funded Project Query Form API exposing programmatic access to NEH grant records. Documentation is published as a PDF describing query parameters and response structure.
    humanURL: https://securegrants.neh.gov/publicquery/
    tags:
      - Grants
      - Humanities
      - Query
    properties:
      - type: Documentation
        url: https://securegrants.neh.gov/publicquery/api.pdf
      - type: Portal
        url: https://securegrants.neh.gov/publicquery/main.aspx
      - type: BulkData
        url: https://securegrants.neh.gov/open/data/
common:
  - type: Website
    url: https://www.neh.gov/
  - type: OpenData
    url: https://www.neh.gov/data
  - type: BulkData
    url: https://securegrants.neh.gov/open/data/
  - type: Contact
    url: https://www.neh.gov/about/contact
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
