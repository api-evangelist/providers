---
aid: predictive-oncology-model-and-data-clearinghouse
name: Predictive Oncology Model and Data Clearinghouse
description: The Predictive Oncology Model and Data Clearinghouse (MoDaC) is a National Cancer Institute platform that supports cancer research through advanced algorithms and machine learning techniques to analyze complex datasets, including genetic information, clinical data, and imaging studies. MoDaC serves as a centralized hub for storing, sharing, and discovering cancer research datasets and trained models, fostering collaboration among researchers and accelerating the advancement of cancer therapies.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cancer Research
  - Clinical Data
  - Datasets
  - Machine Learning
  - Oncology
created: '2024-11-07'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/predictive-oncology-model-and-data-clearinghouse/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: predictive-oncology-model-and-data-clearinghouse:modac-api
    name: MoDaC REST API
    description: The MoDaC REST API provides programmatic access to upload and download assets, manage associated metadata, and search for assets against these metadata. Assets include datasets and machine learning models contributed by the cancer research community. The API is documented in OpenAPI 3.0 format and exposes endpoints for bulk registration, data object and collection management, metadata queries, and permissions handling.
    humanURL: https://modac.cancer.gov/
    tags:
      - Cancer Research
      - Datasets
      - Machine Learning
      - REST API
    properties:
      - type: Documentation
        url: https://modac.cancer.gov/
      - type: Swagger UI
        url: https://modac.cancer.gov/swagger-ui/4.14.0/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/predictive-oncology-model-and-data-clearinghouse/refs/heads/main/openapi/predictive-oncology-model-and-data-clearinghouse-openapi.json
common:
  - type: Portal
    url: https://modac.cancer.gov/
  - type: About
    url: https://modac.cancer.gov/aboutPage
  - type: Help
    url: https://modac.cancer.gov/helpPage
  - type: Contact
    url: https://modac.cancer.gov/contactUsPage
  - type: Login
    url: https://modac.cancer.gov/login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
