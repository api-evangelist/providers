---
aid: bureau-of-international-labor-affairs
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-international-labor-affairs/refs/heads/main/apis.yml
name: Bureau of International Labor Affairs
tags:
  - Federal Government
  - International
  - Labor
  - Standards
  - Child Labor
  - Forced Labor
  - Human Trafficking
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-25'
modified: '2026-04-23'
position: Consumer
description: ILAB strengthens global labor standards; enforces labor commitments; promotes equity; and combats child labor, forced labor, and human trafficking.
apis:
  - aid: bureau-of-international-labor-affairs:dol-ilab-data-api
    name: DOL ILAB Data API
    tags:
      - Federal Government
      - Labor
      - International
      - Child Labor
      - Forced Labor
    humanURL: https://www.dol.gov/agencies/ilab/our-work/data-research
    baseURL: https://api.dol.gov/V1/ILAB
    properties:
      - url: https://www.dol.gov/agencies/ilab/our-work/data-research
        type: Documentation
      - url: https://developer.dol.gov/
        type: Portal
      - url: https://catalog.data.gov/dataset?organization=dol-gov&q=ilab
        type: DataAPI
    description: ILAB provides data on child labor, forced labor, and human trafficking across countries. The DOL developer API provides programmatic access to ILAB datasets including country-level labor standards assessments, lists of goods produced by child labor or forced labor, and trade agreement labor compliance data.
    features:
      - Child Labor Data
      - Forced Labor Data
      - Country Profiles
      - Trade Agreement Compliance
    useCases:
      - Research global labor standards violations
      - Track goods produced with child or forced labor
      - Monitor trade agreement labor commitments
      - Support CSR due diligence workflows
  - aid: bureau-of-international-labor-affairs:ilab-sweat-and-toil-data
    name: ILAB Sweat and Toil Data
    tags:
      - Federal Government
      - Child Labor
      - Forced Labor
    humanURL: https://www.dol.gov/agencies/ilab/our-work/data-research/sweat-toil
    properties:
      - url: https://www.dol.gov/agencies/ilab/our-work/data-research/sweat-toil
        type: Documentation
      - url: https://developer.dol.gov/
        type: Portal
    description: The Sweat and Toil dataset covers child labor and forced labor in over 130 countries, including goods identified as produced by child or forced labor, country advancement levels, and suggested actions.
    features:
      - Goods Produced by Child Labor
      - Goods Produced by Forced Labor
      - Country Advancement Level
      - Suggested Government Actions
    useCases:
      - Supply chain due diligence
      - ESG reporting
      - Academic research on child labor
      - Policy analysis
common:
  - type: Website
    url: https://www.dol.gov/agencies/ilab
  - type: Portal
    url: https://developer.dol.gov/
  - type: Privacy Policy
    url: https://www.dol.gov/general/privacynotice
  - type: Data Research
    url: https://www.dol.gov/agencies/ilab/our-work/data-research
  - type: Data Portal
    url: https://catalog.data.gov/dataset?organization=dol-gov&q=ilab
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
