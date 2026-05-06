---
aid: freddie-mac
name: Freddie Mac
description: Freddie Mac (Federal Home Loan Mortgage Corporation) provides liquidity, stability, and affordability to the U.S. housing market. Its Single-Family API solutions span origination, selling and delivery, and servicing, delivering data and decisioning at each stage of the mortgage lifecycle.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Federal Government
  - Housing
  - Mortgage
  - Lending
  - Servicing
url: https://raw.githubusercontent.com/api-evangelist/freddie-mac/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: freddie-mac:single-family-apis
    name: Freddie Mac Single-Family APIs
    description: Suite of APIs across the mortgage lifecycle including AIM Check, Affordable Check, Property Insights, Pricing and Committing, Resolve workout decisioning, and Total MI reconciliations and claims.
    humanURL: https://sf.freddiemac.com/tools-learning/apis/our-api-solutions
    tags:
      - Mortgage
      - Origination
      - Servicing
    properties:
      - type: Documentation
        url: https://sf.freddiemac.com/tools-learning/apis/our-api-solutions
      - type: Documentation
        name: Getting Started With APIs
        url: https://sf.freddiemac.com/tools-learning/apis/getting-started-with-apis
      - type: DeveloperPortal
        url: https://developer.freddiemac.com/public/
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/freddie-mac/refs/heads/main/capabilities/freddie-mac-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/freddie-mac/refs/heads/main/rules/freddie-mac-rules.yml
common:
  - type: Website
    url: https://www.freddiemac.com/
  - type: Documentation
    url: https://sf.freddiemac.com/tools-learning/apis/our-api-solutions
  - type: DeveloperPortal
    url: https://developer.freddiemac.com/public/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
