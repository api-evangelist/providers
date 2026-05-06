---
aid: us-african-development-foundation
url: https://raw.githubusercontent.com/api-evangelist/us-african-development-foundation/refs/heads/main/apis.yml
name: US African Development Foundation
tags:
  - Federal Government
  - International Development
  - Africa
  - Grants
  - Nonprofit
  - Economic Development
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-20'
modified: '2026-05-03'
position: Consumer
description: The US African Development Foundation (USADF) is an independent federal agency established by Congress in 1980 to invest directly in African grassroots enterprises and social entrepreneurs. USADF provides grant capital of up to $250,000, capacity-building assistance, and convening opportunities to develop, grow, and scale African enterprises and entrepreneurs. USADF grant data is publicly accessible via the USASpending.gov API, and grant opportunities are posted to Grants.gov. Between 2019 and 2023, USADF awarded more than $141 million in grants to over 1,050 community enterprises in Africa, directly affecting 6.2 million people.
specificationVersion: '0.19'
apis:
  - aid: us-african-development-foundation:grants-api
    name: USADF Grants Data API
    description: Access to USADF grant award data through the USASpending.gov API. Provides programmatic access to USADF grants, awards, recipients, and spending profiles as reported to the federal awards transparency system. USADF data is available via the USASpending API using the USADF agency identifier (CGAC 166).
    humanURL: https://www.usaspending.gov/agency/african-development-foundation
    baseURL: https://api.usaspending.gov
    tags:
      - Grants
      - Awards
      - Spending
      - Transparency
      - Federal Awards
    properties:
      - type: Documentation
        url: https://api.usaspending.gov/docs/endpoints
      - type: OpenAPI
        url: openapi/usadf-grants-api-openapi.yml
      - type: JSONSchema
        url: json-schema/grants-api-award-schema.json
      - type: JSONSchema
        url: json-schema/grants-api-recipient-schema.json
  - aid: us-african-development-foundation:grant-opportunities-api
    name: USADF Grant Opportunities API
    description: Access to USADF grant opportunity listings through the Grants.gov API. USADF posts open grant solicitations on Grants.gov for African grassroots enterprises, cooperatives, and social entrepreneurs seeking funding. Grant amounts up to $250,000 for African-led development initiatives.
    humanURL: https://www.grants.gov/search-grants?agencyCode=ADF
    baseURL: https://apply07.grants.gov
    tags:
      - Grant Opportunities
      - Funding
      - Applications
      - Africa
    properties:
      - type: Documentation
        url: https://www.grants.gov/developers.html
      - type: OpenAPI
        url: openapi/usadf-grant-opportunities-api-openapi.yml
      - type: JSONSchema
        url: json-schema/grant-opportunities-api-opportunity-schema.json
common:
  - type: Website
    url: https://www.usadf.gov
  - type: Portal
    url: https://www.usaspending.gov/agency/african-development-foundation
    title: USASpending Spending Profile
  - type: DataAPI
    url: https://api.usaspending.gov
    title: USASpending API
  - type: DataAPI
    url: https://www.grants.gov/search-grants?agencyCode=ADF
    title: Grants.gov USADF Listings
  - type: GitHubOrganization
    url: https://github.com/usadf
  - type: JSONLD
    url: json-ld/us-african-development-foundation-context.jsonld
  - type: SpectralRules
    url: rules/us-african-development-foundation-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/us-african-development-foundation-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/african-development-grants.yaml
    title: African Development Grants
  - type: NaftikoCapability
    url: capabilities/shared/grants-api.yaml
    title: Grants API (Shared)
  - type: Features
    data:
      - name: Grant Award Transparency
        description: USADF grant award data publicly accessible via USASpending.gov API, including recipient, country, amount, and award period for all USADF grants.
      - name: Grant Opportunity Listings
        description: USADF posts open grant solicitations on Grants.gov for African grassroots enterprises seeking funding up to $250,000.
      - name: Agency Spending Profile
        description: Comprehensive USADF spending data accessible through USASpending.gov including account data, award breakdowns, and budget authority.
      - name: Recipient Data
        description: Data on organizations receiving USADF grants across 24 African countries, including grant amounts, periods of performance, and program areas.
  - type: UseCases
    data:
      - name: Grant Transparency Research
        description: Researchers and journalists accessing USADF grant award data through USASpending API to analyze funding patterns across African countries.
      - name: Grant Opportunity Discovery
        description: African enterprises and NGOs finding and applying for USADF grant opportunities through Grants.gov listings.
      - name: Federal Spending Analysis
        description: Policy analysts tracking USADF budget authority, obligations, and outlays through USASpending federal account data.
      - name: Development Impact Tracking
        description: Development finance institutions and donors assessing USADF program reach and impact through award data and recipient profiles.
  - type: Integrations
    data:
      - name: USASpending.gov
        description: Federal awards transparency platform providing API access to all USADF grant awards, recipient data, and spending profiles.
      - name: Grants.gov
        description: Federal grant opportunity portal where USADF posts open solicitations for African grassroots enterprise grants.
      - name: SAM.gov
        description: System for Award Management where USADF grant recipients register to receive federal award funding.
      - name: FPDS-NG
        description: Federal Procurement Data System tracking USADF contract and interagency agreement spending.
      - name: USAID OIG
        description: USAID Office of Inspector General providing independent oversight of USADF grants administration and partnerships.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
