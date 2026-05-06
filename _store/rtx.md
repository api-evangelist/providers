---
aid: rtx
name: RTX
description: 'RTX Corporation is a leading American aerospace and defense company comprising three market businesses: Collins Aerospace, Pratt & Whitney, and Raytheon. Raytheon develops the EAGLE (Enhanced Automated Graphical Logistics Environment) software platform for integrated logistics support and logistic support analysis across defense programs. RTX BBN Technologies (a Raytheon subsidiary) develops open-source software including SPARQL triple stores, NLP frameworks, and TAK ecosystem plugins for government and military situational awareness platforms.'
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Defense
  - Aerospace
  - Government
  - Logistics
  - Intelligence
  - Military
created: '2025-01-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/rtx/refs/heads/main/apis.yml
specificationVersion: '0.19'
x-fortune: Fortune 500
apis:
  - aid: rtx:eagle-api
    name: RTX EAGLE API
    description: The RTX EAGLE (Enhanced Automated Graphical Logistics Environment) API provides integration capabilities for the EAGLE logistics support analysis platform developed by Raytheon. EAGLE manages product support throughout a defense system's entire lifespan, enabling users to build and maintain logistics data, create reports, and support fielded systems through operations and maintenance. The API supports integration with intelligence analysis, data management, and analytics workflows used in defense and government environments.
    humanURL: https://www.rtx.com/raytheon/eagle
    baseURL: https://api.rtx.com/eagle
    tags:
      - Defense
      - Logistics
      - Intelligence
      - Analytics
      - Government
    properties:
      - type: Documentation
        url: https://www.rtx.com/raytheon/eagle
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/rtx/refs/heads/main/openapi/rtx-eagle-api-openapi.yml
common:
  - type: Website
    url: https://www.rtx.com/
  - type: Developer
    url: https://www.rtx.com/raytheon/eagle
  - type: GitHub
    url: https://github.com/raytheonbbn
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
