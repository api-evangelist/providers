---
aid: federal-motor-carrier-safety-administration
name: Federal Motor Carrier Safety Administration
description: As the lead federal government agency responsible for regulating and providing safety oversight of commercial motor vehicles (CMVs), FMCSA's mission is to reduce crashes, injuries, and fatalities involving large trucks and buses.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Federal Government
  - Safety
  - Transportation
url: https://raw.githubusercontent.com/api-evangelist/federal-motor-carrier-safety-administration/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-motor-carrier-safety-administration:federal-motor-carrier-safety-administration
    name: Federal Motor Carrier Safety Administration QCMobile API
    tags:
      - Carriers
      - Safety
      - Transportation
    humanURL: https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess
    baseURL: https://mobile.fmcsa.dot.gov/qc/services
    properties:
      - url: https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/federal-motor-carrier-safety-administration/refs/heads/main/openapi/federal-motor-carrier-safety-administration-openapi.yml
        type: OpenAPI
    description: The FMCSA QCMobile API provides access to commercial motor carrier safety data including carriers, vehicles, drivers, inspections, and crashes. Authentication uses a WebKey passed as a query parameter on each request.
common:
  - type: Website
    url: https://www.fmcsa.dot.gov/
  - type: Documentation
    url: https://mobile.fmcsa.dot.gov/QCDevsite/docs/apiAccess
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
