---
aid: sumif
url: https://raw.githubusercontent.com/api-evangelist/sumif/refs/heads/main/apis.yml
apis:
- name: SUMIF API
  description: Performs conditional summation based on specified criteria.
  image: https://example.com/sumif-api.png
  humanURL: https://docs.example.com/sumif
  baseURL: https://api.example.com/v1
  version: '1.0'
  tags:
  - Conditional
  - Filtering
  - Sum
  properties:
  - type: Documentation
    url: https://docs.example.com/sumif/reference
  - type: OpenAPI
    url: https://api.example.com/openapi/sumif.json
  - type: Swagger
    url: https://api.example.com/swagger/sumif
  - type: Postman Collection
    url: https://www.postman.com/collections/sumif-api
  - type: Authentication
    url: https://docs.example.com/sumif/authentication
  - type: Pricing
    url: https://example.com/pricing
  - type: Rate Limits
    url: https://docs.example.com/sumif/rate-limits
  - type: Status
    url: https://status.example.com
  - type: Support
    url: https://support.example.com
  - type: Terms of Service
    url: https://example.com/terms
  - type: Privacy Policy
    url: https://example.com/privacy
  contact:
  - type: Email
    url: mailto:api@example.com
  - type: Twitter
    url: https://twitter.com/exampleapi
  - type: Support
    url: https://support.example.com/contact
  endpoints:
  - name: Basic SUMIF
    description: Sum values based on a single condition
    method: POST
    path: /sumif
    parameters:
    - name: range
      type: array
      required: true
      description: Array of values to evaluate
    - name: criteria
      type: string
      required: true
      description: Condition to match (e.g., ">100", "=Active")
    - name: sum_range
      type: array
      required: false
      description: Array of values to sum (uses range if not specified)
  - name: SUMIFS (Multiple Criteria)
    description: Sum values based on multiple conditions
    method: POST
    path: /sumifs
    parameters:
    - name: sum_range
      type: array
      required: true
      description: Array of values to sum
    - name: criteria_ranges
      type: array
      required: true
      description: Array of ranges to evaluate
    - name: criteria
      type: array
      required: true
      description: Array of conditions to match
  - name: Batch SUMIF
    description: Process multiple SUMIF operations in a single request
    method: POST
    path: /sumif/batch
    parameters:
    - name: operations
      type: array
      required: true
      description: Array of SUMIF operation objects
name: SUMIF
tags:
- Aggregation
- Calculation
- Conditional
- Data Analysis
- Spreadsheet
type: Contract
image: https://example.com/sumif-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: API for conditional sum operations across datasets.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

