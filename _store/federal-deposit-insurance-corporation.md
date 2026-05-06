---
aid: federal-deposit-insurance-corporation
name: Federal Deposit Insurance Corporation
description: The Federal Deposit Insurance Corporation (FDIC) is an independent agency of the United States government that provides deposit insurance to depositors in US commercial banks and savings institutions. The FDIC also supervises and examines banks for safety and soundness, promotes consumer protection, and publishes the BankFind Suite API for accessing data on FDIC-insured institutions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-04-28'
position: Consumer
tags:
  - Banking
  - Federal Government
  - Financial Data
  - Insurance
url: https://raw.githubusercontent.com/api-evangelist/federal-deposit-insurance-corporation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-deposit-insurance-corporation:bankfind
    name: FDIC BankFind Suite API
    description: The FDIC BankFind Suite API provides programmatic access to data about FDIC-insured banks and savings institutions, including institution profiles, branch locations, financial summaries, historical records, failures, deposits, and demographic data.
    humanURL: https://banks.data.fdic.gov/docs/
    baseURL: https://banks.data.fdic.gov/api
    tags:
      - Banking
      - Financial Data
      - Insurance
    properties:
      - type: Documentation
        url: https://banks.data.fdic.gov/docs/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/federal-deposit-insurance-corporation/refs/heads/main/openapi/bankfind.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/federal-deposit-insurance-corporation/refs/heads/main/rules/bankfind-rules.yml
common:
  - type: Website
    url: https://www.fdic.gov/
  - type: Documentation
    url: https://banks.data.fdic.gov/docs/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
