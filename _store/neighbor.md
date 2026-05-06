---
aid: neighbor
name: Neighbor
description: The Neighbor API allows trusted hosts to retrieve reports related to their account, including active reservations and payout transfers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Storage
  - Marketplace
  - Reporting
created: '2025-02-09'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/neighbor/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: neighbor:neighbor
    name: Neighbor
    description: The Neighbor API allows trusted users to retrieve reservation and transfer reports related to their account.
    humanURL: https://api.neighbor.com/
    baseURL: https://api.neighbor.com
    tags:
      - Reporting
      - Storage
    properties:
      - type: Documentation
        url: https://api.neighbor.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/neighbor/refs/heads/main/openapi/neighbor-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
