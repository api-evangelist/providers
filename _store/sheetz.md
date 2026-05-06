---
aid: sheetz
url: https://raw.githubusercontent.com/api-evangelist/sheetz/refs/heads/main/apis.yml
apis:
  - aid: sheetz:sheetz-edi-integration
    name: Sheetz EDI Integration
    tags:
      - B2B
      - EDI
      - Supply Chain
      - Retail
    humanURL: https://www.b2bgateway.net/trading-partner/sheetz-distribution-services/
    properties:
      - url: https://www.b2bgateway.net/trading-partner/sheetz-distribution-services/
        type: Documentation
    description: Sheetz Distribution Services EDI and API integration capabilities enable suppliers and trading partners to exchange electronic data interchange documents including purchase orders, invoices, advance ship notices, and inventory feeds with Sheetz enterprise systems. Supported via third-party EDI providers and direct API connections.
  - aid: sheetz:sheetz-loyalty-api
    name: Sheetz Loyalty and Rewards API
    tags:
      - Loyalty
      - Rewards
      - Mobile
      - Retail
    humanURL: https://www.sheetz.com/mySheetz
    properties:
      - url: https://www.sheetz.com/mySheetz
        type: Documentation
    description: The Sheetz Rewards loyalty platform powered by Ignite Retail Technology provides a unified loyalty engine with advanced data insights and integration across point of sale, mobile, and digital channels. Enables partners to access customer rewards, offers, and engagement data through API-based integrations.
name: Sheetz
tags:
  - Convenience Store
  - Energy
  - Food Service
  - Fortune 500
  - Fuel
  - Retail
type: Contract
image: https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Sheetz_logo.svg/2560px-Sheetz_logo.svg.png
access: 3rd-Party
created: '2025-01-01'
modified: '2026-05-02'
position: Consumer
description: Sheetz, Inc. is an American chain of convenience stores and coffee shops headquartered in Altoona, Pennsylvania. Operating more than 800 company-owned stores across Pennsylvania, West Virginia, Maryland, Ohio, Virginia, North Carolina, and Michigan, Sheetz is one of the largest convenience store chains in the United States. The company offers fuel, food service, coffee, and retail products, supported by a mobile app for ordering, rewards, and store locator services. Sheetz provides B2B EDI and API integration capabilities for suppliers and distribution partners.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
common:
  - url: https://www.sheetz.com
    type: Website
  - url: https://www.sheetz.com/mySheetz
    type: Loyalty Program
  - url: https://www.b2bgateway.net/trading-partner/sheetz-distribution-services/
    type: EDI Integration
  - url: https://www.sheetz.com/careers
    type: Careers
  - url: https://www.sheetz.com/legal/privacy-policy
    type: Privacy Policy
  - url: https://www.sheetz.com/legal/terms-of-use
    type: Terms of Service
  - url: https://github.com/sheetz
    type: GitHub Organization
  - type: Features
    data:
      - name: Mobile Ordering
        description: Order ahead through the Sheetz mobile app for food, drinks, and fuel.
      - name: Loyalty Rewards
        description: Earn and redeem points through the MySheetz Card loyalty program powered by Ignite Retail Technology.
      - name: Digital Payments
        description: Pay via mobile app at the pump and in-store with integrated digital wallet support.
      - name: Store Locator
        description: Find nearby Sheetz locations, hours, services, and amenities via API or mobile app.
      - name: EDI Integration
        description: B2B EDI integration for suppliers covering purchase orders, invoices, and advance ship notices.
      - name: Fuel Price API
        description: Access current fuel prices across Sheetz locations for integration with third-party mapping and fleet services.
  - type: UseCases
    data:
      - name: Supplier Integration
        description: Connect supplier ERP systems to Sheetz distribution and ordering workflows via EDI.
      - name: Fleet Fueling
        description: Integrate Sheetz fuel pricing and payment data into fleet management systems.
      - name: Loyalty Platform Integration
        description: Connect third-party apps and services to the MySheetz Rewards loyalty engine.
      - name: Mobile Commerce
        description: Build integrations for mobile ordering, payment, and pickup at Sheetz locations.
  - type: Integrations
    data:
      - name: Ignite Retail Technology
        description: Loyalty platform powering MySheetz Rewards with unified data insights across POS, mobile, and digital.
      - name: TrueCommerce B2BGateway
        description: Third-party EDI provider enabling supplier connectivity to Sheetz Distribution Services.
      - name: Verifone
        description: POS and payment terminal integration at Sheetz store locations.
---
