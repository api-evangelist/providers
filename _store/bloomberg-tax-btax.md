---
aid: bloomberg-tax-btax
name: Bloomberg Tax (BTAX)
description: Bloomberg Tax (BTAX) is a comprehensive tax research, planning, and compliance platform providing tax professionals with authoritative primary sources, expert analysis, and practical tools. Bloomberg Tax covers federal, state, and international tax law and provides data APIs for integrating tax rates, regulations, and guidance into enterprise tax technology workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-tax-btax/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Tax
  - Tax Research
  - Tax Compliance
  - Tax Planning
  - Federal Tax
  - International Tax
  - Bloomberg Tax
apis:
  - aid: bloomberg-tax-btax:btax-data-api
    name: Bloomberg Tax Data API
    description: Access Bloomberg Tax data including tax rates, regulations, guidance, and compliance data for integration into enterprise tax technology systems and workflows. Covers federal, state, and international tax data.
    humanURL: https://pro.bloombergtax.com/
    baseURL: https://api.bloombergtax.com
    tags:
      - Tax Rates
      - Tax Regulations
      - Compliance Data
      - Federal Tax
      - State Tax
    properties:
      - type: Documentation
        url: https://pro.bloombergtax.com/
  - aid: bloomberg-tax-btax:btax-transfer-pricing
    name: Bloomberg Tax Transfer Pricing
    description: Specialized transfer pricing research and data platform providing comparables databases, country-by-country reporting data, and transfer pricing documentation tools for multinational tax compliance.
    humanURL: https://pro.bloombergtax.com/transfer-pricing/
    baseURL: https://api.bloombergtax.com/transfer-pricing
    tags:
      - Transfer Pricing
      - International Tax
      - BEPS
      - Comparables
    properties:
      - type: Documentation
        url: https://pro.bloombergtax.com/transfer-pricing/
common:
  - type: Portal
    url: https://pro.bloombergtax.com/
  - type: Documentation
    url: https://pro.bloombergtax.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://pro.bloombergtax.com/contact/
  - type: Features
    data:
      - name: Primary Tax Sources
        description: Access to IRC, regulations, rulings, and court decisions.
      - name: Expert Analysis
        description: Bloomberg Tax practitioner analysis and practice portfolios.
      - name: Tax Rates Database
        description: Federal, state, local, and international tax rates data.
      - name: News and Updates
        description: Real-time tax news and regulatory update alerts.
      - name: Transfer Pricing Tools
        description: Comparables databases and documentation tools for transfer pricing.
      - name: Workpapers Integration
        description: Integration with tax workpaper and compliance software.
  - type: UseCases
    data:
      - name: Tax Research
        description: Research federal and state tax law using authoritative primary sources.
      - name: Tax Planning
        description: Analyze tax planning strategies with expert guidance and analysis.
      - name: International Tax Compliance
        description: Navigate international tax obligations and transfer pricing rules.
      - name: Tax Technology Integration
        description: Integrate Bloomberg Tax data into tax software and ERP systems.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
