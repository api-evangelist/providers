---
aid: lincoln-national
name: Lincoln National
description: Lincoln National Corporation, operating as Lincoln Financial Group, is a diversified financial services company offering annuities, retirement plan services, life insurance, and group protection products. The company provides solutions for employers, brokers, and retirement professionals through its LincSmart platform of API integrations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Annuities
  - Benefits
  - Enrollment
  - HR
  - Insurance
  - Retirement
url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: lincoln-national:lincsmart-enrollment-api
    name: Lincoln Financial LincSmart Enrollment API
    description: The LincSmart Enrollment API ensures that employee elections and demographic information are synced in real time, eliminating lengthy setup time for weekly batch files.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/index.html
    baseURL: https://www.lincolnfinancial.com
    tags:
      - Benefits
      - Enrollment
      - HR
      - Insurance
    properties:
      - type: Documentation
        url: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/openapi/lincoln-national-openapi.yml
  - aid: lincoln-national:lincsmart-eoi-api
    name: Lincoln Financial LincSmart EOI Solution API
    description: The LincSmart EOI Solution API sends benefits enrollment decisions to employee platforms in real time, eliminating manual work and paper forms for evidence of insurability.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/assets/resources/info/eoi.html
    baseURL: https://www.lincolnfinancial.com
    tags:
      - Benefits
      - Evidence of Insurability
      - HR
      - Insurance
    properties:
      - type: Documentation
        url: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/assets/resources/info/eoi.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/openapi/lincoln-national-openapi.yml
  - aid: lincoln-national:lincsmart-plan-design-api
    name: Lincoln Financial LincSmart Plan Design API
    description: The LincSmart Plan Design API allows plan information like rules and rates to flow from Lincoln to benefits administration platforms automatically.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/assets/resources/info/plan.html
    baseURL: https://www.lincolnfinancial.com
    tags:
      - Benefits
      - HR
      - Insurance
      - Plan Design
    properties:
      - type: Documentation
        url: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/assets/resources/info/plan.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/openapi/lincoln-national-openapi.yml
common:
  - type: Website
    url: https://www.lincolnfinancial.com
  - type: LincSmartPlatform
    url: https://www.lincolnfinancial.com/public/static/digitalbrochure/gp/lincsmart/index.html
  - type: Portal
    url: https://www.mylincolnportal.com
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/lincoln-national/refs/heads/main/openapi/lincoln-national-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
