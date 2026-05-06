---
aid: cardtonic
url: https://raw.githubusercontent.com/api-evangelist/cardtonic/refs/heads/main/apis.yml
name: Cardtonic
description: Cardtonic is an Africa-focused fintech platform that lets users trade gift cards (sell unused cards for cash and buy over 14,000 local and international gift cards), issue virtual dollar cards, pay bills (airtime, data, electricity, TV, betting), purchase eSIMs in 140+ countries, and shop for gadgets through its Just Gadgets storefront. Cardtonic supports Naira and Cedi settlement for users in Nigeria and Ghana, holds PCI DSS certification, and operates under Nigeria Data Protection Commission (NDPC) oversight. For businesses, Cardtonic offers a Gift Card Developer API (currently waitlist-only) that lets merchants embed gift card purchasing, sales, bulk ordering, inventory, and redemption into websites, mobile apps, and point-of-sale systems.
type: Index
x-type: company
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Africa
  - Bill Payments
  - eSIM
  - Finance
  - Fintech
  - Gift Cards
  - Ghana
  - Nigeria
  - Payments
  - Virtual Dollar Cards
created: '2025-02-08'
modified: '2026-04-23'
specificationVersion: '0.19'
apis:
  - aid: cardtonic:gift-card-developer-api
    name: Cardtonic Gift Card Developer API
    description: The Cardtonic Gift Card Developer API enables merchants and platforms to integrate gift card services into their websites, mobile apps, and point-of-sale systems. The API exposes a catalog of more than 14,000 gift cards for purchase and sale, bulk ordering with instant reporting, inventory and redemption management, and branding/customization hooks. As of 2026 the API is in waitlist mode and developer credentials are issued through Cardtonic on request.
    humanURL: https://cardtonic.com/developer
    tags:
      - Gift Cards
      - Fintech
      - Payments
    properties:
      - url: https://cardtonic.com/developer
        type: Documentation
      - url: https://cardtonic.com/developer
        type: Signup
      - url: openapi/cardtonic-openapi.yml
        type: OpenAPI
    x-features:
      - Catalog of 14,000+ local and international gift cards
      - Purchase and sale flows for merchant integration
      - Bulk ordering with instant reporting
      - Inventory and redemption management
      - Branding/white-label customization hooks
      - Web, mobile, and POS integration patterns
      - Waitlist-based onboarding
    x-use-cases:
      - Rewards and employee recognition platforms
      - Remittance and cross-border cash-out flows
      - Neobank and wallet gift card storefronts
      - Retail POS gift card upsell and resale
      - Loyalty and referral programs
      - Corporate procurement and bulk gifting
  - aid: cardtonic:virtual-dollar-card
    name: Cardtonic Virtual Dollar Card
    description: Cardtonic Virtual Dollar Cards are user-facing USD-denominated cards that let African customers pay merchants that accept Visa/Mastercard globally. The product is currently consumed through the Cardtonic app and dashboard; programmatic access for partners is available on request alongside the Gift Card Developer API waitlist.
    humanURL: https://cardtonic.com/virtual-dollar-card
    tags:
      - Cards
      - Fintech
      - Virtual Dollar Cards
    properties:
      - url: https://cardtonic.com/virtual-dollar-card
        type: Documentation
    x-features:
      - USD-denominated virtual cards for online spending
      - Load and settle in Naira/Cedis
      - App and dashboard controls for issuance and spend
      - PCI DSS certified issuance
    x-use-cases:
      - Cross-border subscription payments (SaaS, streaming)
      - Online shopping on global merchants
      - Travel and ad-platform spend for SMBs
      - Remote worker payouts
  - aid: cardtonic:bill-payments
    name: Cardtonic Bill Payments
    description: Cardtonic Bill Payments cover airtime top-ups, mobile data, electricity, TV subscriptions, and betting wallets across more than 100 countries, consumed through the Cardtonic app and dashboard. Partner access is available on request.
    humanURL: https://cardtonic.com/
    tags:
      - Bill Payments
      - Fintech
      - Payments
    properties:
      - url: https://cardtonic.com/
        type: Documentation
    x-features:
      - Airtime and mobile data top-ups
      - Electricity and TV subscription payments
      - Betting wallet funding
      - 100+ country coverage
      - App, web, and dashboard channels
    x-use-cases:
      - Consumer bill-payment super-app scenarios
      - Diaspora bill pay for family members
      - Agent-banking and mobile-money integrations
common:
  - type: Website
    url: https://cardtonic.com/
  - type: Developer
    url: https://cardtonic.com/developer
  - type: Dashboard
    url: https://dashboard.cardtonic.com/
  - type: Login
    url: https://cardtonic.com/login
  - type: Sign Up
    url: https://cardtonic.com/register
  - type: About
    url: https://cardtonic.com/about
  - type: Blog
    url: https://cardtonic.com/blog
  - type: FAQ
    url: https://cardtonic.com/faq
  - type: Contact
    url: https://cardtonic.com/contact
  - type: Terms of Service
    url: https://cardtonic.com/terms
  - type: Privacy Policy
    url: https://cardtonic.com/privacy
  - type: X
    url: https://x.com/cardtonic
  - type: LinkedIn
    url: https://www.linkedin.com/company/cardtonic
  - type: Instagram
    url: https://www.instagram.com/cardtonic/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
