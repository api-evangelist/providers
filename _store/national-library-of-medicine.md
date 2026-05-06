---
aid: national-library-of-medicine
name: National Library of Medicine
description: The National Library of Medicine, part of the National Institutes of Health, is the world's largest biomedical library. It collects, organizes, and provides access to medical literature and information to support research and decision-making in healthcare, including PubMed and ClinicalTrials.gov.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-library-of-medicine/refs/heads/main/apis.yml
created: '2024-12-03'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Federal Government
  - Health
  - Library
  - Medicine
apis:
  - aid: national-library-of-medicine:national-library-of-medicine
    name: National Library of Medicine E-utilities
    tags:
      - Health
      - Medicine
      - Bibliographic
      - Research
    humanURL: https://www.ncbi.nlm.nih.gov/home/develop/api
    baseURL: https://eutils.ncbi.nlm.nih.gov/entrez/eutils
    properties:
      - url: https://www.ncbi.nlm.nih.gov/home/develop/api
        type: Documentation
      - url: https://www.ncbi.nlm.nih.gov/books/NBK25500/
        type: GettingStarted
      - url: https://www.ncbi.nlm.nih.gov/books/NBK25497/
        type: Reference
      - url: https://raw.githubusercontent.com/api-evangelist/national-library-of-medicine/refs/heads/main/openapi/national-library-of-medicine-openapi.yml
        type: OpenAPI
    description: The E-utilities are the public API to the NCBI Entrez system providing access to all Entrez databases including PubMed, PMC, Gene, Nuccore, and Protein through a suite of server-side programs for search, link, and retrieval operations.
common:
  - type: Website
    url: https://www.nlm.nih.gov/
  - type: Portal
    url: https://www.ncbi.nlm.nih.gov/home/develop/api/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
