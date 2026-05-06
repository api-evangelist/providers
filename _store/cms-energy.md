---
aid: cms-energy
url: https://raw.githubusercontent.com/api-evangelist/cms-energy/refs/heads/main/apis.yml
name: CMS Energy
x-type: company
tags:
  - Electric
  - Energy
  - Green Button
  - Michigan
  - Natural Gas
  - Utility
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-23'
specificationVersion: '0.19'
description: CMS Energy is an energy holding company whose primary subsidiary is Consumers Energy, an electric and natural gas utility serving customers in Michigan. Consumers Energy participates in the Green Button Connect My Data (GBCMD) program, exposing customer-authorized energy usage data to third parties via OAuth 2.0 - typically brokered through UtilityAPI - for use in energy management, demand response, EV charging, solar, and sustainability applications.
apis:
  - aid: cms-energy:consumers-green-button-api
    name: Consumers Energy Green Button Connect My Data API
    tags:
      - Energy Usage
      - Green Button
      - OAuth2
      - Smart Meter
      - Utility
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://utilityapi.com/docs/utilities/consumersenergy
    properties:
      - url: https://utilityapi.com/docs/utilities/consumersenergy
        type: Documentation
      - url: https://utilityapi.com/
        type: Portal
    description: The Consumers Energy Green Button Connect My Data API exposes customer-authorized electric and natural-gas usage data to registered third parties using the NAESB ESPI / Green Button standard. Authorization uses OAuth 2.0 with single sign-on or test-account scopes; data is delivered as Green Button XML or JSON via UtilityAPI's standardized endpoints (Meters, Bills, Intervals, Billing Summaries). Third parties register with Consumers Energy, are issued a client_id, and start in sandbox mode before being approved for live data.
    x-features:
      - name: Green Button Standard
        description: NAESB ESPI / Green Button XML for usage point and interval data.
      - name: Meters Endpoint
        description: Retrieve individual meter information for an authorized customer.
      - name: Bills Endpoint
        description: Retrieve bill history and charges.
      - name: Intervals Endpoint
        description: Retrieve granular interval-usage time series.
      - name: Billing Summaries
        description: Retrieve account-level summary data.
      - name: OAuth 2.0
        description: Customer authorization via OAuth 2.0 with SSO or test scopes.
      - name: Sandbox Test Accounts
        description: Built-in test residential and commercial scenarios for development.
    x-useCases:
      - name: Energy Efficiency
        description: Pull usage data into energy efficiency and benchmarking apps.
      - name: Demand Response
        description: Power demand-response and load-management programs.
      - name: Solar and EV
        description: Inform solar sizing and EV-charging optimization with real usage.
      - name: Sustainability Reporting
        description: Aggregate usage into Scope 2 emissions and ESG reporting.
common:
  - url: https://www.cmsenergy.com
    type: Website
  - url: https://www.consumersenergy.com
    name: Consumers Energy
    type: Website
  - url: https://utilityapi.com/docs/utilities/consumersenergy
    name: Consumers Energy on UtilityAPI
    type: Documentation
  - url: https://www.cmsenergy.com/about-cms-energy/consumers-energy/
    name: About Consumers Energy
    type: About
  - url: https://www.cmsenergy.com/contact-us/default.aspx
    name: Contact Us
    type: Support
  - url: https://www.cmsenergy.com/privacy-statement/default.aspx
    name: Privacy Statement
    type: PrivacyPolicy
  - url: https://twitter.com/CMSEnergy
    name: CMS Energy on X
    type: X
  - url: https://www.linkedin.com/company/cms-energy/
    name: CMS Energy on LinkedIn
    type: LinkedIn
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
