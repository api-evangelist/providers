---
aid: atmos-energy
name: Atmos Energy
description: |
  Atmos Energy is one of the largest natural-gas-only distributors in the United States, delivering natural gas to residential, commercial, public-authority, and industrial customers across multiple states including Texas, Louisiana, Mississippi, Tennessee, Colorado, Kansas, and Virginia. The company provides online account management, a Builder Portal for developers and contractors, and digital service request capabilities for natural gas connections and meter installations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Natural Gas
  - Utilities
  - Infrastructure
url: https://raw.githubusercontent.com/api-evangelist/atmos-energy/refs/heads/main/apis.yml
created: '2026-03-23'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: atmos-energy:atmos-energy-account-management
    name: Atmos Energy Account Management
    description: |
      Online account management portal for Atmos Energy customers providing access to billing, payment, usage history, service requests, and account settings for residential and commercial natural gas customers.
    humanURL: https://www.atmosenergy.com/account-center/
    baseURL: https://www.atmosenergy.com
    tags:
      - Account Management
      - Billing
      - Natural Gas
      - Utilities
    properties:
      - type: Documentation
        url: https://www.atmosenergy.com/account-center/
  - aid: atmos-energy:atmos-energy-builder-portal
    name: Atmos Energy Builder Portal
    description: |
      The Atmos Energy Builder Portal enables builders and property developers to request and schedule natural gas service lines and meter sets for new construction projects including residential subdivisions and commercial developments.
    humanURL: https://www.atmosenergy.com/customer-service/builder-developer-resources/
    baseURL: https://www.atmosenergy.com
    tags:
      - Builder Services
      - Construction
      - Natural Gas
      - Service Requests
    properties:
      - type: Documentation
        url: https://www.atmosenergy.com/customer-service/builder-developer-resources/
      - type: Portal
        url: https://www.atmosenergy.com/customer-service/builder-developer-resources/
common:
  - type: Website
    url: https://www.atmosenergy.com
  - type: Portal
    url: https://www.atmosenergy.com/account-center/
  - type: Contact
    url: https://www.atmosenergy.com/contact-us/
  - type: Support
    url: https://www.atmosenergy.com/customer-service/
  - type: PrivacyPolicy
    url: https://www.atmosenergy.com/privacy-policy/
  - type: TermsOfService
    url: https://www.atmosenergy.com/terms-of-use/
  - type: Features
    data:
      - name: Online Bill Pay
        description: Pay natural gas bills online through the Atmos Energy Account Center with options for one-time or recurring autopay.
      - name: Usage History
        description: View historical natural gas usage data and billing history through the online account management portal.
      - name: Service Requests
        description: Submit service start, stop, and transfer requests online for residential and commercial natural gas accounts.
      - name: Builder Portal
        description: Online portal for builders and property developers to schedule new gas service line installations and meter sets for construction projects.
      - name: Budget Billing
        description: Enroll in budget billing to spread natural gas costs evenly across 12 months for predictable monthly payments.
  - type: UseCases
    data:
      - name: Residential Account Management
        description: Manage natural gas accounts for homes including billing, payments, usage monitoring, and service requests.
      - name: Commercial Account Management
        description: Manage multi-site commercial and industrial natural gas accounts across Atmos Energy service territories.
      - name: New Construction Gas Service
        description: Request and schedule new gas service line installations and meter sets for residential subdivisions and commercial developments.
      - name: Energy Assistance Programs
        description: Access Atmos Energy Share the Warmth and other assistance programs for customers experiencing financial hardship.
  - type: Integrations
    data:
      - name: PaymentService
        description: Integrated payment processing for online bill pay through secure third-party payment processors.
      - name: State Energy Assistance Programs
        description: Integration with state-level Low Income Home Energy Assistance Program (LIHEAP) for customer assistance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
