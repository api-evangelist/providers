---
aid: national-science-foundation
name: National Science Foundation
description: The National Science Foundation (NSF) is an independent federal agency that supports fundamental research and education in all the non-medical fields of science and engineering. NSF provides grants and funding to researchers and institutions to drive innovation, discovery, and progress.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-science-foundation/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Research
  - Science
apis:
  - aid: national-science-foundation:national-science-foundation
    name: National Science Foundation API
    tags:
      - Research
      - Science
    humanURL: https://www.nsf.gov/developer
    baseURL: https://api.nsf.gov/services/v1/
    properties:
      - url: https://www.nsf.gov/developer
        type: Documentation
      - url: https://resources.research.gov/common/webapi/awardapisearch-v1.htm
        type: Reference
      - url: https://raw.githubusercontent.com/api-evangelist/national-science-foundation/refs/heads/main/openapi/national-science-foundation-openapi.yml
        type: OpenAPI
    description: The NSF API provides an interface to Research Spending and Results functionality available through NSF's Research.gov system, including award search data showing how federal research dollars are being spent.
common:
  - type: Website
    url: https://www.nsf.gov/
  - type: Portal
    url: https://www.nsf.gov/developer
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
