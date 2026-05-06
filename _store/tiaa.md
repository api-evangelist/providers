---
aid: tiaa
url: https://raw.githubusercontent.com/api-evangelist/tiaa/refs/heads/main/apis.yml
name: TIAA
description: TIAA (Teachers Insurance and Annuity Association of America) is a leading provider of financial services in the academic, research, medical, cultural, and government fields. Originally founded to provide retirement security for educators, TIAA now offers retirement services, insurance, brokerage, and investment management products to individuals and institutions. TIAA operates a developer portal at developer.tiaa.org exposing APIs for financial data aggregation (FDX standard), secure income account management, and gateway integrations enabling plan portability and fintech connectivity.
image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
tags:
  - Finance
  - Financial Data
  - Fintech
  - Insurance
  - Investment Management
  - Retirement
  - Wealth Management
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tiaa:tiaa-fdx-api
    name: TIAA Financial Data Exchange API
    description: The TIAA Financial Data Exchange (FDX) API provides customer account details to authorized fintechs and financial aggregators with customer consent. Built on the FDX open-standard (OAuth 2.0), it offers a secure alternative to screen scraping and enables third-party apps to retrieve account balances, transactions, investment positions, and income data from TIAA retirement and brokerage accounts.
    image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
    humanURL: https://developer.tiaa.org/public/fdx
    baseURL: https://api.tiaa.org/fdx/v6
    tags:
      - Account Aggregation
      - Financial Data
      - FDX
      - Open Finance
      - Retirement
    properties:
      - type: Documentation
        url: https://developer.tiaa.org/public/fdx
      - type: Authentication
        url: https://developer.tiaa.org/public/fdx#authentication
      - type: OpenAPI
        url: openapi/tiaa-fdx-openapi.yml
  - aid: tiaa:tiaa-sia-api
    name: TIAA Secure Income Account API
    description: The TIAA Secure Income Account (SIA) API enables recordkeepers and plan administrators to integrate TIAA's guaranteed lifetime income product into custom target-date model portfolios and managed account solutions. Built using the OpenAPI Specification (OAS) and authenticated via OAuth 2.0 Client Credentials Flow, the SIA API supports account setup, contribution management, and participant income projections for defined contribution plan participants.
    image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
    humanURL: https://developer.tiaa.org/public/sia
    baseURL: https://api.tiaa.org/sia/v1
    tags:
      - Annuity
      - Guaranteed Income
      - Plan Administration
      - Recordkeeping
      - Retirement
      - Secure Income
    properties:
      - type: Documentation
        url: https://developer.tiaa.org/public/sia
      - type: Authentication
        url: https://developer.tiaa.org/public/sia#authentication
      - type: OpenAPI
        url: openapi/tiaa-sia-openapi.yml
  - aid: tiaa:tiaa-gateway-api
    name: TIAA Gateway API
    description: The TIAA Gateway is a cloud-based API layer enabling product portability and interoperability across retirement ecosystem partners. It allows banking institutions, financial aggregators, and plan sponsor platforms to expose TIAA retirement account data within their own apps and experiences. The Gateway supports FDX, ACORD, and SPARK standards and has more than 10 external partners connected.
    image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
    humanURL: https://www.tiaa.org/public/pdf/t/tiaa-gateway-drives-product-portability.pdf
    baseURL: https://api.tiaa.org/gateway/v1
    tags:
      - Financial Data
      - Integration
      - Open Finance
      - Plan Portability
      - Retirement
    properties:
      - type: Documentation
        url: https://www.tiaa.org/public/pdf/t/tiaa-gateway-drives-product-portability.pdf
      - type: Portal
        url: https://developer.tiaa.org
  - aid: tiaa:tiaa-payroll360-api
    name: TIAA Payroll360 API
    description: TIAA Payroll360 enables direct API connections between HR and payroll systems and TIAA's plan administration platform, automating deductions management, employer onboarding, and payroll data integrity. Supports SPARK 2.0 CR and TIAA-specific FLEX and OPS formats.
    image: https://www.tiaa.org/content/dam/prod/tiaa/images/tiaa-logo.svg
    humanURL: https://developer.tiaa.org/public/payroll360
    baseURL: https://api.tiaa.org/payroll360/v1
    tags:
      - HR
      - Payroll
      - Plan Administration
      - Retirement
      - SPARK
    properties:
      - type: Documentation
        url: https://developer.tiaa.org/public/payroll360
common:
  - type: Portal
    url: https://developer.tiaa.org
  - type: Website
    url: https://www.tiaa.org
  - type: Documentation
    url: https://developer.tiaa.org/public/fdx
  - type: Blog
    url: https://www.tiaa.org/public/learn
  - type: LinkedIn
    url: https://www.linkedin.com/company/tiaa
  - type: Twitter
    url: https://twitter.com/tiaa
  - type: Privacy Policy
    url: https://www.tiaa.org/public/pdf/t/privacy_notice.pdf
  - type: Terms of Service
    url: https://www.tiaa.org/public/pdf/t/tiaa_website_terms_of_use.pdf
  - type: JSON-LD
    url: json-ld/tiaa-context.jsonld
  - type: JSONSchema
    url: json-schema/tiaa-account-schema.json
  - type: JSONSchema
    url: json-schema/tiaa-participant-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
