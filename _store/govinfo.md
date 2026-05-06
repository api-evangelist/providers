---
aid: govinfo
name: GovInfo
url: https://raw.githubusercontent.com/api-evangelist/govinfo/refs/heads/main/apis.yml
description: The GovInfo API, provided by the U.S. Government Publishing Office (GPO), provides services for developers and webmasters to access GovInfo content and metadata, including search, packages, granules, collections, related items, and published documents.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: 3rd-Party
position: Consuming
parent: government-publishing-office
tags:
  - Federal Government
  - Government Publishing
  - Documents
  - Open Data
created: '2024-11-14'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: govinfo:govinfo
    name: GovInfo API
    description: The GovInfo API exposes search, package, granule, collection, related-item, and published-document endpoints for accessing U.S. federal government publications and their metadata.
    humanURL: https://api.govinfo.gov/docs/
    baseURL: https://api.govinfo.gov
    tags:
      - Documents
      - Federal Government
      - Search
    properties:
      - type: Documentation
        url: https://api.govinfo.gov/docs/
      - type: GettingStarted
        url: https://www.govinfo.gov/developers
      - type: SignUp
        url: https://www.govinfo.gov/api-signup
      - type: GitHub
        url: https://github.com/usgpo/api
      - type: OpenAPI
        url: openapi/openapi.yml
common:
  - type: Portal
    url: https://www.govinfo.gov
  - type: DeveloperPortal
    url: https://www.govinfo.gov/developers
  - type: Documentation
    url: https://api.govinfo.gov/docs/
  - type: SignUp
    url: https://www.govinfo.gov/api-signup
  - type: GitHub
    url: https://github.com/usgpo/api
  - type: Authentication
    url: https://api.data.gov
  - type: License
    url: https://github.com/usgpo/api/blob/master/LICENSE.md
  - type: TermsOfService
    url: https://www.govinfo.gov/about/policies
  - type: PrivacyPolicy
    url: https://www.govinfo.gov/privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
