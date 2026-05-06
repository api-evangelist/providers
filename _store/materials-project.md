---
aid: materials-project
name: Materials Project
description: The Materials Project API provides direct access to the Materials Project database, a large-scale computational materials science database with data on tens of thousands of materials. The API is offered free of charge and supports machine learning, automated analysis, and bulk data downloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/materials-project/refs/heads/main/apis.yml
tags:
  - Chemistry
  - Materials Science
  - Physics
  - Research
  - Scientific Computing
created: '2025-02-06'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: materials-project:materials-project-api
    name: Materials Project API
    description: The Materials Project API allows anyone to have direct access to current, up-to-date information from the Materials Project database in a structured way, enabling analysis, machine learning, and bulk downloads of materials science data.
    humanURL: https://next-gen.materialsproject.org/api
    baseURL: https://api.materialsproject.org
    tags:
      - Materials Science
      - Research
    properties:
      - type: Documentation
        url: https://next-gen.materialsproject.org/api
      - type: Getting Started
        url: https://docs.materialsproject.org/downloading-data/using-the-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/materials-project/refs/heads/main/openapi/materials-project-openapi.yml
common:
  - type: Portal
    url: https://materialsproject.org/
  - type: Documentation
    url: https://docs.materialsproject.org/
  - type: GitHub Organization
    url: https://github.com/materialsproject
  - type: Sign Up
    url: https://materialsproject.org/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
