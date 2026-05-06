---
aid: peopleforce
name: PeopleForce
description: PeopleForce is an HR platform whose REST API allows retrieving information about HR entities such as employees, candidates, vacancies, leave requests, departments, divisions, and positions, and performing actions on them.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - HR
  - Human Resources
  - Recruitment
  - Employees
created: '2025-02-08'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/peopleforce/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: peopleforce:peopleforce
    name: PeopleForce API
    description: PeopleForce REST API for managing HR entities including employees, candidates, vacancies, leave requests, departments, divisions, and positions.
    humanURL: https://developer.peopleforce.io/docs/getting-started
    baseURL: https://app.peopleforce.io/api/public/v2
    tags:
      - HR
      - Human Resources
      - Recruitment
      - Employees
    properties:
      - type: Documentation
        url: https://developer.peopleforce.io/docs/getting-started
      - type: Reference
        url: https://developer.peopleforce.io/reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/peopleforce/refs/heads/main/openapi/peopleforce-openapi.yml
common:
  - type: Portal
    url: https://peopleforce.io/
  - type: Documentation
    url: https://developer.peopleforce.io/docs/getting-started
  - type: Login
    url: https://app.peopleforce.io
  - type: Website
    url: https://peopleforce.io/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
