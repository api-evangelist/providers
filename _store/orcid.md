---
aid: orcid
name: ORCID
description: ORCID provides a persistent digital identifier (an ORCID iD) that you own and control, and that distinguishes you from every other researcher. ORCID provides a public API for reading data from ORCID records and a member API for creating and updating records.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Academic
  - Identity
  - Researchers
created: '2025-02-06'
modified: '2026-03-16'
url: https://raw.githubusercontent.com/api-evangelist/orcid/refs/heads/main/apis.yml
specificationVersion: '0.19'
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
common:
  - type: Portal
    url: https://orcid.org/
  - type: Documentation
    url: https://info.orcid.org/documentation/
  - type: Getting Started
    url: https://info.orcid.org/documentation/api-tutorials/
  - type: Authentication
    url: https://info.orcid.org/documentation/api-tutorials/api-tutorial-get-and-authenticated-orcid-id/
  - type: Sign Up
    url: https://orcid.org/register
  - type: Login
    url: https://orcid.org/signin
  - type: Terms of Service
    url: https://info.orcid.org/terms-and-conditions-of-use/
  - type: Privacy Policy
    url: https://info.orcid.org/privacy-policy/
  - type: Support
    url: https://support.orcid.org/
  - type: GitHub Organization
    url: https://github.com/ORCID
  - type: Website
    url: https://orcid.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
