---
aid: federal-communications-commission
name: Federal Communications Commission
description: The Federal Communications Commission (FCC) regulates interstate and international communications by radio, television, wire, satellite, and cable in the United States. The FCC exposes public APIs including the Electronic Comment Filing System (ECFS) and the FCC Open Data portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Communications
  - Federal Government
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-communications-commission:ecfs
    name: FCC ECFS API
    description: The FCC Electronic Comment Filing System (ECFS) public API provides programmatic access to filings, proceedings, and submissions made to the Federal Communications Commission.
    humanURL: https://www.fcc.gov/ecfs/
    baseURL: https://publicapi.fcc.gov/ecfs
    tags:
      - Communications
      - Filings
      - Proceedings
    properties:
      - type: Documentation
        url: https://www.fcc.gov/reports-research/developers
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/openapi/ecfs.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/rules/ecfs-rules.yml
  - aid: federal-communications-commission:opendata
    name: FCC Open Data API
    description: The FCC Open Data Portal exposes datasets via the Socrata Open Data API (SODA), including the Pirate Radio Broadcasting Database, broadband deployment data, and consumer complaint summaries.
    humanURL: https://opendata.fcc.gov/
    baseURL: https://opendata.fcc.gov
    tags:
      - Communications
      - Open Data
      - Broadband
    properties:
      - type: Documentation
        url: https://opendata.fcc.gov/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/openapi/opendata.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/federal-communications-commission/refs/heads/main/rules/opendata-rules.yml
common:
  - type: Website
    url: https://www.fcc.gov/
  - type: Documentation
    url: https://www.fcc.gov/reports-research/developers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
