---
aid: national-institutes-of-health
name: National Institutes of Health
description: The National Institutes of Health (NIH), a part of the U.S. Department of Health and Human Services, is the nation's medical research agency making important discoveries that improve health and save lives. NIH operates the RePORTER API for exposing data about NIH-funded research projects and the publications associated with them.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-institutes-of-health/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Health
  - Research
  - Funding
  - Publications
apis:
  - aid: national-institutes-of-health:reporter-api
    name: NIH RePORTER API
    tags:
      - Funding
      - Publications
      - Research
    humanURL: https://api.reporter.nih.gov
    baseURL: https://api.reporter.nih.gov
    properties:
      - url: https://api.reporter.nih.gov
        type: Documentation
      - url: https://reporter.nih.gov/
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/national-institutes-of-health/main/openapi/national-institutes-of-health-openapi.yml
        type: OpenAPI
    description: The NIH RePORTER API provides programmatic access to NIH-funded research projects and their associated publications. The Projects endpoint accepts a rich criteria object including fiscal years, principal investigators, organizations, agencies, activity codes, and award amounts. The Publications endpoint accepts PubMed identifiers, application identifiers, and core project numbers.
common:
  - type: Website
    url: https://www.nih.gov/
  - type: Portal
    url: https://api.reporter.nih.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
