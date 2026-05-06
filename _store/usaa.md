---
aid: usaa
url: https://raw.githubusercontent.com/api-evangelist/usaa/refs/heads/main/apis.yml
apis:
  - aid: usaa:open-banking-aggregation
    name: USAA Open Banking via Aggregators
    tags:
      - Banking
      - Open Banking
      - Financial Data Exchange
      - Account Aggregation
      - Military Finance
    humanURL: https://www.usaa.com
    properties:
      - url: https://www.usaa.com
        type: Website
      - url: https://www.financialdataexchange.org/FDX/FDX/News/Spotlights/Member%20Spotlight%20USAA.aspx
        type: Documentation
    description: USAA provides open banking data access to its members' accounts through API aggregators (Plaid, Flinks/Mastercard Open Banking). USAA is an active member of the Financial Data Exchange (FDX) and follows FDX API standards for secure data sharing with authorized third-party applications and fintechs. USAA does not maintain a public developer portal but supports member-permissioned data sharing through established aggregator connections.
  - aid: usaa:github-open-source
    name: USAA Open Source GitHub Projects
    tags:
      - Open Source
      - Developer Tools
      - Machine Learning
      - Security
    humanURL: https://github.com/usaa
    properties:
      - url: https://github.com/usaa
        type: GitHub
      - url: https://usaa.github.io
        type: Website
    description: USAA maintains public open source projects on GitHub including developer tooling, quality gates, ML workflow tools, and cybersecurity integrations. Projects include sonar-quality-gates (Gradle quality gate plugin), indexa (dependency analysis), vogel (actuarial ML workflow), and Assemblyline security service integrations.
name: USAA
tags:
  - Financial Services
  - Banking
  - Insurance
  - Military Finance
  - Open Banking
  - Fortune 100
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: USAA (United Services Automobile Association) is a financial services group offering banking, investing, and insurance products exclusively to people and families that serve, or have served, in the United States military. As a Fortune 100 company, USAA provides auto insurance, homeowners insurance, life insurance, banking, investments, and retirement products. USAA is an active member of the Financial Data Exchange (FDX) and provides open banking connectivity through API aggregators including Plaid and Mastercard Open Banking (formerly Flinks).
features:
  - Open Banking via FDX-aligned API aggregators
  - Account balance and transaction data access
  - Member-permissioned data sharing
  - Open source developer tools
useCases:
  - Personal finance app integration
  - Account aggregation for members
  - Military family financial planning
  - Insurance and banking product access
integrations:
  - Plaid
  - Mastercard Open Banking
  - Financial Data Exchange (FDX)
solutions:
  - Military Financial Services
  - Open Banking
  - Personal Finance Management
github:
  - https://github.com/usaa
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
