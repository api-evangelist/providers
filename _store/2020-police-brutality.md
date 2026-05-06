---
aid: 2020-police-brutality
url: https://raw.githubusercontent.com/api-evangelist/2020-police-brutality/refs/heads/main/apis.yml
name: 2020 Police Brutality
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Brutality
  - Civil Rights
  - Policing
  - Public Data
description: This repository accumulates and contextualizes evidence of police brutality during the 2020 George Floyd protests. The goal is to assist journalists, politicians, prosecutors, activists and concerned individuals who can use the evidence accumulated here for political campaigns, news reporting, public education and prosecution of criminal police officers.
created: '2024-11-13'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: 2020-police-brutality:2020-police-brutality
    name: 2020 Police Brutality API
    tags:
      - Brutality
      - Civil Rights
      - Incidents
      - Policing
    humanURL: https://github.com/2020PB/police-brutality/tree/data_build
    baseURL: https://raw.githubusercontent.com/2020PB/police-brutality/data_build
    properties:
      - url: https://github.com/2020PB/police-brutality/tree/data_build
        type: Documentation
      - url: openapi/2020-police-brutality-openapi.yml
        type: OpenAPI
      - url: json-schema/2020-police-brutality-incident-schema.json
        type: JSONSchema
      - url: json-schema/2020-police-brutality-incident-collection-schema.json
        type: JSONSchema
      - url: json-ld/2020-police-brutality-context.jsonld
        type: JSON-LD
    description: This repository accumulates and contextualizes evidence of police brutality during the 2020 George Floyd protests. Data is available as JSON and CSV files from the data_build branch, including geolocation, tags, dates, and source links for each incident.
common:
  - type: GitHubOrganization
    url: https://github.com/2020PB
  - type: GitHubRepository
    url: https://github.com/2020PB/police-brutality
  - type: Documentation
    url: https://github.com/2020PB/police-brutality/blob/main/README.md
  - type: SpectralRules
    url: rules/2020-police-brutality-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/2020-police-brutality-incident-research.yaml
  - type: Vocabulary
    url: vocabulary/2020-police-brutality-vocabulary.yaml
  - type: Features
    data:
      - name: Incident Documentation
        description: Documented evidence of police brutality with descriptions, dates, locations, and source links
      - name: Location Data
        description: GPS geolocation coordinates for each incident, enabling geographic analysis
      - name: Tag Classification
        description: Categorical tags classifying incident types (foam-bullet, tear-gas, pepper-spray, etc.)
      - name: Multiple Data Formats
        description: Data available in JSON (v1 and v2) and CSV formats for different use cases
      - name: Source Verification
        description: Each incident includes links to source documentation for verification
      - name: Open Data
        description: MIT licensed open dataset available for public use
  - type: UseCases
    data:
      - name: Journalism and Reporting
        description: Investigative journalists use incident data for news reporting on police conduct
      - name: Legal Proceedings
        description: Prosecutors and civil rights attorneys use evidence for criminal and civil cases
      - name: Academic Research
        description: Researchers study patterns in police use of force during protests
      - name: Policy Advocacy
        description: Activists and policymakers use data to support police reform campaigns
      - name: Public Education
        description: Organizations use the data to educate the public about police brutality
      - name: Geographic Analysis
        description: Researchers map incidents by location to identify geographic patterns
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
