---
aid: southwest-gas
name: Southwest Gas
description: Southwest Gas Holdings is a natural gas distribution company that purchases, distributes, and transports natural gas for customers in Arizona, Nevada, and California. As a Fortune 1000 utility company headquartered in Las Vegas, Nevada, Southwest Gas serves over 2 million customers through its regulated utility segment and also operates Centuri Group, a full-service utility infrastructure services company.
url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Fortune 1000
  - Natural Gas
  - Utility
  - Energy
apis:
  - aid: southwest-gas:southwest-gas-my-account-api
    name: Southwest Gas My Account API
    description: The Southwest Gas My Account API powers the online customer portal and mobile application for natural gas utility customers in Arizona, Nevada, and California. Customers can view usage history, pay bills, manage account settings, and receive outage notifications through the portal.
    humanURL: https://myaccount.swgas.com/
    baseURL: https://myaccount.swgas.com
    tags:
      - Natural Gas
      - Customer Account
      - Utility
      - Billing
    properties:
      - type: Website
        url: https://myaccount.swgas.com/Portal/
      - type: Mobile Application
        url: https://www.swgas.com/en/mobile-app
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/json-schema/southwest-gas-account-schema.json
      - type: JSON Schema
        url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/json-schema/southwest-gas-usage-schema.json
  - aid: southwest-gas:southwest-gas-agency-portal-api
    name: Southwest Gas Agency Portal API
    description: The Southwest Gas Agency Portal provides access for charitable organizations and assistance agencies to look up customer accounts and submit utility assistance pledges on behalf of customers in need.
    humanURL: https://agency.swgas.com/Portal/
    baseURL: https://agency.swgas.com
    tags:
      - Natural Gas
      - Agency
      - Assistance
      - Utility
    properties:
      - type: Website
        url: https://agency.swgas.com/Portal/
      - type: FAQs
        url: https://h1www.swgas.com/en/agency-portal-faqs
common:
  - type: Website
    url: https://www.swgas.com
  - type: Customer Portal
    url: https://myaccount.swgas.com/
  - type: Agency Portal
    url: https://agency.swgas.com/Portal/
  - type: Mobile App
    url: https://www.swgas.com/en/mobile-app
  - type: Investor Relations
    url: https://investors.swgasholdings.com/
  - type: LinkedIn
    url: https://www.linkedin.com/company/southwest-gas
  - type: X
    url: https://twitter.com/SouthwestGas
  - type: JSON-LD Context
    url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/json-ld/southwest-gas-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/southwest-gas/refs/heads/main/vocabulary/southwest-gas-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
