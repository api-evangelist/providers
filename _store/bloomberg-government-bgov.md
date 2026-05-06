---
aid: bloomberg-government-bgov
name: Bloomberg Government (BGOV)
description: Bloomberg Government (BGOV) is a comprehensive intelligence platform for professionals working at the intersection of government and business. BGOV provides legislative tracking, regulatory intelligence, government contracting data, federal budget analysis, and policy research tools. It offers APIs and data feeds for integrating government and regulatory data into enterprise workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bloomberg-government-bgov/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Government
  - Legislative
  - Regulatory
  - Government Contracting
  - Federal Budget
  - Policy Research
  - Bloomberg
apis:
  - aid: bloomberg-government-bgov:bgov-data-api
    name: Bloomberg Government Data API
    description: Access BGOV legislative, regulatory, and government contracting data programmatically. Retrieve bill tracking, regulatory actions, federal contract awards, and lobbying disclosures for integration into research and compliance workflows.
    humanURL: https://about.bgov.com/
    baseURL: https://api.bgov.com
    tags:
      - Legislative
      - Regulatory
      - Government Data
      - Contracting
    properties:
      - type: Documentation
        url: https://about.bgov.com/
  - aid: bloomberg-government-bgov:bgov-contracting-api
    name: BGOV Government Contracting Intelligence
    description: Access federal contract award data, procurement intelligence, and vendor spending data. Track USASpending.gov data enriched with Bloomberg analytics for competitive intelligence and business development.
    humanURL: https://about.bgov.com/federal-contracting-intelligence/
    baseURL: https://api.bgov.com/contracting
    tags:
      - Government Contracting
      - Federal Contracts
      - USASpending
      - Procurement
    properties:
      - type: Documentation
        url: https://about.bgov.com/federal-contracting-intelligence/
common:
  - type: Portal
    url: https://www.bloomberg.com/professional/
  - type: Documentation
    url: https://about.bgov.com/
  - type: TermsOfService
    url: https://www.bloomberg.com/notices/tos/
  - type: PrivacyPolicy
    url: https://www.bloomberg.com/privacy/
  - type: Support
    url: https://about.bgov.com/contact/
  - type: Features
    data:
      - name: Legislative Tracking
        description: Real-time tracking of bills, hearings, and committee activity across Congress.
      - name: Regulatory Intelligence
        description: Monitor federal agency rulemaking, proposed rules, and final regulations.
      - name: Government Contracting Data
        description: Federal contract awards, task orders, and spending analysis.
      - name: Federal Budget Analysis
        description: Appropriations tracking, budget requests, and spending trends.
      - name: Lobbying Disclosure Data
        description: Lobbying registrations, disclosures, and advocacy activity tracking.
  - type: UseCases
    data:
      - name: Government Relations
        description: Track legislation and regulatory developments affecting business interests.
      - name: Federal Contracting
        description: Identify contracting opportunities and analyze competitor awards.
      - name: Policy Research
        description: Deep research on policy developments and their business implications.
      - name: Compliance Monitoring
        description: Monitor regulatory changes for compliance and risk management.
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
