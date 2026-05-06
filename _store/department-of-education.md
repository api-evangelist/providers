---
aid: department-of-education
name: Department of Education
description: The U.S. Department of Education (ED) is a federal agency that manages and coordinates federal assistance to education and establishes policy for it. ED's mission is to promote student achievement and preparation for global competitiveness, and to ensure equal access to education. The Department exposes a portfolio of public APIs through api.data.gov, NCES, and the Open Data Platform (ODP) at data.ed.gov for postsecondary outcomes, institutional characteristics, and federal education programs.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - College Scorecard
  - Education
  - Federal Government
  - Higher Education
  - IPEDS
  - K-12
  - NCES
  - Open Data
  - Postsecondary
url: https://raw.githubusercontent.com/api-evangelist/department-of-education/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: government
position: Producer
access: Public
apis:
  - aid: department-of-education:college-scorecard-api
    name: College Scorecard API
    description: The College Scorecard API provides programmatic access to postsecondary institution and field-of-study data published by the U.S. Department of Education. The API exposes more than 6,000 schools and over 1,900 data points per institution drawn from IPEDS, the National Student Loan Data System (NSLDS), and U.S. Department of the Treasury sources, including cost, completion, earnings, debt, and demographic outcomes. Requests require an api.data.gov API key passed via the api_key query parameter.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://collegescorecard.ed.gov/data/
    baseURL: https://api.data.gov/ed/collegescorecard/v1
    tags:
      - College Scorecard
      - Earnings
      - Higher Education
      - Postsecondary
      - Schools
    properties:
      - type: Documentation
        url: https://collegescorecard.ed.gov/data/api-documentation/
      - type: API
        url: https://collegescorecard.ed.gov/data/api/
      - type: Data
        url: https://collegescorecard.ed.gov/data/
      - type: GitHub
        url: https://github.com/RTICWDT/college-scorecard
      - type: Sign Up
        url: https://api.data.gov/signup/
    contact:
      - FN: College Scorecard
        email: scorecarddata@rti.org
        url: https://collegescorecard.ed.gov/data/
  - aid: department-of-education:open-data-platform-api
    name: Department of Education Open Data Platform API
    description: The Department of Education Open Data Platform (ODP) at data.ed.gov is built on CKAN and exposes a CKAN-compatible REST API for searching, retrieving, and downloading the Department's public datasets. The API surface mirrors CKAN package, resource, group, and search actions over JSON.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://data.ed.gov/
    baseURL: https://data.ed.gov/api/3
    tags:
      - CKAN
      - Datasets
      - Open Data
    properties:
      - type: Documentation
        url: https://data.ed.gov/about
      - type: FAQ
        url: https://data.ed.gov/faq
      - type: User Guide
        url: https://data.ed.gov/pages/publichelp
      - type: CKAN Reference
        url: https://docs.ckan.org/en/2.8/api/
    contact:
      - FN: Department of Education ODP
        email: ODP@ed.gov
        url: https://data.ed.gov/
  - aid: department-of-education:ipeds-data
    name: IPEDS Data
    description: The Integrated Postsecondary Education Data System (IPEDS) gathers data annually from every college, university, and technical and vocational institution that participates in the federal student financial aid programs. NCES distributes IPEDS data via downloadable CSV files, Access databases, and a Find Your College tool rather than a public REST API; many of these datasets are also exposed via the College Scorecard and ODP APIs.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://nces.ed.gov/ipeds
    baseURL: https://api.example.com
    tags:
      - Bulk Data
      - Higher Education
      - IPEDS
      - NCES
      - Postsecondary
    properties:
      - type: Documentation
        url: https://nces.ed.gov/ipeds
      - type: Use the Data
        url: https://nces.ed.gov/ipeds/use-the-data
      - type: Find Your College
        url: https://nces.ed.gov/ipeds/find-your-college
      - type: Downloads
        url: https://nces.ed.gov/ipeds/use-the-data/download-access-database
    contact:
      - FN: NCES IPEDS
        url: https://nces.ed.gov/ipeds
  - aid: department-of-education:edfacts-data
    name: EDFacts Data
    description: EDFacts is a centralized data collection through which state education agencies submit pre-kindergarten through grade 12 (PK-12) education data to the U.S. Department of Education. EDFacts data are published as downloadable files and are also accessible through partner APIs such as the Urban Institute Education Data Explorer.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www2.ed.gov/about/inits/ed/edfacts/index.html
    baseURL: https://api.example.com
    tags:
      - Bulk Data
      - EDFacts
      - K-12
      - State Data
    properties:
      - type: Documentation
        url: https://www2.ed.gov/about/inits/ed/edfacts/index.html
      - type: Data Files
        url: https://www2.ed.gov/about/inits/ed/edfacts/data-files/index.html
      - type: Education Data Explorer
        url: https://educationdata.urban.org/documentation/
    contact:
      - FN: EDFacts
        email: EDFacts@ed.gov
        url: https://www2.ed.gov/about/inits/ed/edfacts/index.html
common:
  - type: Website
    url: https://www.ed.gov
  - type: Open Data Platform
    url: https://data.ed.gov/
  - type: Developer Portal
    url: https://api.data.gov/
  - type: NCES
    url: https://nces.ed.gov/
  - type: College Scorecard
    url: https://collegescorecard.ed.gov/
  - type: Federal Student Aid
    url: https://studentaid.gov
  - type: Data.gov ED Catalog
    url: https://catalog.data.gov/dataset?organization=ed-gov
  - type: News
    url: https://www.ed.gov/news
  - type: Contact
    url: https://www.ed.gov/about/contact-us
  - type: Privacy Policy
    url: https://www.ed.gov/notices/privacy
  - type: GitHub Organization
    url: https://github.com/usedgov
  - type: JSON-LD
    url: json-ld/department-of-education-context.jsonld
  - type: Vocabulary
    url: vocabulary/department-of-education-vocabulary.yml
  - type: Capabilities
    url: capabilities/department-of-education-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
