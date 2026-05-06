---
aid: department-of-justice
name: Department of Justice
description: The U.S. Department of Justice (DOJ) is the federal executive department responsible for enforcing the law and defending the interests of the United States. DOJ exposes a portfolio of public APIs and data feeds including the DOJ News API for press releases, speeches, and blog entries from the Office of Public Affairs, the FOIA.gov developer APIs, the Bureau of Justice Statistics NCVS and NIBRS APIs, and the DOJ Open Data Catalog.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Bureau of Justice Statistics
  - Crime
  - Federal Government
  - FOIA
  - Justice
  - News
  - Open Data
  - Press Releases
  - Statistics
url: https://raw.githubusercontent.com/api-evangelist/department-of-justice/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-justice:doj-news-api
    name: DOJ News API
    description: The DOJ News API exposes more than 14,000 press releases, speeches, and blog entries from the Office of Public Affairs as a JSON web service. Endpoints under /api/v1/ provide list and detail views for each content type and support filtering by title, date, component, and topic, along with pagination and field selection.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.justice.gov/developer/api-documentation/api_v1
    baseURL: https://www.justice.gov/api/v1
    tags:
      - Blog
      - News
      - Office of Public Affairs
      - Press Releases
      - Speeches
    properties:
      - type: Documentation
        url: https://www.justice.gov/developer/api-documentation/api_v1
      - type: Developer
        url: https://www.justice.gov/developer
      - type: Open Government
        url: https://www.justice.gov/open/developer-resources
      - type: GitHub Client
        url: https://github.com/rOpenGov/usdoj
    contact:
      - FN: DOJ Office of Public Affairs
        url: https://www.justice.gov/contact-us
  - aid: department-of-justice:foia-annual-report-api
    name: FOIA.gov Annual Report API
    description: The FOIA.gov developer resources expose annual FOIA report data as XML conforming to the FOIA Annual Report XML schema. Reports can be retrieved by agency abbreviation and year through a documented endpoint pattern.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.foia.gov/developer/
    baseURL: https://www.foia.gov/api
    tags:
      - Annual Report
      - FOIA
      - XML
    properties:
      - type: Documentation
        url: https://www.foia.gov/developer/
      - type: Reference
        url: https://www.foia.gov/developer/agency-api/
    contact:
      - FN: Office of Information Policy
        url: https://www.justice.gov/oip
  - aid: department-of-justice:bjs-ncvs-api
    name: BJS National Crime Victimization Survey (NCVS) API
    description: The Bureau of Justice Statistics NCVS API provides REST access to the National Crime Victimization Survey datasets. Endpoints expose Personal Victimization, Personal Population, Household Victimization, and Household Population data in JSON and CSV. The API uses a path, resource, and query parameter structure with a default page size of 1,000 records.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
    baseURL: https://bjs.ojp.gov/api
    tags:
      - BJS
      - Crime
      - NCVS
      - Statistics
      - Victimization
    properties:
      - type: Documentation
        url: https://bjs.ojp.gov/national-crime-victimization-survey-ncvs-api
      - type: NCVS Program
        url: https://bjs.ojp.gov/data-collection/ncvs
      - type: Featured
        url: https://bjs.ojp.gov/featured/national-crime-victimization-survey-ncvs-application-programming-interface-api
      - type: Data Tools
        url: https://bjs.ojp.gov/data/data-analysis-tools
    contact:
      - FN: Bureau of Justice Statistics
        url: https://bjs.ojp.gov/about-bjs-website
  - aid: department-of-justice:bjs-nibrs-api
    name: BJS NIBRS National Estimates API
    description: The Bureau of Justice Statistics NIBRS National Estimates API provides REST access to the National Incident-Based Reporting System estimates including victimization counts and rates. Endpoints return JSON or CSV and follow a path, resource, query parameter structure with a default page size of 1,000 records.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
    baseURL: https://bjs.ojp.gov/api
    tags:
      - BJS
      - Crime
      - National Estimates
      - NIBRS
      - Statistics
    properties:
      - type: Documentation
        url: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs-national-estimates-api
      - type: NIBRS Program
        url: https://bjs.ojp.gov/national-incident-based-reporting-system-nibrs
      - type: Codebook
        url: https://bjs.ojp.gov/document/nibrs-codebook-supplementary-documentation.pdf
    contact:
      - FN: Bureau of Justice Statistics
        url: https://bjs.ojp.gov/about-bjs-website
  - aid: department-of-justice:doj-open-data-catalog
    name: DOJ Open Data Catalog
    description: DOJ publishes datasets through the Open Government program and the Department's Data Inventory. Datasets are also surfaced on Data.gov under the doj-gov organization and are accessible via the CKAN-compatible Data.gov API.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.justice.gov/data
    baseURL: https://catalog.data.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://www.justice.gov/data
      - type: Open Government
        url: https://www.justice.gov/open
      - type: Data.gov DOJ
        url: https://catalog.data.gov/organization/doj-gov
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: DOJ Open Data
        url: https://www.justice.gov/open
common:
  - type: Website
    url: https://www.justice.gov
  - type: Open Government
    url: https://www.justice.gov/open
  - type: Developer
    url: https://www.justice.gov/developer
  - type: News
    url: https://www.justice.gov/news
  - type: FOIA
    url: https://www.foia.gov
  - type: Office of Information Policy
    url: https://www.justice.gov/oip
  - type: Bureau of Justice Statistics
    url: https://bjs.ojp.gov
  - type: Office of Justice Programs
    url: https://www.ojp.gov
  - type: FBI
    url: https://www.fbi.gov
  - type: DEA
    url: https://www.dea.gov
  - type: ATF
    url: https://www.atf.gov
  - type: U.S. Marshals
    url: https://www.usmarshals.gov
  - type: Bureau of Prisons
    url: https://www.bop.gov
  - type: Data.gov DOJ Catalog
    url: https://catalog.data.gov/organization/doj-gov
  - type: Privacy Policy
    url: https://www.justice.gov/legalpolicies
  - type: Contact
    url: https://www.justice.gov/contact-us
  - type: GitHub Organization
    url: https://github.com/usdoj
  - type: JSON-LD
    url: json-ld/department-of-justice-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-justice-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-justice-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
