---
aid: data-analysis-tools-bureau-of-justice-statistics
name: Bureau of Justice Statistics Data Analysis Tools
url: https://raw.githubusercontent.com/api-evangelist/data-analysis-tools-bureau-of-justice-statistics/refs/heads/main/apis.yml
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Crime Statistics
  - Federal Government
  - NCVS
  - NIBRS
  - Open Data
  - SODA
  - Statistics
  - Victimization
created: '2024-11-30'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
description: The Bureau of Justice Statistics (BJS) is the agency within the U.S. Department of Justice responsible for collecting, analysing, and disseminating crime, criminal-justice, expenditure, and victimisation data. BJS exposes selected datasets through Socrata Open Data APIs and offers interactive data analysis tools such as the Justice Expenditure and Employment Tool (JEET) and the National Crime Victimization Survey (NCVS) Quick Tables.
apis:
  - aid: data-analysis-tools-bureau-of-justice-statistics:ncvs-api
    name: BJS NCVS API
    description: The National Crime Victimization Survey (NCVS) API exposes selected NCVS datasets via the Socrata Open Data API. Datasets are addressed by four-character resource codes and may be queried with SoQL clauses such as $select, $where, $group, $order, and $limit, returning JSON or CSV.
    humanURL: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
    baseURL: https://api.ojp.gov/bjsdataset/v1
    tags:
      - Crime Statistics
      - NCVS
      - SODA
      - Victimization
    properties:
      - type: Documentation
        url: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
      - type: Featured
        url: https://bjs.ojp.gov/featured/national-crime-victimization-survey-ncvs-application-programming-interface-api
      - type: OpenAPI
        url: openapi/bjs-ncvs-api-openapi.yml
      - type: JSONSchema
        url: json-schema/bjs-dataset-row.json
      - type: Rules
        url: rules/bjs-ncvs-api-rules.yml
      - type: Capabilities
        url: capabilities/bjs-data-analysis-tools-capabilities.yml
  - aid: data-analysis-tools-bureau-of-justice-statistics:nibrs-api
    name: BJS NIBRS National Estimates API
    description: The NIBRS National Estimates API publishes selected National Incident-Based Reporting System national-estimates datasets via the Socrata Open Data API, addressable via four-character resource codes and queryable with SoQL.
    humanURL: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
    baseURL: https://api.ojp.gov/bjsdataset/v1
    tags:
      - Crime Statistics
      - NIBRS
      - SODA
    properties:
      - type: Documentation
        url: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
      - type: OpenAPI
        url: openapi/bjs-nibrs-api-openapi.yml
      - type: JSONSchema
        url: json-schema/bjs-dataset-row.json
common:
  - type: Website
    url: https://bjs.ojp.gov/
  - type: Data Analysis Tools
    url: https://bjs.ojp.gov/data/data-analysis-tools
  - type: Data Collections
    url: https://bjs.ojp.gov/data-collections
  - type: Publications
    url: https://bjs.ojp.gov/library
  - type: DOJ Developer
    url: https://www.justice.gov/developer
  - type: JSON-LD
    url: json-ld/bjs-context.jsonld
  - type: Vocabulary
    url: vocabulary/bjs-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
