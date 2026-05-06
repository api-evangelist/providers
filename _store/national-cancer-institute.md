---
aid: national-cancer-institute
name: National Cancer Institute
description: The National Cancer Institute (NCI) is the federal government's principal agency for cancer research and training, part of the National Institutes of Health. NCI provides data and APIs for cancer genomics, clinical trials, and drug information.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://www.cancer.gov/
created: '2024-12-25'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Cancer
  - Federal Government
  - Health
  - Research
apis:
  - aid: national-cancer-institute:gdc-api
    name: NCI Genomic Data Commons API
    tags:
      - Cancer
      - Data
      - Genomics
    humanURL: https://gdc.cancer.gov/developers/gdc-application-programming-interface-api
    baseURL: https://api.gdc.cancer.gov/
    properties:
      - url: https://gdc.cancer.gov/developers/gdc-application-programming-interface-api
        type: Documentation
      - url: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/national-cancer-institute/main/openapi/national-cancer-institute-openapi.yml
        type: OpenAPI
    description: The GDC API provides access to genomic and clinical data from the NCI Genomic Data Commons, supporting cancer research and precision medicine. Endpoints include status, projects, cases, files, annotations, data download, manifest generation, BAM slicing, and submission.
common:
  - type: Website
    url: https://www.cancer.gov/
  - type: Portal
    url: https://gdc.cancer.gov/developers/gdc-application-programming-interface-api
  - type: Documentation
    url: https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
