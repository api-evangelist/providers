---
aid: consolidated-edison
name: Consolidated Edison
url: https://raw.githubusercontent.com/api-evangelist/consolidated-edison/refs/heads/main/apis.yml
tags:
  - Energy
  - Fortune 500
  - Green Button
  - Natural Gas
  - New York
  - Steam
  - Utility
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-28'
position: Consumer
specificationVersion: '0.19'
x-type: company
description: Consolidated Edison, Inc. (Con Edison) is a Fortune 500 holding company that, through its subsidiaries, provides electric, natural gas, and steam service to customers in New York City and Westchester County. Con Edison does not publish a general-purpose developer portal; programmatic data access is delivered through the Green Button Connect My Data (GBC) program, which lets authorized third parties retrieve customer energy usage data via the NAESB Energy Services Provider Interface (ESPI) standard once the customer grants consent through Con Edison's authorization portal.
apis:
  - aid: consolidated-edison:green-button-connect
    name: Green Button Connect My Data
    tags:
      - Energy
      - Green Button
      - OAuth2
      - Smart Meter
      - Usage Data
    humanURL: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
    properties:
      - url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
        type: Documentation
      - url: https://www.coned.com/en/business-partners/access-customer-data
        type: Authentication
    description: Green Button Connect My Data is the OAuth2-based ESPI service that lets Con Edison customers authorize a registered third party to receive their interval energy usage and account data on a recurring basis. Third parties register through Con Edison's onboarding process to obtain client credentials, then exchange them for access tokens that retrieve ESPI Atom/XML resources for usage points, meter readings, and electric power usage summaries.
  - aid: consolidated-edison:green-button-download
    name: Green Button Download My Data
    tags:
      - CSV
      - Energy
      - Green Button
      - Self-Service
      - Usage Data
      - XML
    humanURL: https://www.coned.com/en/save-money/make-better-energychoices-with-green-button
    properties:
      - url: https://www.coned.com/en/save-money/make-better-energychoices-with-green-button
        type: Documentation
    description: Customer-driven file export that lets Con Edison residential and small commercial accounts download up to one year of smart-meter interval data as CSV or ESPI XML directly from the My Account portal. Useful for one-shot analytics, audits, and migrating data into third-party tools without requiring an OAuth integration.
common:
  - type: Website
    url: https://www.coned.com
  - type: Customer Portal
    url: https://www.coned.com/en/accounts-billing
  - type: Become a Third Party
    url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/become-a-third-party
  - type: Share My Data Overview
    url: https://www.coned.com/en/accounts-billing/share-energy-usage-data/share-my-data
  - type: Investor Relations
    url: https://investor.conedison.com
  - type: Careers
    url: https://www.conedjobs.com
  - type: Privacy Policy
    url: https://www.coned.com/en/about-us/privacy-statement
  - type: Terms of Service
    url: https://www.coned.com/en/about-us/terms-of-use
  - type: Support
    url: https://www.coned.com/en/contact-us
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
