---
aid: customs-advisory-services
url: https://raw.githubusercontent.com/api-evangelist/customs-advisory-services/refs/heads/main/apis.yml
apis:
- name: Tariff Classification API
  description: Provides HS code classification and tariff rate lookups for products.
  image: https://example.com/images/tariff-api.png
  humanURL: https://customsadvisory.com/tariff-classification
  baseURL: https://api.customsadvisory.com/v1/tariff
  tags:
  - Classification
  - HS Codes
  - Tariff Rates
  properties:
  - type: Documentation
    url: https://docs.customsadvisory.com/tariff-classification
  - type: OpenAPI
    url: https://api.customsadvisory.com/openapi/tariff.yaml
  - type: Authentication
    url: https://docs.customsadvisory.com/authentication
  contact:
  - FN: Tariff API Support
    email: tariff-api@customsadvisory.com
    X-twitter: customsadvisory
- name: Trade Compliance API
  description: Manages compliance requirements, restricted party screening, and export controls.
  image: https://example.com/images/compliance-api.png
  humanURL: https://customsadvisory.com/trade-compliance
  baseURL: https://api.customsadvisory.com/v1/compliance
  tags:
  - Compliance
  - Export Controls
  - Sanctions
  - Screening
  properties:
  - type: Documentation
    url: https://docs.customsadvisory.com/trade-compliance
  - type: OpenAPI
    url: https://api.customsadvisory.com/openapi/compliance.yaml
  - type: Sandbox
    url: https://sandbox.customsadvisory.com/v1/compliance
  contact:
  - FN: Compliance API Support
    email: compliance-api@customsadvisory.com
- name: Advisory Services API
  description: Access to customs advisory consultations, rulings database, and expert guidance.
  image: https://example.com/images/advisory-api.png
  humanURL: https://customsadvisory.com/advisory-services
  baseURL: https://api.customsadvisory.com/v1/advisory
  tags:
  - Advisory
  - Consultations
  - Expert Guidance
  - Rulings
  properties:
  - type: Documentation
    url: https://docs.customsadvisory.com/advisory-services
  - type: OpenAPI
    url: https://api.customsadvisory.com/openapi/advisory.yaml
  - type: Pricing
    url: https://customsadvisory.com/pricing
  contact:
  - FN: Advisory API Support
    email: advisory-api@customsadvisory.com
- name: Duty Calculator API
  description: Calculates duties, taxes, and fees for international shipments.
  image: https://example.com/images/duty-calc-api.png
  humanURL: https://customsadvisory.com/duty-calculator
  baseURL: https://api.customsadvisory.com/v1/duty-calculator
  tags:
  - Duty Calculation
  - Fees
  - Shipping Costs
  - Taxes
  properties:
  - type: Documentation
    url: https://docs.customsadvisory.com/duty-calculator
  - type: OpenAPI
    url: https://api.customsadvisory.com/openapi/duty-calculator.yaml
  - type: Rate Limits
    url: https://docs.customsadvisory.com/rate-limits
  contact:
  - FN: Calculator API Support
    email: calculator-api@customsadvisory.com
name: Customs Advisory Services
tags:
- Advisory Services
- Customs
- Import/Export
- Regulatory
- Tariff Classification
- Trade Compliance
type: Contract
image: https://example.com/images/customs-advisory-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for managing customs advisory services, trade compliance, and regulatory guidance.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

