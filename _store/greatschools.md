---
aid: greatschools
name: GreatSchools
description: GreatSchools provides school information, ratings, and quality data via its Developer Hub APIs, including the School Essentials API for school details and the School Quality API for GreatSchools rating bands.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Schools
  - Education
  - Ratings
  - Geolocation
url: https://raw.githubusercontent.com/api-evangelist/greatschools/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: greatschools:school-essentials
    name: GreatSchools School Essentials API
    description: Retrieve key information about schools across the United States based on proximity to a location or filtered by name, type, and more. Returns school names, addresses, grades offered, type, and website links.
    humanURL: https://www.greatschools.org/api
    tags:
      - Schools
      - Education
      - Geolocation
    properties:
      - type: Pricing
        url: https://www.greatschools.org/api
      - type: Developer Hub
        url: https://www.greatschools.org/api
  - aid: greatschools:school-quality
    name: GreatSchools School Quality API
    description: Builds on School Essentials by adding GreatSchools School Rating Bands (below average, average, above average) to assess school quality.
    humanURL: https://www.greatschools.org/api
    tags:
      - Schools
      - Education
      - Ratings
    properties:
      - type: Pricing
        url: https://www.greatschools.org/api
      - type: Developer Hub
        url: https://www.greatschools.org/api
common:
  - type: Website
    url: https://www.greatschools.org
  - type: Developer Hub
    url: https://www.greatschools.org/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
