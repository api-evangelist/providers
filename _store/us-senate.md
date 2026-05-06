---
aid: us-senate
url: https://raw.githubusercontent.com/api-evangelist/us-senate/refs/heads/main/apis.yml
apis:
  - aid: us-senate:lda-api
    name: Senate Lobbying Disclosure Act (LDA) API
    tags:
      - Lobbying
      - Government Transparency
      - Federal Government
      - Open Data
      - Campaign Finance
    humanURL: https://lda.senate.gov/api/
    properties:
      - url: https://lda.senate.gov/api/
        type: Documentation
      - url: https://lda.senate.gov/api/redoc/v1/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-senate/refs/heads/main/openapi/us-senate-lda-openapi.yml
        type: OpenAPI
    description: The Senate Lobbying Disclosure Act (LDA) REST API provides public access to lobbying disclosure filings, registrations, quarterly activity reports (LD-2), and semi-annual contribution reports (LD-203) submitted under the Lobbying Disclosure Act. Includes data on registrants, clients, lobbyists, and lobbying activities. An API key increases rate limits from 15 to 120 requests per minute.
name: US Senate
tags:
  - Federal Government
  - Lobbying
  - Government Transparency
  - Campaign Finance
  - Open Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: The United States Senate is one of the two chambers of Congress, responsible for representing the interests of the individual states and ensuring that federal legislation is passed in a fair and representative manner. The Senate plays a crucial role in the legislative process, with its members debating and voting on bills and resolutions that affect the country as a whole. The Senate also administers the Lobbying Disclosure Act (LDA) reporting system, which requires lobbyists and lobbying firms to register and report their activities, clients, and campaign contributions for public transparency.
features:
  - Lobbying Filing Search and Retrieval
  - Registrant Information
  - Client Information
  - Lobbyist Profiles
  - Campaign Contribution Reports
  - Reference Data (Issue Codes, Government Entities)
useCases:
  - Government transparency research
  - Lobbying activity monitoring and analysis
  - Campaign finance research
  - Policy influence tracking
  - Compliance verification for lobbyists
  - Investigative journalism
integrations:
  - data.gov
solutions:
  - Government Transparency
  - Lobbying Compliance
  - Policy Research
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
