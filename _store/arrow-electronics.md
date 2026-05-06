---
aid: arrow-electronics
url: https://raw.githubusercontent.com/api-evangelist/arrow-electronics/refs/heads/main/apis.yml
name: Arrow Electronics
tags:
  - Electronics
  - Components
  - Supply Chain
  - Procurement
  - Distribution
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-19'
description: Arrow Electronics is a global provider of products, services, and solutions to industrial and commercial users of electronic components and enterprise computing solutions. With over 2,200 suppliers and more than 200,000 customers worldwide, Arrow serves as a vital link in the technology supply chain, enabling the design, manufacture, and operation of electronic components. Arrow provides REST APIs for pricing and availability lookups, order placement, and supply chain automation, enabling distributors, OEMs, and procurement teams to integrate electronic component sourcing directly into their systems.
apis:
  - aid: arrow-electronics:pricing-availability-api
    name: Arrow Electronics Pricing and Availability API
    description: The Arrow Electronics Pricing and Availability API enables programmatic search for electronic components, retrieval of real-time pricing data, and inventory availability across Arrow's global inventory pools including ACNA/NAC, VERICAL, EUROPE, ASIA, AEP, C1S, PSG, and RFPD. Returns results in JSON or XML format.
    humanURL: https://developers.arrow.com/api/index.php/site/page?view=Itemservice
    baseURL: https://api.arrow.com/itemservice/v4
    tags:
      - Pricing
      - Availability
      - Electronics
      - Components
      - Inventory
    properties:
      - type: Documentation
        url: https://developers.arrow.com/api/index.php/site/page?view=Itemservice
      - type: Authentication
        url: https://developers.arrow.com/api/index.php/site/page?view=gettingStarted
  - aid: arrow-electronics:order-api
    name: Arrow Electronics Order API
    description: The Arrow Electronics Order API enables automated order placement for electronic components at Arrow.com and Verical.com, and allows programmatic retrieval of order status information for existing orders. Requires SHA-256 encoded credentials and a Credit account.
    humanURL: https://developers.arrow.com/api/index.php/site/page?view=orderApi
    baseURL: https://api.arrow.com
    tags:
      - Orders
      - Procurement
      - E-Commerce
      - Supply Chain
    properties:
      - type: Documentation
        url: https://developers.arrow.com/api/index.php/site/page?view=orderApi
      - type: Authentication
        url: https://developers.arrow.com/api/index.php/site/page?view=gettingStarted
common:
  - type: Portal
    url: https://developers.arrow.com/
    title: Developer Portal
  - type: GettingStarted
    url: https://developers.arrow.com/api/index.php/site/page?view=gettingStarted
    title: Getting Started
  - type: BestPractices
    url: https://developers.arrow.com/api/index.php/site/page?view=bestPractices
    title: Best Practices
  - type: TermsOfService
    url: https://developers.arrow.com/api/index.php/site/page?view=terms
    title: Terms and Conditions
  - type: Portal
    url: https://www.arrow.com/
    title: Arrow Electronics Website
  - type: Support
    url: mailto:api@arrow.com
    title: API Support Email
  - type: Features
    data:
      - name: Global Inventory Search
        description: Search across up to 8 global inventory pools simultaneously including Arrow NAC, Verical, European, Asian, and specialty component inventories.
      - name: Real-Time Pricing
        description: Retrieve current pricing data for electronic components including quantity breaks, lead times, and packaging options.
      - name: Automated Order Placement
        description: Place orders programmatically for components at Arrow.com and Verical.com without manual web interaction, enabling supply chain automation.
      - name: Order Status Tracking
        description: Retrieve status information for existing orders to track fulfillment and shipping progress programmatically.
      - name: Multi-Format Support
        description: APIs return data in JSON (default) and XML formats, with JSONP support for browser-based integrations.
  - type: UseCases
    data:
      - name: ERP Integration
        description: Manufacturers and distributors integrate Arrow's Pricing and Availability API with their ERP systems (SAP, Oracle, etc.) to automate component sourcing and procurement workflows.
      - name: Bill of Materials Pricing
        description: Design engineers use the API to retrieve bulk pricing for entire Bills of Materials during product cost estimation and component selection.
      - name: Automated Procurement
        description: Procurement systems use the Order API to automatically replenish component inventory when stock reaches reorder thresholds.
      - name: Supply Chain Visibility
        description: Operations teams use availability data across multiple inventory pools to manage component risk and identify alternative sourcing options.
  - type: Integrations
    data:
      - name: Verical
        description: Arrow's Verical marketplace for independent distribution is accessible via the same API infrastructure, extending component sourcing to the spot market.
      - name: Arrow Enterprise Computing Solutions
        description: Integration with Arrow's enterprise computing division for server, storage, and cloud component procurement alongside electronic components.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
