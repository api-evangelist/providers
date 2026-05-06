---
aid: liberty-mutual-insurance
name: Liberty Mutual Insurance
description: Liberty Mutual Insurance Group is one of the largest global property and casualty insurers, headquartered in Boston, Massachusetts. The company offers a wide range of insurance products and services, including personal automobile, homeowners, workers compensation, and commercial lines, and exposes API-based insurance solutions for partners across the insurance lifecycle from quote-and-purchase through policyholder service and claims.
type: Contract
position: Producer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Casualty
  - Commercial Lines
  - Insurance
  - Personal Lines
  - Property
  - Renters
  - Safety Data
created: '2026-03-21'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/liberty-mutual-insurance/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: liberty-mutual-insurance:renters-insurance-api
    name: Liberty Mutual Renters Insurance API
    description: The Liberty Mutual Renters Insurance API streamlines the process to purchase coverage, allowing partners to offer affordable renters insurance to customers, tenants, and employees with an easy quote and bind experience integrated into websites, apps, or tools.
    humanURL: https://www.libertymutual.com/renters-api
    baseURL: https://api.libertymutual.com
    tags:
      - Bind
      - Insurance
      - Quote
      - Renters
    properties:
      - type: Documentation
        url: https://www.libertymutual.com/renters-api
      - type: OpenAPI
        url: openapi/liberty-mutual-insurance-renters-insurance-api-openapi.yml
  - aid: liberty-mutual-insurance:solaria-labs-api
    name: Liberty Mutual Solaria Labs API
    description: The Liberty Mutual Solaria Labs API aggregates public data on auto theft, parking citations, and crashes using proprietary insurance knowledge. Developers and data scientists can analyze the data to identify safest driving routes and places to park in major US cities.
    humanURL: https://developer.libertymutual.com/
    baseURL: https://developers.solarialabs.com
    tags:
      - Data Analytics
      - Innovation
      - Insurance
      - Safety
    properties:
      - type: Documentation
        url: https://developer.libertymutual.com/
      - type: OpenAPI
        url: openapi/liberty-mutual-insurance-solaria-labs-api-openapi.yml
common:
  - type: Website
    url: https://www.libertymutual.com/
  - type: Developer
    url: https://developer.libertymutual.com/
  - type: About
    url: https://www.libertymutual.com/about-lm
  - type: News
    url: https://www.libertymutual.com/about-lm/newsroom
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
