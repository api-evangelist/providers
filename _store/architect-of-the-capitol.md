---
aid: architect-of-the-capitol
name: Architect of the Capitol
description: The Architect of the Capitol (AOC) serves Congress and the Supreme Court as builder and steward of Capitol Hill's landmark buildings and grounds, preserving historic structures, monuments, art, and gardens across the Capitol campus.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Capitol Hill
  - Congress
  - Historic Preservation
  - Government Services
url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/apis.yml
created: '2024-11-21'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: architect-of-the-capitol:aoc-data-api
    name: Architect of the Capitol Data API
    description: The AOC Data API provides access to public information about Capitol campus buildings, art collections, historic preservation projects, and congressional facilities management.
    humanURL: https://www.aoc.gov/
    tags:
      - Capitol Campus
      - Buildings
      - Art Collections
      - Historic Preservation
      - Facilities
    properties:
      - type: Documentation
        url: https://www.aoc.gov/
      - type: GettingStarted
        url: https://www.aoc.gov/about-us
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/openapi/aoc-data-api.yaml
common:
  - type: Portal
    url: https://www.aoc.gov/
  - type: Documentation
    url: https://www.aoc.gov/
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/rules/aoc-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/vocabulary/aoc-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/architect-of-the-capitol/refs/heads/main/json-ld/aoc-data-api-context.jsonld
  - type: Features
    data:
      - name: Capitol Campus Buildings
        description: Information about the US Capitol, House and Senate office buildings, Library of Congress, and Supreme Court.
      - name: Art Collections
        description: Access to the Capitol art collection catalog including paintings, sculptures, and historic artifacts.
      - name: Historic Preservation Projects
        description: Data on preservation and restoration projects across the Capitol campus.
      - name: Accessibility Information
        description: Accessibility features and visitor accommodations across Capitol campus facilities.
      - name: Congressional Facilities
        description: Management of congressional office space, hearing rooms, and support facilities.
  - type: UseCases
    data:
      - name: Visitor Information
        description: Provide Capitol campus visitor information including building access, tours, and facilities.
      - name: Art Research
        description: Research the Capitol art collection for educational and historical purposes.
      - name: Historic Preservation
        description: Track preservation project status and outcomes for historic Capitol structures.
      - name: Congressional Services
        description: Support congressional staff with facilities management and space planning information.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
