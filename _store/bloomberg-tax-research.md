---
aid: bloomberg-tax-research
name: Bloomberg Tax Research
description: Bloomberg Tax Research provides tax professionals with comprehensive access to primary sources, expert practitioner analysis, portfolios, and tax news for conducting in-depth tax research. The platform covers federal income tax, state and local tax (SALT), international tax, estate planning, benefits, payroll, and transfer pricing research.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-tax-research/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Tax Research
  - Federal Tax
  - State Tax
  - International Tax
  - Tax Analysis
  - Bloomberg Tax
apis:
  - aid: bloomberg-tax-research:btax-research-api
    name: Bloomberg Tax Research API
    description: Programmatic access to Bloomberg Tax research content including tax portfolios, practitioner analysis, primary sources, and tax news for integration into legal research and tax technology platforms.
    humanURL: https://pro.bloombergtax.com/tax-research/
    baseURL: https://api.bloombergtax.com/research
    tags:
      - Tax Research
      - Portfolios
      - Analysis
      - Primary Sources
    properties:
      - type: Documentation
        url: https://pro.bloombergtax.com/tax-research/
  - aid: bloomberg-tax-research:salt-research
    name: Bloomberg Tax SALT Research
    description: State and local tax (SALT) research platform covering income, sales, property, and other state and local tax types with state-by-state analysis and guidance.
    humanURL: https://pro.bloombergtax.com/state-local-tax-research/
    baseURL: https://api.bloombergtax.com/salt
    tags:
      - SALT
      - State Tax
      - Local Tax
      - Sales Tax
    properties:
      - type: Documentation
        url: https://pro.bloombergtax.com/state-local-tax-research/
common:
  - type: Portal
    url: https://pro.bloombergtax.com/
  - type: Documentation
    url: https://pro.bloombergtax.com/tax-research/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://pro.bloombergtax.com/contact/
  - type: Features
    data:
      - name: Tax Portfolios
        description: Practitioner-authored portfolio analysis on tax topics.
      - name: Primary Sources
        description: Access to Internal Revenue Code, Treasury regulations, and rulings.
      - name: State Tax Research
        description: State and local tax research across all 50 states.
      - name: International Tax Research
        description: Global tax research covering international income tax and treaties.
      - name: Tax News
        description: Breaking tax news and regulatory updates.
      - name: Payroll and Benefits
        description: Payroll tax and employee benefits research and compliance.
  - type: UseCases
    data:
      - name: Federal Tax Research
        description: Research complex federal income tax issues with authoritative sources.
      - name: State Tax Compliance
        description: Research state tax obligations and filing requirements.
      - name: International Tax Planning
        description: Analyze international tax structures and treaty positions.
      - name: Estate Planning
        description: Research estate, gift, and generation-skipping transfer tax issues.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
