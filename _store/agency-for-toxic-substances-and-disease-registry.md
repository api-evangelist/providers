---
aid: agency-for-toxic-substances-and-disease-registry
url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/apis.yml
name: Agency for Toxic Substances and Disease Registry
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Diseases
  - Federal Government
  - Public Health
  - Toxic Substances
  - Environmental Health
  - Hazardous Materials
description: ATSDR protects communities from harmful health effects related to exposure to natural and man-made hazardous substances. It is a federal public health agency within the U.S. Department of Health and Human Services. ATSDR provides toxicological profiles, minimum risk levels, substance priority rankings, and exposure investigation data for hazardous chemicals.
created: '2024-11-21'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: agency-for-toxic-substances-and-disease-registry:atsdr-toxic-substance-profiles-api
    name: ATSDR Toxic Substance Profiles API
    tags:
      - Toxicology
      - Hazardous Substances
      - Public Health
      - Environmental Health
    humanURL: https://www.atsdr.cdc.gov/substances/index.asp
    baseURL: https://data.cdc.gov/resource
    properties:
      - url: https://www.atsdr.cdc.gov/substances/index.asp
        type: Documentation
      - url: https://www.atsdr.cdc.gov/mrls/index.asp
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/openapi/atsdr-toxic-substance-profiles-openapi.yml
        type: OpenAPI
    description: Access ATSDR toxicological profiles, minimum risk levels (MRLs), substance priority list rankings, and exposure investigation data for hazardous chemicals found at Superfund sites and in the environment.
common:
  - type: Website
    url: https://www.atsdr.cdc.gov/
  - type: Portal
    url: https://www.atsdr.cdc.gov/api
  - type: DataPortal
    url: https://data.cdc.gov/browse?category=Environmental+Health
  - type: GettingStarted
    url: https://www.atsdr.cdc.gov/substances/index.asp
  - type: Documentation
    url: https://www.atsdr.cdc.gov/mrls/index.asp
  - type: Documentation
    url: https://www.atsdr.cdc.gov/spl/index.html
  - type: FOIA
    url: https://www.hhs.gov/foia/index.html
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/rules/atsdr-spectral-rules.yml
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/capabilities/toxic-substance-monitoring.yaml
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-schema/atsdr-tox-profile-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-schema/atsdr-mrl-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/json-ld/atsdr-toxicology-context.jsonld
    type: JSONLDContext
  - url: https://raw.githubusercontent.com/api-evangelist/agency-for-toxic-substances-and-disease-registry/refs/heads/main/vocabulary/atsdr-vocabulary.yaml
    type: Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
