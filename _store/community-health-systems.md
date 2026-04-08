---
aid: community-health-systems
url: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/apis.yml
apis:
- aid: community-health-systems:patient-access-api
  name: Community Health Systems Patient Access API
  tags:
  - FHIR
  - Healthcare
  - Interoperability
  - Patient Access
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.chs.net
  humanURL: https://www.chs.net
  properties:
  - url: https://www.chs.net
    type: Documentation
  - url: openapi/chs-patient-access-api-openapi.yml
    type: OpenAPI
  description: Community Health Systems provides healthcare interoperability APIs pursuant to the CMS Interoperability and Patient Access Final Rule (CMS-9115-F). The Patient Access API allows third-party applications to retrieve data concerning adjudicated claims, encounters, formulary data, and clinical data using FHIR (Fast Healthcare Interoperability Resources) standards.
- aid: community-health-systems:provider-directory-api
  name: Community Health Systems Provider Directory API
  tags:
  - FHIR
  - Healthcare
  - Interoperability
  - Provider Directory
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.chs.net
  humanURL: https://www.chs.net
  properties:
  - url: https://www.chs.net
    type: Documentation
  description: The Community Health Systems Provider Directory API allows third-party applications and payers to retrieve provider and pharmacy directory information in compliance with CMS interoperability requirements. The API uses FHIR standards for healthcare data exchange.
name: Community Health Systems
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: For more than 40 years, CHS has been developing and operating healthcare delivery systems committed to helping people get well and live healthier.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

