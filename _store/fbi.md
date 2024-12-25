---
aid: fbi
name: Federal Bureau of Investigation
type: Index
description: |-
  The Federal Bureau of Investigation (FBI) is the domestic intelligence and security service of the United States and its principal federal law enforcement agency. 
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
- FBI
- Federal Government
created: '2024-10-18'
modified: '2024-10-18'
url: http://example.com/apis.json
specificationVersion: '0.18'
apis:
- aid: fbi:most-wanted-api
  name: Most Wanted API
  description: The FBI Wanted API is designed to help developers easily get information on the FBI Wanted program.
  image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://www.fbi.gov/wanted/api
  baseURL: https://api.fbi.gov
  tags:
  - Criminals
  - Law Enforcement
  - Most Wanted
  properties:
  - type: Documentation
    url: https://www.fbi.gov/wanted/api
  - type: OpenAPI
    url: openapi.yml
maintainers:
- FN: Kin Lane
  X-twitter: apievangelist
  email: info@apievangelist.com
---