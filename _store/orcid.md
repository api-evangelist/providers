---
aid: orcid
url: https://raw.githubusercontent.com/api-evangelist/orcid/refs/heads/main/apis.yml
apis:
- aid: orcid:orcid-public-api
  name: ORCID Public API
  description: The ORCID Public API allows reading publicly available data from ORCID records. Based on version 3.0 of the ORCID message schema.
  humanURL: https://info.orcid.org/documentation/features/public-api/
  baseURL: https://pub.orcid.org/v3.0
  tags:
  - Identity
  - Public
  - Researchers
  properties:
  - type: Documentation
    url: https://info.orcid.org/documentation/features/public-api/
  - type: Authentication
    url: https://info.orcid.org/documentation/features/public-api/#easy-faq-2472
  - type: Getting Started
    url: https://info.orcid.org/documentation/api-tutorials/api-tutorial-read-data-on-a-record/
- aid: orcid:orcid-member-api
  name: ORCID Member API
  description: The ORCID Member API allows member organizations to read, write, and update data on ORCID records with user permission.
  humanURL: https://info.orcid.org/documentation/features/member-api/
  baseURL: https://api.orcid.org/v3.0
  tags:
  - Identity
  - Member
  - Researchers
  properties:
  - type: Documentation
    url: https://info.orcid.org/documentation/features/member-api/
  - type: Authentication
    url: https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/
name: ORCID
tags:
- Academic
- Identity
- Researchers
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-07'
position: Consumer
description: ORCID provides a persistent digital identifier (an ORCID iD) that you own and control, and that distinguishes you from every other researcher. ORCID provides a public API for reading data from ORCID records and a member API for creating and updating records.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

