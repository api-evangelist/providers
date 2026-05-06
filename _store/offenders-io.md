---
aid: offenders-io
name: Offenders.io
description: Offenders.io is a technology company that specializes in providing innovative solutions for managing and monitoring offender populations. Their platform utilizes advanced data analytics and artificial intelligence to track and analyze the behavior of individuals who have been convicted of crimes. Offenders.io operates an industry-leading database of National Registered Sex Offenders for the United States, offering criteria-based search, facial recognition, and batch processing.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Sex Offenders
  - Public Safety
  - Criminal Records
created: '2024-11-13'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/offenders-io/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: offenders-io:offenders-io
    name: Offenders.io
    description: Industry-leading database of National Registered Sex Offenders API for the United States. Supports criteria-based search (name, dob, city, zip, state), facial recognition, geospatial radius queries, and batch processing.
    humanURL: https://offenders.io/
    baseURL: https://api.offenders.io
    tags:
      - Sex Offenders
      - Search
      - Geospatial
    properties:
      - type: Documentation
        url: https://offenders.io/how-to-integrate-with-offender-registry-api-complete-developer-guide/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/offenders-io/refs/heads/main/openapi/offenders-io-openapi.yml
common:
  - type: Website
    url: https://offenders.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
