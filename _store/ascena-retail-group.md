---
aid: ascena-retail-group
url: https://raw.githubusercontent.com/api-evangelist/ascena-retail-group/refs/heads/main/apis.yml
name: Ascena Retail Group
tags:
  - Retail
  - Fashion
  - Apparel
  - E-Commerce
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-19'
description: Ascena Retail Group was a specialty apparel retailer that operated multiple women's and tween-girl clothing brands through retail stores, outlets, and e-commerce. The company operated brands including Ann Taylor, LOFT, Lane Bryant, Catherines, Cacique, and others. Ascena filed for Chapter 11 bankruptcy in July 2020 and sold off its brands. Ann Taylor and LOFT were acquired by Sycamore Partners in 2020 and continue to operate. Lane Bryant and Catherines were also sold to new owners. The company did not expose a public developer API during its operation. Current API resources, if any, exist under the successor brand owners.
apis:
  - aid: ascena-retail-group:ann-taylor-api
    name: Ann Taylor / LOFT E-Commerce Platform
    description: Ann Taylor and LOFT (formerly Ascena brands, now owned by Sycamore Partners) operate e-commerce platforms with standard retail APIs for product catalog, order management, loyalty programs, and customer accounts.
    humanURL: https://www.anntaylor.com/
    baseURL: https://www.anntaylor.com
    tags:
      - Fashion
      - Retail
      - Women's Apparel
      - E-Commerce
    properties:
      - type: Documentation
        url: https://www.anntaylor.com/
common:
  - type: Portal
    url: https://www.anntaylor.com/
    title: Ann Taylor Website
  - type: Portal
    url: https://www.loft.com/
    title: LOFT Website
  - type: Features
    data:
      - name: Multi-Brand Retail Operations
        description: Ascena operated multiple fashion brands targeting different women's and tween demographics through retail stores, outlet locations, and e-commerce channels.
      - name: Loyalty Programs
        description: Brand-specific loyalty and rewards programs for frequent shoppers across Ann Taylor, LOFT, Lane Bryant, and other brands.
      - name: Omnichannel Commerce
        description: Integrated in-store and online shopping experiences across all Ascena brands, including ship-from-store and buy-online-pickup-in-store.
  - type: UseCases
    data:
      - name: Fashion Retail Shopping
        description: Customers shop for women's and tween apparel across Ascena brand stores and e-commerce platforms.
      - name: Loyalty and Rewards
        description: Repeat customers earn and redeem rewards points through brand loyalty programs.
  - type: Integrations
    data:
      - name: Sycamore Partners
        description: Ann Taylor and LOFT were acquired by Sycamore Partners in 2020 following Ascena's bankruptcy filing.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
