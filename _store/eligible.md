---
aid: eligible
name: Eligible
description: Eligible provides insurance billing APIs for healthcare businesses, enabling the integration of insurance billing experiences into healthcare applications. The platform supports eligibility verification, coverage discovery, claims submission and tracking, payment estimation, enrollment, and remittance processing across a large network of US payers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Billing
  - Eligibility
  - Healthcare
  - Insurance
  - Claims
url: https://raw.githubusercontent.com/api-evangelist/eligible/refs/heads/main/apis.yml
created: '2024-07-02'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: eligible:coverage
    name: Eligible Coverage API
    description: The Coverage API performs real-time insurance eligibility and benefits verification for a patient against a payer. Clients submit provider NPI, payer ID, and member identity information and receive structured benefit details including plan status, copays, coinsurance, deductibles, and out-of-pocket maximums.
    humanURL: https://eligible.com/
    tags:
      - Coverage
      - Eligibility
      - Healthcare
      - Insurance
    properties:
      - type: Documentation
        url: https://eligible.com/
  - aid: eligible:claims
    name: Eligible Claims API
    description: The Claims API supports submission, tracking, and status checking of professional and institutional healthcare claims to payers across the Eligible network. The API also provides claim acknowledgement, rejection, and remittance retrieval workflows for healthcare billing applications.
    humanURL: https://eligible.com/
    tags:
      - Claims
      - Billing
      - Healthcare
      - Insurance
    properties:
      - type: Documentation
        url: https://eligible.com/
  - aid: eligible:payment-estimation
    name: Eligible Payment Estimation API
    description: The Payment Estimation API calculates expected patient out-of-pocket amounts for a service before it is rendered, combining benefit details from a coverage check with provider contracted rates and accumulators. The API helps providers offer transparent cost estimates and collect patient responsibility at the point of service.
    humanURL: https://eligible.com/
    tags:
      - Payment Estimation
      - Cost Transparency
      - Healthcare
      - Billing
    properties:
      - type: Documentation
        url: https://eligible.com/
  - aid: eligible:enrollment
    name: Eligible Enrollment API
    description: The Enrollment API manages the trading partner enrollment workflow that providers must complete with payers in order to exchange eligibility, claims, and remittance transactions through Eligible. The API supports submission, tracking, and status retrieval of enrollment requests.
    humanURL: https://eligible.com/
    tags:
      - Enrollment
      - Trading Partner
      - Healthcare
      - Insurance
    properties:
      - type: Documentation
        url: https://eligible.com/
  - aid: eligible:payers
    name: Eligible Payers API
    description: The Payers API exposes the directory of insurance payers supported by Eligible, including payer identifiers, names, supported transaction types, enrollment requirements, and webhook capabilities. Clients use this API to select payers and check the status of supported transactions.
    humanURL: https://eligible.com/
    tags:
      - Payers
      - Directory
      - Healthcare
      - Insurance
    properties:
      - type: Documentation
        url: https://eligible.com/
common:
  - type: Website
    url: https://eligible.com/
  - type: Documentation
    url: https://eligible.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
