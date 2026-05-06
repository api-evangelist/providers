---
aid: federal-bureau-of-prisons
name: Federal Bureau of Prisons
description: The Federal Bureau of Prisons (BOP) is responsible for the custody and care of federal inmates in the United States. The BOP operates the inmate locator and publishes facility information online but does not currently offer a public, documented developer API.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-30'
modified: '2026-04-28'
position: Consumer
tags:
  - Corrections
  - Federal Government
  - Prisons
url: https://raw.githubusercontent.com/api-evangelist/federal-bureau-of-prisons/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-bureau-of-prisons:federal-bureau-of-prisons
    name: Federal Bureau of Prisons
    humanURL: https://www.bop.gov
    description: The Federal Bureau of Prisons web presence including the inmate locator and facility directory. No public developer API is currently published.
    tags:
      - Corrections
      - Prisons
    properties:
      - type: Website
        url: https://www.bop.gov
      - type: InmateLocator
        url: https://www.bop.gov/inmateloc/
      - type: FacilityLocator
        url: https://www.bop.gov/locations/list.jsp
common:
  - type: Website
    url: https://www.bop.gov
  - type: Careers
    url: https://www.bop.gov/jobs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
